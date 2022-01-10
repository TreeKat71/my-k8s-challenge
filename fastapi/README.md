
## For ingress
Edit the deployment : fastapi `command` 
```bash
spec:
  template:
    spec:
      containers:
      - name: fastapi
        command:
        - /venv/bin/uvicorn
        - ...
        - --root-path    <--- add this
        - /fastapi       <--- add this

# https://fastapi.tiangolo.com/advanced/behind-a-proxy/#proxy-with-a-stripped-path-prefix
```


