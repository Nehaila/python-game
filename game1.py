import pygame
import sys
import random
import time

pygame.init() 
keys=pygame.key.get_pressed()
position= width, height = 800,600						# this is a tuple   #pos_height is the y top left position
pos1_width = 200	#Top left x position
size= 40		
pos1_height=height-size*2
pos2_width=random.randint(size, width)
pos2_height=0
pos22_height=0
pos22_width=random.randint(size, width)
game_over= False
screen= pygame.display.set_mode((width,height))			# Create screen display

clock=pygame.time.Clock()

pygame.draw.rect(screen, (255,0,0), (pos1_width,pos1_height,size,size))
x=random.randint(size, width)
y=random.randint(size, width)

def drop_other_enemies(List1,element1):
	p=0
	for p in range(5):
		pos22_width = List1[p]
		pygame.draw.rect(screen, (0,255,0), (pos22_width,pos22_height,size,size)) 
		if (pos22_width >= pos1_width) and (pos22_width <= (pos1_width + size))  and (pos22_height +size) >= pos1_height and (pos22_height +size) <= (pos1_height+size):
			pygame.display.update()	
			game_over = True
			print("Game over loser")
			pygame.quit()
		elif (pos22_width+size) >= pos1_width and (pos22_width+size) <= (pos1_width - size) and (pos22_height+size<= pos1_height) and (pos22_height +size >= (pos1_height+size)):
			pygame.display.update()	
			game_over=True
			print("Game over loser")
			pygame.quit()
		else:
			game_over=False
			element= random.randint(size, width)
			List1.append(element1)



def drop_enemies(List,element):
	j=0
	for j in range(6):
		pos2_width = List[j]
		pygame.draw.rect(screen, (0,255,0), (pos2_width,pos2_height,size,size))
		if (pos2_width >= pos1_width) and (pos2_width <= (pos1_width + size))  and (pos2_height +size) >= pos1_height and (pos2_height +size) <= (pos1_height+size):
			pygame.display.update()	
			game_over = True
			print("Game over loser")
			pygame.quit()
		elif (pos2_width+size) >= pos1_width and (pos2_width+size) <= (pos1_width - size) and (pos2_height+size<= pos1_height) and (pos2_height +size >= (pos1_height+size)):
			pygame.display.update()	
			game_over=True
			print("Game over loser")
			pygame.quit()
		elif (pos2_width + size >= pos1_width) and (pos2_width + size <= (pos1_width + size)) and (pos2_height +size) >= pos1_height and (pos2_height +size) <= (pos1_height+size):
			pygame.display.update()	
			game_over=True
			print("Game over loser")
			pygame.quit()
		element= random.randint(size, width)
		List.append(element)
		
while not game_over:
	L=[random.randint(size, width)]
	LL=[random.randint(size, width)]
	pos2_height=0
	pos22_height=0
	while pos2_height <= height and pos22_height <= height:
		drop_enemies(L,x) 
		#drop_enemies(LL,y)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				syst.exit()
			if event.type == pygame.KEYDOWN:
						
				if event.key == pygame.K_LEFT:
					pos1_width -= size
			
				elif event.key== pygame.K_RIGHT:
					pos1_width +=size
			
		pygame.display.update()	
		
		pos2_height += size

		if pos2_height >= size*4:
			drop_other_enemies(LL,y)
			pos22_height += size


		pygame.draw.rect(screen, (255,0,0), (pos1_width,pos1_height,size,size))

		pygame.display.update()	

		screen.fill((0,0,0))
		
		clock.tick(6)

