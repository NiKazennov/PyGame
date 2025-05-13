import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
slow=5

rect = pygame.Rect(135, 220, 30, 30) 
vel = 5
jump = False
jumpCount = 0
jumpMax = 15
obj_x=130
obj_y=150
num_iter=0
img_list=[]
img_list2=[]
img_list3=[]
for i in range(6):
    img=pygame.image.load(f"Frog/Frog_0-{i+1}.png.png")
    img_list.append(img)
for i in range(6):
    img2=pygame.image.load(f"Platform/Platform_{i}.png")
    img_list2.append(img2)

run = True
while run:
    
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax

    keys = pygame.key.get_pressed()    
    rect.centerx = (rect.centerx + (keys[pygame.K_d] - keys[pygame.K_a]) * vel) % 300
    
    if jump:
        rect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False 

    window.fill((0, 0, 64))
    num_iter+=1
    num_frame=num_iter//slow%6
    pygame.draw.rect(window, (64, 64, 64), (0, 250, 300, 50))
    window.blit(img_list2[num_frame],[obj_x,obj_y])
    window.blit(img_list[num_frame],rect.center)
    pygame.display.flip()

pygame.quit()
exit() 
