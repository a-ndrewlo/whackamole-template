import pygame

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(32,32)))
            z=1
            while z!=20:
                x=32*z
                pygame.draw.line(screen, color="black",start_pos=(x,0),end_pos=(x,512))
                z+=1
            y=1
            while y != 16:
                x=32*y
                pygame.draw.line(screen, color="black",start_pos=(0,x),end_pos=(640,x))
                y+=1
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
