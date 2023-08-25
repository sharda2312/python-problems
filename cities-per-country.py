# Using following list of cities per country,

india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Write a program that asks user to enter a city name and it should tell which country the city belongs to
city = input("Please enter city name: ")
if (city in india):
    print("this city belongs to india") 
elif (city in pakistan):
    print("this city belongs to pakistan")
elif (city in bangladesh):
    print("this city belongs to bangladesh")
else:
    print("sorry! my knowledge is limited i don't know this city belong to which country.")