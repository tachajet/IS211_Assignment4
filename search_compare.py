def sequential_search(a_list, a_item):
	pos = 0
	a_found = False
	from time import time
	seqsearch_timer=time()
	while pos < len(a_list) and not a_found:
		if a_list[pos] == a_item:
			a_found = True
		else:
			pos = pos+1
	seqsearch_timer=(time()-seqsearch_timer)
	return a_found,seqsearch_timer
def ordered_sequential_search(b_list, b_item):
	pos = 0
	found = False
	stop = False
	from time import time
	o_seqsearch_timer=time()
	while pos < len(b_list) and not found and not stop:
		if b_list[pos] == b_item:
			found = True
		else:
			if b_list[pos] > b_item:
				stop=True
			else:
				pos=pos+1
	o_seqsearch_timer=(time()-o_seqsearch_timer)
	return found,o_seqsearch_timer


def binary_search(a_list, item):
	first = 0
	last = len(a_list) - 1
	found = False
	from time import time
	b_search_timer=time()
	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	b_search_timer=(time()-b_search_timer)
	return found,b_search_timer

def main():
	from random import randint
	t_list=[]
	for x in range(0,100):
		t_list.append([])
		m=randint(1, 3)
		if m==1:
			for y in range(0,500):
				n=randint(1, 200)
				t_list[x].append(n)
		if m==2:
			for y in range(0,1000):
				n=randint(1, 200)
				t_list[x].append(n)
		else:
			for y in range(0,10000):
				n=randint(1, 200)
				t_list[x].append(n)
	s_search_counter=[]
	os_search_counter=[]
	b_search_counter=[]
	for a in range(0,100):
		s_search_counter.append(sequential_search(t_list[a], -1)[1])
	for b in range(0,100):
		t_list[b].sort()
		os_search_counter.append(ordered_sequential_search(t_list[b], -1)[1])
		b_search_counter.append(binary_search(t_list[b], -1)[1])
	s_search_avg=0
	for s in s_search_counter:
		s_search_avg+=s
	os_search_avg=0
	for o in os_search_counter:
		os_search_avg+=o
	b_search_avg=0
	for z in b_search_counter:
		b_search_avg+=z
	print("Sequential Search took %10.7f seconds to run, on average" % (s_search_avg/100))
	print("Ordered Sequential Search took %10.7f seconds to run, on average" % (os_search_avg/100))
	print("Binary Search took %10.7f seconds to run, on average" % (b_search_avg/100))
	
		
if __name__=="__main__":
	main()