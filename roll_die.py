#Dice Simulator: 
# Roll a die and display the outcome. 
# Save the result in the database and show statistics.

import random
import pandas as pd

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

data = {
    'Total roll': [total_roll],
    '1': [count1],
    '2': [count2],
    '3': [count3],
    '4': [count4],
    '5': [count5],
    '6': [count6]
}

df = pd.DataFrame(data)

y = input("Do you want to know your statistics?")
if y.lower() == "yes":
    print(df)