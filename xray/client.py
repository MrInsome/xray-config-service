import grpc
from typing import Optional, Tuple
from proto.generated import xray_config_pb2, xray_config_pb2_grpc


class XrayConfigClient:
    def __init__(self, host: str = 'localhost', port: int = 50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = xray_config_pb2_grpc.XrayConfigServiceStub(self.channel)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.channel:
            self.channel.close()

    def create_client(self, email: str, password: str, method: str = 'aes-256-gcm') -> Tuple[bool, str]:
        """Create new Shadowsocks client"""
        try:
            response = self.stub.CreateClient(
                xray_config_pb2.CreateClientRequest(
                    client=xray_config_pb2.Client(
                        email=email,
                        password=password,
                        method=method
                    )
                )
            )
            return response.success, response.message
        except grpc.RpcError as e:
            return False, f"RPC Error: {e.code()}: {e.details()}"

    def read_client(self, email: str) -> Optional[dict]:
        """Get client details by email"""
        try:
            response = self.stub.ReadClient(xray_config_pb2.ReadClientRequest(email=email))

            if not response.email:
                return None

            return {
                'email': response.email,
                'password': response.password,
                'method': response.method
            }
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise

    def update_client(self, email: str, new_password: str = None, new_method: str = None, new_email: str = None ) -> Tuple[bool, str]:
        """Update existing client"""
        try:
            # Get current client data
            current = self.read_client(email)
            if not current:
                return False, "Client not found"

            # Merge changes
            updated_client = xray_config_pb2.Client(
                email=new_email if new_email else email,
                password=new_password if new_password else current['password'],
                method=new_method if new_method else current['method']
            )

            response = self.stub.UpdateClient(
                xray_config_pb2.UpdateClientRequest(
                    email=email,
                    client=updated_client
                )
            )
            return response.success, response.message
        except grpc.RpcError as e:
            return False, f"RPC Error: {e.code()}: {e.details()}"

    def delete_client(self, email: str) -> Tuple[bool, str]:
        """Remove client by email"""
        try:
            response = self.stub.DeleteClient(
                xray_config_pb2.DeleteClientRequest(email=email)
            )
            return response.success, response.message
        except grpc.RpcError as e:
            return False, f"RPC Error: {e.code()}: {e.details()}"


# Пример использования
if __name__ == '__main__':
    with XrayConfigClient() as client:
        # Создание клиента
        success, msg = client.create_client(
            email="new.user@example.com",
            password="strongpassword123",
            method="chacha20-poly1305"
        )
        print(f"Create: {success} - {msg}")

        # Чтение клиента
        user_data = client.read_client("new.user@example.com")
        print("Read:", user_data)

        # Обновление клиента
        success, msg = client.update_client(
            email="new.user@example.com",
            new_password="evenstronger456"
        )
        print(f"Update: {success} - {msg}")

        # Удаление клиента
        success, msg = client.delete_client("new.user@example.com")
        print(f"Delete: {success} - {msg}")