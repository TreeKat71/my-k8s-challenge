VERSION=$1  # kubeadm=1.23.0-00

apt-mark unhold kubeadm && \
apt-get update && \
apt-get install -y kubeadm=$VERSION && \
apt-mark hold kubeadm

if  [ $2 = "--client" ]; then
    apt-mark unhold kubectl && \
    apt-get install -y kubectl=$VERSION && \
    apt-mark hold kubectl
fi

kubeadm version