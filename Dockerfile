FROM waggle/plugin-torch:1.4.0

COPY . .

ENTRYPOINT [ "python3", "stress.py" ]
