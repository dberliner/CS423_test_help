print("All input fields are integers\n");
print("NOTICE: IN THE SLIDES THE ANSWER IN MB WAS CALCULATED AS KB/1000 \n")

emulate = int(raw_input("0 to emulate this error, 1 to not: "))
if emulate == 0:
	kbtomb = 1024.0
else: 
	kbtomb=1000.0

rpm = raw_input("RPM (leave blank if rev/sec is given): ")
rps = raw_input("RPS (leave blank if rev/min is given): ")

if rpm != "":
	rps=int(rpm)/60
else:
	rps=int(rps)

trans = int(raw_input("Enter sector size (in bytes)"))
sectors = int(raw_input("Enter sectors per track "))

print("Sustained Average: " + str(rps * sectors * trans) + " bytes per second")
print("Sustained Average: " + str(float(rps * sectors * trans)/1024) + " kb per second")
print("Sustained Average: " + str(float(rps * sectors * trans)/(1024*kbtomb)) + " mb per second")
print("Sustained Average: " + str(float(rps * sectors * trans)/(1024*kbtomb*1024)) + " gb per second")
raw_input("Press any key to exit");