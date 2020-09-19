def sequential_search(a_list, a_item):
	from timeit import Timer
	seqsearch_timer=Timer("sequential_search()", "from __main__ import sequential_search")
	pos = 0
	a_found = False
	while pos < len(a_list) and not a_found:
		if a_list[pos] == a_item:
			a_found = True
		else:
			pos = pos+1
	return a_found,seqsearch_timer
def ordered_sequential_search(b_list, b_item):
	pos = 0
	found = False
	stop = False
	from timeit import Timer
	o_seqsearch_timer=Timer("ordered_sequential_search()", "from __main__ import ordered_sequential_search")
	while pos < len(b_list) and not found and not stop:
		if b_list[pos] == b_item:
			found = True
		else:
			if b_list[pos] > b_item:
				stop=True
			else:
				pos=pos+1
	return found


def binary_search(a_list, item):
	first = 0
	last = len(a_list) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))

b_test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(b_test_list, 3))
print(ordered_sequential_search(b_test_list, 13))
print(binary_search(b_test_list, 3))
print(binary_search(b_test_list, 13))
