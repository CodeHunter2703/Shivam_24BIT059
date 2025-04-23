# with open("love1.txt",'w') as f:
#     f.write("""Love is a big thing.\nA heart likes a hug.\nA hug is warm.\nThe hug is good.\nAn eye looks at a smile.\nThe smile is shiny.\nA laugh makes a day fun.\nA love is everywhere.\nA star in the sky is a love.\nAn apple is a love.\nA sun is a love.\nThe sun is happy.\nA happy is love.\nA mommy is love.\nA daddy is love.\nThe puppy is love.\nA love is big.\nAn love is small.\nThe love is all.\nLove is love.\nThe love! A love! An love!\n""")
#     f.close()
with open("love1.txt") as f:
    data=f.read()
    l=data.split()
    print(l)
idx=0
while idx < len(l):
    if l[idx].lower() in ['a',"an","the"]:
        l[idx]=""
        continue
    idx+=1
essay=" ".join(l)
with open("love1.txt",'a') as f:
    f.write(essay)
