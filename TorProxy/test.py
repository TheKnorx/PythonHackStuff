import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", type=str, help="starts Tor and returns socket Object", required=False)
group.add_argument("-r", type=str, help="restarts Tor and returns socket object", required=False)
group.add_argument("-c", type=str, help="closes Tor and resets the proxy", required=False)
args = parser.parse_args()

print(args.t)