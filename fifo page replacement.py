import sys
pattern = raw_input("Enter page accesses as a case sensitive string, one character an access: ")
num = int(raw_input("Enter size of cache"))
cache = []
for i in range(0,num):
	cache.append("")
faults = 0

print("Ref, Fault?, Page Contents\n")
for page in str(pattern):
	sys.stdout.write(page + ', ')
	found = False
	for i in range(0,num):
		if cache[i] ==  page:
			found = True
	if found == False:
		sys.stdout.write("Yes, ")
		cache.insert(0,page)
		faults = faults + 1
	else:
		sys.stdout.write("No, ")
		
	for i in range(0,num):
		sys.stdout.write(cache[i] + ', ')
	sys.stdout.write("\n")