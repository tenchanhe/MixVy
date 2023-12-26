# n team *2
# allgame row107

import pandas as pd
import random
import csv

def grouping(n, group, allteam, allgame):
    for i in range(n):
        for j in range(i+1, n, 1):
            # n team
            for k in range(32):
                if(allteam[k].name == group[i]):
                    inA = int(k)
                    break
                
            #n team
            for k in range(32):
                if(allteam[k].name == group[j]):
                    inB = int(k)
                    break
                
            allgame.append(Game(allteam[inA], allteam[inB], allteam[inA].time+allteam[inB].time))
    return allgame

class Team:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.playthisweek = False

class Game:
    def __init__(self, ta, tb, tc):
        self.teamA = ta
        self.teamB = tb
        self.timecannot = tc
        self.endgame = False
        self.playtime = 0

    def insert_playtime(self, time):
        self.playtime = time

    def end(self):
        self.endgame = True

if __name__ == "__main__":
    sheet = pd.read_excel("./112-1米克斯混排比賽報名表單-回覆.xlsx")
    
    # print(sheet)
    
    TA = ['資管','財政','英文','哲學','風管','歷史','東南','歐語']
    TB = ['日文','傳院藍','土文','政治','心理','經濟','教育','國貿']
    TC = ['民族','地政','社會','財管','斯語','傳院白','應數','法律']
    TD = ['資科','統計','阿語','金融','會計','外交','企管','中文']
    

    allteam = []
    #n team
    for j in range(32):
        line = sheet['無法出賽時間（最多三個時段）'][j].split(', ')
        timein = []
        #n time cannot
        for i in range(3):
            if line[i][2] == '一':
                if line[i][5] == '0':
                    timein.append('10')
                elif line[i][5] == '1':
                    timein.append('11')
                elif line[i][5] == '2':
                    timein.append('12')
                elif line[i][5] == '3': 
                    timein.append('13')

            elif line[i][2] == '二':
                if line[i][5] == '2':
                    timein.append('22')
                elif line[i][5] == '3':
                    timein.append('23')
            
            elif line[i][2] == '三':
                if line[i][5] == '2':
                    timein.append('32')
                elif line[i][5] == '3':
                    timein.append('33')
            
            elif line[i][2] == '四':
                if line[i][5] == '2':
                    timein.append('42')
                elif line[i][5] == '3':
                    timein.append('43')
            
            elif line[i][2] == '五':
                if line[i][5] == '2':
                    timein.append('52')
                elif line[i][5] == '3':
                    timein.append('53')
            
            else:
                print('Error')
        
        allteam.append(Team(sheet['代表系隊'][j], timein))

    # for i in range(32):
    #     print(allteam[i].name, allteam[i].time)

    allgame = []
    allgame = grouping(8, TA, allteam, allgame)
    allgame = grouping(8, TB, allteam, allgame)
    allgame = grouping(8, TC, allteam, allgame)
    allgame = grouping(8, TD, allteam, allgame)
                
    print(len(allgame))
    # for i in range(len(allgame)):
    #     print(allgame[i].teamA.name, allgame[i].teamB.name, allgame[i].playtime)
    random.shuffle(allgame)

    for i in range(len(allgame)):
        timecan = ['10','11','12','13','22','23','32','33','42','43','52','53']
        for k in range(len(allgame[i].timecannot)):
            if allgame[i].timecannot[k] in timecan:
                timecan.remove(allgame[i].timecannot[k])
        print(allgame[i].teamA.name, allgame[i].teamB.name, timecan)
        
        # print(allgame[i].teamA.name, allgame[i].teamB.name, allgame[i].timecannot)

    print('')
    alltime = ['10','11','12','13','22','23','32','33','42','43','52','53']
    realtime = ['星期一 10:00~11:00','星期一 11:00~12:00','星期一 12:00~13:00','星期一 13:00~14:00',
                '星期二 12:00~13:00','星期二 13:00~14:00',
                '星期三 12:00~13:00','星期三 13:00~14:00',
                '星期四 12:00~13:00','星期四 13:00~14:00',
                '星期五 12:00~13:00','星期五 13:00~14:00']
    
    # set how many weeks
    for i in range(15):
        teamthisweek = []
        for j in range(len(realtime)):
            #print(j)
            found = False
            for k in range(len(allgame)):
                if allgame[k].endgame == False and allgame[k].teamA.name not in teamthisweek and allgame[k].teamB.name not in teamthisweek:
                    for l in range(len(allgame[k].timecannot)):
                        if allgame[k].timecannot[l] == alltime[j]:
                            break
                        
                        if l==len(allgame[k].timecannot)-1 and allgame[k].timecannot[l]!=alltime[j]:
                            allgame[k].insert_playtime(alltime[j])
                            allgame[k].end()
                            teamthisweek.append(allgame[k].teamA.name)
                            teamthisweek.append(allgame[k].teamB.name)
                            found = True

                            print(allgame[k].teamA.name, allgame[k].teamB.name, allgame[k].playtime, realtime[alltime.index(allgame[k].playtime)])

                if found == True:
                    break
            
        #print(teamthisweek)
        print('')
