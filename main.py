import pygame

import words

import buttons

import random

from settings import Settings

pygame.init()

hm_settings = Settings()

win = pygame.display.set_mode((hm_settings.screen_width, hm_settings.screen_height))
win.fill(hm_settings.bg_color)


def main():

    def checkPlay():
        def redrawWindow():
            win.fill((hm_settings.bg_color))
            picture = pygame.image.load("images/background.bmp")
            win.blit(picture, (0, 0))
            playButton.draw(win, (0, 0, 0))
            myFont = pygame.font.SysFont(None, 60)
            textSurface = myFont.render("HANGMAN", False, (94, 152, 255))
            win.blit(textSurface, (437, 250))

        playButton = buttons.playButton

        run = True
        while run:
            redrawWindow()
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.isOver((pos)):
                        catWindow()


    def catWindow():
        def redrawWindow():
            win.fill((hm_settings.bg_color))
            picture = pygame.image.load("images/background.bmp")
            win.blit(picture, (0, 0))
            myFont = pygame.font.SysFont(None, 60)
            textSurface = myFont.render("CHOOSE A CATEGORY", False, (255, 217, 101))
            win.blit(textSurface, (320, 20))

            animalButton.draw(win, (0, 0, 0))
            foodButton.draw(win, (0, 0, 0))
            vehiclesButton.draw(win, (0, 0, 0))
            colorsButton.draw(win, (0, 0, 0))
            footwearButton.draw(win, (0, 0, 0))
            singersButton.draw(win, (0, 0, 0))
            designerBrandsButton.draw(win, (0, 0, 0))
            streetwearButton.draw(win, (0, 0, 0))
            indonesianCitiesButton.draw(win, (0, 0, 0))
            capitalCitiesButton.draw(win, (0, 0, 0))
            socialMediaButton.draw(win, (0, 0, 0))
            tvShowsButton.draw(win, (0, 0, 0))
            randomButton.draw(win, (0, 0, 0))


        animalButton = buttons.animalButton
        foodButton = buttons.foodButton
        vehiclesButton = buttons.vehiclesButton
        colorsButton = buttons.colorsButton
        footwearButton = buttons.footwearButton
        singersButton = buttons.singersButton
        designerBrandsButton = buttons.designerBrandsButton
        streetwearButton = buttons.streetwearButton
        indonesianCitiesButton = buttons.indonesianCitiesButton
        capitalCitiesButton = buttons.capitalCitiesButton
        socialMediaButton = buttons.socialMediaButton
        tvShowsButton = buttons.tvShowsButton
        randomButton = buttons.randomButton


        run = True
        while run:
            redrawWindow()
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if animalButton.isOver((pos)):
                        playGame(words.cat_animals)

                    if foodButton.isOver((pos)):
                        playGame(words.cat_food)

                    if vehiclesButton.isOver((pos)):
                        playGame(words.cat_vehicles)

                    if colorsButton.isOver((pos)):
                        playGame(words.cat_colors)

                    if footwearButton.isOver((pos)):
                        playGame(words.cat_footwear)

                    if singersButton.isOver((pos)):
                        playGame(words.cat_singers)

                    if designerBrandsButton.isOver((pos)):
                        playGame(words.cat_designerBrands)

                    if streetwearButton.isOver((pos)):
                        playGame(words.cat_streetwear)

                    if indonesianCitiesButton.isOver((pos)):
                        playGame(words.cat_indonesianCities)

                    if capitalCitiesButton.isOver((pos)):
                        playGame(words.cat_capitalCities)

                    if socialMediaButton.isOver((pos)):
                        playGame(words.cat_socialMedia)

                    if tvShowsButton.isOver((pos)):
                        playGame(words.cat_tvShows)

                    if randomButton.isOver((pos)):
                        playGame(words.cat_random)


    class HangmanPlay:
        def __init__(self):
            self.chosenTheWord = None
            self.triedLetters = []
            self.chosenWordList = {}
            self.revealedWord = {}
            self.displayedWord = ""
            self.tries = 8


        def displayWord(self):
            self.chosenWordList = {str(k): "_ " for k in self.chosenTheWord}
            self.revealedWord = {str(k): "HIDE" for k in self.chosenWordList}

        def checkDisplayWord(self):
            theWord = [letter for letter in self.chosenTheWord]
            display_word = ""
            for char in theWord:
                if self.revealedWord[char] is "HIDE":
                    display_word += "_ "
                else:
                    display_word += str(char)
            self.displayedWord = display_word

        def checkLetter(self, letter):
            if letter not in self.triedLetters:
                if letter in self.chosenWordList:
                    self.revealedWord[letter] = "FOUND"
                    self.triedLetters.append(letter)
                else:
                    self.tries -= 1
                    self.triedLetters.append(letter)


    hangman = HangmanPlay()


    def playGame(chosenCat):
        wordList = chosenCat
        chosenWord = random.choice(wordList)
        hangman.chosenTheWord = chosenWord

        hangman.displayWord()
        hangman.checkDisplayWord()

        if words.cat_random == words.cat_animals:
            randomName = "ANIMALS"
        if words.cat_random == words.cat_food:
            randomName = "FOOD"
        if words.cat_random == words.cat_vehicles:
            randomName = "VEHICLES"
        if words.cat_random == words.cat_colors:
            randomName = "COLORS"
        if words.cat_random == words.cat_footwear:
            randomName = "FOOTWEAR"
        if words.cat_random == words.cat_singers:
            randomName = "SINGERS"
        if words.cat_random == words.cat_designerBrands:
            randomName = "DESIGNER BRANDS"
        if words.cat_random == words.cat_streetwear:
            randomName = "STREETWEAR"
        if words.cat_random == words.cat_indonesianCities:
            randomName = "INDONESIAN CITIES"
        if words.cat_random == words.cat_capitalCities:
            randomName = "CAPITAL CITIES"
        if words.cat_random == words.cat_socialMedia:
            randomName = "SOCIAL MEDIA"
        if words.cat_random == words.cat_tvShows:
            randomName = "TV SHOWS"


        def redrawWindow():
            win.fill((hm_settings.bg_color))
            picture = pygame.image.load("images/background.bmp")
            win.blit(picture, (0, 0))
            start = pygame.image.load("images/start.png")
            try1 = pygame.image.load("images/try1.png")
            try2 = pygame.image.load("images/try2.png")
            try3 = pygame.image.load("images/try3.png")
            try4 = pygame.image.load("images/try4.png")
            try5 = pygame.image.load("images/try5.png")
            try6 = pygame.image.load("images/try6.png")
            try7 = pygame.image.load("images/try7.png")
            if hangman.tries == 8:
                win.blit(start, (430, 210))
            if hangman.tries == 7:
                win.blit(start, (430, 210))
            if hangman.tries == 6:
                win.blit(try1, (430, 210))
            if hangman.tries == 5:
                win.blit(try2, (430, 210))
            if hangman.tries == 4:
                win.blit(try3, (430, 210))
            if hangman.tries == 3:
                win.blit(try4, (430, 210))
            if hangman.tries == 2:
                win.blit(try5, (430, 210))
            if hangman.tries == 1:
                win.blit(try6, (430, 210))
            if hangman.tries == 0:
                win.blit(try7, (430, 210))

            if chosenCat == words.cat_animals:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: ANIMALS", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_food:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: FOOD", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_vehicles:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: VEHICLES", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_colors:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: COLORS", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_footwear:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: FOOTWEAR", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_singers:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: SINGERS", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_designerBrands:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: DESIGNER BRANDS", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_streetwear:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: STREETWEAR", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_indonesianCities:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: INDONESIAN CITIES", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_capitalCities:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: CAPITAL CITIES", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_socialMedia:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: SOCIAL MEDIA", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_tvShows:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: TV SHOWS", False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))

            if chosenCat == words.cat_random:
                myFont = pygame.font.SysFont(None, 60)
                catText = myFont.render("The category is: " + randomName, False, (255, 217, 101))
                wordDisplay = myFont.render(hangman.displayedWord, False, (0, 0, 255))
                win.blit(catText, (50, 50))
                win.blit(wordDisplay, (50, 120))
                if hangman.displayedWord == chosenWord:
                    winGame = myFont.render("You got the word right!", False, (0, 0, 255))
                    win.blit(winGame, (50, 190))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))
                if hangman.tries == 0:
                    myFont = pygame.font.SysFont(None, 60)
                    loseGame = myFont.render("You did not guess the word!", False, (0, 0, 255))
                    loseMessage = myFont.render("The word was: " + chosenWord, False, (0, 0, 255))
                    win.blit(loseGame, (50, 190))
                    win.blit(loseMessage, (50, 260))
                    playAgainButton = buttons.playAgainButton
                    playAgainButton.draw(win, (0, 0, 0))


        run = True

        while run:
            redrawWindow()
            hangman.checkDisplayWord()
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                playAgainButton = buttons.playAgainButton

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    hangman.checkLetter(letter=None)
                    if event.key is pygame.K_a:
                        hangman.checkLetter("a")
                    elif event.key is pygame.K_b:
                        hangman.checkLetter("b")
                    elif event.key is pygame.K_c:
                        hangman.checkLetter("c")
                    elif event.key is pygame.K_d:
                        hangman.checkLetter("d")
                    elif event.key is pygame.K_e:
                        hangman.checkLetter("e")
                    elif event.key is pygame.K_f:
                        hangman.checkLetter("f")
                    elif event.key is pygame.K_g:
                        hangman.checkLetter("g")
                    elif event.key is pygame.K_h:
                        hangman.checkLetter("h")
                    elif event.key is pygame.K_i:
                        hangman.checkLetter("i")
                    elif event.key is pygame.K_j:
                        hangman.checkLetter("j")
                    elif event.key is pygame.K_k:
                        hangman.checkLetter("k")
                    elif event.key is pygame.K_l:
                        hangman.checkLetter("l")
                    elif event.key is pygame.K_m:
                        hangman.checkLetter("m")
                    elif event.key is pygame.K_n:
                        hangman.checkLetter("n")
                    elif event.key is pygame.K_o:
                        hangman.checkLetter("o")
                    elif event.key is pygame.K_p:
                        hangman.checkLetter("p")
                    elif event.key is pygame.K_q:
                        hangman.checkLetter("q")
                    elif event.key is pygame.K_r:
                        hangman.checkLetter("r")
                    elif event.key is pygame.K_s:
                        hangman.checkLetter("s")
                    elif event.key is pygame.K_t:
                        hangman.checkLetter("t")
                    elif event.key is pygame.K_u:
                        hangman.checkLetter("u")
                    elif event.key is pygame.K_v:
                        hangman.checkLetter("v")
                    elif event.key is pygame.K_w:
                        hangman.checkLetter("w")
                    elif event.key is pygame.K_x:
                        hangman.checkLetter("x")
                    elif event.key is pygame.K_y:
                        hangman.checkLetter("y")
                    elif event.key is pygame.K_z:
                        hangman.checkLetter("z")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playAgainButton.isOver((pos)):
                        reset()
                        catWindow()



    def reset():
        hangman.chosenTheWord = None
        hangman.triedLetters = []
        hangman.chosenWordList = {}
        hangman.revealedWord = {}
        hangman.displayedWord = ""
        hangman.tries = 8


    checkPlay()
    catWindow()
    playGame(chosenCat=None)

main()

"""A lot of the code used and the implementation of it was based from a hangman game by BoxTurtle488 on GitHub
The images used for this game was also taken from BoxTurtle488's hangman game
the link to the repository is: https://github.com/BoxTurtle488/graphical_hangman_pygame"""