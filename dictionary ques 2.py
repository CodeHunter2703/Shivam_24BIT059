d1={1:["ICT",24,25600000],2:["MECH",25,2560000],3:["CS",26,256000],4:["CS",27,256000],5:["ICT",28,25600],6:["MECH",27,2560],7:["CHEM",28,2560]}
d2=[]
for k,v in d1.items():
    d2.append(v)
#max=d1[1][2]
# for i in d2:
#     max=i[2]
#     for i in d2:
#         if max<i[2]:
# #             print(f"the maximum salary for dept{i[0]} is {max} ")
# d3={}

# for i in d1:
#     if i[0] not in d3.keys():
#         d3[i[0]]=i[2]
#     else:
#         if i[2]>d3[i[0]]:
#             d3[i[0]]=i[2]
# print(d3)

# for k,v in d1.items():
#     for key, val in d1.items():
#         if key in d3.keys():
#             if val[2]>v[2]:
#                 d3[val[0]] = val[2]
#         else:
#             d3[v[0]]=v[2]
# print(d3)
d5={}
for i in d1.values():
    if i[0] not in d5.keys():
        d5[i[0]]=i[2]
    else:
        if i[2]>d5[i[0]]:
            d5[i[0]]=i[2]
print(d5)