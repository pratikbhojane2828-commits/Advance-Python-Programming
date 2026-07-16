

class library:
    name_list=[]
    book_list=[]
    def registration(self):
        name=input("enter your name=")
        self.name_list.append(name)
        print( "registration is succesfull")

    def adding_new_books(self):
        book_name=input("enter your book name for add in library=")
        self.book_list.append(book_name)
        print("Adding book Succesfully!!!!")

    def borrowing_book(self):
        self.books=["1.Basic of python","2.basic of dsa","3.basic of java ","4.basic of c++"]
        print("select your book:")
        for i in self.books:
            print(i)

    def returning_book(self):
        self.returning_book_name=input("enetr your returning bopok name=")
        print("returning book succesfulll")



obj=library()
print("Welcome to Library!!!!!")
print("please select your work....")


while(True):
    methods=["1. Registration","2.Adding new books","3.borrowing books","4.returning books","5.end"]
    for i in methods:
        print(i)
    number=int(input("enter your number for work="))
    if number==1:
            obj.registration()
    elif number==2:
            obj.adding_new_books()
    elif number==3:
            obj.borrowing_book()
    elif number==4:
            obj.returning_book()
    else:
            break


    