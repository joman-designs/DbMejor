import pygame
import os
pygame.init()

print("hello world")

WIDTH, HEIGHT = 2048, 1024
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Helloo World!")
WHITE = (255, 255, 255)

FPS = 60
VEL = 10

DUDE_WIDTH, DUDE_HEIGHT = 128, 128

dude_left_1_image = pygame.image.load(
    os.path.join("assets", 'dude_left_1.png'))
dude_left_1 = pygame.transform.scale(dude_left_1_image, (DUDE_WIDTH, DUDE_HEIGHT))
dude_left_2_image = pygame.image.load(
    os.path.join("assets", 'dude_left_2.png'))
dude_left_2 = pygame.transform.scale(dude_left_2_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_right_1_image = pygame.image.load(
    os.path.join("assets", 'dude_right_1.png'))
dude_right_1 = pygame.transform.scale(dude_right_1_image, (DUDE_WIDTH, DUDE_HEIGHT))
dude_right_2_image = pygame.image.load(
    os.path.join("assets", 'dude_right_2.png'))
dude_right_2 = pygame.transform.scale(dude_right_2_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_up_1_image = pygame.image.load(
    os.path.join("assets", 'dude_up_1.png'))
dude_up_1 = pygame.transform.scale(dude_up_1_image, (DUDE_WIDTH, DUDE_HEIGHT))
dude_up_2_image = pygame.image.load(
    os.path.join("assets", 'dude_up_2.png'))
dude_up_2 = pygame.transform.scale(dude_up_2_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_down_1_image = pygame.image.load(
    os.path.join("assets", 'dude_down_1.png'))
dude_down_1 = pygame.transform.scale(dude_down_1_image, (DUDE_WIDTH, DUDE_HEIGHT))
dude_down_2_image = pygame.image.load(
    os.path.join("assets", 'dude_down_2.png'))
dude_down_2 = pygame.transform.scale(dude_down_2_image, (DUDE_WIDTH, DUDE_HEIGHT))




dude_left_image = pygame.image.load(
    os.path.join('assets', 'dude_left.png'))
dude_left = pygame.transform.scale(dude_left_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_right_image = pygame.image.load(
    os.path.join('assets', 'dude_right.png'))
dude_right = pygame.transform.scale(dude_right_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_up_image = pygame.image.load(
    os.path.join('assets', 'dude_up.png'))
dude_up = pygame.transform.scale(dude_up_image, (DUDE_WIDTH, DUDE_HEIGHT))

dude_down_image = pygame.image.load(
    os.path.join('assets', 'dude_down.png'))
dude_down = pygame.transform.scale(dude_down_image, (DUDE_WIDTH, DUDE_HEIGHT))


def draw_window(dude_rect, dude_image):
    SCREEN.fill((WHITE))
    SCREEN.blit(dude_image, (dude_rect.x, dude_rect.y))
    pygame.display.update()

def swap_feet(current_foot):
    if current_foot == "lf":
        return "rf"
    else:
       return "lf"

def main():
    dude_foot = "lf"
    dude_rect = pygame.Rect(450, 250, DUDE_WIDTH, DUDE_HEIGHT)
    dude_image = dude_left
    clock = pygame.time.Clock()
    running = True
    dude_orient = "left"
    
    
    while running: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_pressed = pygame.key.get_pressed()

        is_stopped = (
            keys_pressed[pygame.K_w] == False and 
            keys_pressed[pygame.K_a] == False and 
            keys_pressed[pygame.K_s] == False and 
            keys_pressed[pygame.K_d] == False 
        )
        if is_stopped:
            if dude_orient == "left":
                dude_image = dude_left
            if dude_orient == "right":
                dude_image = dude_right
            if dude_orient == "down":
                dude_image = dude_down
            if dude_orient == "up":
                dude_image = dude_up

        if keys_pressed[pygame.K_a]: #left
            dude_foot = swap_feet(dude_foot)
            dude_rect.x -= VEL
            dude_orient = "left"
            
            if dude_foot == "lf":
                dude_image = dude_left_1
            else:
                dude_image = dude_left_2
        if keys_pressed[pygame.K_d]: #right
            dude_foot = swap_feet(dude_foot)
            dude_rect.x += VEL
            dude_orient = "right"
            
            if dude_foot == "lf":
                dude_image = dude_right_1
            else:
                dude_image = dude_right_2
        if keys_pressed[pygame.K_w]: #up
            dude_foot = swap_feet(dude_foot)
            dude_rect.y -= VEL
            dude_orient = "up"
            
            if dude_foot == "lf":
                dude_image = dude_up_1
            else:
                dude_image = dude_up_2
        if keys_pressed[pygame.K_s]: #down
            dude_foot = swap_feet(dude_foot)
            dude_rect.y += VEL
            dude_orient = "down"
            
            if dude_foot == "lf":
                dude_image = dude_down_1
            else:
                dude_image = dude_down_2
        # print(moving)
        

        if dude_rect.x < 0:
            dude_rect.x += VEL
        if dude_rect.x + DUDE_WIDTH > WIDTH:
            dude_rect.x -= VEL
        if dude_rect.y < 0:
            dude_rect.y += VEL
        if dude_rect.y + DUDE_HEIGHT > HEIGHT:
            dude_rect.y -= VEL

        SCREEN.fill((WHITE))
        
        draw_window(dude_rect, dude_image)
        
    pygame.quit

if __name__ == "__main__":
    main()