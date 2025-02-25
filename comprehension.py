x,y,z,n=1,1,2,3
lst=[ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  ]
print("the number of possible pairs:",lst,sep='\n')
nlst = [a for a in lst if sum(a)<=n ]
print("the number of possible pairs but sum less than n :",nlst,sep='\n')