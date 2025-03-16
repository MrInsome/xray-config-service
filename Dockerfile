FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache libstdc++ && \
    pip install --no-cache-dir grpcio protobuf

COPY xray/xray_config_service.py .
COPY proto/generated/ proto/generated/

VOLUME /usr/local/etc/xray/

EXPOSE 50051

CMD ["python", "xray_config_service.py"]