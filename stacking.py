def emptychecker(l):
    if l == []:
        return False
    else:
        return True


def pusher(l):
    ans = 'y'
    while ans != '0':
        ask = int(input("Enter the Number you want to push into list"))
        l.append(ask)
        print(l)
        ans = input("you want to add more then press any key\nOr press 0 for exit()")
    return l


def poper(l):
    popped = l.pop()
    print(f"The pop() element form the list is {popped}")
    print(l)
    return l
l=[]
choice='shivam'
while choice!='0':
    user = int(input("Enter the choice \n [1] for Pushing a value \n [2] for Popping the value  "))
    if user== 1 :
        l=pusher(l)
        print(f"final list is {l}")
        continue
    elif user == 2:
        if emptychecker(l) == False:
            print("\tERROR!!! \nthe list is empty push some values first")
        else:
            l=poper(l)
    choice=input("Enter any key except '0' for continuing stacking.....")