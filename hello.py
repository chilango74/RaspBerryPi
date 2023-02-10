for i in range(1, 40): 
    if (i % 2 == 0) and (i !=2):
        continue
    elif (i % 3 == 0) and (i !=3):
        continue
    elif i % 5 == 0:
        continue
    else:
        print(i)