#! python3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "Stuff"))


from gui import GUI

from quest import Hexaco, QuestInstructions
from intros import Initial, Intro, Ending
from demo import Demographics
from cheating import CheatingInstructions, Cheating, Instructions2, BDM, BDMResult, Auction, Wait
from cheating import AuctionResult, EndCheating, Login, AuctionWait
from debriefing import DebriefingInstructions, DebriefCheating1, DebriefCheating2, DebriefCheating3, DebriefCheating4
from lottery import Lottery, LotteryWin
from dicelottery import LotteryInstructions, DiceLottery
from charity import Charity
from questionnaire import Prosociality


frames = [Initial,
          Login,
          Intro,          
          Charity,
          CheatingInstructions,
          Cheating,
          Instructions2,
          Cheating,
          BDM,
          BDMResult,
          Cheating,
          Auction,
          Wait,
          AuctionResult,
          Cheating,
          AuctionWait,
          Auction,
          Wait,
          AuctionResult,
          Cheating,
          AuctionWait,
          Auction,
          Wait,
          AuctionResult,
          Cheating,
          AuctionWait,
          BDM,
          BDMResult,
          Cheating,
          EndCheating,    
          DebriefingInstructions,      
          DebriefCheating1,
          DebriefCheating2,
          DebriefCheating3,
          DebriefCheating4,
          Lottery,
          LotteryWin,
          LotteryInstructions,
          DiceLottery,
        #   AnchoringInstructions, 
        #   Anchoring,
          QuestInstructions,
          Hexaco,
          Prosociality,
          Demographics,
          Ending
         ]

if __name__ == "__main__":
    GUI(frames, load = os.path.exists("temp.json"))