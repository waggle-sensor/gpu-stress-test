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

## Running the gpu-stress-test container

### amd64 platform

For the latest nvidia-container-runtime version use

```
docker run -ti --rm \
  --gpus all \
  gpu_stress_test
```

otherwise use

```
docker run -ti --rm \
  --runtime nvidia \
  gpu_stress_test
```

### armv7 platform

TBD

### arm64 platform

```
docker run -ti --rm \
  --device=/dev/nvhost-ctrl \
  --device=/dev/nvhost-ctrl-gpu \
  --device=/dev/nvhost-prof-gpu \
  --device=/dev/nvmap \
  --device=/dev/nvhost-gpu \
  --device=/dev/nvhost-as-gpu \
  --env LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/tegra \
  -v /usr/lib/aarch64-linux-gnu/tegra:/usr/lib/aarch64-linux-gnu/tegra \
  gpu_stress_test
```
