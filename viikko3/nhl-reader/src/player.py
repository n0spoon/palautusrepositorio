
class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.score = goals + assists
    
    def __str__(self):
        return f'{self.name:25} {self.team:4} {self.goals:2} + {self.assists:2} = {self.score:2}'
