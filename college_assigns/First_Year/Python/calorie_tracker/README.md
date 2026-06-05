# <p align="center">Daily Calorie Tracker CLI</p>

Simple command‑line tool to log meals, calculate total and average calories, compare against a user daily limit, and optionally save a session report. Built as an individual mini project for the course: Programming for Problem Solving using Python.

---

## Project Overview
A lightweight Python script (tracker.py) that:
- Prompts the user for a daily calorie limit
- Collects meal names and calorie values
- Computes total and average calories
- Warns if limit exceeded
- Displays a formatted summary table
- Optionally saves a log to calorie_log.txt

---

## Learning Objectives Covered
| Objective | How Addressed |
|-----------|---------------|
| input(), type conversion | Used for numeric (float/int) and text inputs |
| Lists & data storage | Parallel lists: meal_names, calorie_val |
| Arithmetic & comparison | Total, average, limit comparison, warning |
| String formatting | f-strings, \n, \t, decorative lines |
| File I/O | Writes structured log with timestamp |
| Logical thinking | Structured task flow (Tasks 1–6) |

---

## Program Flow (Task Mapping)
| Task | Implementation in tracker.py |
|------|-------------------------------|
| Task 1 | Header comments + welcome prints |
| Task 2 | Loop over user-specified meal count; append to lists |
| Task 3 | sum() for total, average = total / count |
| Task 4 | if total_cal > daily_lim → warning string |
| Task 5 | Formatted table using tabs & lines |
| Task 6 (Bonus) | Optional save with timestamp using datetime |

---

## Sample Run (Example 1)
```
--- Daily Calorie Tracker CLI by Suhani Yadav ---

Enter your daily calorie limit: 2000
How many meals do you want to enter:3

Meal 1:
Meal name: Vada Pav 
Calories for Vada Pav: 600

Meal 2:
Meal name: Sandwich
Calories for Sandwich: 700

Meal 3:
Meal name: Icecream
Calories for Icecream: 800

Meal Name 			           Calories:
--------------------------------------------------
Vada Pav 			             600.0 cal
Sandwich 			             700.0 cal
Icecream		               800.0 cal

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!

Do you want to save this report? (Y/N): y

Saved to calorie_log.txt.
```

---

## Generated Log Format in calorie_log.txt
```
CALORIE TRACKER LOG - 2025-10-06 19:36:54.744298
Daily Calorie Limit: 2000.0

Meal Name 			 Calories 
Vada Pav: 			 600.0 cal 

Sandwich: 			 700.0 cal 

Icecream: 			 800.0 cal 

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!
```

---

## Sample Run (Example 2)
```
--- Daily Calorie Tracker CLI by Suhani Yadav ---

Enter your daily calorie limit: 2000
How many meals do you want to enter:3

Meal 1:
Meal name: Apple 
Calories for Apple: 600

Meal 2:
Meal name: Banana
Calories for Banana: 700

Meal 3:
Meal name: Kiwi
Calories for Kiwi: 800

Meal Name 			           Calories:
--------------------------------------------------
Apple    			             600.0 cal
Banana  			             700.0 cal
Kiwi    		               800.0 cal

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!

Do you want to save this report? (Y/N): y

Saved to calorie_log.txt.
```

---

## Generated Log Format in calorie_log.txt
```
CALORIE TRACKER LOG - 2025-10-06 19:36:54.744298
Daily Calorie Limit: 2000.0

Meal Name 			 Calories 
Apple:    			 600.0 cal 

Banana: 			   700.0 cal 

Kiwi:     			 800.0 cal 

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!
```

---

## Sample Run (Example 3)
```
--- Daily Calorie Tracker CLI by Suhani Yadav ---

Enter your daily calorie limit: 2000
How many meals do you want to enter:3

Meal 1:
Meal name: Golgappe 
Calories for Golgappe: 600

Meal 2:
Meal name: Baingan Bharta
Calories for Baingan Bharta: 700

Meal 3:
Meal name: Chicken Tikka
Calories for Chicken Tikka: 800

Meal Name 			           Calories:
--------------------------------------------------
Golagppe 			             600.0 cal
Baingan Bharta 			       700.0 cal
Chicken Tikka		           800.0 cal

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!

Do you want to save this report? (Y/N): y

Saved to calorie_log.txt.
```

---

## Generated Log Format in calorie_log.txt
```
CALORIE TRACKER LOG - 2025-10-06 19:36:54.744298
Daily Calorie Limit: 2000.0

Meal Name 			 Calories 
Golgappe: 			 600.0 cal 

Baingan Bharta:  700.0 cal 

Chicken Tikka: 	 800.0 cal 

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!
```

## Details
- Suhani Yadav
- 2501410032
- B.Tech CSE Cyber Security(First Semester)
- 7th October 2025
- Programming With Python - Lab Assignment 1
