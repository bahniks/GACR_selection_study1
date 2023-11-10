import os

studies = ["Login",
           "Cheating 1",
           "Cheating 2",
           "BDM Control Questions",
           "BDM",
           "Cheating 3",
           "Auction Control Questions",
           "Auction",
           "Auction Result",
           "Cheating 4",
           "Auction",
           "Auction Result",
           "Cheating 5",
           "Auction",
           "Auction Result",
           "Cheating 6",
           "BDM",
           "Cheating 7",
           "Debriefing1",
           "Debriefing2",
           "Debriefing3",
           "Debriefing4",
           "Lottery",
           "Dice Lottery",
           "Hexaco",
           "Attention checks",
           "Prosociality",
           "Demographics",
           "Ending"
           ]


columns = {"Login": ("id", "BDM1", "BDM2", "condition"),
           "Charity": ("id", "charity"),
           "Cheating 1": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Cheating 2": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"),
           "BDM Control Questions": ("id", "question", "answer"),
           "BDM": ("id", "block", "bid"),
           "Cheating 3": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Auction Control Questions": ("id", "question", "answer"),
           "Auction": ("id", "block", "bid", "prediction"),
           "Auction Result": ("id", "block", "version", "maxoffer", "secondoffer", "myoffer"),
           "Cheating 4": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Cheating 5": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Cheating 6": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Cheating 7": ("id", "block", "trial", "version", "condition", "roll", "prediction", "report", "reward", "charity", "time", "time1", "time2"), 
           "Debriefing1": ("id", "bdm_process", "auction_process"),
           "Debriefing2": ("id", "bdm_reward", "bdm_charity_loss", "bdm_charity_loss_others", "bdm_others_bids", "bdm_others_prediction", "bdm_fun", "bdm_ease", "bdm_reward_influence", "bdm_charity_loss_influence", "bdm_winner", "bdm_overcome_others", "auction_reward", "auction_charity_loss", "auction_charity_loss_others", "auction_others_bids", "auction_others_prediction", "auction_fun", "auction_ease", "auction_reward_influence", "auction_charity_loss_influence", "auction_winner", "auction_overcome_others"),
           "Debriefing3": ("id", "bdm_unfair", "bdm_risky", "bdm_not_understood", "bdm_complicated", "auction_unfair", "auction_risky", "auction_not_understood", "auction_complicated"),
           "Debriefing4": ("id", "others_charity_interest", "you_charity_interest", "aware_cheating", "aware_preventing_cheating", "aware_preventing_loss"),           
           "Lottery": ("id", "choice1", "choice2", "choice3", "choice4", "choice5", "chosen", "win"),
           "Dice Lottery": ("id", "rolls", "reward"),
           "Hexaco": ("id", "number", "answer", "item"),           
           "Attention checks": ("id", "part", "failed"),
           "Prosociality": ("id", "item", "answer"),
           "Demographics": ("id", "sex", "age", "language", "student", "field"),
           "Ending": ("id", "reward", "chosen_block"),

           "Perception cheating": ("id", "before_attention", "before_thinking", "before_cheating", "before_fun",
                                   "before_justification", "before_random", "after_attention", "after_thinking",
                                   "after_cheating",  "after_fun", "after_justification", "after_random"),
           "Debriefing": ("id", "comments", "aim_dice", "aim_correct", "demand", "immoral", "truth") 
           }

frames = ["Initial",
          "Login",
          "Intro",          
          "Charity",
          "CheatingInstructions",
          "Cheating",
          "Instructions2",
          "Cheating",
          "BDM",
          "BDMResult",
          "Cheating",
          "Auction",
          "Wait",
          "AuctionResult",
          "Cheating",
          "AuctionWait",
          "Auction",
          "Wait",
          "AuctionResult",
          "Cheating",
          "AuctionWait",
          "Auction",
          "Wait",
          "AuctionResult",
          "Cheating",
          "AuctionWait",
          "BDM",
          "BDMResult",
          "Cheating",
          "EndCheating",    
          "DebriefingInstructions",      
          "DebriefCheating1",
          "DebriefCheating2",
          "DebriefCheating3",
          "DebriefCheating4",
          "Lottery",
          "LotteryWin",
          "LotteryInstructions",
          "DiceLottery",
          "QuestInstructions",
          "Hexaco",
          "Prosociality",
          "Demographics",
          "Ending",
          "Exit"
         ]

for study in studies:
    with open("{} results.txt".format(study), mode = "w") as f:
        f.write("\t".join(columns[study]))

with open("Time results.txt", mode = "w") as times:
    times.write("\t".join(["id", "order", "frame", "time"]))


files = os.listdir()
for file in files:
    if ".py" in file or "results" in file or "file.txt" in file or "STATION" in file or ".txt" not in file:
        continue

    with open(file) as datafile:
        #filecount += 1 #
        count = 1
        for line in datafile:

            study = line.strip()
            if line.startswith("time: "):
                with open("Time results.txt", mode = "a") as times:
                    times.write("\n" + "\t".join([file, str(count), frames[count-1], line.split()[1]]))
                    count += 1
                    continue
            if study in studies:
                with open("{} results.txt".format(study), mode = "a") as results:
                    for line in datafile:
                        content = line.strip()
                        if not content:
                            break
                        else:
                            results.write("\n" + content)
                        
                

    
        
