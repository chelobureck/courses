# Программа для вычисления обшего и среднего расхода за неделю
# Program for calculating total and average consumption for a week

Monday = int(input("Расходы за понедельник: "))  # Expenses for Monday
Tuesday = int(input("Расходы за вторник: "))     # Expenses for Tuesday
Wednesday = int(input("Расходы за среду: "))     # Expenses for Wednesday
Thursday = int(input("Расходы за четверг: "))    # Expenses for Thursday
Friday = int(input("Расходы за пятницу: "))      # Expenses for Friday
Saturday = int(input("Расходы за субботу: "))    # Expenses for Saturday
Sunday = int(input("Расходы за воскресенье: "))  # Expenses for Sunday

Total = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday  # Total weekly expenses
Average = Total / 7  # Average weekly expenses

print("Общие расходы за неделю: ", Total)       
# Total expenses for the week
print("Средние расходы за неделю: ", round(Average, 1)) 
# Average expenses for the week