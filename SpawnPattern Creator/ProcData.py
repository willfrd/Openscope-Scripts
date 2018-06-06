def ProcCheck(Proc, Nat):
    if Nat == "arrival":
        ProcList = ["DEVLA3P", "DEVLA3Q", "TERTO7P", "TERTO4Q", "LARYS2P", "LARYS2X", "RASEP2P", "RASEP2Q"] #Arrival Procedures
    else:
        ProcList =["SAMAR6M", "SAMAR5N", "SAMAR1Y", "VASTO6M", "VASTO5N", "VASTO1Y", "KORAL6M", "KORAL5N", "KORAL1V", "KORAL1W", "LORPO3M", "LORPO1N", "LARYS1M", "LARYS1N"] #Departure Procedures
    Res = False
    i = 0
    while Res == False and i < len(ProcList):
        if Proc == ProcList[i]:
            Res = True
        i = i + 1
    return Res
    
def AltSp(Proc, Nat):
    if Nat == "arrival":
        Alt = 0
        Sp = 0
        Rwy = "03"
##        if Proc == "DEVLA3P":
##            Alt = 25000
##            Sp = 450
##            Rwy = "03"
##        elif Proc == "DEVLA3Q":
##            Alt = 25000
##            Sp = 450
##            Rwy = "21"
##        elif Proc == "TERTO7P":
##            Alt = 30000
##            Sp = 480
##            Rwy = "03"
##        elif Proc == "TERTO4Q":
##            Alt = 21000
##            Sp = 400
##            Rwy = "21"
##        elif Proc == "LARYS2P":
##            Alt = 
##            Sp = 
##            Rwy = "03"
##        elif Proc == "LARYS2X":
##            Alt = 
##            Sp = 
##            Rwy = "21"
##        elif Proc == "RASEP2P":
##            Alt = 11000 or 13000 [ATR] and 15000 [CRJ]
##            Sp = 270 [ATR] and 380 [CRJ]
##            Rwy = "03"
##        elif Proc == "RASEP2Q":
##            Alt = 11000 or 13000 [ATR] and 15000 [CRJ]
##            Sp = 270 [ATR] and 380 [CRJ]
##            Rwy = "21"
    else:
        Alt = 0
        Sp = 0
        if Proc == "SAMAR6M" or Proc == "SAMAR1Y" or Proc == "VASTO6M" or Proc == "VASTO1Y" or Proc == "KORAL6M" or Proc == "KORAL1V" or Proc == "LORPO3M" or Proc == "LARYS1M":
            Rwy = "03"
        elif Proc == "SAMAR5N" or Proc == "VASTO5N" or Proc == "KORAL5N" or Proc == "KORAL1W" or Proc == "LORPO1N" or Proc == "LARYS1N":
            Rwy = "21"
    return Alt, Sp, Rwy
            
        
