city = input().lower()
while True:
    city2 = input().lower()
    if city[-1] != city2[0]:
        print(city2)
        break
    city = city2