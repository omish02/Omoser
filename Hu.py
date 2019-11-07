import numpy as np
array=np.array([[80,40,50,46],[40,70,20,25],[30,10,20,30],[35,20,25,30]])
redArr=array.copy()
num=0
for i in range(0,4) :
    minimum=redArr[i][0]
    for j in range(0,4) :
        if minimum>redArr[i][j] :
            minimum=redArr[i][j]
    for j in range(0,4) :
        redArr[i][j]=redArr[i][j]-minimum
for i in range(0,4) :
    minimum=redArr[0][i]
    for j in range(0,4) :
        if minimum>redArr[j][i] :
            minimum=redArr[j][i]
    for j in range(0,4) :
        redArr[j][i]=redArr[j][i]-minimum
print(redArr)     
while num!=4 :
    colDel=[0,0,0,0]
    rowDel=[0,0,0,0]
    flagrow=[0,0,0,0]
    flagcol=[0,0,0,0]
    cost=0
    num=0    
    for i in range(0,4) :
        for j in range(0,4) :
            if redArr[i][j]==0 :
                flagrow[i]+=1
    print(flagrow)
    for i in range(0,4) :
        if flagrow[i]==1 :
            for j in range(0,4) :
                if redArr[i][j]==0 and colDel[j]==0 :
                    cost=cost+array[i][j]
                    num+=1
                    colDel[j]=1
                    for k in range(0,4) :
                        if redArr[k][j]==0 :
                            flagrow[k]-=1
    for i in range(0,4) :
        for j in range(0,4) :
            if redArr[j][i]==0 and colDel[i]==0 :
                flagcol[i]+=1
    for i in range(0,4) :
        if flagcol[i]==1 :
            for j in range(0,4) :
                if redArr[j][i]==0 and rowDel[j]==0 :
                    cost=cost+array[j][i]
                    num+=1
                    rowDel[j]=1
                    for k in range(0,4) :
                        if redArr[j][k]==0 :
                            flagcol[k]-=1
    print(redArr)
    print(num)
    if num==4 :
        break
    minimum=9999
    for i in range(0,4) :
        for j in range(0,4) :
            if rowDel[i]==0 and colDel[j]==0 and minimum>redArr[i][j] :
                minimum=redArr[i][j]
    for i in range(0,4) :
        for j in range(0,4) :
            if rowDel[i]==0 and colDel[j]==0 :
                redArr[i][j]-=minimum
            elif rowDel[i]==1 and colDel[j]==1 :
                redArr[i][j]+=minimum
print(f"The Array : \n{array}")
print(f"The total Cost of optimization is=\n{cost}")
