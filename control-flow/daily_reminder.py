task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify the message if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium"]:
    message += ". Consider completing it soon."

# Print the final reminder
print(message)