main_set=["Anthony","Andrew"
,"Almanzo"""
,"Bailey"
,"Brooke"
,"Blake"
,"Bella"
,"Brooklyn"
,"Brynn"
,"Baani"
,"Baasim"
,"Babita,","Amos"
,"Achilles"
,"Augustus"
,"Alexander"
,"Aaron"
,"Atlas"
,"Ambrose"]
Aset=set([])
Bset=set([])
main_set=set(main_set)
for i in main_set:
    if "A" in i :
        Aset.add(i)
    elif "B" in i:
        Bset.add(i)
print(f"the names with A {Aset}\nthe names with B {Bset}")