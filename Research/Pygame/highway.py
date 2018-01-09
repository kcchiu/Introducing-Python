"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import numpy as np
 
# Define some colors
BLACK = (0, 0, 0)
GREY = (128,128,128)
LGREY = (180, 180, 180)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
 
pygame.init()

# Highway environment init
time_lanes_1 = 0
time_lanes_2 = 0
lanes_hor_num = 5
lanes_ver_num = 10
lanes_width = 3
lanes_length = 40
lanes_hor_sep = 40
lanes_ver_sep = 40
lanes_pos_ver_start_1 = 0
lanes_pos_ver_end_1 = 0
lanes_pos_ver_start_2 = 0
lanes_pos_ver_end_2 = 0

unit_length = lanes_ver_num * (lanes_length + lanes_ver_sep)
scr_width = 700
scr_length = unit_length - lanes_ver_sep

car_pos_ver = 0.5*scr_length
car_pos_hor = 120+10
car_speed = 0
press_updwn_cnt = 0

cars_num = 0
cars_total = 20
cars_timer = np.zeros([cars_total])
cars_pos_ver = np.zeros([cars_total]) - 120
cars_acc = np.zeros([cars_total])
cars_lanes_init = 40 * np.random.choice([1,2,3,4],cars_total) + 10
cars_lanes = cars_lanes_init
time_cars = np.zeros([cars_total])

fps = 60*5
reward = 0

font = pygame.font.SysFont('Calibri', 25, True, False)
text_hor_pos = lanes_hor_num*(lanes_length + lanes_ver_sep)

# Set the width and height of the screen [width, height]
size = (scr_width, scr_length)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
#                print("K_LEFT")
                car_pos_hor -= 40
                
            if event.key == pygame.K_RIGHT:
#                print("K_RIGHT")
                car_pos_hor += 40
                
    if car_pos_hor >= 170:
        car_pos_hor = 170
    elif car_pos_hor <= 50:
        car_pos_hor = 50
                    
    if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
        press_updwn_cnt += 0.01
        car_pos_ver -= 1 + press_updwn_cnt
        car_speed = -40 - press_updwn_cnt*10
    elif( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
        press_updwn_cnt += 0.01
        car_pos_ver += 1+press_updwn_cnt
        car_speed = 40 + press_updwn_cnt*10
    else:
        press_updwn_cnt = 0
    
    if car_pos_ver > (scr_length - 40):
        car_pos_ver = scr_length - 40
    elif car_pos_ver < 0:
        car_pos_ver = 0
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, LGREY, [0, 0, 30, scr_length])
    pygame.draw.rect(screen, LGREY, [210, 0, 30, scr_length])
    
    time_lanes_1 += 1
    time_lanes_2 += 1
    
    for i in range(lanes_ver_num):
        for j in range(lanes_hor_num):
            lanes_pos_ver_start_1 = time_lanes_1
            lanes_pos_ver_end_1 = lanes_length + time_lanes_1
            
            lanes_pos_ver_start_2 = time_lanes_2
            lanes_pos_ver_end_2 = lanes_length + time_lanes_2
            
            if lanes_pos_ver_start_1 == scr_length:
                time_lanes_1 = -lanes_length - unit_length
                lanes_pos_ver_end_1 = 0
                lanes_pos_ver_start_1 = -lanes_length - unit_length
                
            if lanes_pos_ver_start_2 == 2*scr_length + lanes_ver_sep:#6*2*80-40:
                time_lanes_2 = -lanes_length
                lanes_pos_ver_end_2 = 0
                lanes_pos_ver_start_2 = -lanes_length - unit_length
                
                
            pygame.draw.line(screen, BLACK, 
                             [40 + j*lanes_hor_sep, lanes_pos_ver_start_1 + i*(lanes_ver_sep+lanes_length)], 
                             [40 + j*lanes_hor_sep, lanes_pos_ver_end_1 + i*(lanes_ver_sep+lanes_length)], 
                             lanes_width)
            pygame.draw.line(screen, BLACK, 
                             [40 + j*lanes_hor_sep, lanes_pos_ver_start_2 + i*(lanes_ver_sep+lanes_length) - unit_length], 
                             [40 + j*lanes_hor_sep, lanes_pos_ver_end_2 + i*(lanes_ver_sep+lanes_length) - unit_length], 
                             lanes_width)
    
    pygame.draw.rect(screen, GREEN, [car_pos_hor, car_pos_ver, 20, 40])
    
    result = np.random.randn(1)
    
    if result > 2.5:
        if cars_num >= cars_total:
            cars_num = cars_total
        else:
            cars_num += 1
#    if cars_num == 10:
#        if result > 2.5:
#            cars_num -= 1
    
    time_cars = time_cars + 1
    
    cars_speed_chg_period = fps*np.random.choice([3,5,7,11],cars_total)
    cars_lanes_chg_period = fps*np.random.choice([3,5,7,11],cars_total)
    
    for i in range(cars_num):
        if time_cars[i] % cars_speed_chg_period[i] != 0:
    #        cars_pos_ver = 10*(np.random.random(10)-0.5)
    #        time_cars = 0
    #        cars_acc += (np.random.random(10)-0.5)
            cars_pos_ver[i] = cars_pos_ver[i] + cars_acc[i]
        else:
            cars_acc[i] = (np.random.random(1) - 0.5)
        
        if time_cars[i] % cars_lanes_chg_period[i] == 0:
            cars_lanes[i] = cars_lanes[i] + 40 * np.random.choice([-1,0,1],1, p=[0.25,0.5,0.25])
    
#    for i in range(cars_num):
        cars_timer[i] += 1
#        pygame.draw.rect(screen, BLACK, [120 + 10, cars_timer[i]+cars_pos_ver[i], 20, 40])
        if cars_pos_ver[i] > scr_length:
            cars_pos_ver[i] = scr_length
        elif cars_pos_ver[i] < 0 - 120:
            cars_pos_ver[i] = 0 - 120
        
        if cars_lanes[i] >=170:
            cars_lanes[i] = 170
        elif cars_lanes[i] <= 50:
            cars_lanes[i] = 50
            
        pygame.draw.rect(screen, BLACK, [cars_lanes[i], cars_pos_ver[i], 20, 40])
        
#        if (cars_lanes[i] == car_pos_hor) and (abs(int(cars_pos_ver[i]) - int(car_pos_ver)) < 50):
        
        if (cars_lanes[i] == car_pos_hor) and (abs(int(cars_pos_ver[i]) - int(car_pos_ver)) < 50):
            reward -= 1
            text_crash = font.render("CRASH!", True, RED)
            screen.blit(text_crash, [text_hor_pos, 270])
        else:
            reward += 0.01
    
#    print(cars_timer + cars_pos_ver)
#    print(cars_pos_ver)
    
    text_speed = font.render('%.1f' % ((fps)/3-car_speed), True, BLACK)
    screen.blit(text_speed, [text_hor_pos, 150])
    
    text_cars = font.render(str(cars_num), True, BLACK)
    screen.blit(text_cars, [text_hor_pos, 180])
    
    text_hit = font.render("Reward:", True, BLUE)
    screen.blit(text_hit, [text_hor_pos, 210])
    
    text_hit = font.render('%.1f' % reward, True, BLUE)
    screen.blit(text_hit, [text_hor_pos, 240])
    
    car_speed = 0
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(fps)
 
# Close the window and quit.
pygame.quit()