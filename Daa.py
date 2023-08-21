def TSP(i, s):
    if not s:
        return c[i][1],[i]
    else:
        ways=[]
        for j in s:
            new_s=s[: :]
            new_s.remove(j)
            dis,p=TSP(j,new_s)
            ways.append([dis+c[i][j],p])
        min_path=min(ways,key=lambda x:x[0])
        path=[i]+min_path[1]
        return min_path[0],path


c = [[0,0,0,0,0],
     [0,0,10,15,20],
     [0,5,0,9,10],
     [0,6,13,0,12],
     [0,8,8,9,0]]

dis,path=TSP(1,[2,3,4])
path.append(1)
print(dis,path)
