print('Standard form to vertex form V 1.3')
print('press 1 to accept questions')
while True:    
    work = []
    answers = []
    done = 0
    up_to = int(input('what do you want to find:'))
    add_up_to = int(input('add up to:'))
    number_to_find = up_to

    if up_to <= 0:
        up_to =up_to-1
    else:
        up_to = up_to+1
    up_to_positive = up_to
    if up_to <= 0:
        up_to_positive = up_to_positive * -1

    print('finding numbers divisible by', up_to, 'please wait...')
    def divide(number_to_find):
        for i in range(up_to_positive):
            if not i == 0:
                divide =  number_to_find / i
                if divide % 1 == 0:
                    work.append(divide)
                

        for i in range(up_to_positive):
            if not i == 0:
                negative_i = i * -1
                divide =  number_to_find / negative_i
                if divide % 1 == 0:
                    work.append(divide)

    divide(number_to_find)       

    print('Finishing up...')
    up_to= up_to + 0.0
    add_up_to = add_up_to + 0.0
    if up_to <= 0:
        up_to = up_to+1
    else:
        up_to = up_to -1
    for i in range(len(work)):
        for b in range(len(work)):
            add1 = work[i]
            add2 = work[b]
            sum = add1 + add2
            if add_up_to == sum:
                check = add1 * add2
                print(check, '+', up_to)
                if up_to < 0:
                    up_to - 1
                elif up_to >= 0:
                    up_to + 1

                print(up_to)
                if up_to == check:
                    answers.append(add1)
                    answers.append(add2)

    print('answer:',answers)
    repeat = input('Stop?:')
    if repeat == '1':
        break


