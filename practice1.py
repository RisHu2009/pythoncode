#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
name=str(input("Enter Your Name "))
age=int(input("Enter your age"))
current_year =2025
year_when_100=(current_year + (100-age))
print("You will turn 100 years old in Year ",year_when_100)