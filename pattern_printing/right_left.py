def pattern_right_fromLeft(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end='')
        for j in range(i+1):
            print("*", end=' ')
        print()
pattern_right_fromLeft(5)