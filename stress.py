import argparse
import os
import sys
import time

import torch

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r",
    "--runtime",
    nargs="?",
    default=300,
    type=int,
    help="Number of seconds to run the stress test",
)
args = parser.parse_args()

x = torch.linspace(0, 4, 16 * 1024 ** 2).cuda()

timeout = time.time() + args.runtime

while True:
    x = x * (1.0 - x)
    if time.time() > timeout:
        sys.exit(os.EX_OK)
