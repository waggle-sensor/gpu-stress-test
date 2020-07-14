# gpu-stress-test

This is a simple piece of PyTorch code to stress test a GPU.

## Building and Pushing to Dockerhub

```sh
docker buildx build -t waggle/gpu-stress-test --platform linux/amd64,linux/arm/v7 --push .
```
