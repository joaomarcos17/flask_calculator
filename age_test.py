def birthday():
    # initialize variables
    day_of_birth = 2
    month_of_birth = 3
    year_of_birth = 1998
    current_year = int(input("Enter the current year: "))
    # subtract variables
    age = current_year - year_of_birth
    # if else statemant
    if day_of_birth == 5 and month_of_birth == 5:

        age - 1

    elif day_of_birth == 5 and month_of_birth == 4:

        age - 1
    # print output with the age calculated 
    print(f"I will be {age} years old")
    
birthday()

      

