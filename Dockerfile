FROM nvcr.io/nvidia/l4t-ml:r32.4.3-py3

COPY . .

ENTRYPOINT [ "python3", "stress.py"]
CMD ["-m 1"]
