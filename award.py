swimming_time = input("Enter the swimming time in minutes: ")
#if the time taken is under 20 minutes, the swimmer gets a gold medal
if float(swimming_time) < 20:
    print("Gold Medal")
#elif the time taken is more than 20 and less then 25, the swimmer gets a silver medal
elif float(swimming_time) >= 20 and float(swimming_time) < 25:
    print("Silver Medal")
#elif the time taken is more than 25 and less then 30, the swimmer gets a bronze medal
elif float(swimming_time) >= 25 and float(swimming_time) < 30:
    print("Bronze Medal")
#else if the time taken is more than 30, the swimmer does not get a medal
else:
    print("No Medal")
#the swimmer gets a medal based on the time taken
#the time taken is inputted in minutes

cycle_time = input("Enter the cycling time in minutes: ")
#if the time taken is under 20 minutes, the cyclist gets a gold medal
if float(cycle_time) < 20:
    print("Gold Medal")
#elif the time taken is more than 20 and less then 25, the cyclist gets a silver medal
elif float(cycle_time) >= 20 and float(cycle_time) < 25:
    print("Silver Medal")
#elif the time taken is more than 25 and less then 30, the cyclist gets a bronze medal
elif float(cycle_time) >= 25 and float(cycle_time) < 30:
    print("Bronze Medal")
#else if the time taken is more than 30, the cyclist does not get a medal
else:
    print("No Medal")
#the cyclist gets a medal based on the time taken
#the time taken is inputted in minutes

running_time = input("Enter the running time in minutes: ")
#if the time taken is under 20 minutes, the runner gets a gold medal
if float(running_time) < 20:
    print("Gold Medal")
#elif the time taken is more than 20 and less then 25, the runner gets a silver medal
elif float(running_time) >= 20 and float(running_time) < 25:
    print("Silver Medal")
#elif the time taken is more than 25 and less then 30, the runner gets a bronze medal
elif float(running_time) >= 25 and float(running_time) < 30:
    print("Bronze Medal")
#else if the time taken is more than 30, the runner does not get a medal
else:
    print("No Medal")
#the runner gets a medal based on the time taken
#the time taken is inputted in minutes