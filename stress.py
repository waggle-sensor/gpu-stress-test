import argparse
import os
import sys
import time

import torch

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m", "--Minutes", nargs="?", const=5, type=int, help="Number of minutes to run the stress test"
)
args = parser.parse_args()

num_minutes = float(args.Minutes)

x = torch.linspace(0, 4, 16 * 1024 ** 2).cuda()

timeout = time.time() + 60 * num_minutes

while True:
    x = x * (1.0 - x)
    if time.time() > timeout:
        sys.exit(os.EX_OK)
