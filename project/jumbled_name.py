import random


def jumbled_names(lst_of_names):
    funny_names = []  # store funny names
    first_names = []  # store all first names
    last_names = []  # store all last names

    # Appending all first names and last names in respective lists
    for name in lst_of_names:
        name = name.split(" ", 1)
        first_names.append(name[0])
        last_names.append(name[1])

    # Jumbling the names
    for fname in first_names:
        lname = random.choice(last_names)
        funny_names.append(f"{fname} {lname}")
        last_names.remove(lname)
    return funny_names


if __name__ == '__main__':

    print("\nWelcome to Funny Names Generator")
    no_of_names = int(input("\nEnter the number of your Friends:\n"))
    names = []
    print("\nNow Enter the First & Last Names of your Friends one by one")
    for i in range(no_of_names):
        full_name = input(f"{i+1}: ").title()
        names.append(full_name)
    funny_name_lst = jumbled_names(names)
    input("\nYour Funny Names List is ready.."
          "\nBut are you ready to see your Funny Name?"
          "\nIf yes then Press Enter\n")
    for name in funny_name_lst:
        print(name)