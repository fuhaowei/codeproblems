#use BST
#either own implementation
#or (sorted list -> python implementation of it)
#sorted list guarantees me logn search, insert, delete
#why logn?

from sortedcontainers import SortedList

class Leaderboard:

    def __init__(self):
        self.leaderboard = SortedList()
        self.scores = {}


    def addScore(self, playerId: int, score: int) -> None:

        #if this player was originally in the dict alr
        if playerId in self.scores:
            #remove his score from leaderboard
            if (self.scores[playerId], playerId) in self.leaderboard:
                self.leaderboard.remove((self.scores[playerId], playerId))

        else:
            self.scores[playerId] = 0

        #if score wasnt originally in/ or even after
        #update new score
        #add to score
        self.scores[playerId] += score
        self.leaderboard.add((self.scores[playerId], playerId))


    def top(self, K: int) -> int:
        total = 0
        for idx in range(len(self.leaderboard)-K, len(self.leaderboard)):
            total += self.leaderboard[idx][0]
        return total
        

    def reset(self, playerId: int) -> None:
        #remove form leaderboard
        self.leaderboard.remove((self.scores[playerId], playerId))
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)