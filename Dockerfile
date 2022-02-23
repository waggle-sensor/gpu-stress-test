FROM waggle/plugin-base:1.1.1-ml

COPY . .

ENTRYPOINT [ "python3", "stress.py"]
CMD ["-m 5"]