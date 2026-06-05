# Name : Suhani Yadav 
# Date : 07/10/2025
# Project : Daily Calorie Tracker CLI 

#Task 1 : Welcome Message 
print("\n!! Welcome to Daily Calorie Tracker CLI by Suhani Yadav !!")

#Task 2 : Input & Store data 
meal_data = []   
calorie_data = []

daily_limit = int(input("\nEnter your daily calorie limit = "))

n = int(input("\n Enter total no of meal you want to check = "))
for i in range(n):
    print(f"\nmeal {i+1}:")
    meal = input(" Enter the meal name :  ")
    calories = float(input(" Enter the calorie amount : "))
    meal_data.append(meal)
    calorie_data.append(calories)
    
# Task 3 : to calculate the total and average calories 
total_calorie = sum(calorie_data)
average_calorie = total_calorie/len(calorie_data)

# Task 4: Limit warning system 
if total_calorie > daily_limit :
    print("\n WARNING !! Limit has exceeded !! ")
    print("Your calorie intake has exceeded by",total_calorie-daily_limit,"cal")
else:
    print("\n SUCCESS !! Within limit !! ")

# Task 5 : Formatted outputs using \t and \n       
print(f"\n MEALS NAME \t\t\tCALORIES ")  
print (" ------------------------ ")
for i in range(len(meal_data)):
    print(f" {meal_data[i]} \t\t\t{calorie_data[i]} cal")
print(f" \nTotal calorie: {total_calorie} cal")
print(f"Average calorie : {average_calorie} cal")


# Task 6 : Saving logs to a text file using file handling 
s = input("\n Do you want to save this report? (Y/N) : ").lower()
if s == "y":
    with open("calorie_log.txt", "w") as f:
        f.write(f"daily calorie limit : {daily_limit}\n\n")
        f.write("meal name \t\t\t calories \n")
        for i in range(len(meal_data)):
            f.write(f"{meal_data[i]}: \t\t\t {calorie_data[i]} cal \n\n")
        f.write(f"Total calories : {total_calorie}\n")    
        f.write(f"Average calories : {average_calorie}\n")
    print("\n Saved to calorie_log.txt.")  
else :
    print("\n Report not saved.")
