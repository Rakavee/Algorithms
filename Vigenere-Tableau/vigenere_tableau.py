
# coding: utf-8

# In[14]:



vlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# In[15]:


#Initialize the two-dimensional array starting at Tableau(0,0) and ending at Tableau(25,25) by rows.
#This is also the original tableau.

original_table = [ [0]*26 for _ in range(26) ]
for l in range(len(vlist)):
    original_table[l] = vlist[l:]+vlist[:l]


print('----ORIGINAL VIGENERE TABLEAU----')
print('No. of rows:',len(original_table))
print('No. of columns:',len(original_table[0]))
    


# In[16]:


print('----Initialize the two-dimensional array starting at Tableau(0,0) and ending at Tableau(25,25) by rows.----\n')
for i in range(len(original_table)):
    for j in range(len(original_table[0])):
        print('|',original_table[i][j],end=' ')
    print('|\n')


# In[17]:


#Initialize the two-dimensional array starting at Tableau(0,0) and ending at Tableau(25,25) by columns.
table2 = [ [0]*26 for _ in range(26) ]
for l in range(len(vlist)):
    k = vlist[l:]+vlist[:l]
    for m in range(len(table2)):
        table2[m][l]=k[m]


# In[18]:


print('----Initialize the two-dimensional array starting at Tableau(0,0) and ending at Tableau(25,25) by columns.----\n')
for i in range(len(table2)):
    for j in range(len(table2[0])):
        print('|',table2[i][j],end=' ')
    print('|\n')


# In[19]:


#Initialize the two-dimensional array starting at Tableau(0,25) and ending at Tableau(25,0) by rows.

table3 = [ [0]*26 for _ in range(26) ]
for l in range(len(vlist)):
    k = vlist[l:]+vlist[:l]
    table3[l] = k[::-1]


print('----Initialize the two-dimensional array starting at Tableau(0,25) and ending at Tableau(25,0) by rows.----\n')
for i in range(len(table3)):
    for j in range(len(table3[0])):
        print('|',table3[i][j],end=' ')
    print('|\n')


# In[20]:


#Initialize the two-dimensional array starting at Tableau(0,25) and ending at Tableau(25,0) by columns.
table2 = [ [0]*26 for _ in range(26) ]
for l in range(len(vlist)):
    k = vlist[l:]+vlist[:l]
    k = k[::-1]
    for m in range(len(table2)):
        table2[m][l]=k[m]


print('----Initialize the two-dimensional array starting at Tableau(0,25) and ending at Tableau(25,0) by columns.----\n')
for i in range(len(table2)):
    for j in range(len(table2[0])):
        print('|',table2[i][j],end=' ')
    print('|\n')


# In[21]:


#Initialize the two-dimensional array starting at Tableau(25,0) and ending at Tableau(0,25) by rows.

table3 = [ [0]*26 for _ in range(26) ]
for l in range(len(vlist)):
    table3[l] = vlist[-(l+1):]+vlist[:-(l+1)]


print('----Initialize the two-dimensional array starting at Tableau(25,0) and ending at Tableau(0,25) by rows.----\n')
for i in range(len(table3)):
    for j in range(len(table3[0])):
        print('|',table3[i][j],end=' ')
    print('|\n')


# In[22]:


#Initialize the two-dimensional array starting at Tableau(25,0) and ending at Tableau(0,25) by columns.
table4 = [ [0]*26 for _ in range(26) ]
j=0
while(j < 26):
    i=25
    k=0
    while(i >= 0):
        table4[j][k]=original_table[i][j]
        i = i-1
        k = k+1
    j = j+1
print('----Initialize the two-dimensional array starting at Tableau(25,0) and ending at Tableau(0,25) by columns.----\n')
for i in range(len(table4)):
    for j in range(len(table4[0])):
        print('|',table4[i][j],end=' ')
    print('|\n')


# In[23]:


#Initialize the two-dimensional array starting at Tableau(25,25) and ending at Tableau(0,0) by rows.
table5 = [ [0]*26 for _ in range(26) ]
i=25
m=0
while(i >= 0):
    j=25
    k=0
    while(j >= 0):
        table5[m][k]=original_table[i][j]
        j = j-1
        k = k+1
    i = i-1
    m = m+1

print('----Initialize the two-dimensional array starting at Tableau(25,25) and ending at Tableau(0,0) by rows.----\n')
for i in range(len(table5)):
    for j in range(len(table5[0])):
        print('|',table5[i][j],end=' ')
    print('|\n')


# In[24]:


#Initialize the two-dimensional array starting at Tableau(25,25) and ending at Tableau(0,0) by columns.
table6 = [ [0]*26 for _ in range(26) ]
i=25
m=0
while(i >= 0):
    j=25
    k=0
    while(j >= 0):
        table5[m][k]=original_table[j][i]
        j = j-1
        k = k+1
    i = i-1
    m = m+1

print('----Initialize the two-dimensional array starting at Tableau(25,25) and ending at Tableau(0,0) by columns.----\n')
for i in range(len(table5)):
    for j in range(len(table5[0])):
        print('|',table5[i][j],end=' ')
    print('|\n')


# In[25]:


original_table


# In[32]:


sd_table = []
for i in range(len(original_table)):
    for j in range(len(original_table)):
        sd_table.append(original_table[i][j])


# In[35]:


print("------Single Dimensional Output------")
sd_table


# In[37]:


for i in range(26*26):
    print(sd_table[i],end=" ")

