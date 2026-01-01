import random

x = "yes"

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
 
while x == "yes":
    
    no = random.randint(1,6)
    
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