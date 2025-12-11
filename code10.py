for i in range (4):
    for j in range (1==i):
        print("A P Q R" , end="")
    for j in range (2==i):
        print("A B Q R" , end="")
    for j in range (3==i):
        print("A B C R")
    for j in range (4==i+1):
        print("A B C D" , end="")
            
    
    print()
patterns = [
    "",               # i = 0 → print nothing
    "1234",        # i = 1
    "234",        # i = 2
    "34\n4"  # i = 3 → two lines
]

for i in range(4):
    print(patterns[i])
