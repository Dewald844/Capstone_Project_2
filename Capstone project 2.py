#Task 15.00 
    ##Author : Dewald Haasbroek
    ##Date  : 25/07/2020
    ##Time : 10:00 


# imports 

import pygame
import random

#initializing modules 

pygame.init()

# Screen dimensions W and H 

screen_width = 1440
screen_height = 680

#creates screen and gives it width and height 

screen = pygame.display.set_mode((screen_width,screen_height))

#Creates player and ads image ot player and enemy 

player = pygame.image.load('player.jpg')
enemy = pygame.image.load('monster.jpg')
prize = pygame.image.load('prize.jpg')

# Get width and height of image for boundary ditection 

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

#Store positions of enemy and plpayer as veriables 

player_posX = 100
player_posY = 50

#Enemy to start of at random y position 

enemy_posX = screen_width
enemy_posY = random.randint(0, screen_height - enemy_height)

# Check if up and down left and right key is pressed by usiing an boolean variable 

keyUp = False 
keyDown = False
keyLeft = False
keyRight = False 

# Game loop 
    # Game loops run over and over again 
    # Screen needs to update and refresh and apply changes 

while 1:
    
    screen.fill(0) #clears screen  Should also be able to display an background image ? 
    screen.blit(player, (player_posX , player_posY))#draws player to specified position 
    screen.blit(enemy, (enemy_posX , enemy_posY))

    pygame.display.flip() # Updates screen

    # Loop that loops trough events during game 
    
    for event in pygame.event.get() :
        #check if user quits program 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # Check if key is pressed 
        
        if event.type == pygame.KEYDOWN:
            # Test if the key pressed is the key wanted 
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True 
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True 
        
        if event.type == pygame.KEYUP:
            # Test if the key released is the key wanted 
            
            if event.key == pygame.K_UP:
                keyUp = False 
            if event.key == pygame.K_DOWN:
                keyDown = False 
            if event.key == pygame.K_LEFT:
                keyLeft = False 
            if event.key == pygame.K_RIGHT:
                keyRight = False 
        
        
    # After keys are checked update game acccrodingly (moving player)
    
    if keyUp == True:
        if player_posY > 0:
            player_posY -=1
    if keyDown == True:
        if player_posY < screen_height - image_height:
            player_posY += 1 
    if keyLeft == True:
        if player_posX < screen_width - image_width:
            player_posX -= 1
    if keyRight == True:
        if player_posX > 0 :
            player_posX += 1 
    
        
    # enemy boundries
        # Coding the bounding boxes around die enemy image 
        # Coding the bounding boxes around player image 
        # If boxes intersep there is an collision 
            # wright tto test if collision occurs 
    
    enemyBB = pygame.Rect(enemy.get_rect())   
    
    enemyBB.left = enemy_posX
    enemyBB.top = enemy_posY
    
    playerBB = pygame.Rect(player.get_rect())
    
    playerBB.left = player_posX
    playerBB.top = player_posY 
    
    if playerBB.colliderect(enemyBB):
        
        # Displaying if game has been lost 
        
        print("You lose") 
        pygame.quit()
        exit(0)

    
    if enemy_posX < 0 - enemy_width:
        
        # Displaying if game is won     

        win = True
        print(" !!!  You Win  !!!")

    enemy_posX -= 0.30 
    

    
