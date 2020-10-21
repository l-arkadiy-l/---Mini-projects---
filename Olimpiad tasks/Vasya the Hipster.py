red, blue = list(map(int, input().split()))
counter_1 = 0
counter_2 = 0
while red >= 2 or blue >= 2 or (red >= 1 and blue >= 1):
    if red and blue:
        red -= 1
        blue -= 1
        counter_1 += 1
    elif red:
        red -= 2
        counter_2 += 1
    elif blue:
        blue -= 2
        counter_2 += 1
print(counter_1, counter_2)
