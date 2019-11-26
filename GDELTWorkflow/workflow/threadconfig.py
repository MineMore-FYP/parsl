from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

maxThreads = 4
local_threads = Config(
    executors=[
        ThreadPoolExecutor(
            max_threads=maxThreads,
            label='local_threads'
        )
    ]
)

