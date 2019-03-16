
# coding: utf-8

# Sources: https://www.sanfoundry.com/python-program-solve-n-queen-problem-without-recursion/
# <br>
# https://github.com/dimitri4d/Eight-Queens-unique-solutions <br>
# Sources do not use linked lists.

# # Linked List implementation of Non-Recursive N-Queens Problem with unique solutions

# In[4]:


#Node class for linked list implementation.
class Node: 
    def __init__(self, right=None, left=None, up=None, down=None, data=None): 
        self.right = right 
        self.left = left
        self.up = up 
        self.down = down
        self.data = data


# In[5]:


#main nQueensBoard class with the required attributes and methods.

class nQueensBoard:
    def __init__(self, size):
        self.size = size #size of the board.
        self.queen_columns = [] #queen_columns[r]=c where r,c denotes the position of the queens on the board.
        self.solutions = [] #list to store all the possible solutions.
        self.nodes=[ [0]*self.size for _ in range(self.size) ] #initialize nodes of the board.
        
        #create the linked list structure using Node class and give links to the nodes.
        for i in range(self.size):
            for j in range(self.size):
                self.nodes[i][j] = Node(data=0)
                if i > 0:
                    self.nodes[i][j].up = self.nodes[i-1][j]
                    self.nodes[i-1][j].down = self.nodes[i][j]
                if j > 0:
                    self.nodes[i][j].left = self.nodes[i][j-1]
                    self.nodes[i][j-1].right = self.nodes[i][j]
    
    #check if the particular cell is safe for placing the queen.
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
    
    #function to check if the position is safe and place queens. If a position does not lead to a solution, then backtrack.
    #Finally call the get_unique method to get the unique solutions and fill and print solutions on the board.
    def populate(self, size):
        
        number_of_solutions = 0
        sol1 = []
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
                   # print("1")
                    #print(self.solutions)
                    l=self.queen_columns
                    self.solutions.append(list(l))
                    #print("2")
                    #print(self.solutions)
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
            
        
        print('Number of all_solutions:', number_of_solutions)
        self.get_unique()
        
        
    def print_board(self,solution):
        current_node = self.nodes[0][0]
        next_row = current_node.down
        print("+----+----+----+----+----+----+----+-----+")
        while(current_node):
            print("| ",current_node.data, end = " ")
            if(current_node.right != None):
                current_node = current_node.right
            elif(current_node.down != None):
                current_node = next_row
                next_row = current_node.down
                print(' |')
                print("+----+----+----+----+----+----+----+-----+")
            else:
                print(' |')
                print("+----+----+----+----+----+----+----+-----+")
                break
        print("\n")

    def fill_board(self,solution):
        for row in range(self.size):
            for column in range(self.size):
                if column == solution[row]:
                    self.nodes[row][column].data = "Q"
                else:
                    self.nodes[row][column].data = "-"

        self.print_board(solution)
        
    #obtain the similar positions of Queens through rotation.    
    def dup_rotate(self,temp1):
        n = len(temp1)
        tp = [0] * n
        for i in range(n):
            tp[temp1[i]] = n - i - 1
        return tp
    #obtain the similar positions of Queens through reflection. 
    def dup_reflect(self,temp2):
        n = len(temp2)
        rp = [0] * n
        for i in range(n):
            rp[temp2[i]] = i
        return rp
    
    #remove rotated and reflected positions from the solutions list.
    def get_unique(self):
        sol=self.solutions[:]
        unique =[]
        #print(self.solutions)
        while len(sol) != 0:
            temp1 = sol[0]
            unique.append(temp1)
            #perform symmetry operations and remove duplicates
            for i in (temp1,
                      self.dup_rotate(temp1),
                      self.dup_rotate(self.dup_rotate(temp1)),
                      self.dup_rotate(self.dup_rotate(self.dup_rotate(temp1))),
                      self.dup_reflect(temp1),
                      self.dup_rotate(self.dup_reflect(temp1)),
                      self.dup_rotate(self.dup_rotate(self.dup_reflect(temp1))),
                      self.dup_rotate(self.dup_rotate(self.dup_rotate(self.dup_reflect(temp1))))):
                try:
                    sol.remove(i)
                except:
                    pass
        
        print("Number of unique solutions:",len(unique))
        
        #Fill the board with unique solutions and print them
        j=1
        for i in unique:
            print("Unique Solution",j,":",i)
            self.fill_board(i)
            j = j+1

    



# In[6]:


n = int(input('Enter n: '))
board1 = nQueensBoard(size = n)
board1.populate(n)

