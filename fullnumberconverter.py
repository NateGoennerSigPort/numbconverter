repeater =  True
while (repeater == True):
    print("Welcome to EZ Converter")
    selector = int(input("Please select the conversion you wish to preform.\n1. For Number to Hexadecimal.\n2. For Hexadecimal to Number.\n3. For Number to Binary\n"))
    if (selector == 1):
        print("Welcome to Number to Hexadecimal Converter")
        orgnum = int(input("Please enter number to convert "))
        def NumbertoHex(orgnum):
            hexdec = ""
            remain = 0
            hexadd = ""
            possiblelet = 0
            while (orgnum != 0):
                remain = orgnum % 16
                orgnum = orgnum // 16
                if ((remain > 9 and remain < 16)):
                    possiblelet = remain - 10
                    if (possiblelet == 0):
                        hexadd = "A"
                    if (possiblelet == 1):
                        hexadd = "B"
                    if (possiblelet == 2):
                        hexadd = "C"
                    if (possiblelet == 3):
                        hexadd = "D"
                    if (possiblelet == 4):
                        hexadd = "E"
                    if (possiblelet == 5):
                        hexadd = "F"
                else:
                    hexadd = str(remain)
                hexdec = hexadd + hexdec    
            return hexdec
        print("Your hexadecimal is", NumbertoHex(orgnum))
    if (selector == 2):
        print("Welcome to Hexadecimal to Number Converter")
        hexadec = input("Please enter your Hexadecimal ")
        newdec = int(hexadec,16)
        print("Your converted decimal is", newdec)
    if (selector == 3):
        print("Welcome to Number to Binary Converter")
        numorg = int(input("Please enter your number to convert "))
        binnumber = ""
        while (numorg >= 1):
            newreemain = str(numorg % 2)
            binnumber = binnumber + newreemain
            numorg = numorg // 2
        binnumber = binnumber[::-1]
        print(binnumber)
    x = input("Done Converting? Input 1\nTo Continue Input Anything Else\n")
    if (x == "1"):
        repeater = False
    
