tcase=int(input())
for i in range(tcase):
	jobs=input().split()
	total=int(jobs[0])
	uncompleted=int(jobs[1])
	completed=input().split()
	for j in range(total-uncompleted):
		completed[j]=int(completed[j])
	completed.sort()
	for j in range(len(completed)):
		print(completed[j],end=' ')
		j+=1
	for j in range(1,len(completed)):
		print(completed[j],end=' ')
		j+=1
