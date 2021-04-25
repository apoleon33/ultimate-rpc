import psutil
import json
from time import*
import time
from pypresence import Presence
with open("app.json", "r") as read:
    file=json.load(read)
print(file)
RPC = Presence(835141269801009176)
a=0
actual=0
start_time=time.time()
close=True
while True:
	pids=psutil.pids()
	for i in range(0,len(pids)) :
		print('ca marche la')
		for x,var in file["app"].items():
			try:
				process= psutil.Process(pids[i])
			except:
				print(4)
				#i=0
			print(2)
			try:
				if process.name()==x and process.status()=='running':
					print(3)
					actual=process
					print(4)
					RPC=Presence(file['app'][x]['id'])
					RPC.connect()
					while close is True:
						try:
							process.status()
							print(5)
							RPC.update(state=str(file['app'][x]['state']),large_image="icon",start=start_time,)
							#a=1
						except:
							close=False
					RPC.clear()
			except:
				pass
		close=True
		x=0
		i=0
	sleep(1)
	'''try:
		if a==1 and actual.status()=='sleeping':
			print('sleeping')
		else:
			#RPC.clear()
			print("cleaned!")
	except:
		pass'''