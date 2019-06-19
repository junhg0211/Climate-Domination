import pygame


class Root:
    class Display:
        size = [1280, 720]

    running = True

    window = pygame.display.set_mode(Display.size)


class Keyboard:
    lalt = False
    ralt = False


class Cursor:
    position = pygame.mouse.get_pos()

    previous_pressed = pressed = pygame.mouse.get_pressed()
    start_pressing = list(pressed)
    end_pressing = list(pressed)


class Color:
    background = (222, 222, 222)


class RootObject:
    objects = []

    @staticmethod
    def add(_obj):
        RootObject.objects.append(_obj)

    def tick(self):
        pass

    def render(self):
        pass


pygame.display.set_caption('Climate Domination')

while Root.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Root.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                Keyboard.lalt = True
            elif event.key == pygame.K_RALT:
                Keyboard.ralt = True
            elif event.key == pygame.K_F4:
                if Keyboard.lalt or Keyboard.ralt:
                    Root.running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT:
                Keyboard.lalt = False
            elif event.key == pygame.K_RALT:
                Keyboard.ralt = False

    Root.window.fill(Color.background)

    pygame.display.flip()
pygame.quit()
