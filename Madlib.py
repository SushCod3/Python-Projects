def my_madlib():  # Defining a funciton to put it all inside of one function

    name = input("Name: ")  # input() is used to get the input from the user
    age = input("Age: ")
    career = input("What do you wanna be in life?\n")
    expected_year = input("Which year do you think you can achieve it by?\n")

    madlib_passage = f"Hello, World! \nMy name is {name} and I'm {age} years old. \nI want to become a {career} in life. \nAnd I'm going to achieve my goal by the year of {expected_year}!"
    # We used the f method here on our madlib
    # We could also use the + operator or the format() function

    print(madlib_passage)


my_madlib()
