import sys



def addr(reg,a,b,c):

	#addr (add register) stores into register C the result of adding register A and register B.
	reg[c] = reg[a] + reg[b]

	return reg

def addi(reg,a,b,c):

	#addi (add immediate) stores into register C the result of adding register A and value B.
	reg[c] = reg[a] + b

	return reg

def mulr(reg,a,b,c):
	#mulr (multiply register) stores into register C the result of multiplying register A and register B.
	#return (self.after[self.c] == (self.before[self.a] * self.before[self.b]))
	reg[c] = reg[a] * reg[b]

	return reg

def muli(reg,a,b,c):
	#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
	reg[c] = reg[a] * b
	return reg

def banr(reg,a,b,c):
	#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
	reg[c] = (reg[a] & reg[b])
	return reg

def bani(reg,a,b,c):
	#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
	reg[c] = (reg[a] & b)
	return reg

def borr(reg,a,b,c):
	#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
	reg[c] = (reg[a] | reg[b])
	return reg

def bori(reg,a,b,c):
	#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
	reg[c] = (reg[a] | b)
	return reg

def setr(reg,a,b,c):
	#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
	reg[c] = reg[a]
	return reg

def seti(reg,a,b,c):
	#seti (set immediate) stores value A into register C. (Input B is ignored.)
	reg[c] = a
	return reg

def gtir(reg,a,b,c):
	if(a > reg[b]):
		reg[c] =1
	else:
		reg[c] =0
	return reg

def gtri(reg,a,b,c):


	# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.

	if(reg[a] > b):
		reg[c] =1
	else:
		reg[c] =0
	return reg

def gtrr(reg,a,b,c):


	# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

	if(reg[a] > reg[b]):
		reg[c] =1
	else:
		reg[c] =0
	return reg

def eqir(reg,a,b,c):


	# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.

	if( a == reg[b]):
		reg[c] = 1
	else:
		reg[c] = 0
	return reg

def eqri(reg,a,b,c):


	# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.

	if( reg[a] == b):
		reg[c] = 1
	else:
		reg[c] = 0
	return reg

def eqrr(reg,a,b,c):


	# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.

	if( reg[a] == reg[b]):
		reg[c] = 1
	else:
		reg[c] = 0
	return reg

class Example():
	def __init__(self,before,action,after):
		self.before = before
		self.action = action
		self.after = after

		self.opcode = action[0]
		self.a 		= action[1]
		self.b 		= action[2]
		self.c 		= action[3]

		self.candidates = self.get_all_candidate_actions()

	def get_all_candidate_actions(self):
		candidates = set([])
		if(self.could_be_addr()):
			candidates.add("addr")
		if(self.could_be_addi()):
			candidates.add("addi")
		if(self.could_be_mulr()):
			candidates.add("mulr")
		if(self.could_be_muli()):
			candidates.add("muli")
		if(self.could_be_banr()):
			candidates.add("banr")
		if(self.could_be_bani()):
			candidates.add("bani")
		if(self.could_be_borr()):
			candidates.add("borr")
		if(self.could_be_bori()):
			candidates.add("bori")
		if(self.could_be_setr()):
			candidates.add("setr")
		if(self.could_be_seti()):
			candidates.add("seti")
		if(self.could_be_gtir()):	
			candidates.add("gtir")
		if(self.could_be_gtri()):
			candidates.add("gtri")
		if(self.could_be_gtrr()):
			candidates.add("gtrr")
		if(self.could_be_eqri()):
			candidates.add("eqri")
		if(self.could_be_eqir()):
			candidates.add("eqir")
		if(self.could_be_eqrr()):
			candidates.add("eqrr")
		return candidates

	def could_be_addr(self):
		#addr (add register) stores into register C the result of adding register A and register B.
		return (self.after[self.c] == (self.before[self.a] + self.before[self.b]))

	def could_be_addi(self):
		#addi (add immediate) stores into register C the result of adding register A and value B.
		return (self.after[self.c] == (self.before[self.a] + self.b))

	def could_be_mulr(self):
		#mulr (multiply register) stores into register C the result of multiplying register A and register B.
		return (self.after[self.c] == (self.before[self.a] * self.before[self.b]))

	def could_be_muli(self):
		#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
		return (self.after[self.c] == (self.before[self.a] * self.b))

	def could_be_banr(self):
		#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
		return (self.after[self.c] == (self.before[self.a] & self.before[self.b]))

	def could_be_bani(self):
		#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
		return (self.after[self.c] == (self.before[self.a] & self.b))

	def could_be_borr(self):
		#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
		return (self.after[self.c] == (self.before[self.a] | self.before[self.b]))

	def could_be_bori(self):
		#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
		return (self.after[self.c] == (self.before[self.a] | self.b))

	def could_be_setr(self):
		#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
		return (self.after[self.c] == (self.before[self.a]))

	def could_be_seti(self):
		#seti (set immediate) stores value A into register C. (Input B is ignored.)
		return (self.after[self.c] == (self.a))

	def could_be_gtir(self):
		# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False
		if (self.a > self.before[self.b]):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		
	def could_be_gtri(self):
		# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False

		gt = self.before[self.a] > self.b

		if (gt):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		
		
	def could_be_gtrr(self):
		# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False

		gt = self.before[self.a] > self.before[self.b]

		if (gt):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		

	def could_be_eqir(self):
		# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False

		eq = self.a == self.before[self.b]

		if (eq):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		
	def could_be_eqri(self):
		# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False

		eq = self.before[self.a] == self.b

		if (eq):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		
	def could_be_eqrr(self):
		# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.

		if(self.after[self.c] not in [0,1]):
			return False

		eq = self.before[self.a]== self.before[self.b]

		if (eq):
			return (self.after[self.c] == 1)
		else:
			return (self.after[self.c] == 0)
		
	def __str__(self):
		return (str(self.before) +"+"+ str(self.action) +"="+ str(self.after) + "opcode-" + str(self.opcode))
	def __repr__(self):
		return str(self)


def compromise_opcodes_to_function(opcode_candidates):


	possible_opcode_functions = {}
	for op in opcode_candidates:
		possible_opcode_functions[op] = set.intersection(*opcode_candidates.get(op))

	opcodes_to_function = {}


	while (len(opcodes_to_function) < len(possible_opcode_functions)):
		for code in possible_opcode_functions:
			if(len(possible_opcode_functions.get(code)) == 1):
				opcode_to_remove = list(possible_opcode_functions.get(code))[0]
				opcodes_to_function[code] = opcode_to_remove
				for op_remove in possible_opcode_functions:
					try:
						possible_opcode_functions.get(op_remove).remove(opcode_to_remove)
					except:
					 	pass
	return opcodes_to_function


behaves_like_three_or_more_opcodes = 0
opcode_all_candidates = {}

instructions = []


with open(sys.argv[1]) as f:
	data = f.readlines()
	line = 0
	while line <3235:
		before = list(map(int,data[line].strip().split("[")[1].split("]")[0].split(",")))
		action = list(map(int,data[line+1].strip().split()))
		after = list(map(int,data[line+2].strip().split("[")[1].split("]")[0].split(",")))

		e = Example(before,action,after)

		if(len(e.candidates)>=3):
			behaves_like_three_or_more_opcodes +=1

		if(opcode_all_candidates.get(e.opcode)):
			opcode_all_candidates[e.opcode].append(e.candidates)
		else:
			opcode_all_candidates[e.opcode] = [e.candidates]

		line +=4
	instructions = [list(map(int,e.strip().split())) for e in data[3238:]]



print(f"part 1: {behaves_like_three_or_more_opcodes}")


opcode_functions = compromise_opcodes_to_function(opcode_all_candidates)


#	0: 		eqir
#	1: 		borr 
#	2: 		addr
#	3: 		gtri 
#	4:		muli
#	5: 		gtir
#	6: 		mulr
#	7: 		banr 
#	8: 		bori
#	9: 		eqri
#	10: 	eqrr
#	11: 	bani 
#	12: 	setr 
#	13: 	gtrr
#	14: 	addi
#	15: 	seti
 

def operate(instruction,reg,legend):
	(opcode,a,b,c) = (instruction[0],instruction[1],instruction[2],instruction[3])
	func = legend.get(opcode)

	if(func == "addr"):
		return(addr(reg,a,b,c))
	
	if(func == "addi"):
		return(addi(reg,a,b,c))
	
	if(func == "mulr"):
		return(mulr(reg,a,b,c))
	
	if(func == "muli"):
		return(muli(reg,a,b,c))
	
	if(func == "banr"):
		return(banr(reg,a,b,c))
	
	if(func == "bani"):
		return(bani(reg,a,b,c))
	
	if(func == "borr"):
		return(borr(reg,a,b,c))
	
	if(func == "bori"):
		return(bori(reg,a,b,c))
	
	if(func == "setr"):
		return(setr(reg,a,b,c))
	
	if(func == "seti"):
		return(seti(reg,a,b,c))
	
	if(func == "gtir"):
		return(gtir(reg,a,b,c))
	
	if(func == "gtri"):
		return(gtri(reg,a,b,c))
	
	if(func == "gtrr"):
		return(gtrr(reg,a,b,c))	

	if(func == "eqri"):
		return(eqri(reg,a,b,c))	

	if(func == "eqir"):
		return(eqir(reg,a,b,c))

	return(eqrr(reg,a,b,c))


registers = [0,0,0,0]

for ins in instructions:
	registers = operate(ins,registers,opcode_functions)

print(f"part 2: {registers}")