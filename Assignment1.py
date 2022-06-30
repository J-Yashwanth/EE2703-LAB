
"""
EE2703 Applied Programming Lab - 2022
Assignment 1: Solution
Jarpla Yashwanth - EE20B048
26th January 2021
"""

#INPUT: .netlist file
#OUTPUT: Identifies errors in SPICE program code, and displays the tokens in reverse order


from sys import argv, exit

"""
Checking whether the given inputs are the required ones, and whether the given file name 
is correct and the file exists. If not the open function throws an error.
"""

if len(argv) == 2 :	
	file = argv[1]
else:
	print("Number of arguments must be 2")
	exit(0)

# File Handling    
try:
	f = open(file)
	lines = f.readlines()
	f.close()
except:
	print("File not found")
	exit(0)

	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
"""
The constant variables 'start_Cir' and 'end_Cir' determines the start and end of the
described circuit.  The 'start' and 'end' variables denote thet starting and ending line of 
the circuit simulation program. 
"""
start_Cir = '.circuit'
end_Cir = '.end'
start = -1
end = -2


"""
The location of each line is stored, and the endline character is removed from each 'line'.
Following that, the 'line' is split into two parts, the comment and the program code. The 
comment is ignored and only the program code is saved in the variable 'line'. The tab spaces
are converted to spaces and then the lines are stripped out of their leading and trailing 
spaces and then compared to find the beginning and the ending of the code.
"""

for line in lines:

	location = lines.index(line)
	line = line.replace('\n','')
	line = line.split('#')[0]
	line = line.replace('\t',' ')	
	line=line.strip()
	lines[location] = line

	if line[:len(start_Cir)] == start_Cir:
		start = location
	elif line[:len(end_Cir)] == end_Cir:
		end = location;	

if start >= end:
	print("Circuit Block Invalid")
	exit(0)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Token = []

for line in lines[start+1:end]:
	
	"""
	The location of each line is stored. From 'line' a 'linelist' of words/tokens are 
	created i.e., tokens are separated by space are stored in 'linelist'. If the linelist 
	is empty this iteration is ignored
	"""
	location = lines.index(line)
	linelist = line.split(" ")
	linelist = [elem for elem in linelist if elem != ""]

	if linelist == []:
		continue
		
	"""
	Following that, the 'linelist' is checked for whether it is a resistor, capacitor, inductor
	dependent and independent voltage and currect sources and appended to the 'Token'. In case of
	resistor, inductor, capacitor independent voltage and current source, the relations depends 
	on only two nodes - thus 4 tokens. Similarly in case of voltage dependent sources, there are 
	6 tokens, and in case of current dependent sources, there are 5 tokens. The intial letter of
	label of the elements denote the element type. The label of nodes must also be alphanumeric. 
	"""
	if linelist[0][0] == 'R' or 'L' or 'C' or 'V' or 'I' :	
		if len(linelist) != 4:
			print("Incorrect Number of Parameters: Line ",location)
			exit(0)
		if linelist[1].isalnum() != True or linelist[2].isalnum() != True :
			print("Incorrect Node Designation - only alphanumeric variables: Line ",location)
			exit(0)
		
	elif linelist[0][0] ==  'E' or 'G':
		if len(linelist) != 6:
			print("Incorrect Number of Parameters: Line ",location)
			exit(0)
		if linelist[1].isalnum() != True or linelist[2].isalnum() != True or linelist[3].isalnum() != True or linelist[4].isalnum() != True:
			print("Incorrect Node Designation - only alphanumeric variables: Line ",location)
			exit(0)
	

	elif linelist[0][0] ==  'H' or 'F':
		if len(linelist) != 5:
			print("Incorrect Number of Parameters: Line ",location)
			exit(0)
		if linelist[1].isalnum() != True or linelist[2].isalnum() != True:
			print("Incorrect Node Designation - only alphanumeric variables: Line ",location)
			exit(0)
		if linelist[3][0] != 'V':
			print("Incorrect Voltage Label: Line ",location)
			exit(0)
	
	Token.append(linelist)
	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Now the tokens are then printed in the reverse order		
"""	
length = len(Token)
for i in range(length-1,-1,-1):
	print(' '.join(Token[i]))


	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
