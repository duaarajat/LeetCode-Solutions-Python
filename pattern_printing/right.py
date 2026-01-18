def pattern_right(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print()
pattern_right(5) 