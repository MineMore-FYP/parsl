from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

# Map function that returns double the input integer
@python_app
def app_double(x):
    return x*2

# Reduce function that returns the sum of a list
#@python_app
#def app_sum(inputs=[]):
#    return sum(inputs)

# Create a list of integers
items = range(0,10)


# Map phase: apply an *app* function to each item in list
mapped_results = []
for i in items:
    x = app_double(i)
    print(x)
    print(i)
    #mapped_results.append(x)

# Reduce phase: apply an *app* function to the set of results
#total = app_sum(inputs=mapped_results)

#print(total.result())
