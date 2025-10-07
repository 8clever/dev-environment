
import argparse

prog = argparse.ArgumentParser("dev_environments")

prog.add_argument("action", choices=['add', 'list', 'rm'], help="Action")

args = prog.parse_args()

if args.action == 'add':
  import add
if args.action == 'list':
  import list
if args.action == 'rm':
  import rm