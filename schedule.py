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
    sheet = pd.read_excel("time111.xlsx")
    
    # print(sheet)
    
    TA = ['資科','地政','外交','中文','日文','歐語','國貿','財管']
    TB = ['民族','歷史','會計','斯語','傳院藍','英文','資管','社會']
    TC = ['法律','企管','政治','應數','經濟','心理','創國','金融']
    TD = ['統計','財政','公行','傳院白','阿語','土文','風管','哲學']
    

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
        
        allteam.append(Team(sheet['負責人系級'][j], timein))

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
            
        print(teamthisweek)
        print('')