"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if left > right:
		return -1

	middle = (right+left)//2

	if mylist[middle] == key:
		return middle
	elif mylist[middle] < key:
		return _binary_search(mylist, key, middle+1, right)
	else:
		return _binary_search(mylist, key, left, middle-1)

	### TODO

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([2,3,5,7,8], 3) == 1
	assert binary_search([4,5,7,9,10], 9) == 3





def time_search(search_fn, mylist, key):

	start_time = time.time() * 1000
	search_fn(mylist, key)
	end_time = time.time() * 1000
	return (end_time - start_time)

	### TODO


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

	time_list = []

	for size in sizes:
		current_tuple = []
		mylist = []
		for i in (range(int(size)-1)):
			mylist.append(i)

		linear_search_time = time_search(linear_search, mylist, -1)
		binary_search_time = time_search(binary_search, mylist, -1)

		current_tuple.append(int(size))
		current_tuple.append(linear_search_time)
		current_tuple.append(binary_search_time)

		time_list.append(current_tuple)

	return time_list

	### TODO

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())
