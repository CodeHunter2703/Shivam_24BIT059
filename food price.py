l=[("apple","cherry","banana","watermelon"),(250,680,86,70)]
price=list(l[1])
fruits=[]
price.sort(reverse=True)
for i in price:
    for j in range(len((l[1]))):
        if i == l[1][j]:
            fruits.append(l[0][j])
            continue
for idx,j in enumerate(fruits):
    print(f"fruit : {j} | Price: {price[idx]}")