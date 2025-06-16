#This app will calculate how much memory modules you'll need in your computer, preserving dual-channel or not.
import time
n = 1 #count variable
k = 0 #count variable
print("Let's calculate how much memory modules you'll need in your computer, preserving dual-channel.")
time.sleep(1)
while k > 64 or k == 0: #verify input
    while True:
        try:
            k = int(input("How much memory in GB you is gonna to take?(64gb max) "))
            break
        except:
            print('Must be an integer number.')
    if k > 64 or k == 0:
        print('Must be less than 64 and different from 0.')
time.sleep(1)
gb_to_MB = 1024 * k #convert GB to MB
if 8 <= k < 16: #social interation
    print("That's a good amount.")
elif  16<= k < 32:
    print("You're gonna to play cities skyline?")
elif 32 <= k <= 64:
    print("WOWW! Let's go make a rocket!")
time.sleep(1)
def how_much_modules(memory_in_MB): #return how much modules you'll need for 4, 16, 32 and 64.
    p = [1024*4, 1024*8, 1024*16, 1024*32]
    n = 0
    modules_quantity = ['','','','']
    for x in p:
        modules_quantity[n] = memory_in_MB // p[n]
        n += 1    
    return modules_quantity
def is_Dual_Channel_Capable(modules_quantity): #verify if the modules quantity is a pair number
    dual_channel_capable = ['', '', '', '']
    n = 0
    for x in modules_quantity:
        if modules_quantity[n] % 2 == 0:
            dual_channel_capable[n] = True
        else:
            dual_channel_capable[n] = False
        n += 1
    return dual_channel_capable
modules_quantity = how_much_modules(gb_to_MB) #modules quantity for each size in a lista 4 to 32
is_dual_channel = is_Dual_Channel_Capable(modules_quantity) #if the modules quantity is pair, value in list is true, if not, is false.
modules = [4, 8, 16, 32] #modules memory sizes
if modules_quantity[0] >= 1: #if the 4gb modules number is less than 1 no make sense to buy anything.
    print(f"You'll need {gb_to_MB} MegaBytes of memory.")
    time.sleep(1)
    print('You can buy: ')
else:
    print("It's better to buy nothing.")
time.sleep(1)
p = 0 #count variable. I don't know how to use enumerate yet, next att.
for x in modules_quantity:
    if modules_quantity[p] != 0:
        if modules_quantity[p] <= 4:
            if is_dual_channel[p] == True:
                print(f'{modules_quantity[p]} modules of {modules[p]}gb, preserving Dual-Channel.')
            else:
                print(f'{modules_quantity[p]} modules of {modules[p]}gb, without Dual-Channel.')
        else:
            print(f'No support in any motherboard for {modules_quantity[p]} modules of {modules[p]}gb')
    elif modules_quantity[p] > 4:
        print('Is better to buy Nothing.')
    p += 1
    time.sleep(1)
