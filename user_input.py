# Program that requests for user input
# Author: Oguntuase Victor
# Description: This is the first assignment for the Python Module

name = ""
# custom messages
print(f"{'  INPUTS  ':*^50}")  # string templating with f-strings
name_msg = "\nPlease enter your name: "
age_msg = f"\nHow old are you {name}: "
location_msg = "\nFinally, what is your location?: "

# Accepting user inputs
print(name_msg)
name = input(">> ")

print(age_msg)
age = input(">> ")

print(location_msg)
location = input(">> ")

print(f"\n{'  OUTPUT  ':*^50}")
# Printing out the desired response.
print(f"\nNice to meet you {name.title()} from {location.title()}." +
      f"\nIts cool that you are {age} years old." + "\n\nBye for now!\n")
print("[Program Complete]")
print(f"{'  END  ':*^50}")
