
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        for value in self.reader.get_players():
            if value.nationality == nationality:
                players_by_nationality.append(value)
        players_by_nationality.sort(key=lambda x:(x.goals), reverse=True)
        players_by_nationality.sort(key=lambda x:(x.score), reverse=True)

        return players_by_nationality