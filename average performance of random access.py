print("All input fields are integers\n");
print("NOTICE: IN THE SLIDES VALUES ARE SOMETIMES MB = KB*1000 \n")

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


seek = int(raw_input("Enter seek time in ms "))
seek = float(seek)

rotLatency = 1.0/rps * 0.5 * 1000.0 # in ms
SATR = float(rps * sectors * trans)/(1024.0*kbtomb) #in MB
readTime = (float(trans/(1024.0*1000.0))/SATR)*kbtomb # in ms (lovely unit conversions)
totalSeek = seek + rotLatency + readTime # in ms
ETR = float(1/totalSeek) * float(trans/1024.0)

print("Effective transferring rate: " + str(ETR))
raw_input("Press any key to exit");