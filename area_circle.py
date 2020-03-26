
def area_of_a_circle():
    # constant value of PI
    PI = 3.141592653589793238
    try:
        # takes in user input and try to convert it to float
        r = float(input("Enter radius: "))
        # returns a result that is rounded off to 2 decimal places
        return round(PI * (r ** 2), 2)
    # throws an error in conversion to float fails (str to float)
    except ValueError:
        return "Radius must be an integer or float"


a = area_of_a_circle()
print(a)