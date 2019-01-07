def get_task_length(id):
	return (ord(id)-4)

def get_free_workers(d):
	free_workers = []
	for i in d:
		if(d.get(i)==-1):
			free_workers.append(i)
	return free_workers

def get_busy_workers(d):
	busy_workers = []
	for i in d:
		if(d.get(i) != -1):
			busy_workers.append(i)
	return busy_workers

def get_next_task(candidate_next_moves,unmet_dependencies):

	list_of_next_possible_moves = list(candidate_next_moves)
	list_of_next_possible_moves.sort()
	if(len(list_of_next_possible_moves) ==0):
		return None

#	print(f"checking list of possible moves: {list_of_next_possible_moves}")
#	print(f"to see if any have unmet_dependencies of zero {unmet_dependencies}")
	for i in list_of_next_possible_moves:
		if(unmet_dependencies.get(i) ==0):
			#print(f"next task is {i}")
			return i
	return None



def task_scheduler(nodes,first_tasks,unmet_dependencies,task_time,workers):
	print(f"starting task scheduler for nodes:{task_time}")
	time = -1 
	candidate_next_tasks = first_tasks
	visited = []
	worker_tasks = {} # -1 = free, else task number.

	for i in range(workers):
		worker_tasks[i] = -1

	while sum(task_time.values()) > 0:
		time+=1

		for worker in get_busy_workers(worker_tasks):
			# update current busy workers
			currently_working_on = worker_tasks[worker]
			#toiling away...
			task_time[currently_working_on] -= 1
			#task finished
			if(task_time[currently_working_on] == 0):
				worker_tasks[worker] = -1 	
				if(nodes.get(currently_working_on) != None):
					for new_node in nodes.get(currently_working_on):
						unmet_dependencies[new_node] -= 1
						if(new_node not in visited):
							candidate_next_tasks.add(new_node)


		#make as many workers busy
		for worker in get_free_workers(worker_tasks):
			#assign task
			current_task = get_next_task(candidate_next_tasks,unmet_dependencies)
			if(current_task != None):
				candidate_next_tasks.remove(current_task)
				worker_tasks[worker] = current_task
				visited.append(current_task)

		print(f"\t{time}\t{worker_tasks[0]}\t{worker_tasks[1]}\t{worker_tasks[2]}\t{worker_tasks[3]}\t{worker_tasks[4]}")


	return (time)


nodes = {}
visited = []
number_of_dependencies = {}

task_time = {}
task_time[-1] = 0
workers = 5 # not 215

with open("data/day7.txt","r") as f:

	from_nodes = set()
	to_nodes = set()

	lines = f.readlines()
	for line in lines:
		this_node = line.split(" ")[1].split(" ")[0]
		next_node = line.split(" ")[7]
		# print(line)
		# print(this_node,next_node)
		if(number_of_dependencies.get(next_node)):
			number_of_dependencies[next_node]+=1
		else:
			number_of_dependencies[next_node]=1

		from_nodes.add(this_node)
		to_nodes.add(next_node)
		if(nodes.get(this_node)):
			nodes[this_node].append(next_node)
		else:
			nodes[this_node] = [next_node]


print(f"nodes: {nodes}")
starting_nodes = from_nodes - to_nodes

all_nodes = from_nodes.union(to_nodes)

for n in starting_nodes:
	number_of_dependencies[n] = 0
print(f"dependencies: {number_of_dependencies}")

for i in all_nodes:
	task_time[i] = get_task_length(i)


task_scheduler(nodes,starting_nodes,number_of_dependencies,task_time,workers)