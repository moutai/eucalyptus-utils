import os
import subprocess

s=[]
f = open('eucamap.txt', 'w')
f.write('VNET_MACMAP=\"')
for ip in range(13,240):
	# generate the ip 
	ipadd="=10.80.160."+str(ip)+" "
	# generate the mac
	p = subprocess.Popen("sh easymac.sh -x | awk -F \" \" \'{print $4}\'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
    		mac=line.strip().rstrip()
		break
	#retval = p.wait()
	#print mac
	#concat together
	pair= mac+ipadd
	#print pair
	# write the pair
	f.write(pair)	
f.write('\"')
f.close()


