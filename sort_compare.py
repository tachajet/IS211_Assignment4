def insertion_sort(a_list):
	from time import time
	insert_time=time()
	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index
		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position = position - 1
		a_list[position] = current_value
		return time()-insert_time

def shell_sort(a_list):
	from time import time
	shell_time=time()
	sublist_count = len(a_list) // 2
	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(a_list, start_position, sublist_count)
		sublist_count = sublist_count // 2
		return time()-shell_time
def gap_insertion_sort(a_list, start, gap):
	for i in range(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i
		while position >= gap and a_list[position - gap] >current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value
def python_sort(b_list):
	from time import time
	sort_time=time()
	b_list.sort()
	return time()-sort_time
def main():
	from random import randint
	#generating a list that has 100 lists of 500, 1000, and 10000 values
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
	insert_counter=[]
	shell_counter=[]
	sort_counter=[]
	for a in range(3,5):
		insert_counter.append(insertion_sort(t_list[a]))
		shell_counter.append(shell_sort(t_list[a]))
		sort_counter.append(python_sort(t_list[a]))
	s_sort_avg=0
	for s in shell_counter:
		s_sort_avg+=s
	i_sort_avg=0
	for i in insert_counter:
		i_sort_avg+=i
	p_sort_avg=0
	for p in sort_counter:
		p_sort_avg+=p
	print("Shell sort took %10.7f seconds to run, on average" %(s_sort_avg/100))
	print("Insert sort took %10.7f seconds to run, on average" %(i_sort_avg/100))
	print("Python sort took %10.7f seconds to run, on average" %(p_sort_avg/100))
	
		
if __name__=="__main__":
	main()