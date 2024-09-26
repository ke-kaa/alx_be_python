task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == 'yes':
    bound = True
else:
    bound = False

if bound:
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print("Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")