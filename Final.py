import csv


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




# test
if __name__ == '__main__':
    teamA = Team('Team A')
    teamA.read_from_file('Monte-Carlo-PLAYERS1.csv', 'Monte-Carlo-TEAM.csv')
    for i in teamA.Players:
        print(i)
    print(teamA.Name)
    print(teamA.Performance)
    print(teamA.Formation)
    print(teamA.coach)
    print(teamA.Home_court)
    print(teamA.variance)



