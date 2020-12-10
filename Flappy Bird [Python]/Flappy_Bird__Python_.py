import pygame, sys, random
def draw_floor():
    screen.blit(floor_surface,(floor_x_position,900))
    screen.blit(floor_surface,(floor_x_position+576,900))
pygame.init()


def create_pipe():
    random_pipe_pos= random.choice(pipe_height)
    bottom_pipe=pipe_surface.get_rect(midtop=(600,random_pipe_pos))
    top_pipe=pipe_surface.get_rect(midbottom=(600,random_pipe_pos-300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe,pipe)

def check_collisions(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
        if bird_rect.top <-100 or bird_rect.bottom >=900:
            return False
        
    return True
screen = pygame.display.set_mode((576,1024))#hight 1024, width 576
clock = pygame.time.Clock()
     

#Game Variables
gravity=0.25
bird_movement=0

bg_surface=pygame.image.load('assets/background-day.png').convert() #importing image and convert to better work with py file
bg_surface=pygame.transform.scale2x(bg_surface)
floor_surface=pygame.image.load('assets/base.png').convert() 
floor_surface=pygame.transform.scale2x(floor_surface)
floor_x_position=0

bird_surface= pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface= pygame.transform.scale2x(bird_surface)
bird_rect= bird_surface.get_rect(center= (100,512))

pipe_surface=pygame.image.load('assets/pipe-green.png').convert()
pipe_surface=pygame.transform.scale2x(pipe_surface)
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)


pipe_height= [400,800, 600]
game_active=True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement=0
                bird_movement-=12
            if event.key == pygame.K_SPACE and game_active== False:
                game_active=True
                pipe_list.clear()
                bird_rect.center = (100,512)
                bird_movement=0

        if event.type == SPAWNPIPE:
            print('pipe')
            pipe_list.extend(create_pipe())
            print(pipe_list)
                
    #BACKGROUND
    screen.blit(bg_surface,(0,0))
    if game_active:
    #BIRD
        screen.blit(bird_surface, bird_rect)
        bird_movement+=gravity
        bird_rect.centery+=bird_movement
        game_active =check_collisions(pipe_list)
        
        #PIPES

        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)

    #FLOOR
    floor_x_position-=1
    draw_floor()
    if floor_x_position<-576:
        floor_x_position=0
    pygame.display.update()
    clock.tick(120)