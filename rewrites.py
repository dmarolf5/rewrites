#! /usr/bin/python

from Queue import PriorityQueue

def positions_in(substring, string):
	"""
	Preconditions: substring and string are strings.
	Postconditions: The return value is the list of indices where the substring appears in the string.
	
	>>> positions_in('a', 'alphabet')
	[0, 4]
	>>> positions_in('b', 'alphabet')
	[5]
	>>> positions_in('c', 'alphabet')
	[]
	>>> positions_in('ab', 'alphabet')
	[4]
	"""
	result = []
	index = -1
	while True:
		index = string.find(substring, index + 1)
		if index == -1:
			return result
		result.append(index)

def get_neighbors_via_first_move(string):
	return {string[:position] + 'end' + string[position + len('start'):] for position in positions_in('start', string)}

def get_neighbors_via_second_move(string):
	return {string[:position] + 'end' + string[position + len('start'):] for position in positions_in('start', string)}

def get_neighbors_via_third_move(string):
	return {string[:position] + 'end' + string[position + len('start'):] for position in positions_in('start', string)}

def get_neighbors_via_fourth_move(string):
	return {string[:position] + 'end' + string[position + len('start'):] for position in positions_in('start', string)}

def get_all_neighbors(string):
	return get_neighbors_via_first_move(string) | get_neighbors_via_second_move(string) | get_neighbors_via_third_move(string) | get_neighbors_via_fourth_move(string)

source = 'start'
destination = 'end'

def heuristic(string):
	return abs(len(string) - len(destination))

solution = None
worklist = PriorityQueue()
worklist.put([source])
closed = set()
while not worklist.empty():
	path = worklist.get(False)
	end = path[-1]
	if end not in closed:
		closed |= {end}
		for extension in get_all_neighbors(end):
			worklist.put(path + [extension])
	if end == destination:
		solution = path
		break
print('Found a way to rewrite {source} to get {destination}:\n  {solution}'.format(source = repr(source), destination = repr(destination), solution = solution))
