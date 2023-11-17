import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(root, 'backend', 'headless')
sys.path += [root, backend_path]

os.chdir(root)

from webui import *
