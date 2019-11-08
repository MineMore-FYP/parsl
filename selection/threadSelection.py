from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)
from selectUserDefinedColumns import *


@python_app
