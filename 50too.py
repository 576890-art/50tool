import os
import random
import hashlib
import datetime
import platform

# Clear screen
os.system("clear")

# ================= Logo + Developer Info First =================
print("\033[1;32m")
print("=================================")
print("        ARAFAT TERMUX TOOL")
print("=================================")
print("Developer : Arafat")
print("GitHub    : https://github.com/576890-art")
print("Facebook  : https://www.facebook.com/arafat576890")
print("WhatsApp  : 01989333156")
print("Telegram  : https://t.me/arafat_tech")
print("Email     : arafat342422@gmail.com")
print("=================================\n")

# ================= Main Menu Loop =================
while True:
    print("""
1  Password Generator
2  Termux Auto Install Tool
3  Username Generator
4  Random Number
5  OTP Generator
6  MD5 Hash
7  SHA1 Hash
8  Show Time
9  Show Date
10 Binary Converter
11 Random Emoji
12 Random Color
13 Random Country
14 Random Joke
15 Palindrome Check
16 Text Reverse
17 Word Count
18 Uppercase
19 Lowercase
20 Random Phone
21 Random Email
22 Random Year
23 Random Month
24 Random Day
25 Random Character
26 Random Quote
27 System Info
28 Python Version
29 Show Files
30 Show Current Folder
31 Disk Usage
32 IP Info
33 Ping Test
34 DNS Lookup
35 Create File
36 Read File
37 Delete File
38 Clear Screen
39 Show Calendar
40 Show Uptime
41 Dice Roll
42 Coin Flip
43 Random Game Number
44 Random Password Strength
45 Random Username
46 Random Letter
47 Random Digit
48 About Developer
49 Restart Tool
50 Exit
""")
    choice=input("Select option : ")

    if choice=="1":
        chars="abcdefghijklmnopqrstuvwxyz123456789"
        print("Password:", "".join(random.choice(chars) for i in range(10)))

    elif choice=="2":
        print("\nStarting Termux Auto Install...\n")
        os.system("pkg update -y && pkg upgrade -y")
        os.system("pkg install python -y python2 git wget nano curl figlet lolcat -y")
        print("\nAll packages installed successfully!\n")

    elif choice=="3":
        print("Username:", random.choice(["arafat","coder","dev","tech"]) + str(random.randint(10,999)))

    elif choice=="4":
        print("Random Number:", random.randint(1,10000))

    elif choice=="5":
        print("OTP:", random.randint(100000,999999))

    elif choice=="6":
        text=input("Enter text: ")
        print("MD5:", hashlib.md5(text.encode()).hexdigest())

    elif choice=="7":
        text=input("Enter text: ")
        print("SHA1:", hashlib.sha1(text.encode()).hexdigest())

    elif choice=="8":
        print("Time:", datetime.datetime.now().time())

    elif choice=="9":
        print("Date:", datetime.date.today())

    elif choice=="10":
        num=int(input("Enter number: "))
        print("Binary:", bin(num))

    elif choice=="11":
        print("Emoji:", random.choice(["😀","😎","🔥","🚀","💻"]))

    elif choice=="12":
        print("Color Code:#%06x" % random.randint(0,0xFFFFFF))

    elif choice=="13":
        print("Country:", random.choice(["USA","UK","Germany","Japan","Canada"]))

    elif choice=="14":
        print("Joke:", random.choice(["Why Python? Because it's easy!","Debugging = removing bugs!","Programmer life = coffee + code"]))

    elif choice=="15":
        text=input("Enter word: ")
        print("Palindrome" if text==text[::-1] else "Not Palindrome")

    elif choice=="16":
        text=input("Enter text: ")
        print(text[::-1])

    elif choice=="17":
        text=input("Enter sentence: ")
        print("Word Count:", len(text.split()))

    elif choice=="18":
        text=input("Enter text: ")
        print(text.upper())

    elif choice=="19":
        text=input("Enter text: ")
        print(text.lower())

    elif choice=="20":
        print("Phone Number: 01"+str(random.randint(300000000,999999999)))

    elif choice=="21":
        print("Email:", random.choice(["alex","sam","john","rafi","ali"])+"@gmail.com")

    elif choice=="22":
        print("Year:", random.randint(1990,2030))

    elif choice=="23":
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        print("Month:", random.choice(months))

    elif choice=="24":
        print("Day:", random.randint(1,31))

    elif choice=="25":
        print("Random Character:", random.choice("abcdefghijklmnopqrstuvwxyz"))

    elif choice=="26":
        print("Quote:", random.choice(["Code is life","Stay focused","Never give up"]))

    elif choice=="27":
        print(platform.system(), platform.release())

    elif choice=="28":
        print("Python Version:", platform.python_version())

    elif choice=="29":
        os.system("ls")

    elif choice=="30":
        os.system("pwd")

    elif choice=="31":
        os.system("df -h")

    elif choice=="32":
        os.system("curl ifconfig.me")

    elif choice=="33":
        host=input("Enter host to ping: ")
        os.system(f"ping -c 4 {host}")

    elif choice=="34":
        host=input("Enter host for DNS lookup: ")
        os.system(f"nslookup {host}")

    elif choice=="35":
        fname=input("Enter file name to create: ")
        open(fname,"w").close()
        print(f"{fname} created!")

    elif choice=="36":
        fname=input("Enter file name to read: ")
        if os.path.exists(fname):
            print(open(fname).read())
        else:
            print("File not found")

    elif choice=="37":
        fname=input("Enter file name to delete: ")
        if os.path.exists(fname):
            os.remove(fname)
            print(f"{fname} deleted!")
        else:
            print("File not found")

    elif choice=="38":
        os.system("clear")

    elif choice=="39":
        os.system("cal")

    elif choice=="40":
        os.system("uptime")

    elif choice=="41":
        print("Dice:", random.randint(1,6))

    elif choice=="42":
        print(random.choice(["HEAD","TAIL"]))

    elif choice=="43":
        print("Random Game Number:", random.randint(1,1000))

    elif choice=="44":
        chars="abcdefghijklmnopqrstuvwxyz123456789"
        print("Random Password Strength Test:", "".join(random.choice(chars) for i in range(10)))

    elif choice=="45":
        print("Random Username:", random.choice(["arafat","coder","dev","tech"])+str(random.randint(10,999)))

    elif choice=="46":
        print("Random Letter:", random.choice("abcdefghijklmnopqrstuvwxyz"))

    elif choice=="47":
        print("Random Digit:", random.randint(0,9))

    elif choice=="48":
        print("Developer: Arafat")
        print("GitHub: https://github.com/576890-art")
        print("Facebook: https://www.facebook.com/arafat576890")
        print("WhatsApp: 01989333156")
        print("Telegram: https://t.me/arafat_tech")
        print("Email: arafat342422@gmail.com")

    elif choice=="49":
        os.system("python tool.py")

    elif choice=="50":
        print("Goodbye Arafat")
        break

    else:
        print("Invalid option")
