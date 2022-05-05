# functions go here

# checks input is a number more than zero
from turtle import width


def num_check(question):
  
  valid = False
  while not valid:

    error = "please enter a number that is more than zero"

    try:
      response = float(input(question))

      if response > 0:
        return response

      else:
        print(error)
        print()

    except ValueError:
      print(error)



# main routine goes here

keep_going = ""
while keep_going == "":

  width = num_check("Width: ")
  height  = num_check("Height: ")

  # calculate area (width x height)
  area = width * height

  #calculate perimeter (width + height) x 2
  perimeter = 2 * (width + height)

  # Output area and perimeter
  print("Perimeter:   {}  units".format(perimeter))
  print("Area:    {}  sqaure  units".format(area))


  keep_going = input("press <enter> to keep going or any key to quit")

print()
print("thanks for using the area / perimeter calculator")