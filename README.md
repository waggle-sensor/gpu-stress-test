# gpu-stress-test

This is a simple piece of PyTorch code to stress test a GPU.

## Buildx building and pushing to Dockerhub

```
docker buildx build -t iperezx/gpu-stress-test:latest --platform linux/amd64,linux/arm/v7,linux/arm64 --push .
```

## Build and run on device
```
docker build -t iperezx/gpu-stress-test:latest .
```
The docker has an entrypoint and a default value in the cmd. The python script expects to be pass in the number of minutes to run the stress test. 
Python usage:
```
python stress.py -m 1
```
Docker usage:
```
docker run -it --rm --runtime nvidia --network host iperezx/gpu-stress-test:latest
```
Docker usage with changing the number of minutes to 2:
```
docker run -it --rm --runtime nvidia --network host iperezx/gpu-stress-test:latest -m 2
```

Push image to Dockerhub:
```
docker push iperezx/gpu-stress-test:latest
```

## Kubernetes Cronjob
The cronjob is meant to run the gpu stress in a periodic fashion.
```
kubectl create -f cronjob.yaml
```

Check if it was created:
```
kubectl get cronjobs
```

Watch until one is created:
```
kubectl get jobs --watch
```

Delete cronjob:
```
kubectl delete -f cronjob.yaml
```

