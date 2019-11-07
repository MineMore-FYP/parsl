from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


from python1 import *
from python2 import *

@python_app
def fun_1(i):
	return x*i

@python_app
def fun_2(i):
	return y*i

@python_app
def app_sum(inputs=[]):
    return sum(inputs)

ranges = range(1,11)
mapped= []

	
for i in ranges:
	x1 = fun_2(i)
	mapped.append(x1.result())

print(mapped)
