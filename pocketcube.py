# moves are only: L  L' D  D' B  B' (in Singmaster notation)
# represented as  1 -1  2 -2  3 -3
Rr = L =  1 +3
Lr = R = -1 +3
Ur = D =  2 +3
Dr = U = -2 +3
Fr = B =  3 +3  
Br = F = -3 +3

# sequences of moves (algorithms) are list of moves
#
# there are 8 cubies: 0-6 (7 is the origin), also representing positions
# UP: 
#        5  6
#        4  V (8)
# DOWN (rotating on the x axis):
#        1  2
#        0  3
#
# orientation of cubies is given by white or yellow.
# for each cubie can be: 
# L    R 
# D    U 
# B    F 
#
#
# A solved cube state:
#
# state = {
#    positions =    [0, 1, 2, 3, 4, 5, 6], # that is, each cubie is in its position; position[0] specifies which cubie is in position 0 (BDL)
#    orientations = [D, D, D, D, U,U,U]  # that is, each cubie in position 0-3 (face D) are facing down, the other are facing up 
#
# }
#
# or simply = [0, 1, 2, 3, 4, 5, 6, D, D, D, D, U,U,U ]   # that is, a vector of 14 elements
#

def get_solved_cube():
	solved_cube = [0, 1, 2, 3, 4, 5, 6] + [D, D, D, D, U, U, U]
	return solved_cube

# Rotation Rules
# (1,1)     ->  4 4
# (-2,3)    ->  1 6
# (3,2)     ->  6 5
# (2,-3)    ->  5 0
# (-3,-2)   ->  0 1
# orientations
# Lr

oL  = [None] * 7
oLr = list(oL)
oD  = list(oL)
oDr = list(oL)
oB  = list(oL)
oBr = list(oL)


for fr, to in [(U,F),(F,D),(D,B),(B,U),(L,L)]:  # pairs of from -> to orientations
	oL[fr] = to
	oLr[to] = fr

for fr, to in [(D,D),(F,R),(R,B),(B,L),(L,F)]:  # pairs of from -> to orientations
	oD[fr] = to
	oDr[to] = fr

for fr, to in [(B,B),(U,L),(L,D),(D,R),(R,U)]:  # pairs of from -> to orientations
	oB[fr] = to
	oBr[to] = fr


def apply_moves(s, seq):
	s = list(s) # create a new list object (copy the state s)
	for m in seq:
		s = move(s,m)
	return s

def move(s, m):
	""" Get a cube state s and apply move m, then return new state
		Moves are only: L  L' D  D' B  B' (in Singmaster notation)
		represented as  1 -1  2 -2  3 -3

		NOTE: they are applied IN PLACE (input cube state will change)
	"""
	s = list(s) # create a new list object (copy the state s)

	if m==L: 
		# positions
		s[5],s[0],s[1],s[4] = s[0],s[1],s[4],s[5]

		# orientations
		s[5+7],s[0+7],s[1+7],s[4+7] =	oL[s[0+7]], oL[s[1+7]], oL[s[4+7]], oL[s[5+7]]

	elif m==Lr:
		s[0],s[1],s[4],s[5] = s[5],s[0],s[1],s[4] 
		s[0+7],s[1+7],s[4+7],s[5+7] =	oLr[s[5+7]], oLr[s[0+7]], oLr[s[1+7]], oLr[s[4+7]]

	elif m==D:
		s[0],s[1],s[2],s[3] = s[3],s[0],s[1],s[2]
		s[0+7],s[1+7],s[2+7],s[3+7] = oD[s[3+7]], oD[s[0+7]], oD[s[1+7]], oD[s[2+7]]

	elif m==Dr:
		s[3],s[0],s[1],s[2] = s[0],s[1],s[2],s[3]
		s[3+7],s[0+7],s[1+7],s[2+7] =  oDr[s[0+7]], oDr[s[1+7]], oDr[s[2+7]], oDr[s[3+7]]

	elif m==B:
		s[6],s[3],s[0],s[5] = s[3],s[0],s[5],s[6]
		s[6+7],s[3+7],s[0+7],s[5+7] = oB[s[3+7]], oB[s[0+7]], oB[s[5+7]], oB[s[6+7]]

	elif m==Br:
		s[3],s[0],s[5],s[6] = s[6],s[3],s[0],s[5]
		s[3+7],s[0+7],s[5+7],s[6+7] = oBr[s[6+7]],oBr[s[3+7]],oBr[s[0+7]],oBr[s[5+7]]

	else: raise Exception('move have to be in [-3, +3]')

	return s

_o = {L:'L',B:'B',D:'D',R:'R',U:'U',F:'F'}

def letter_from_move(m):
	l = {L:'L',B:'B',D:'D',R:'L\'',U:'D\'',F:'B\''}
	return l[m]


def print_cube(s):
	o = _o
	
	print ' '*4 + '{0}{1}'.format( s[5] , o[s[5+7]] ) + ' {0}{1}'.format( s[6] , o[s[6+7]] )
	print ' '*4 + '{0}{1}'.format( s[4] , o[s[4+7]] ) + ' 7U'

	print ' '*4 + '{0}{1}'.format( s[1] , o[s[1+7]] ) + ' {0}{1}'.format( s[2] , o[s[2+7]] )
	print ' '*4 + '{0}{1}'.format( s[0] , o[s[0+7]] ) + ' {0}{1}'.format( s[3] , o[s[3+7]] )
	print

def state2number(s):
	val = 0
	for i,n in enumerate(reversed(s)):
		val += n*10**i
	return val
	
def number2state(n):
	s = [None]*14
	for i in range(len(s)):
		s[i] = n%10
		n /= 10
	return [x for x in reversed(s)]


#assert 
#print move(get_solved_cube(),L)
#print move(get_solved_cube(),D)
#print move(get_solved_cube(),B)

