
articles = ['solar_farms.txt', 'solar_panels.txt', 'clean_energy.txt']
big_words =  ['electric', 'battery', 'energy', 'wind', 'solar'] 

for article in articles:
    file = open(article, 'r', errors='ignore')
    content = file.read()
    words = content.split()

    length = len(words)
    points = 0

    for w in words:
        if w in big_words:
            points += big_words.index(w) + 1

    print(f'{article[:-4]}\tSize={length}\tScore={points}')

    file.close()
