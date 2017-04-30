from collections import defaultdict 
import sys

n = 2
fileName = sys.argv[1]
if len(sys.argv) > 2:

	n = int(sys.argv[2])
	fileName = sys.argv[3]
	
graph = open(fileName + '.txt')
listOfteams = defaultdict(list)
connection = defaultdict(list)
key = 1
totalCon = 0
Q = 0

for line in graph:
	
	line.rstrip()
	parts = line.split()
	
	team1 = parts[0]
	team2 = parts[1]
	
	connection[team1].append(team2)
	connection[team2].append(team1)

print(connection.keys())
for k in connection.keys():    
	listOfteams['omada' + str(key)].append(k)
	key = key + 1
	
for l in connection.keys():
	totalCon = len(connection[l]) + totalCon
	
for team in connection.keys():
	sum = - (len(connection[team])/totalCon)**2
	Q = Q + sum

while len(listOfteams.keys()) > n:
	
	maxDQ = 0
	deletedKey1 = 0
	deletedKey2 = 0	
			
	for i in listOfteams.keys():                                                
		for j in listOfteams.keys():                                           	
			if i != j:
				counter = 0
				counteri = 0
				counterj = 0
				
				for x in listOfteams[i]:                                            
					for x1 in listOfteams[i]:                                      
					
						z = len(connection[x1]) - connection[x1].count(x)
						counteri = counteri + z
						
					for y in listOfteams[j]:                                  
						for y1 in listOfteams[j]:                             
						
							z = len(connection[y1]) - connection[y1].count(y)
							counter = counter + z
							
						if x in connection[y]:
							counterj = counterj + 1
			
				aiaj = (counteri/totalCon) * (counterj/totalCon)
				eij = counter/totalCon
				DQ = 2 * (eij - aiaj)
				
				if maxDQ < DQ:
					maxDQ = DQ
					Q = Q + DQ
					deletedKey1 = i
					deletedKey2 = j
					
	for o in listOfteams[deletedKey1]:
		listOfteams[key].append(o)
				
	for h in listOfteams[deletedKey2]:
		listOfteams[key].append(h)
				
	listOfteams.pop(deletedKey1, None)
	listOfteams.pop(deletedKey2, None)
	key = key + 1
	
for v in listOfteams.keys():
	print (listOfteams[v])
print (Q)

graph.close()
