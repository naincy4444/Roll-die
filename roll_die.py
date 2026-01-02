#Dice Simulator: 
# Roll a die and display the outcome. 
# Save the result in the database and show statistics.

import random
import sqlite3

conn = sqlite3.connect("dice.db")
cursor = conn.cursor()



cursor.execute("""CREATE table die_roll(
	total_rolls int primary key,
	one int not null,
    two int not null,
    three int not null,
    four int not null,
    five int not null,
    six int not null
);
""")

x = "yes"

count1 = count2 = count3 = count4 = count5 = count6 = 0
count_roll = 0

while x == "yes":
    
    no = random.randint(1,6)
    count_roll += 1
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

    cursor.execute("""
    INSERT INTO die_roll (total_rolls, one, two, three, four, five, six)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (count_roll, count1, count2, count3, count4, count5, count6))

    conn.commit()

    x=input("Do you want to roll again? : ")
    print("\n")


y = input("Do you want to know your statistics?")
if y.lower() == "yes":
    cursor.execute("SELECT * FROM die_roll")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()