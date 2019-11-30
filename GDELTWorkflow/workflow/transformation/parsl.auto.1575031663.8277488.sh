
		source /etc/profile
		source ~/.profile
		
process_worker_pool.py  --max_workers=2 -p 0 -c 1.0 -m None --poll 10 --task_url=tcp://10.0.0.1:54985 --result_url=tcp://10.0.0.1:54882 --logdir=/home/mpiuser/Documents/FYP/parsl/GDELTWorkflow/workflow/transformation/remote_htex --block_id=0 --hb_period=30 --hb_threshold=120 