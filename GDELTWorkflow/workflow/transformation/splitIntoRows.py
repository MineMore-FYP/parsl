import pandas as pd
import numpy as np

import parsl

from parsl.config import Config
from parsl.providers import AdHocProvider
from parsl.channels import SSHChannel
from parsl.addresses import address_by_query
from parsl.executors import HighThroughputExecutor

from parsl.providers import LocalProvider
from parsl.channels import LocalChannel
from parsl.executors import HighThroughputExecutor

from datetime import datetime

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

#from userScript import userDefinedColumsToAggregate

user_opts = {'adhoc':
             {'username': 'mpiuser',
              'script_dir': '/home/mpiuser/Documents/FYP/parsl/GDELTWorkflow/workflow/transformation',
              'remote_hostnames': ['10.0.0.1','10.0.0.2']
             }
}

remote_htex = Config(
    executors=[
	
        HighThroughputExecutor(
            label='remote_htex',
	    address = '10.0.0.1',
            max_workers=2,
            #address=address_by_query(),
            worker_logdir_root=user_opts['adhoc']['script_dir'],
            provider=AdHocProvider(
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init="""
		source /etc/profile
		source ~/.profile
		""",
                channels=[SSHChannel(hostname=m,
                                     username=user_opts['adhoc']['username'],
                                     script_dir=user_opts['adhoc']['script_dir'],
                ) for m in user_opts['adhoc']['remote_hostnames']]
            )
        ),
	HighThroughputExecutor(
            label="htex_Local",
            worker_debug=True,
            cores_per_worker=1,
            provider=LocalProvider(
                channel=LocalChannel(),
                init_blocks=1,
                max_blocks=1,
            ),
        )
    ],
    max_idletime=2.0,
    #  AdHoc Clusters should not be setup with scaling strategy.
    strategy=None,
)

df = pd.read_csv("/home/mpiuser/Documents/FYP/test4.csv")
columnsToAggregate = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]

import parsl
from parsl import load, python_app
#from parsl.configs.local_threads import config
#load(config)
parsl.load(remote_htex)

@python_app
def splitIntoRows(startRowIndex, endRowIndex, dFrame, columnsToAggregate):
	import pandas as pd
	import numpy as np
	df = pd.DataFrame()
	df = dFrame.iloc[np.r_[startRowIndex : endRowIndex] , : ]

	columnList = list(df.columns.values)

	for i in columnsToAggregate:
		column1 = i[0]
		print(i[0])
		#column1index = df.columns.get_loc(column1)
		column2 = i[1]
		#column2index = df.columns.get_loc(column2)
		newColumn = i[2]
		newColumnList = []

		newColumnList = columnList
		newColumnList.remove(column1)
		newColumnList.remove(column2)
		newColumnList.append(newColumn)

		print(newColumnList)
	

		dfNew = pd.DataFrame(columns = newColumnList)
		#print(dfNew)

		for index,row in df.iterrows():

			if row[column1] == row[column2]:
				x = row[column1]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)

			elif not row.notnull()[column1] and not row.notnull()[column2]:
				#print("2")
				print("both null")

			elif row.notnull()[column1] and not row.notnull()[column2]:
				#print("3")
				x = row[column1]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)

			elif row.notnull()[column2] and not row.notnull()[column1]:
				#print("4")
				x = row[column2]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)
			else:
				x = row[column1]
				y = row[column2]

				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd1 = pd.Series([x], index=[newColumn])
				rowAdd2 = pd.Series([y], index=[newColumn])	
				row1 = row.append(rowAdd1)
				dfNew = dfNew.append(row1, ignore_index=True)
				row2 = row.append(rowAdd2)
				dfNew = dfNew.append(row2, ignore_index=True)
				print(row)
			


		#print(dfNew)
		return dfNew
		#dfNew.to_csv ("/home/amanda/FYP/testcsv/RFout1.csv", index = False, header=True)

def getDuration(startTime,endTime):
	difference = endTime - startTime
	#difference = difference.strftime("%H:%M:%S")
	return difference

startTime = datetime.now().replace(microsecond=0)
print('Start Time: ' + str(startTime) + '\n')


maxDivs = 10
results = []
numOfRows = df.shape[0]

#df1 = splitIntoRows(0,100,df,columnsToAggregate)
#print(df1.result())

for i in range(0,200000,2000):
	df1 = splitIntoRows(i,i+2000,df,columnsToAggregate)
	print(i)
	results.append(df1)

# Wait for all apps to finish and collect the results
outputs = [i.result() for i in results]

endTime = datetime.now().replace(microsecond=0)

print('\nEnd Time: ' + str(endTime) + ' Caluculation Done!\n')
print('Duration ' + str(getDuration(startTime,endTime)))

# Print results
print(outputs)


