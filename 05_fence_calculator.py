# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()


# Main Routine goes here
# Start of calculator loop

keep_going = ""
while keep_going == "":
    width = num_check("width: ")
    height = num_check("height: ")
    cost_per_m = num_check("cost per meter: ")

    # Calculate perimeter (width + height) x 2
    perimeter = 2 * (width + height)
    # Calculate the cost of the fencing (perimeter x price / meter)
    cost = perimeter * cost_per_m
    # Output the perimeter and cost of the fencing
    print(f"Perimeter: {perimeter:.1f} units")
    print(f"Cost of fence: {cost:.1f} units")
    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the Fencing cost calculator")
