# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
def get_even_ints(numbers):
	even_ints = []
	for num in numbers:
		if num % 2 == 0:
			even_ints.append(num)
	return even_ints
print(get_even_ints(numbers))

# 2. Print the difference between the largest and smallest value:
def get_diff(numbers):
	sorted_list = sorted(numbers)
	diff = sorted_list[-1] - sorted_list[0]
	return diff
print(get_diff(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
def check_two_adjacency(numbers):
	sorted_list = sorted(numbers)
	for i in range (len(sorted_list)-1):
		if sorted_list[i] == 2:
			if sorted_list[i+1] == 2:
				return True
	return False
print(check_two_adjacency(numbers))

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
def print_but_ignore(numbers):
	sum = 0
	pause = False
	for i in range(len(numbers)):
		if numbers[i] == 6:
			pause = True
			continue
		elif numbers[i] == 7:
			pause = False
			continue
		if not pause:
			sum += numbers[i]
	return sum

print(print_but_ignore([11, 6, 4, 99, 7, 11]))

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
def print_sum_not_13(numbers):
	sum = 0
	for i in range(len(numbers)):
		if i != 0 and numbers[i-1] == 13:
			continue
		if numbers[i] == 13:
			continue
		sum += numbers[i]
	return sum
print(print_sum_not_13([5,13,2]))