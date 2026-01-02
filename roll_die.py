#Dice Simulator: 
# Roll a die and display the outcome. 
# Save the result in the database and show statistics.

import random

count1 = count2 = count3 = count4 = count5 = count6 = 0
total_roll = 0

x = "yes"

while x == "yes":
    
    no = random.randint(1,6)
    total_roll += 1
    if no == 1:
        print( "_________") 
        print("|         |")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("|_________|")
        count1 += 1
    if no == 2:
        print("[---------]")
        print("[  0      ]")
        print("[         ]")
        print("[      0  ]")
        print("[---------]")
        count2 += 1
    if no == 3:
        print("[---------]")
        print("[0        ]")
        print("[    0    ]")
        print("[        0]")
        print("[---------]")
        count3 += 1
    if no == 4:
        print("[---------]")
        print("[ 0     0 ]")
        print("[         ]")
        print("[ 0     0 ]")
        print("[---------]")
        count4 += 1
    if no == 5:
        print("[---------]")
        print("[ 0     0 ]")
        print("[    0    ]")
        print("[ 0     0 ]")
        print("[---------]")
        count5 += 1
    if no == 6:
        print("[---------]")
        print("[  0   0  ]")
        print("[  0   0  ]")
        print("[  0   0  ]")
        print("[---------]")
        count6 += 1

    x=input("Do you want to roll again? : ")
    print("\n")

y = input("Do you want to know your statistics? (yes/no): ")
if y.lower() == "yes":
    print("\nSTATISTICS")
    print("Total rolls:", total_roll)
    print("1:", count1)
    print("2:", count2)
    print("3:", count3)
    print("4:", count4)
    print("5:", count5)
    print("6:", count6)
