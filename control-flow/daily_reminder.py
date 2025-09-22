task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
is_time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder_message = f"Note: '{task}' is a medium priority task"
    case 'low':
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Error: Invalid priority entered. Please try again with 'high', 'medium', or 'low'."

if is_time_bound == 'yes' and priority in ['high', 'medium']:
  
    reminder_message += " that requires immediate attention today!"

print(reminder_message)
