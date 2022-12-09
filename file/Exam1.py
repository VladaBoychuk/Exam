f = open('text.txt',"r")

my_file = input("Enter your word ---> ")
rows = f.read().split("\n\n")

p = False
for lines in rows:
    if my_file in lines:
        print(f"\n{lines}")
        p = True
if p == False:
    print("No words(")