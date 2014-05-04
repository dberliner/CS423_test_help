import sys
pattern = raw_input("Enter page accesses as a case sensitive string, one character an access: ")
num = int(raw_input("Enter size of cache"))
cache = []
list = {}
for i in pattern:
	if i not in list.keys():
		list[i] = 0

for i in range(0,num):
	cache.append("")

faults = 0
evictions = 0
accessTime = 0

print("Ref, Fault?, Eviction?, Page Contents\n")
for page in str(pattern):
	sys.stdout.write(page + ', ')
	found = False
	#Go though the cache and see if the page is current in
	for i in range(0,num):
		if cache[i] ==  page:
			found = True
			
	#If the page is not current in the cache we need to evict something
	if found == False:
		sys.stdout.write("Yes, ")
		#figure out which page to evict
		least = sys.maxint
		leastIndex = 0
		for index in range(0,len(cache)):
			item = cache[index]
			# if the item is none evict immediately
			if item == "":
				cache[index] = page
				least = sys.maxint
				break
			else:
				if list[item] < least: # If this page hasn't been accesed in longer than the current least, set it for replacement
					least = list[item]
					leastIndex=index
		if least != sys.maxint: # evict the page if applicable.
			cache[leastIndex] = page
			evictions = evictions + 1
			sys.stdout.write("Yes, ")
		else:
			sys.stdout.write("No , ")
			
		faults = faults + 1
	else:
		sys.stdout.write("No , No , ")
		
	list[page] = accessTime
	accessTime = accessTime + 1
		
	for i in range(0,num):
		if cache[i] != "":
			sys.stdout.write(cache[i] + '(' + str(list[cache[i]]) + '), ')
		else:
			sys.stdout.write(cache[i] + ', ')
			
	sys.stdout.write("\n")
print("Total faults: " + str(faults)) 
print("Total evictions: " + str(evictions)) 