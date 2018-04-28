import csv
from numpy.random import choice
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

class Team:
    Name = ''
    Players = []
    coach = {}
    Formation = {}
    Performance = 0.0
    variance = 0.0
    Home_court = False

    def __init__(self, name):
        self.Name = name
        self.Players = []
        self.coach = {}
        self.Formation = {}
        self.Performance = 0.0
        self.variance = 0.0
        self.Home_court = False

    # Read information from csv files
    def read_from_file(self, players_info, team_info):
        # Read players information
        with open(players_info, newline='') as player:
            player_reader = csv.reader(player)
            for row in player_reader:
                if row[0] == 'PLAYERS':
                    continue
                foul = False
                health = False
                if row[4] == '1':
                    foul = True
                if row[5] == '1':
                    health = True
                f = lambda x: float(x) if x != 'NA' else 'NA'
                self.Players.append({'Name': row[0], 'POSITION': row[1], 'PERFORMANCE(This Season)': f(row[2]),
                                    'PERFORMANCE(Past)': f(row[3]), 'FOULS': foul, 'HEALTH': health})
        # Read team information
        with open(team_info, newline='') as team:
            team_reader = csv.reader(team)
            for row in team_reader:
                if row[0] == self.Name:
                    if row[3] == '1':
                        self.Home_court = True
                    self.Name = row[0]
                    formation = row[1].split(',')
                    tendency = row[2].split(',')
                    for i in range(len(formation)):
                        i0 = formation[i][0]
                        i1 = formation[i][1]
                        i2 = formation[i][2]
                        self.Formation[(int(i0), int(i1), int(i2))] = int(tendency[i])
                    self.coach = row[4]
                    self.variance = row[5]
                    self.Performance = row[6]


team_a = Team('Team A')
team_a.read_from_file('Monte-Carlo-PLAYERS1.csv', 'Monte-Carlo-TEAM.csv')
team_a_formation = team_a.Formation
team_a_players = team_a.Players

team_b = Team('Team B')
team_b.read_from_file('Monte-Carlo-PLAYERS2.csv', 'Monte-Carlo-TEAM.csv')
team_b_formation = team_b.Formation
team_b_players = team_b.Players



def normalize_Numbers(number_list):
    normalized_result = []
    sum = 0
    for i in number_list:
        sum += i
    for i in number_list:
        normalized_result.append(i/sum)
    return normalized_result


def choose_line_ups(formation,players):

    count = 0
    count_ = 0
    score = 0
    score_ = 0

    # draw a formation
    formation_list = []
    for i in formation:
        forma = ""
        for s in i:
          forma += str(s)
        formation_list.append(forma)
    formation_weight = normalize_Numbers(list(formation.values()))
    draw_formation = choice(formation_list, 1, p=formation_weight)
    draw_formation = tuple(map(tuple, draw_formation))[0]
    formation_outcome = []
    for e in draw_formation:
        formation_outcome.append(int(e))

    # take the fouls and health condition into consideration
    defenders = []
    midfields = []
    forwards = []
    goalkeeper = []
    defenders_weights = []
    midfields_weights = []
    forwards_weights = []
    goalkeeper_weights = []
    for player in players:
        weight = 1
        if player['FOULS'] == True:
            weight = weight * 0.7
        if player['HEALTH'] == True:
            weigth = weight * 0.6
        if player['POSITION'] == 'Goalkeeper':
            goalkeeper.append(player.get('Name'))
            goalkeeper_weights.append(weight)
        elif player['POSITION'] == 'Defender':
            defenders.append(player.get('Name'))
            defenders_weights.append(weight)
        elif player['POSITION'] == 'Midfielder':
            midfields.append(player.get('Name'))
            midfields_weights.append(weight)
        elif player['POSITION'] == 'Forward':
            forwards.append(player.get('Name'))
            forwards_weights.append(weight)

    goalkeeper_weights = normalize_Numbers(goalkeeper_weights)
    defenders_weights = normalize_Numbers(defenders_weights)
    midfields_weights = normalize_Numbers(midfields_weights)
    forwards_weights = normalize_Numbers(forwards_weights)

    goalkeeper_lineup = list(choice(goalkeeper,1,replace= False, p = goalkeeper_weights))
    defenders_lineup = list(choice(defenders,formation_outcome[0],replace= False, p = defenders_weights))
    midfields_lineup = list(choice(midfields,formation_outcome[1],replace= False,p = midfields_weights))
    forwards_lineup = list(choice(forwards,formation_outcome[2],replace= False,p = forwards_weights))

    # extract the player performance after randomly choose
    final_lineup = goalkeeper_lineup + defenders_lineup + midfields_lineup + forwards_lineup
    performance_current = []
    performance_past = []

    for player in players:
        for i in final_lineup:
            if player['Name'] == i :
                performance_current.append(player.get('PERFORMANCE(This Season)'))
                performance_past.append(player.get('PERFORMANCE(Past)'))

    #Calculate the player score
    for i in performance_current:
        if i != 'NA':
            count += 1
            score += int(i)
    for i in performance_past:
        if i != 'NA':
            count_ += 1
            score_ += int(i)

    avg_score = (float(score/count) + float(score_/count_))/2

    return goalkeeper_lineup, defenders_lineup, midfields_lineup, forwards_lineup, avg_score




#Calculate the result using Monte_Carlo

win_count = 0
lose_count = 0
point_A = []
point_B = []
mean_A = 0
mean_B = 0
std_A = 0
std_B = 0
echo = 100

for i in range(echo):

    pointA = float(choose_line_ups(team_a_formation,team_a_players)[4])
    pointB = float(choose_line_ups(team_b_formation,team_b_players)[4])
    point_A.append(pointA)
    point_B.append(pointB)

    if pointA > pointB:
        win_count += 1
    else:
        lose_count += 1

mean_A = float(np.mean(np.asarray(point_A)))
mean_B = float(np.mean(np.asarray(point_B)))
std_A = float(np.std(np.asarray(point_A)))
std_B = float(np.std(np.asarray(point_B)))

print("WIN rate(A)", win_count/100)

#print the graph (A)

A = np.linspace(mean_A - 3*std_A, mean_A + 3*std_A, 100)
plt.plot(A,mlab.normpdf(A, mean_A, std_A))

plt.show()

# B = np.linspace(mean_B - 3*std_B, mean_B + 3*std_B, 100)
# plt.plot(B,mlab.normpdf(B, mean_B, std_B))
#
# plt.show()






