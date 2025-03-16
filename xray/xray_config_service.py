import json
import logging
from concurrent import futures
import grpc
from proto.generated import xray_config_pb2, xray_config_pb2_grpc

CONFIG_PATH = "/usr/local/etc/xray/config.json"
logging.basicConfig(level=logging.DEBUG)


class XrayConfigServicer(xray_config_pb2_grpc.XrayConfigServiceServicer):
    def __load_config(self):
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)

    def __save_config(self, config):
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)

    def __find_client(self, config, email):
        for inbound in config['inbounds']:
            if inbound['protocol'] == 'shadowsocks':
                for idx, client in enumerate(inbound['settings']['clients']):
                    if client['email'] == email:
                        return inbound, idx
        return None, -1

    def CreateClient(self, request, context):
        config = self.__load_config()
        inbound, _ = self.__find_client(config, request.client.email)

        if inbound:
            return xray_config_pb2.OperationResponse(
                success=False,
                message="Client already exists"
            )

        new_client = {
            "password": request.client.password,
            "method": request.client.method,
            "email": request.client.email
        }

        for inbound in config['inbounds']:
            if inbound['protocol'] == 'shadowsocks':
                inbound['settings']['clients'].append(new_client)
                try:
                    self.__save_config(config)
                    return xray_config_pb2.OperationResponse(success=True, message="")
                except Exception as e:
                    return xray_config_pb2.OperationResponse(
                        success=False,
                        message=str(e)
                    )
        return xray_config_pb2.OperationResponse(
            success=False,
            message="Shadowsocks inbound not found"
        )

    def ReadClient(self, request, context):
        config = self.__load_config()
        inbound, idx = self.__find_client(config, request.email)

        if idx == -1:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return xray_config_pb2.Client()

        client = inbound['settings']['clients'][idx]
        return xray_config_pb2.Client(
            password=client['password'],
            method=client['method'],
            email=client['email']
        )

    def UpdateClient(self, request, context):
        config = self.__load_config()
        inbound, idx = self.__find_client(config, request.email)

        if idx == -1:
            return xray_config_pb2.OperationResponse(
                success=False,
                message="Client not found"
            )

        inbound['settings']['clients'][idx] = {
            "password": request.client.password,
            "method": request.client.method,
            "email": request.client.email
        }

        try:
            self.__save_config(config)
            return xray_config_pb2.OperationResponse(success=True, message="")
        except Exception as e:
            return xray_config_pb2.OperationResponse(
                success=False,
                message=str(e)
            )

    def DeleteClient(self, request, context):
        config = self.__load_config()
        inbound, idx = self.__find_client(config, request.email)

        if idx == -1:
            return xray_config_pb2.OperationResponse(
                success=False,
                message="Client not found"
            )

        del inbound['settings']['clients'][idx]

        try:
            self.__save_config(config)
            return xray_config_pb2.OperationResponse(success=True, message="")
        except Exception as e:
            return xray_config_pb2.OperationResponse(
                success=False,
                message=str(e)
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    xray_config_pb2_grpc.add_XrayConfigServiceServicer_to_server(
        XrayConfigServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    logging.info("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()