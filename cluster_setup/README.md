# Steps

1. Install container runtime
    - docker (dockershim will be deprecated soon)
    - containerd
    - CRI-O
2. Install `kubeadm`
3. Create cluster



## Install containerd
```bash
# Excute on all nodes
```



## Install `kubeadm`
> This script will install not only `kubeadm`, but also `kubelet`.

```bash
# Excute on all nodes
$ sudo sh kubeadm.sh <kubeadm_version>

> sudo sh kubeadm.sh 1.22.0-00
```



## Create kubernetes cluster

### Initializing controlplane
```bash
$ kubeadm init <args>   
```
|  args     | description  |
| :----     |  :---- |
| --apiserver-advertise-address  | kubeadm uses the network interface associated with the default gateway to set the advertise address for this particular control-plane node's API server. To use a different network interface, specify the --apiserver-advertise-address=\<ip-address\> |
| --cri-socket  | Specify it if more than one container runtime installed on the provisioned node |
| --control-plane-endpoint  | Endpoint can be either a DNS name or an IP address of a load-balancer. |
| --pod-network-cidr  | Depending on which third-party provider you choose, you might need to set this to a provider-specific value |


### Configure `kubectl`
> To access the cluster as admin, we need to set the credential

```bash
# Excute on your laptop
$ mkdir -p $HOME/.kube
$ scp <controlplane-ip>:/etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config

$ kubectl get node

NAME           STATUS     ROLES                  AGE   VERSION
controlplane   NotReady   control-plane,master   79s   v1.22.0
```



### Installing Pod network
> Here we use weave as an example. You can pick whichever CNI plugin fits your need.

```bash
$ kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```



### Joining nodes
```bash
(node)$ kubeadm join <controlplane-ip>:<controlplane-port> \
--token <token> \
--discovery-token-ca-cert-hash sha256:<hash>
```


---

Found mistakes?
------------


Feel free to contact me through
[email](mailto:muller79924@gmail.com)
in english or chinese.
