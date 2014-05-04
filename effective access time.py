print("Time unit is not important as long as it is consistent across inputs \n")

tlbTime = float(raw_input("TLB lookup time: "))
memCycle = float(raw_input("Time to access memory: "))
ratio = raw_input("hit ratio as decimal 0-1 (leave blank if fraction given): ")
ratioNum = raw_input("hit ratio numerator (leave blank if decimal given): ")
ratioDen = raw_input("hit ratio denominator (leave blank if decimal given): ")
ptnum = int(raw_input("Enter number of page table levels: "))
if ratio == "":
	ratio = float(ratioNum) / float(rationDen)
else: 
	ratio = float(ratio)

EAT = (memCycle + tlbTime) * ratio + (ptnum * memCycle + tlbTime) * (1 - ratio)

print("Effective Access Time = " + str(EAT))

raw_input("Press enter to exit")