# lists

'''
camping_list = ['test','sleeping bag','flashing light','test','sleeping bad','flashing light','test','sleeping bed','flashing light','test','sleeping tag','flashing light']

#print(type(camping_list))
print(len(camping_list))

camp_site = ['Crystal lake', 404, 18, True]

me = camping_list[4]

you = camping_list[9]

print(me)
print(you)


def hello_word():
    print('hello word')

hello_word()

#this is a list function

def list_for_groceries():
    my_list = ['juice','milk','ham','apple','oranges']
    print(my_list)

list_for_groceries()


# the function

def ask_question():
    ask = input("what day is today: ")
    if ask == "easter" or ask == "Easter":
        print(f"today is, {ask} ")
    else:
        print("wrong answer")



ask_question()

#barista_house coffe shop

def barista_house():
    order = input("Hello, welcome to the barista house coffe shop what would you like to drink:\n")
    if order == "capuccino" or order == "Capuccino":
         print("the price is £2 pounds ")

         price = input("would like to order? if yes how many ?")

         if price =="yes":

             print("I will make your order right now")
         else:
             

                 other_things = input("would you like something else: ")
                  if other_things == "expresso" or other_things == "Expresso":
                        print(f"your,{other_things},will be ready in a moment ")
                    elif other_things =="tea" or other_things =="Tea":
                         print(f"your {other_things} will be ready in a moment ")



barista_house()  '''

def barista():

    order = input("Hello, welcome to the barista house coffe shop what would you like to drink:\n")
    
    if order == "capuccino"or order == "coffee":
    
        print(f"the price of {order} is £ 2,00 ")
        
    else:
    
        print(f"sorry we don't serve {order} here ")


barista()