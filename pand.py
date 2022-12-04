"""
The Board class must include:

A constructor that takes two arguments: the number of cities n, and the number of the epicenter.
An attribute, size that contains the number of cities.
A method, move, that takes a single argument, the number of a city to inspect. This method must execute both parts of the time step (inspection followed by disease spread) then return the caseload discovered in the inspection step.
Your class must replicate the following behavior exactly. (Extra print statements are included for clarity, but these will not be graded)

"""

class Board:
    def __init__(self, size, key, bmap = [], turn=0):
        self.size = size
        self.bmap = bmap
        self.turn = 1
        self.key = key
        for i in range(size):
            bmap.append(0)
        bmap[key] = 1
        print("Creating board: ",bmap)        

    def move(self, peek):
        self.turn += 1
        bmap = self.bmap
        new_map = [] 
        
        i = 0
        for num in bmap:
            if i >= max(self.key - self.turn+1,0) and min(i < self.key + self.turn,len(bmap)):
                new_map.append(num+1)
            else:
                new_map.append(num)
            i+=1
        # print("Old board:", bmap)
        print("Checking location {}, Value = {}".format(peek, bmap[peek]))
        self.bmap = new_map
        print("New board:", new_map)
        return bmap[peek]
    

"""Solver Class
The Solver class represents a player that strategically plays the game to identify the epicenter. It must include:

A constructor that includes one argument: a Board instance to be solved.
A method, solve, that takes no arguments.  This method must interact with the Board instance only by checking the size attribute and calling the move method. No other interaction is allowed. The solve method should do this until the location of the epicenter has been deduced, and then return the location.
For example, the commands below show that the solve method has correctly identified the epicenter as location 3.

"""

class Solver:
    def __init__(self, board):
        self.board = board
    def solve(self):
        
        guess = 1
        found, close = False, False
    
        while not found and not close:
            # Basic strategy: Sample the center, then two parts equal (thirds), then three parts equal (fourths), until either the number or a non-zero number appears.  
            denominator = guess + 1
            for i in range(1,denominator):
                guess_loc = round(self.board.size * i/denominator)

                result = self.board.move(guess_loc)

                if result == guess:
                    found = True
                    break
                elif result != 0 :
                    close = True
                    break
                guess +=1 
        if close:
            # If the number revealed is not 0 but also not the pinnacle number, then there are 2 directions we can go - positive or negative. And the distance from the pinnacle corresponds directly with the number of guesses.    
            positions_to_move = guess - result
            result = self.board.move(guess_loc + positions_to_move)

            if result == guess:
                found = True
                
            else:
                guess_loc = guess_loc - positions_to_move
            guess +=1 

        print("Only took us {} guesses".format(guess))
        return guess_loc



## FOR SAMPLING, PLEASE UNCOMMENT:
# board = Board(10,2)
# solver = Solver(board)
# print(solver.solve())