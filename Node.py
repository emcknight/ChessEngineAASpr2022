#Base node class for chess engine
class Node(object):
    #Initialize tree node with name of the move and the score associated to the move
    def __init__(self, move, score):
        self.move = move
        self.score = score
        self.children = []

    #Add the next move as a child node
    def next_move(self, obj):
        self.children.append(obj)

    #Checks to see if the node has children
    def has_children(self):
        return len(self.children) > 0
