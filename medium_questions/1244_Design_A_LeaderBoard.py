class Leaderboard:

    def __init__(self):
        self.scores = []
        self.player_ind = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player_ind:
            self.scores[self.player_ind[playerId]] += score
        else:
            self.player_ind[playerId] = len(self.scores)
            self.scores.append(score)

    def top(self, K: int) -> int:
        return sum(sorted(self.scores)[len(self.scores)-K:])

    def reset(self, playerId: int) -> None:
        index = self.player_ind[playerId]
        self.scores[index] = 0
        
"""
scores = [73, 56]
player_id = {1:0, 2:1}




"""
