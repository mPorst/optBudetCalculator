import time

### Change the following 3 lines
fileName = "VK.rpt"    # The file name
searchString = "--- CSAT alt: any - neu: scalar NaN - Differenz: "    # The string with which you can identify all relevant budget lines in the file
budget = 1.13322e+006 + 15000   # value of budget at point of crash

calculationErrors = 0; # DO NOT CHANGE

print("Das Budget beträgt ", budget, "€.")

with open(fileName,"r") as f:
    for myString in f:
        if(myString.find(searchString) != -1):
            myString = myString.split(searchString)  # Split the string at 
            print (myString) # What remains: ['(...)','-30000. (...)']; so get the -30000
            myString = myString[1].split('.')
            try:
                budget = budget + float(myString[0])
                print("Addiere zum CSAT-Budget den Wert >>", float(myString[0]), "€ << , Ergebnis: ", budget, "€")
            except:
                print(">>>>>>>>>> Ein Wert konnte nicht erkannt werden:", myString[0], " ; ueberspringe...")
                calculationErrors = calculationErrors + 1

print("The calculated budget is: ", budget, "€")
print(calculationErrors, " error occured in the calculation.")
if( calculationErrors > 0 ):
    print("This usually happens when e.g. the value \"any\" was added or subtracted. Please find the line, it is highlighted by several arrows: \">>>\" ")
else:
    print("Everything is fine since no errors occurred")

f.close()
input("Press enter to exit ;)")
        
    
