import psutil
import json
from time import*
import time
from pypresence import Presence
with open("app.json", "r") as read:
    file=json.load(read)
RPC = Presence(835141269801009176)
a=0
actual=0
start_time=time.time()
close=True
while True:
	pids=psutil.pids()
	for i in range(0,len(pids)) :
		for x,var in file["app"].items():
			try:
				process= psutil.Process(pids[i])
			except:
				pass
			try:
				if process.name()==x and process.status()=='running':
					actual=process
					RPC=Presence(file['app'][x]['id'])
					RPC.connect()
					while close is True:
						try:
							process.status()
							RPC.update(state=str(file['app'][x]['state']),large_image="icon",start=start_time,)
						except:
							close=False
					RPC.clear()
			except:
				pass
		close=True
		x=0
		i=0
	sleep(1)