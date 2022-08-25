import argparse
import logging
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
parser.add_argument(
    "-d",
    "--delay",
    nargs="?",
    default=0,
    type=float,
    help="Number of seconds to delay before running the stress test",
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)

logging.info(f"Delay before GPU stress test loop [{args.delay}s]")
time.sleep(args.delay)

x = torch.linspace(0, 4, 16 * 1024 ** 2).cuda()

timeout = time.time() + args.runtime

logging.info(f"Running GPU stress test loop [{args.runtime}s]")
while True:
    x = x * (1.0 - x)
    if time.time() > timeout:
        sys.exit(os.EX_OK)
