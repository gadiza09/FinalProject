import pygame

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(None, 34)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


#Color and Position of buttons
categoryButtonColor = (162, 232, 180)
rightSide = 125
rightMid = 450
leftMid = 775
top = 80
topMid = 212
mid = 344
bottomMid = 476
bottom = 608
buttonWidth = 200
buttonHeight = 92

#All the buttons
playButton = Button((105, 220, 255), 450, 310, 200, 80, "PLAY")
animalButton = Button(categoryButtonColor, rightSide, top, buttonWidth, buttonHeight, "Animals")
foodButton = Button(categoryButtonColor, rightSide, topMid, buttonWidth, buttonHeight, "Food")
vehiclesButton = Button(categoryButtonColor, rightSide, mid, buttonWidth, buttonHeight, "Vehicles")
colorsButton = Button(categoryButtonColor, rightSide, bottomMid, buttonWidth, buttonHeight, "Colors")
footwearButton = Button(categoryButtonColor, rightMid, top, buttonWidth, buttonHeight, "Footwear")
singersButton = Button(categoryButtonColor, rightMid, topMid, buttonWidth, buttonHeight, "Singers")
designerBrandsButton = Button(categoryButtonColor, rightMid, mid, buttonWidth, buttonHeight, "Designer Brands")
streetwearButton = Button(categoryButtonColor, rightMid, bottomMid, buttonWidth, buttonHeight, "Streetwear")
indonesianCitiesButton = Button(categoryButtonColor, leftMid, top, buttonWidth, buttonHeight, "Indonesian Cities")
capitalCitiesButton = Button(categoryButtonColor, leftMid, topMid, buttonWidth, buttonHeight, "Capital Cities")
socialMediaButton = Button(categoryButtonColor, leftMid, mid, buttonWidth, buttonHeight, "Social Media")
tvShowsButton = Button(categoryButtonColor, leftMid, bottomMid, buttonWidth, buttonHeight, "TV Shows")
randomButton = Button(categoryButtonColor, rightMid, bottom, buttonWidth, buttonHeight, "Random")
playAgainButton = Button((105, 220, 255), 450, 600, 200, 80, "PLAY AGAIN")



"""Buttons class was taken from Tech with Tim, on youtube
the link to the code is: https://www.youtube.com/watch?v=4_9twnEduFA"""