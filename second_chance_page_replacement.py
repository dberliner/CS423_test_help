import sys
pattern = raw_input("Enter page accesses as a case sensitive string, one character an access: ")
num = int(raw_input("Enter size of cache"))
nitems = 0
cache = []
for i in range(0,num):
  cache.append([' ',' ']) # pair (page, referenced)
faults = 0

print("Ref, Fault?, Page Contents\n")
for page in str(pattern):
  sys.stdout.write(page + ', ')
  found = False
  for i in range(0,num):
    if cache[i][0] ==  page:
      found = True
      cache[i][1] = '*' # set reference bit
      break
  if found == False:
    sys.stdout.write("Yes, ")
    
    if nitems == num: # there is no free space
      # find someone to evict
      deleted = False
      for j in xrange(num - 1, -1, -1):
        if cache[j][1] == '*': # if reference bit set
          cache[j][1] = ' ' # remove reference bit
        elif cache[j][1] == ' ': # if reference bit not set
          del cache[j]
          nitems -= 1
          deleted = True
          break
      if not deleted:
        del cache[num - 1]
        nitems -= 1
        
    cache.insert(0,[page,'*'])
    nitems += 1  
    faults = faults + 1
  else:
    sys.stdout.write("No , ")
    
  for i in range(0,num):
    sys.stdout.write(cache[i][0] + cache[i][1] + ', ')
  sys.stdout.write("\n")
print("Total faults: " + str(faults)) 
