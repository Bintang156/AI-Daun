X = [[9,6],
    [3,8]
    ]
 
Y = [[4,1],
    [5,2]
    ]
 
result = [[0,0],
    [0,0]
    ]
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)