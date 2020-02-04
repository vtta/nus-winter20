
n = 0
while True:
    try:
        n += 1
        diameter, revolutions, time = map(float, input().strip().split(' '))
        if revolutions == 0:
            break
        distance = diameter * revolutions * 3.1415927 / 5280 / 12
        speed = distance / time * 60 * 60
        print("Trip #{}: {:.2f} {:.2f}".format(n, distance, speed))
    except EOFError:
        break
