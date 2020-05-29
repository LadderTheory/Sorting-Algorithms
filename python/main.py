import random
#import sys
import time

import sort

min = 0
max = 100000
unsorted = list(range(min,max))

for i in range(len(unsorted)): unsorted[i] = random.randrange(1,10)
#unsorted = list(reversed(unsorted)) #Reversed list

#print(unsorted)

algs = [
	#lambda lst: (print("Bubble Sort: ", end=""), sort.bubble(lst)),
	#lambda lst: (print("Selection Sort: ", end=""), sort.selection(lst)),
	lambda lst: (print("Merge Sort (recursive): ", end=""),	sort.merge_recurse(lst)),
	lambda lst: (print("Merge Sort (iterative): ", end=""),	sort.merge_iter(lst)),
	#lambda lst: (print("Quick Sort (iterative): ", end=""), sort.quick_iter(lst)),
	#lambda lst: (print("Quick Sort (recursive): ", end=""), sort.quick_recurse(lst)),
	#lambda lst: (print("Insertion Sort: ", end=""), sort.insertion(lst)),
	#lambda lst: (print("Shell Sort: ", end=""), sort.shell(lst)),
	lambda lst: (print("Gravity Sort: ", end=""), sort.gravity(lst)),
]

for i in range(len(algs)):
	t = time.process_time()

	lst = unsorted.copy()
	algs[i](lst)

	print(str(time.process_time() - t), "seconds")

	if 0:
		print(unsorted)
		print(lst)
		print()