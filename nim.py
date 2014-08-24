# Huiyao Doris Tang
# August 20, 2014

from random import randrange
import heapq

print "\nWelcome to the Nim Game! May the odds (literally) be ever in your favor.\n"

#Boolean for if game is won
won = False


#Generate random number of heaps (3, 5, or 7)
heaps = randrange(3);
heaps = (2*(heaps+1))+1

#Generate heaps and string for number of items in each heap
master_list = []
sizes_str = ""
i = heaps
while i > 0 :
	items = randrange(3)
	items = (2*(items+1)+7)
	heap_list = range(1, items+1)
	heapq.heapify(heap_list)
	master_list.append(heap_list)
	sizes_str += str(items) + " "
	i -= 1

#Print master_list
print "Created " + str(heaps) + " heaps of sizes " + sizes_str + "\n"


#Randomly chose first player
first = randrange(2)

#1 indicates it is that player's turn
#0 indicates it is not that player's turn
human = 0
computer = 0
if first == 0 :
	human = 1
else :
	computer = 1
if human == 1 :
	print "Human goes first."
else :
	print "Computer goes first."


#Onto the game!
while not won :

	#Computer's turn
	if computer == 1 :
		#Choose random heap
		heap_num = randrange(heaps)
		while len(master_list[heap_num]) == 0 :
			heap_num = randrange(heaps)
		heap_num += 1

		#Choose random number of items to remove from chosen heap
		i = len(master_list[heap_num-1])
		items_num = randrange(i)+1

		print "Computer takes " + str(items_num) + " objects from heap " + str(heap_num)
		

	#Human's turn
	else :
		#Prompt human for command line input
		valid_input = False

		while not valid_input :
			try: 
				items_num, heap_num = [int(x) for x in raw_input("Human! Enter the number of objects (Y) to take from what heap (X)- in order: Y X: ").split()]
				while (heap_num <= 0) or (heap_num > heaps) or (items_num <= 0) or (items_num > len(master_list[heap_num-1])) :
					items_num, heap_num = [int(x) for x in raw_input("Human! That was not a good move, try again: ").split()]
				valid_input = True
				break
			except ValueError :
				print "Two values, please."

	#Modify chosen heap
	j = items_num
	while j > 0 :
		heapq.heappop(master_list[heap_num-1])
		j -= 1


	#Display heap sizes
	#Check if any player wins
	won = True
	sizes_str = ""
	i = 0
	while i < heaps :
		heap_len = len(master_list[i])
		if heap_len != 0 :
			won = False
		sizes_str += str(heap_len) + " "
		i += 1
	print sizes_str + "\n"

	if won :
		#Human wins!
		if computer == 1 :
			print "Human wins! Nicely done"
		#Computer wins
		else :
			print "Computer wins! Why don't you try again?"


	#Switch players for next turn
	human = computer
	computer = not human






