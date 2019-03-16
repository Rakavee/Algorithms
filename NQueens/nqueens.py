
# coding: utf-8

# Source: https://www.sanfoundry.com/python-program-solve-n-queen-problem-without-recursion/
# Source does not use linked lists.

# # Linked List implementation of Non-Recursive N-Queens Problem

# In[1]:


class Node: 
    def __init__(self, right=None, left=None, up=None, down=None, data=None): 
        self.right = right 
        self.left = left
        self.up = up 
        self.down = down
        self.data = data


# In[2]:


class nQueensBoard:
    def __init__(self, size):
        self.size = size
        self.queen_columns = [] #queen_columns[r]=c where r,c denotes the position of the queens on the board.
        self.nodes=[ [0]*self.size for _ in range(self.size) ]
        for i in range(self.size):
            for j in range(self.size):
                self.nodes[i][j] = Node(data=0)
                if i > 0:
                    self.nodes[i][j].up = self.nodes[i-1][j]
                    self.nodes[i-1][j].down = self.nodes[i][j]
                if j > 0:
                    self.nodes[i][j].left = self.nodes[i][j-1]
                    self.nodes[i][j-1].right = self.nodes[i][j]
 
    def isSafe(self, column):
        row = len(self.queen_columns)
 
        # check column
        for qc in self.queen_columns:
            if column == qc:
                return False
 
        # check diagonal
        for qr, qc in enumerate(self.queen_columns):
            if qc - qr == column - row:
                return False
 
        # check other diagonal
        for qr, qc in enumerate(self.queen_columns):
            if ((self.size - qc) - qr
                == (self.size - column) - row):
                return False
 
        return True
    
    def print_board(self):
        current_node = self.nodes[0][0]
        next_row = current_node.down
        while(current_node):
            print("| ",current_node.data, end = " ")
            if(current_node.right != None):
                current_node = current_node.right
            elif(current_node.down != None):
                current_node = next_row
                next_row = current_node.down
                print(' |\n')
            else:
                print(' |')
                break
        print("................................................................")
            
    def fill_board(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.queen_columns[row]:
                    self.nodes[row][column].data = "Q"
                    #print('|Q', end=' ')
                else:
                    self.nodes[row][column].data = "-"
                    #print('|-', end=' ')
            #print("|")
        #print("................................................................")
        self.print_board()
 
    
 
    def populate(self, size):
        number_of_solutions = 0

        row = 0
        column = 0
        # iterate over rows of board
        while True:
            while column < size:
                if self.isSafe(column):
                    self.queen_columns.append(column)
                    row += 1
                    column = 0
                    break
                else:
                    column += 1

            # if could not find column to place in or if board is full
            if (column == size or row == size):
                if row == size:
                    self.fill_board()
                    print()
                    number_of_solutions += 1

                    self.queen_columns.pop()
                    row -= 1

                #backtrack
                try:
                    prev_column = self.queen_columns.pop()
                except IndexError:
                    break
                row -= 1
                column = 1 + prev_column

        print('Number of solutions:', number_of_solutions)
 


# In[3]:


n = int(input('Enter n: '))
board1 = nQueensBoard(size = n)
board1.populate(n)

