#
# Copyright 2016, Maurizio Atzori, University of Cagliari (Italy)
#

from pocketcube import *
from sys import stderr, argv
#import multiprocessing

# check input parameter (max_levels)
try:
	max_levels = int(argv[1]) # 2
except:
	print >> stderr, 'Error: you need to specify a distance (an int) representing the maximum number of moves'
	exit(-1)

def n_cores():
	# get number of cores
	try:
		cores = int(argv[2])
		print >> stderr, 'using %d cores as specified' % cores
	except:
		cores = multiprocessing.cpu_count()
		print >> stderr, 'there are %d cores' % cores



solved = get_solved_cube()

sol = {}

sol[state2number(solved)] = []
current_level = sol.copy()


for level in range(1,max_levels+1):
	last_level = current_level
	current_level = {}
	print >> stderr, 'solving level %d' % level,
	#possible_moves = [L,B,D,Lr,Br,Dr]
	for s,seq in last_level.iteritems():
		s = number2state(s)
		possible_moves = [L,B,D,Lr,Br,Dr]
		if level>1: possible_moves.remove(-seq[-1]+6) # ((move-3)*-1)+3 = -move +3 +3 = -move+6
		for m in possible_moves:
			new_s = move(s,m)
			new_s = state2number(new_s)
			if new_s not in sol:
				new_seq = seq + [m]
				current_level[new_s] = new_seq
				sol[new_s] = new_seq
				print new_s, ' '.join([letter_from_move(m) for m in new_seq])  
	print >> stderr, len(sol), len(current_level)
	

#for s, seq in sol.iteritems():
#	print ' '.join([letter_from_move(m) for m in seq])
#	print_cube(number2state(s))
#	pass

#print len(sol)

#print >> stderr, sol

