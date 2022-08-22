number=22
guesses_of_number =1
print("guesses of number is limited only 6 times")
while(guesses_of_number<=6):
      number=int(input("guess the number \n"))
      if number <22:
         print("please enter gretter number\n")
      elif number >22:
         print("please enter smaller number\n")
      else:
         print("you are won\n")
         print(guesses_of_number,"number of guesses you took to finish ")
         break
      print( guesses_of_number," number of guesses left \n")
      guesses_of_number = guesses_of_number + 1

if guesses_of_number > 6:
    print("Game over")
