#creating list 2d list 
matrix=[ [1,2,3],[4,5,6],[7,8,9]]
print(matrix)

#number of rows
rows=len(matrix)
print("rows:",rows)


#number of colums
colums=len(matrix[0])

print("colums:",colums)

#sow 2d in metrix form
print(matrix[2][2])

for i in range(0,rows):
    for j in range(0,colums):
        print(matrix[i][j],end=" ")
        
    print("\n")

matrix2=[[10,20,30],[40,50,60],[70,80,90]]

resultmetrix=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,rows):
    for j in range(0,colums):
     resultmetrix[i][j]=matrix[i][j]+matrix2[i][j]
    
for i in range(0,rows):
    for j in range(0,colums):
        print(resultmetrix[i][j],end=" ")
        
    print("\n")