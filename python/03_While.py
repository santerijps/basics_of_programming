import time

def case1():
    # if {boolean expression (True / False)}:
    while True:
        print("Hello!")
        time.sleep(1)

def case2():
    keep_looping = True
    while keep_looping:
        print("Hello!")
        time.sleep(1)
        keep_looping = False

def case3():
    while True:
        print("Hello!")
        break
        print("World!") # this code is never run

def case4():
    i = 0
    while i < 10:
        i += 1
        print(i)

    # i = 1
    # while i <= 10:
    #     print(i)
    #     i += 1

def case5():
    i = 0
    while i < 10:
        i += 1

        # if i % 2 == 0:
        #     print(i)

        if i % 2 == 1:
            continue

        print(i)
