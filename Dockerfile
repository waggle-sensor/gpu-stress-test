FROM waggle/plugin-base:1.1.1-ml

COPY . .

ENTRYPOINT [ "python3", "stress.py"]
# Updating the number of seconds to run a gpu burn test.
# the -m 5 is no longe accurate
CMD ["-r 300"]
