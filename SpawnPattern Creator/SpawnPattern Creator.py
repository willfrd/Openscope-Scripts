HD = int(input("Insert No. of hours oppened a day: "))

Nat = input("I(nbound)/O(utbound): ") #Nature of the operation
while Nat != "I" and Nat != "O":
    Nat = input("I(nbound)/O(utbound): ")

#for i in range

PriApt = "GCRR" #Input primary aiport
SecApt = input("Secondary Airport? ") #Input second airport
while len(SecApt) != 4:
    SecApt = input("Secondary Airport? ")

if Nat == "I":
    Org = SecApt #Define Origin
    Dest = PriApt #Define Destination
    Nat = "arrival"
elif Nat == "O":
    Org = PriApt #Define Origin
    Dest = SecApt #Define Destination
    Nat = "departure"

import ProcData
Proc = input("Insert procedure: ") #Input specific standard procedure
while len(Proc) != 7 and len(Proc) != 5 or ProcData.ProcCheck(Proc, Nat) == False:
    Proc = input("Insert procedure: ")

Alt, Sp, Rwy = ProcData.AltSp(Proc, Nat)

if len(Proc) == 7:
    Wpt = Proc[:5]
else:
    Wpt = Proc[:3]
#print(Proc[0:5])

#NoFPW = int(input("Input total number of flights a week: ")) #Of all airlines through this procedure and SecApt
NoFPW = 0

OpList = [] #Operation list
NoA = int(input("Number of Airlines: ")) #Number of airlines through this procedure and SecApt
for j in range (NoA):
    Op = [] #Specific Operation

    Airline = input("Airline "+ str(j+1)+ ": ")
    while len(Airline) != 3 and Airline[3] != "/":
        Airline = input("Airline "+ str(j+1)+ ": ")
    
    FW = int(input("Frequency weight airline "+ str(j+1)+ ": ")) #Frequency Weight (with respect to other airlines)

    NoFPW = NoFPW + FW
    
    Op.append(Airline)
    Op.append(FW)
    OpList.append(Op)
print(OpList)

Rate = NoFPW / (7 * HD)
#print(Rate)

f=open("SpawnPattern.txt","a")

f.write("        {" + "\n")
f.write('            "origin": "' + Org + '",' + "\n")
f.write('            "destination": "' + Dest + '",' + "\n")
f.write('            "category": "' + Nat + '",' + "\n")
if Nat == "arrival":
    f.write('            "route": "' + Wpt + "." + Proc + "." + PriApt + Rwy + '",' +"\n")
    f.write('            "altitude": ' + str(Alt) +"," + "\n")
    f.write('            "speed": ' + str(Sp) + "," + "\n")
else:
    f.write('            "route": "' + PriApt + Rwy + "." + Proc + "." + Wpt + '",' +"\n") #Add Airway Capability
    f.write('            "altitude": "",' + "\n")
    f.write('            "speed": "",'+ "\n")

f.write('            "method": "random",' + "\n") #Maybe could be improved
f.write('            "rate": ' + str(Rate) + "," + "\n")
f.write('            "airlines": [' + "\n")
if len(OpList) != 1:
    for k in range(len(OpList) - 1):
        Op = OpList[k]
        f.write('                ["' + Op[0] + '", ' + str(Op[1]) + "]," + "\n")
    Op = OpList[NoA-1]
    f.write('                ["' + Op[0] + '", ' + str(Op[1]) + "]" + "\n")
else:
    Op = OpList[0]
    f.write('                ["' + Op[0] + '", ' + str(Op[1]) + "]" + "\n")
f.write("            ]"+ "\n")
f.write("        }," + "\n")

f.close()

