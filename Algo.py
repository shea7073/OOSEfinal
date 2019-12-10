
def algorithm():

    condition = True

    while condition:
        if weight <= 0 or reps <= 0:
            print("Error")
            return False
        else:
            orm = weight*(1+(reps/40))
            print("Your one rep max is: ", orm)
            return False


algorithm()


