def calculate_love_score(name1, name2):
    count1, count2 = 0, 0
    for letter in name1 + name2:
        if letter in 'true':
            count1 += 1
        if letter in 'love':
            count2 += 1
    print(f"{count1}{count2}")
calculate_love_score('Dennis Reynolds', 'Charlie Kelly')