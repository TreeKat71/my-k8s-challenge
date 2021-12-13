# Steps to upgrade a k8s cluster

From the node aspect, the upgrade workflow at high level:
1. Upgrade a primary control plane node.
2. (HA) Upgrade additional control plane nodes.
3. Upgrade worker nodes.

From the component aspect, the upgrade workflow at high level:
1. Upgrade kubeadm
2. Update kubelet configuration
3. Upgrade kubelet (drain the node while you are doing it)

# Controlplane 
## kubeadm upgrade
### For the first controlplane node
```bash
$ sudo sh kubeadm.sh <kubeadm_version>

$ sudo kubeadm upgrade plan
$ sudo kubeadm upgrade apply <cluster_version>
```

### For the other control plane nodes
```bash
$ sudo sh kubeadm.sh <kubeadm_version>

(not sure)$ sudo kubeadm upgrade plan
$ sudo kubeadm upgrade node
```

## kubelet upgrade
> Refer to the `Kubelet upgrade` block

# Worker nodes
## kubeadm upgrade
```bash
$ sudo sh kubeadm.sh <kubeadm_version>

$ sudo kubeadm upgrade node
```

## kubelet upgrade
> Refer to the `Kubelet upgrade` block

# Kubelet upgrade
```bash
$ kubectl drain <node-to-drain> --ignore-daemonsets

$ sudo sh kubelet.sh <kubelet_version>

$ kubectl uncordon <node-to-drain>
```