from datetime import datetime
import operator



plain_commands = []

with open("data/day4.txt") as data:
	plain_commands=data.readlines()

guard_sleep_mins = {}
guard_minutes_tracker = {}

i = 0

current_guard = 0
fell_asleep_min = -199999


while (i < (len(plain_commands))):

	current_min = int(plain_commands[i].split(":")[1].split("]")[0])
	
	# if the line is that X is now the guard, store the shift events
	if("begins shift" in plain_commands[i]):
	#	print("starting a shift")
		# reset events ( new guard )
		# update who's on shift
		fell_asleep_min = 100000
		current_guard = plain_commands[i].split("#")[1].split(" ")[0]

		if(not guard_sleep_mins.get(current_guard)):
			guard_sleep_mins[current_guard] =0
			guard_minutes_tracker[current_guard] = [0] * 60
	if("falls asleep" in plain_commands[i]):
		fell_asleep_min = current_min
	if("wakes up" in plain_commands[i]):
		for j in range(fell_asleep_min,current_min):
			guard_minutes_tracker[current_guard][j]+=1
			guard_sleep_mins[current_guard] += 1
	i+=1



sleepiest_guard = max(guard_sleep_mins.items(), key=operator.itemgetter(1))[0]
sleepiest_minute_for_sleepiest_guard = guard_minutes_tracker[sleepiest_guard].index(max(guard_minutes_tracker[sleepiest_guard]))
print(f"pt1:\nOverall sleepiest guard, minute: {sleepiest_guard} @ {sleepiest_minute_for_sleepiest_guard}m")
print(f"= {sleepiest_minute_for_sleepiest_guard * int(sleepiest_guard)}")

sleepiest_minute_amount = -1
sleepiest_minute = -1
sleepiest_guard_id = -1

for guard in guard_minutes_tracker:
	guards_sleepiest_minute_amount = max(guard_minutes_tracker[guard])
	guards_sleepiest_minute = guard_minutes_tracker[guard].index(max(guard_minutes_tracker[guard]))

	if guards_sleepiest_minute_amount > sleepiest_minute_amount:
		sleepiest_minute_amount = guards_sleepiest_minute_amount
		sleepiest_minute = guards_sleepiest_minute
		sleepiest_guard_id = int(guard)

print(f"pt2: amount,time of guard most consistently sleeping : {sleepiest_minute_amount} @ {sleepiest_minute}m")
print(f"= {sleepiest_guard_id * sleepiest_minute}")


