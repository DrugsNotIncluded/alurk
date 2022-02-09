# Improved Alpine's Package manager
from src import apk, abuild
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
del_parser = subparsers.add_parser('del')
update_parser = subparsers.add_parser('update')
upgrade_parser = subparsers.add_parser('upgrade')

