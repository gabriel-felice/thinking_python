import time
n = 1
k = 0
print("Let's calculate how much memory modules you'll need in your computer, preserving dual-channel.")
time.sleep(1)
while k > 64 or k == 0:
    while True:
        try:
            k = int(input("How much memory in GB you is gonna to take?(64gb max) "))
            break
        except:
            print('Must be an integer number.')
    if k > 64 or k == 0:
        print('Must be less than 64 and different from 0.')
time.sleep(1)
kingb = 1024 * k
if 8 <= k < 16:
    print("That's a good amount.")
elif  16<= k < 32:
    print("You're gonna to play cities skyline?")
elif 32 <= k <= 64:
    print("WOWW! Let's go make a rocket!")
time.sleep(1)
while 2**n < kingb:
    n += 1
if 2**n >= kingb:
    if 2**n <= 9999:
        memrounded = 2**n//(int('1' + (int(len(str(2**n))) - 1) * '0'))
    else:
        memrounded = 2**n//(int('1' + (int(len(str(2**n))) - 2) * '0'))
    print("You'll need", 2**n, "bits of memory.")
    pent4 = memrounded // 4
    pent8 = memrounded // 8
    pent16 = memrounded // 16
    pent32 = memrounded // 32

    if pent4%2 == 0:
        pent4 = memrounded // 4
    else:
        pent4 = str(memrounded // 4) + "(No Dual-Channel)"
        paridade4 = False
    if pent8%2 == 0:
        pent8 = memrounded // 8
    else:
        pent8 = str(memrounded // 8) + "(No Dual-Channel)"
        paridade8 = False
    if pent16%2 == 0:
        pent16 = memrounded // 16
    else:
        pent16 = str(memrounded // 16) + "(No Dual-Channel)"
        paridade16 = False
    if pent32%2 == 0:
        pent32 = memrounded // 32
    else:
        pent32 = str(memrounded // 32) + "(No Dual-Channel)"
        paridade32 = False
    time.sleep(1)
    try:
        if pent4 + pent8 + pent16 + pent16 == 0:
            print("It's better to buy nothing.")
        else:
            print("You can buy:")
    except:
        print("You can buy:")

    time.sleep(1)
    try:
        if paridade4 == False:
            print(f"{pent4} modules of 4gb.")
            time.sleep(1)
    except:
        if pent4 > 4:
            print(f"{pent4} modules of 4gb does'nt fit in any motherboard.")
            time.sleep(1)
        elif pent4 <=4 and pent4 != 0:
            print(f"{pent4} modules of 4gb.")
            time.sleep(1)
    try:
        if paridade8 == False:
            print(f"{pent8} modules of 8gb.")
            time.sleep(1)
    except:
        if pent8 > 4:
            print(f"{pent8} modules of 8gb does'nt fit in any motherboard.")
            time.sleep(1)
        elif pent8 <= 4 and pent8 != 0:
            print(f"{pent8} modules of 8gb.")
            time.sleep(1)
    try:
        if paridade16 == False:
            print(f"{pent16} modules of 16gb.")
            time.sleep(1)
    except:
        if pent16 > 4:
            print(f"{pent16} modules of 16gb does'nt fit in any motherboard.")
            time.sleep(1)
        elif pent16 <= 4 and pent16 != 0:
            print(f"{pent16} modules of 16gb.")
            time.sleep(1)
    try:
        if paridade32 == False:
            print(f"{pent32} modules of 32gb.")
            time.sleep(1)
    except:
        if pent32 >4:
            print(f"{pent32} modules of 8gb does'nt fit in any motherboard.")
            time.sleep(1)
        elif pent32 <= 4 and pent32 != 0:
            print(f"{pent32} modules of 32gb.")