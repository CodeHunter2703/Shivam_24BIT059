count_num=0
count_alpha=0
def counter(test):
    count_num = 0
    count_alpha = 0
    for i in test:
        if i.isdigit() :
            count_num+=1
        elif i.isalpha():
            count_alpha+=1
    return count_alpha,count_num
test="24BIT059"
tuple1=counter(test)
print(f"the string {test} contains {tuple1[1] } numbers and {tuple1[0]} alphabets")

