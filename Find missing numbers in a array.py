#1-100 missing values in array

x = [20,56,32,76,44,66,75] 
n = 100
list1 = []

list2 = []
for i in range(1,n+1):
	list1.append(i)
print(list1)	
for i in list1:
	if i not in x:
		list2.append(i)
print(list2)		
		



























