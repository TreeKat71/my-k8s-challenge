VERSION=$1  # kubeadm=1.22.0-00

apt-get update
apt-get install -y apt-transport-https ca-certificates curl
# Download the Google Cloud public signing key
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
# Add the Kubernetes apt repository
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
# Install kubelet, kubeadm and kubectl
apt-get update
apt-get install -y kubeadm=$VERSION kubelet=$VERSION
apt-mark hold kubelet kubeadm

if  [ "$2" = "--client" ]; then
    apt-get install -y kubectl=$VERSION
    apt-mark hold kubectl
fi
