task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that should be completed soon!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task that can be the completed soon!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that should be completed today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have a free time.")