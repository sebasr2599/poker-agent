import time
import pytesseract
from agent import Agent
from cardReader import  Capture
import imutils

def main():
    flag = 0
    agent = Agent()
    # tree = Tree()
    # suits = Suits()
    capture = Capture()

    agent.init_game()
    agent.play()


    time.sleep(8)

    img1 = capture.click(618,512,25,25)
    img2 = capture.click(705,495,20,25)
    img3 = capture.click(628,532,20,20)
    img4 = capture.click(746,513,35,30)

    card1Letter = capture.prelude(img1) 
    card2Letter = capture.prelude(img2)
    card1suit = capture.prelude(img3)
    card2suit = capture.prelude(img4)

    # Debugging
    # im = cv2.imread('./Img/rot6.png')
    # im = capture.prelude(im)

    # cv2.imshow("pp",im)
    # cv2.waitKey(5000)

    card1LetterRot = imutils.rotate(card1Letter,-25)
    card2LetterRot = imutils.rotate(card2Letter,22)

    custom_config = "--psm 10"
    L1 = pytesseract.image_to_string(card1Letter,lang='eng',config=custom_config)
    L2 = pytesseract.image_to_string(card2Letter,lang='eng',config=custom_config)
    print(f'card 1 number: {L1} and card 2: {L2}')

    while flag<1000:
        # check if the menu is active 
        text = agent.get_menu() 
        state = agent.get_state()
        deal = agent.get_deal()
        if text == "Call":
            print("here")
            agent.make_decision()
        if text == "Check":
            aux = agent.getHand1()
            agent.make_decision()
            print(aux)
        if state in ["You Win!","Big Win!","Huge Win!"]:
            agent.continue_playing()
        if deal == "Deal Again":
            agent.continue_playing()
        print(flag, sep=" ")
        time.sleep(1)
        flag +=1

    print("Beeep boop game over")
    time.sleep(2)
    agent.closeWindow()
if __name__ == "__main__":
    main()

# keep reading until you get your cards, get the cards suits and ranks and then the center hand
