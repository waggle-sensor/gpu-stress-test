# gpu-stress-test

This is a simple piece of PyTorch code to stress test a GPU.

## Building and Pushing to Dockerhub

```sh
docker buildx build -t waggle/gpu-stress-test --platform linux/amd64,linux/arm/v7,linux/arm64 --push .
```

*Note*: Building on MacOS resulted in the following error
(`failed to solve: rpc error: code = Unknown desc = failed to copy: unexpected EOF`) when
building the `linux/arm64` platform. This was resolved by building and pushing on
a true Ubuntu:18.04 host.
