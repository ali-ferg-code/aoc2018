import sys

# day11.py {serial number} {square start size} {square end size}

def create_matrix(serial_number):

	matrix = []
	cols = []

	for row in range(1,301):
		cols = []
		for col in range(1,301):
			cols.append(get_power_level(col,row,serial_number))
		matrix.append(cols)
	return matrix


def get_hundreds_digit(num):
	word = str(num)
	if len(word)>2:
		return int(word[-3])
	return 0


def get_power_level(col,row,serial):
	rack_id = col + 10
	power_level_start = rack_id * row
	add_serial_num = power_level_start + serial 
	mul_by_rack_id = add_serial_num * rack_id
	hundreds_digit = get_hundreds_digit(mul_by_rack_id)
	return hundreds_digit - 5


def max_subsquare(matrix,square_size):


	cell_matrix = []
	max_power_seen = -10000
	max_power_coordinates = (-1,-1)

	for y in range(0,len(matrix)-(square_size-1)):
		cell_cols = []
		for x in range(0,len(matrix)-(square_size-1)):
			cell_power =0 

			for r in range(square_size):
				cell_power+=sum(matrix[y+r][x:x+square_size])


			if(cell_power>max_power_seen):
				max_power_seen = cell_power
				max_power_coordinates = (x+1,y+1)

	print(f"square: {square_size}, power {max_power_seen}, coords {max_power_coordinates}")
	return max_power_seen


m = create_matrix(int(sys.argv[1]))

for i in range(int(sys.argv[2]),int(sys.argv[3])):
	max_subsquare(m,i)
