VERSION=$1  # kubelet=1.23.0-00

apt-mark unhold kubelet && \
apt-get update && \
apt-get install -y kubelet=$VERSION && \
apt-mark hold kubelet

systemctl daemon-reload
systemctl restart kubelet