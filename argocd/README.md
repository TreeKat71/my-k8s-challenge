# Steps

1. Install ArgoCD
2. For ingress
    - edit the deployment
3. Login the UI
    - get the admin credential



## Install ArgoCD
This is just the simplest setup, which is not recommended for production.
```bash
$ kubectl create namespace argocd

$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## For ingress
Edit the deployment : argocd-server `command` 
```bash
spec:
  template:
    spec:
      containers:
      - name: argocd-server
        command:
        - argocd-server
        - --rootpath    <--- add this
        - /argocd       <--- add this
```

## Get the admin credential
```bash
$ kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d 
```




---
# ArgoCD Introduction

### Manages
- the same cluster, which ArgoCD is on
- external clusters

### Supports
- YAML
- Helm
- Kustomize
- ...


### Application
| Description     | Key         | Value                   |
| --------------- | ----------- | ----------------------- |
| What to deploy  | source      | git repository & path   |
| Where to deploy | destination | k8s cluster & namespace |



        
<!-- https://github.com/argoproj-labs/argocd-autopilot -->
<!-- https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/ -->