import pandas as pd
import random
import csv

def grouping(n, group, allteam, allgame):
	for i in range(n):
		for j in range(i+1, n, 1):
			# n team
			for k in range(23):
				if(allteam[k].name == group[i]):
					inA = int(k)
					break
				
			#n team
			for k in range(23):
				if(allteam[k].name == group[j]):
					inB = int(k)
					break
				
			allgame.append(Game(allteam[inA], allteam[inB], allteam[inA].time+allteam[inB].time))
	return allgame

class Team:
	def __init__(self, name, time):
		self.name = name
		self.time = time
		self.playthisweek = 0

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
	sheet = pd.read_excel("複賽未打.xlsx", header=None)
	ngame = len(sheet)
	
	allgame = []

	for i in range(ngame):
		time = []

		if sheet[0][i][2] == ' ':
			f = 8
			while f < len(sheet[0][i]):
				time.append(sheet[0][i][f]+sheet[0][i][f+1]);
				f += 6
			
			timecant = ['10','11','12','13','22','23','32','33','42','43','52','53']
			for k in range(len(time)):
				if time[k] in timecant:
					timecant.remove(time[k])
	
#print(timecant)
			allgame.append(Game(sheet[0][i][0:2], sheet[0][i][3:5], timecant))
		
		#chuanyuanbai lan
		elif sheet[0][i][3] == ' ':
			f = 9
			while f < len(sheet[0][i]):
				time.append(sheet[0][i][f]+sheet[0][i][f+1]);
				f += 6
			
			timecant = ['10','11','12','13','22','23','32','33','42','43','52','53']
			for k in range(len(time)):
				if time[k] in timecant:
					timecant.remove(time[k])
	
			allgame.append(Game(sheet[0][i][0:3], sheet[0][i][3:6], timecant))
			

				
	#print(len(allgame))
	#for i in range(len(allgame)):
	#		 print(allgame[i].teamA, allgame[i].teamB, allgame[i].timecannot)
	random.shuffle(allgame)

	alltime = ['10','11','12','13','22','23','32','33','42','43','52','53']
	realtime = ['星期一 10:00~11:00','星期一 11:00~12:00','星期一 12:00~13:00','星期一 13:00~14:00',
				'星期二 12:00~13:00','星期二 13:00~14:00',
				'星期三 12:00~13:00','星期三 13:00~14:00',
				'星期四 12:00~13:00','星期四 13:00~14:00',
				'星期五 12:00~13:00','星期五 13:00~14:00']
	
	# set how many weeks
	for i in range(15):
		teamthisweek = []
		teamtwice = []
		for j in range(len(realtime)):
			found = False
			for k in range(len(allgame)):
				
				if allgame[k].endgame == False and allgame[k].teamA not in teamthisweek and allgame[k].teamB not in teamthisweek and allgame[k].teamA not in teamtwice and allgame[k].teamB not in teamtwice:
					for l in range(len(allgame[k].timecannot)):
						if allgame[k].timecannot[l] == alltime[j]:
							break
						
						if l==len(allgame[k].timecannot)-1 and allgame[k].timecannot[l]!=alltime[j]:
							allgame[k].insert_playtime(alltime[j])
							allgame[k].end()
							teamthisweek.append(allgame[k].teamA)
							teamthisweek.append(allgame[k].teamB)
							found = True

							print(allgame[k].teamA, allgame[k].teamB, allgame[k].playtime, realtime[alltime.index(allgame[k].playtime)])

				elif allgame[k].endgame == False and allgame[k].teamA in teamthisweek and allgame[k].teamB not in teamthisweek and j >= 6 and allgame[k].teamA not in teamtwice and allgame[k].teamB not in teamtwice:

					for l in range(len(allgame[k].timecannot)):
						if j%2 == 0:
							for m in range(j-2, j, 1):
								if teamthisweek[m] == allgame[k].teamA:
									break
						elif j%2 == 1:
							for m in range(j-3, j, 1):
								if teamthisweek[m] == allgame[k].teamA:
									break

						if allgame[k].timecannot[l] == alltime[j]:
							break
						
						if l==len(allgame[k].timecannot)-1 and allgame[k].timecannot[l]!=alltime[j]:
							allgame[k].insert_playtime(alltime[j])
							allgame[k].end()
							teamthisweek.append(allgame[k].teamA)
							teamthisweek.append(allgame[k].teamB)
							teamtwice.append(allgame[k].teamA)
							found = True

							print(allgame[k].teamA, allgame[k].teamB, allgame[k].playtime, realtime[alltime.index(allgame[k].playtime)])
				
				elif allgame[k].endgame == False and allgame[k].teamA not in teamthisweek and allgame[k].teamB in teamthisweek and j >= 6 and allgame[k].teamA not in teamtwice and allgame[k].teamB not in teamtwice:


					for l in range(len(allgame[k].timecannot)):
						if j%2 == 0:
							for m in range(j-2, j, 1):
								if teamthisweek[m] == allgame[k].teamA:
									break
						elif j%2 == 1:
							for m in range(j-3, j, 1):
								if teamthisweek[m] == allgame[k].teamA:
									break

						if allgame[k].timecannot[l] == alltime[j]:
							break
						
						if l==len(allgame[k].timecannot)-1 and allgame[k].timecannot[l]!=alltime[j]:
							allgame[k].insert_playtime(alltime[j])
							allgame[k].end()
							teamthisweek.append(allgame[k].teamA)
							teamthisweek.append(allgame[k].teamB)
							teamtwice.append(allgame[k].teamB)
							found = True

							print(allgame[k].teamA, allgame[k].teamB, allgame[k].playtime, realtime[alltime.index(allgame[k].playtime)])

				if found == True:
					break
			
		#print(teamthisweek)
		print('')
