new_list = []
run = True
mini = 1000000.0
maxi = 0
while(run):
    user = input()
    if user != ".":
        new_list.append(float(user))
    else:
        run = False
        for n in new_list:
            maxi = n
            if maxi < mini:
                mini = maxi
        print(mini)
