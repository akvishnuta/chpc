class entitites(object):
	"""docstring for entitites"""
	def __init__(self, power,life,colour,position):
		self.power = power
		self.life = life
		self.colour = colour
		self.position = position
	def print_pos(self):
		print self.position
	def change_pos(self,i,n,size):
		if((self.position[i]==0 and n<0) or (self.position[i]==size and n>0)):
			print 'Operation is out of the matrix'
		else:
			self.position[i]=self.position[i]+n
	def power_ret(self):
		return self.power


class players(entitites):
	"""docstring for players"""
	def __init__(self, p_id,power,life,colour,position):
		self.p_id = p_id
		super(players, self).__init__(power, life, colour,position)
	def fight(self,env,enemy):
		#print env.enemy_pos.values()
		if(self.position in env.enemy_pos.values()):
			key = env.enemy_pos.keys()[env.enemy_pos.values().index(self.position)]
			#print 'Key : ',key
			if (enemy[int(key)-1].power_ret() >self.power_ret()):
				self.life=self.life-1
				if(self.life==0):
					print 'You are killed'
					exit()
				else:
					print 'You encountered an enemy, Life Remaining: '+ str(self.life)
				

class enimies(entitites):
	"""docstring for players"""
	def __init__(self, e_id,power,life,colour,position,env):
		self.e_id = e_id
		super(enimies, self).__init__(power, life, colour,position)
		env.add_enemy(e_id,position)

class Environment():
	enemy_pos={}
	"""docstring for Environment"""
	def __init__(self, matrix_size):
		self.matrix_size = matrix_size
		
	def add_enemy(self,e_id,position):
		self.enemy_pos[str(e_id)] = position


def title_display():
	#os.system('clear')
	k=raw_input('')
	return k

def list_player():
	print '1.Monty, Power:98, Colour:Blue'
	print '2.Heren, Power:78, Colour:BLue'
	k=input('Enter the player no to Choose :')
	return k

#size = input('Enter the size of square matrix(n) :')
size=8
env = Environment(size)
player_no = list_player()
if(player_no==1):
	player = players(1,98,3,'Blue',[size/2,size/2])
elif (player_no==2):
	player = players(2,78,3,'Blue',[size/2,size/2])
enemy = []
enemy.append(enimies(1,100,3,'Red',[1,2],env))
enemy.append(enimies(2,100,3,'Red',[2,1],env))
print 'Enemy position : ',env.enemy_pos['1']
print 'Enemy position : ', env.enemy_pos['2']
print "Welcome to Python Game, Use 'w' 'a' 's' 'd' for controls and 'q' to quit"
k=''
print 'Current Position = ',player.print_pos() 
while (k!='q'):
	k=title_display()
	if k=='w':
		player.change_pos(1,-1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif k=='a':
		player.change_pos(0,-1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif k=='s':
		player.change_pos(1,1,size)
		player.print_pos()
		player.fight(env,enemy)

	elif k=='d':
		player.change_pos(0,1,size)
		player.print_pos()
		player.fight(env,enemy)