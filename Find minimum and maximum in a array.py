# find the min and max


arr = [7,3,4,9,5]
length = len(arr)
'''

max = 0

for i in arr:
	if i > max:
		max = i

min = 7
for i in arr:
	if i <min:
		min = i

print(max,min)		
			
'''	
max = arr[0]
min = arr[0]
for i in range(1,length):
	if max< arr[i]:
		max = arr[i]
for i in range(1,length):		
	if arr[i]<min:
		min = arr[i]	
print(max,min)		







