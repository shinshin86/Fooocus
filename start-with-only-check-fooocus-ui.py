import os
import sys


def ini_fcbh_args():
    from args_manager import args
    return args


root = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(root, 'backend', 'headless')
sys.path += [root, backend_path]

os.chdir(root)

args = ini_fcbh_args()

from webui import *
