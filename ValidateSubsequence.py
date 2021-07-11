array = [-5,-3,-1,1,3,5]
sequence = [-5,-1,5]

def isValidSubsequence(array, sequence):
    sPointer = 0
	aPointer = 0
	while aPointer < len(array) and sPointer < len(sequence):
		if array[aPointer] == sequence[sPointer]:
			sPointer += 1
		aPointer += 1
	
	return sPointer == len(sequence)

isValidSubsequence(array, sequence)
