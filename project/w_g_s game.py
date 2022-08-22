import  random
list=["water","gun","snake"]
print("you are play only 10 time")
computer_point=0
my_point=0
time=0
chance=10
while time<10:
    print("enter your choice:",time)
    my_choice=input()
    computer_choice=random.choice(list)
    print(computer_choice)

    if my_choice=="water" and computer_choice=="snake":
        computer_point += 1
        print("computer make",computer_point,"point")
        time=time+1



    elif my_choice=="snake" and computer_choice=="water":

        my_point+=1
        print("your point is ",my_point,"and computer point is",computer_point)

    elif my_choice=="snake" and computer_choice=="gun":

        computer_point += 1
        print("computer point", computer_point,"your point is ",my_point)


    elif my_choice=="gun" and computer_choice=="snake":

        my_point += 1
        print("your point", my_point,"computer point", computer_point)

    elif my_choice==computer_point:
        print("both are same")
    else:
        print("wrong input")
    print(f"{time} time left out of {chance}")
    time=time+1

print("Game over!")
if computer_point==my_point:
    print("tie")
elif computer_point<my_point:
    print("you won this game")
else:
    print("computer won this game")