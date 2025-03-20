# xray-config-service

A gRPC service for dynamic management of Xray user configurations with hot-reload support.

## Prerequisites

### 1. Xray Core Installation
Ensure **Xray-core** is installed and configured on your server:
```bash
sudo bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

### 2. Hot-Reload Setup
The service requires systemd watchers to automatically restart Xray when the config file changes.

Create the following systemd units:

/etc/systemd/system/xray-restart.service
```
[Unit]
Description=Restart Xray service on config change

[Service]
Type=oneshot
ExecStart=/usr/bin/systemctl restart xray
```

/etc/systemd/system/xray-restart.path
```
[Unit]
Description=Monitor Xray config for changes

[Path]
PathModified=/usr/local/etc/xray/config.json

[Install]
WantedBy=multi-user.target
```

bash
```
systemctl daemon-reload
systemctl enable xray-restart.path
systemctl start xray-restart.path
```

### 3. Host Dockerfile setup
```
git clone git@github.com:MrInsome/xray-config-service.git /app
docker build -t xray-config-service /app/
docker run -d --name xray-config --restart unless-stopped -v /usr/local/etc/xray/:/usr/local/etc/xray/ -p 50051:50051 xray-config-service
```
### 4. Usage Examples

Sample client implementation in xray-config-service/xray/client.py

### 5. Limitations (Current Version)

Protocol Support:
Only Shadowsocks accounts can be managed.
