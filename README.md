# Title: 
Predict Result of a Soccer Game via Monte Carlo Simulation


## Team Member(s):
Amy, Sukey, Wei Chieh

# Monte Carlo Simulation Scenario & Purpose:
Scenario:
We simulate the soccer game of two teams: teamA and teamB. There are several factors that could influence the final result: line-up players list, team formation, team performance player performance and team ranking.
-> line-up player list: Each team has more than 11 team members and we choose the line-up players among the candidate according to several variables: fouls and health condition. And players have their positions respectively. And before we choose the players, we should decide what formation the coach applied.
-> team performance: this attribute bases on the history data but the performance is unstable. We have standard deviation for each team. And the distribution of the performance of each team is also different.
-> player performance: player performance consits of two factors: performance in the past seasons and current performance in this season. We add different weight on different factors and some of the players don't have current performance.
-> team ranking: this attribute bases on the history data.

Purpose:
We want to find out which team has the larger probability to win. And by analyzing the stragtegy package they use, we generalize the pattern of winning team.

## Simulation's variables of uncertainty

1. formation: Each team has some preferred formation strategies.  We assume the probability of applying each formation depends on the weights. For example, 55% of time, team A applies formation of 4:4:2 which means there are four defenders, four midfielders and two forwards.
2. Team performance: this attribute bases on the history data but the performance is unstable. We have standard deviation for each team. And the distribution of the performance of each team is also different (normal distribution for normal team and triangle distribution for bad team).

## Hypothesis or hypotheses before running the simulation:
We write all the player data and team data by ourselves. And there is no other factors that can affect the game result.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)



## Instructions on how to use the program:
There are four files: 
Monte-Carlo-PLAYERS1.csv : contains all the data of players of teamA.
Monte-Carlo-PLAYERS2.csv : contains all the data of players of teamA.
Monte-Carlo-TEAM.csv : contains team information of the two teams.
Final.py : the program

## All Sources Used:
None
