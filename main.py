import psutil
import json
import time
from pypresence import Presence
with open("app.json", "r") as read:
    file=json.load(read)
print(file)
RPC = Presence(835141269801009176)
a=0
actual=0
start_time=time.time()
while True:
	pids=psutil.pids()
	for i in range(0,len(pids)) :
		for x,var in file["app"].items():
			try:
				process= psutil.Process(pids[i])
				if process.name()==x and process.status()=='running':
					actual=process
					RPC = Presence(file['app'][x]['id'])
					RPC.connect() 
					RPC.update(state=str(file['app'][x]['state']),
						large_image="icon",start=start_time,)
					a=1
					print(process.status())
				elif process.name()==x:
					print(closing)
			except:
				i=0
				#sleep(1)
	try:
		if a==1 and actual.status()=='sleeping':
			print('sleeping')
		else:
			RPC.clear()
			print("cleaned!")
	except:
		pass