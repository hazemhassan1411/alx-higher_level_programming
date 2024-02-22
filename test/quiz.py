def que():
    print("what is the beggist planet")
    print("   A. jupitar")
    print("   B. earth")
    print("   C. mercury")

que()
AN = input("your answer: ")
    
while not AN == "a":
    print("_____________________________________________________________")
    print("try again")
    print("_____________________________________________________________")
    que()
    AN = input("your answer: ")

print("_____________________________________________________________")
print("right answer")