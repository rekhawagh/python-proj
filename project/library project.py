class  Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.LendDict={}

    def Display_Book(self):
        print(f"These are books list:{self.booklist}")
    def Lend_Book(self,user,book):
        if book not  in self.LendDict.keys():
          self.LendDict.update({book:user})
          print("Lender book  has been updeted. you can take it now. ")
        else:
            print(f"this book being used by {self.LendDict[book]}")
    def Add_book(self,book):
        self.booklist.append(book)
        print("thank for donate this book.")
    def Return_Book(self,book):
        self.LendDict.pop(book)
        print("you returned successfully.")
if __name__ == '__main__':
    Rekha=Library(['Python','c++ Basic','Java','Data dase algorithm'],'OPEN PUBLIC Library')
    while(True):

        print(F"WELL COME TO OUR LIBRARY ********** {Rekha.name}")
        print("What would you want here:")
        print(' 1: for  Display_Book\n','2: for Lend_Book\n','3:for Add_book\n','4:for  Return_Book ')
        choice=int(input())

        if choice==1:
            Rekha.Display_Book()

        elif choice==2:
            book=input("Enter the book name you want to lend")
            user=input("Enter your name:\n")
            Rekha.Lend_Book(user,book)
        elif choice==3:
            book=input("Enter the book name you want to add")
            Rekha.Add_book(book)
        elif choice==4:
            book=input("Enter the book name you want to Return")

            Rekha.Return_Book(book)
        else:
            print("enter valid option.")

        print("Enter q to quit and enter c to continue. ")
        choose=input()
        if choose=='q':
            break
        elif choose=='c':
            continue

