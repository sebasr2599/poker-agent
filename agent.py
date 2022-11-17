import time
import pyautogui
import pytesseract
from selenium import webdriver
from cardReader import Capture, Suits
from random import seed
from random import randint

class Agent:
    def init_game(self):
        print("Initializing agent")
        url = 'https://www.247freepoker.com/'
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1400,800)
        self.driver.set_window_position(0,0)
        self.driver.get(url)
        self.capture = Capture() 
        self.suit = Suits()
        print("Page loaded")
        print("Starting game")

    def play(self):
        pyautogui.click(600,600)
        time.sleep(1)
        pyautogui.click(710,505)
        time.sleep(3)
        pyautogui.moveTo(100,100)

    def continue_playing(self):
        pyautogui.click(600,600)
        time.sleep(3)

    def newGame(self):
        pyautogui.click(340,280)
        time.sleep(1)
        pyautogui.click(600,600)
        time.sleep(1)
        pyautogui.click(600,600)

    def fold(self):
        pyautogui.click(550,750)
        pyautogui.moveTo(100,100)
        print("folding")
        time.sleep(3)

    def check(self):
        pyautogui.click(750,750)
        pyautogui.moveTo(100,100)
        print("checking")
        time.sleep(3)
    def call(self):
        pyautogui.click(750,750)
        pyautogui.moveTo(100,100)
        print("calling")
        time.sleep(3)
    def raise_money(self):
        print("betting more money")
        value = randint(351,1000)
        pyautogui.click(870,750)
        pyautogui.moveTo(380,750)
        time.sleep(1)
        pyautogui.mouseDown(button='left')
        pyautogui.dragTo(value,750, button='left',duration=1)
        # pyautogui.moveTo(value,750)
        time.sleep(1)
        pyautogui.click(1060,750)
        pyautogui.moveTo(100,100)
        time.sleep(3)

    def closeWindow(self):
        self.driver.close()

    def rankToInt(self,str):
        ranks = {
                'A':1,
                '1':2,
                '2':3,
                '3':4,
                '4':5,
                '5':6,
                '6':7,
                '7':8,
                '8':9,
                '9':10,
                'J':11,
                'Q':12,
                'K':13,
                }
        if str in ranks:
            return ranks.get(str)
        else:
            return 0
    def getHand1(self):
        # get the two images
        img1 = self.capture.click(488,260,18,18)
        img2 = self.capture.click(528,355,30,30)
        
        # preprocess
        rank = self.capture.prelude(img1)
        suit = self.capture.prelude(img2,80,80)
        
        rankStr = self.capture.imageToString(rank)
        suitStr = self.suit.card_suit(suit)

        print(f'The rank of the card is: {rankStr} and the suit is: {suitStr}')
        return [self.rankToInt(rankStr), suitStr]

    def make_decision(self):
        value = randint(0,1000)
        print(f'rand number {value}')
        if(value <100):
            self.fold()
        elif(value>=100 and value <=800):
            self.check()
        else:
            self.raise_money()
    def get_menu(self):
        imMenu = self.capture.click(640,730,120,40)
        menu = self.capture.prelude(imMenu,120,40)
        text = pytesseract.image_to_string(menu)

        return text.strip()

    def get_deal(self):
        stateImg = self.capture.click(580,230,240,50)
        state = self.capture.prelude(stateImg,240,50)
        stateText = pytesseract.image_to_string(state)

        return stateText.strip()
    def get_state(self):
        stateImg = self.capture.click(550,200,320,60)
        state = self.capture.prelude(stateImg,120,60)
        stateText = pytesseract.image_to_string(state)

        return stateText.strip()








