import pygame, random, sys
from pygame.locals import *
import time

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	#x1=first block on the x
	#x2=last block on the x
	#y1=first block on the y
	#y2=last block on the y
	#w1=width
	#w2=width
	#h1=height
	#h2=height

	#print ('x1=',x1,'x2=',x2,'y1=',y1,'y2=',y2,'w1=',w1,'w2=',w2,'h1=',h1,'h2=',h2)

	#How to determine if there is a collision
	#1. If the first block of the snake plus the width of the snake is greater than the position of the last block

	#print ('If x1(',x1,')+w1(',w1,')>x2(',x2,') and x2(',x2,')+w2(',w2,')>x1(',x1,')')
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False


def display(screen,text):
	print ('text=',text)
	f=pygame.font.SysFont('Arial', 30)
	t=f.render('this is a test', True, (0, 0, 0))
	screen.blit(t, (SCREEN_X/2, SCREEN_Y/2))
	pygame.display.update()
	pygame.time.wait(2000)

def die(screen, score):
	f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0))
	screen.blit(t, (SCREEN_X/2, SCREEN_Y/2))
	pygame.display.update()
	pygame.time.wait(2000)
	sys.exit(0)





#dirs indicates direction - 0=down, 1=right, 2=up, 3=left
dirs = 0
DIRECTION='down'

#Set the score to zero
score = 0


#pygame.mixer.init(44100,-16,2,128)
pygame.mixer.init(11000,0,1,512)


#
#Initialize pgame
pygame.init()

#pygame.mixer.music.load('chomp.wav')
chomp=pygame.mixer.Sound('chomp_short.wav')


SCREEN_X=500
SCREEN_Y=500

#Set the position of the 'apple'
applepos = (random.randint(100,SCREEN_X-100), random.randint(100,SCREEN_Y-100))


#Set the screen size
s=pygame.display.set_mode((SCREEN_X,SCREEN_Y))

#Set the caption of the screen

pygame.display.set_caption('Snake')


#Surface is the pygame object for representing images
#Create a 10pxlx10pxl object

APPLE_WIDTH=20
APPLE_HEIGHT=20
#appleimage = pygame.Surface((APPLE_WIDTH,APPLE_HEIGHT))
#appleimage=img=pygame.image.load ('apple.png')

appleimage=img=pygame.image.load ('apple.png')

background_image=pygame.image.load('jungle7.jpg').convert()




#Make it green
#appleimage.fill((0, 255, 0))

#Now, create the snake segment, a 20x20 pixel block
SNAKE_WIDTH=10
SNAKE_HEIGHT=10
img = pygame.Surface((SNAKE_WIDTH,SNAKE_HEIGHT))


SNAKE_X_START=SCREEN_X/2
#The initial X position of each segment of the snake
xs = [SNAKE_X_START, SNAKE_X_START, SNAKE_X_START, SNAKE_X_START, SNAKE_X_START]

SNAKE_Y_START=SCREEN_Y/2
#The initial Y position of each segment of the snake
ys = [SNAKE_Y_START, SNAKE_Y_START-SNAKE_WIDTH, SNAKE_Y_START-(SNAKE_WIDTH*2), SNAKE_Y_START-(SNAKE_WIDTH*3), SNAKE_Y_START-(SNAKE_WIDTH*4	)]


#Make the snake red
img.fill((255, 0, 0))

print ('xs=',xs)
print ('ys=',ys)



#Set the font
f = pygame.font.SysFont('Arial', 20)

#Create a clock object
clock = pygame.time.Clock()
fps=5
#
cnt=1

# time.sleep(5)
# sys.exit()


while True:
	fps=5+(score)

	print ('fps=',fps)

	clock.tick(fps) #Ensures we don't go over 10 FPS

	for event in pygame.event.get(): #Trap any events

		if event.type == QUIT: #The x on the window
			sys.exit(0)
		#dirs indicates direction - 0=down, 1=right, 2=up, 3=left
		elif event.type == KEYDOWN: #Detects a keypress
			if event.key == K_SPACE:
				time.sleep(10)
			if event.key == K_UP and dirs != 0: #If you press up key and we aren't going down, then go up
				dirs = 2 #2=up
			elif event.key == K_DOWN and dirs != 2: #If you press down key aand we aren't going up, then ok
				dirs = 0 #0=down
			elif event.key == K_LEFT and dirs != 1: #If you press the left key and we aren't going right, then ok
				dirs = 3 #3=left
			elif event.key == K_RIGHT and dirs != 3: #If you press the right key and we aren't going left, then ok
				dirs = 1 #1=right

	red=random.randint(200,255)
	img.fill((red,0,0))

	#green=random.randint(200,255)
	#appleimage.fill((0, green, 0))



	i = len(xs)-1 #How many segments the snake has on the X axis
	print ('i=',i)
	#If the snake runs into himself (bad)
	while i >= 2:
	# 	#args are: first block of snake on the x, last block on the x, first on the y, last on the y
	# 	# and then the size of each block of the snake (20x20 pixels)
		if collide(xs[0], xs[i], ys[0], ys[i], SNAKE_WIDTH, SNAKE_WIDTH, SNAKE_HEIGHT, SNAKE_HEIGHT):
			die(s, score)
		i=i-1





	#if the snake runs into the apple (good)
	#args are: first block of snake on the x, x pos of the apple, y pos of the apple
	# and then the size of width of the snake, width of the apple, height of the snake, height of the apple
	if collide(xs[0], applepos[0], ys[0], applepos[1], SNAKE_WIDTH, APPLE_WIDTH, SNAKE_HEIGHT, APPLE_HEIGHT):
		chomp.play()
		score+=1

		# Add another segment
		# segment=xs[len(xs)-1]+20
		# print ('segment=',segment)
		# print ('xs[0]=',xs[0])
		# print ('xs[1]=',xs[1])
		# print ('xs[2]=',xs[2])
		# print ('xs[3]=',xs[3])
		# print ('xs[4]=',xs[4])

		#time.sleep(3)
		# We are going to add a segment to the snake (add an element to each list, x and y)
		# The number doesn't really matter, it's just a placeholder
		#The element gets changed dynamically when the snake moves

		xs.append(500) #Add to the x-length of the snake
		ys.append(500) #Add to the y-length of the snake
		w,h=appleimage.get_size()
		#appleimage=pygame.transform.scale(appleimage,(w+5,h+5))
		applepos=(random.randint(0,SCREEN_X-50),random.randint(0,SCREEN_Y-50))


	if xs[0]>SCREEN_X:
		xs[0]=0
	elif xs[0] <0:
		xs[0]=SCREEN_X-10

	if ys[0] > SCREEN_Y:
		ys[0] = 0
	elif ys[0] < 0:
		ys[0] = SCREEN_Y-10

	print ('xs[0]=',xs[0])
	print ('ys[0]=',ys[0])


	#This is what moves the body
	#Each segment is moved
	i = len(xs)-1
	print ('i=',i)
	while i >= 1:
		xs[i] = xs[i-1]
		ys[i] = ys[i-1]
		#print ('xs[i]=',xs[i])
		i -= 1


	if dirs==0:
		ys[0] += SNAKE_HEIGHT
	elif dirs==1:
		xs[0] += SNAKE_WIDTH
	elif dirs==2:
		ys[0] -= SNAKE_HEIGHT
	elif dirs==3:
		xs[0] -= SNAKE_WIDTH



	# print ('xs[0]=',xs[0])
	# print ('xs[1]=',xs[1])
	# print ('xs[2]=',xs[2])
	# print ('xs[3]=',xs[3])
	# print ('xs[4]=',xs[4])
	# print ('xs[5]=',xs[5])
	# print ('xs[6]=',xs[6])


	# print ('ys[0]=',ys[0])
	# print ('ys[1]=',ys[1])
	# print ('ys[2]=',ys[2])
	# print ('ys[3]=',ys[3])
	# print ('ys[4]=',ys[4])

	#Clear the screen between each animation
	s.fill((255, 255, 255))

	#Draw the background
	s.blit(background_image,(0,0))

	#Draw the snake
	for i in range(0, len(xs)):
		s.blit(img, (xs[i], ys[i]))

	#Draw the apple
	s.blit(appleimage, applepos)
	t=f.render(str(score), True, (0, 0, 0))
	s.blit(t, (SCREEN_X/2, 20))


	#Put it all on the screen
	pygame.display.update()





					
			


