import sys
# coding: utf-8

# In[2]:


class MagicSquare:
    #object initialization with n*n nodes with value 0 and 4 links up,down,right,left.
    def  __init__(self,n=None):
        self.n=n
        self.nodes=[ [0]*self.n for _ in range(self.n) ]
        for i in range(self.n):
            for j in range(self.n):
                self.nodes[i][j] = Node(data=0)
                if i > 0:
                    self.nodes[i][j].up = self.nodes[i-1][j]
                    self.nodes[i-1][j].down = self.nodes[i][j]
                if j > 0:
                    self.nodes[i][j].left = self.nodes[i][j-1]
                    self.nodes[i][j-1].right = self.nodes[i][j]
        
    #populate the data structure with values following the rules of magic square.        
    def populate(self):
	    #find the middle of first row
        mid = int(self.n/2)
		#place 1 in the middle of first row
        self.nodes[0][mid].data = 1
		#current_node is a pointer to the current node we are going to fill.
		#update current_node to the node where 1 is.
        current_node = self.nodes[0][mid]
		#value we are going to store at each node. Incremented at each step.
        k=1
		#calculate total number of values to fill : size of square.
        N=self.n*self.n
		#loop to repeat the steps until the square is completely filled.
        for loop in range(N-1):
            k=k+1
			#conndition to check if we are going out the square at top right corner.
            if(current_node.up == None and current_node.right == None):
			    #If a move takes you out of the square at the upper right-hand corner, place k + 1 immediately below k.
                while(current_node):
                    if(current_node.down.data == 0 and current_node.down != None):
                        current_node.down.data = k
                        current_node = current_node.down
                        break
                    current_node = current_node.down
                
            elif current_node.up == None:
				#If a move takes you above the top row in the jth column, move to the bottom of the jth column and place k + 1 there.
                current_node = current_node.right
                while(current_node.down):
                    current_node = current_node.down
                current_node.data = k

            elif current_node.up.right == None:
			    #If the move takes you outside to the right of the square in the ith row, place k + 1 in the ith row on the left side.
                current_node = current_node.up
                while(current_node.left):
                    current_node = current_node.left
                current_node.data = k

            elif current_node.up.right.data == 0:
			    #after integer k has been placed, move up one row and one column to the right to place the next integer k + 1.
                current_node.up.right.data = k
                current_node = current_node.up.right

            else:
			    #If a move takes you to an already filled cell, place k + 1 immediately below k.
                while(current_node):
                    if(current_node.down.data == 0 and current_node.down != None):
                        current_node.down.data = k
                        current_node = current_node.down
                        break
                    current_node = current_node.down

#class node to initialize each cell as a data structure with data as 0 and 4 links.					
class Node: 
    def __init__(self, right=None, left=None, up=None, down=None, data=None): 
        self.right = right 
        self.left = left
        self.up = up 
        self.down = down
        self.data = data

    
            
        
    
        


# In[5]:

number = int(input("Enter an odd number to generate magic square: "))

#no = 5
new_square = MagicSquare(n=number)
new_square.populate()


# In[6]:


current_node = new_square.nodes[0][0]
next_row = current_node.down
while(current_node):
        print(" | ",current_node.data, end =" ")
        if(current_node.right != None):
            current_node = current_node.right
        elif(current_node.down != None):
            current_node = next_row
            next_row = current_node.down
            print(" |\n")
        else:
            print(" |")
            break
		
