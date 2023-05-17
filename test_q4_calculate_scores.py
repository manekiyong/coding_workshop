from bisect import bisect_left
import sys
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    score = math.floor(n*multiplier + 0.5) / multiplier
    return score


class Teams:
    def __init__(self, name):
        self.name = name
        self.challenges = {}
        self.first_accepted=False
        self.final_score = 0.0

    def attempt(self, challenge, score, lang, status):
        if challenge not in self.challenges:
            self.challenges[challenge] = Challenge()
        self.challenges[challenge].evaluate(score, lang, status)
    
    def finalize(self):
        for challenge in self.challenges:
            self.final_score+=self.challenges[challenge].get_score()
            

class Challenge:
    def __init__(self):
        self.solved_languages = set()
        self.solved = False
        self.penalty = 0.0
        self.score = 0.0
        self.bonus = 0.0
        self.final = 0.0
        
    def evaluate(self, score, lang, status):
        self.score = max(self.score, score)
        if status=='Accepted':
            if not self.solved:
                self.bonus+=(score+1)
                self.solved=True
            else:
                if lang not in self.solved_languages:
                    self.bonus+=1.0
            self.solved_languages.add(lang)
        else:
            self.penalty+=1.0

    def get_score(self):
        self.final = self.score+self.bonus-self.penalty
        return self.final

teams = {}
ranks = {}
rank_pos = 15000

for i, lines in enumerate(sys.stdin):
    lines = lines.strip()
    team, score, challenge, lang, status = lines.split(",")
    score = float(score)
    if team not in teams:
        teams[team] = Teams(team)
        ranks[team] = 0
    teams[team].attempt(challenge, score, lang, status)
    if status == 'Accepted' and ranks[team]==0:
        ranks[team]=rank_pos
        rank_pos-=1

team_score = []
team_rank = []
for team in teams:
    teams[team].finalize()
    score = teams[team].final_score
    score = round_half_up(score, 2)
    idx = bisect_left(team_score, (score, ranks[team]))
    team_score.insert(idx, (score, ranks[team]))
    team_rank.insert(idx, team)

for index, (team, score) in enumerate(zip(reversed(team_rank), reversed(team_score)), start=1):
    print('{0},{1},{2:.2f}'.format(index,team,score[0]))
