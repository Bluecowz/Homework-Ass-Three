
file = open('UAH_sample.txt', 'r')

contents = file.read()

words = contents.split()

# find things with numbers

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

nums = []
for w in words:
    if any((c in numbers) for c in w):
       nums.append(w) 

print(nums)

# find j words 

j_list = set()

for w in words:
    if 'j' in w:
        j_list.add(w)

print(j_list)

# find UAHuntsville

count = 0
for w in words:
    if w == 'UAHuntsville':
        count += 1

print(count)

# find 12 letter long words

words_that_are_exactly_twelve_letters_long = []

for w in words: 
    if len(w) is 12:
        words_that_are_exactly_twelve_letters_long.append(w)
words_that_are_exactly_twelve_letters_long.sort()
print(words_that_are_exactly_twelve_letters_long)

# find all the ' words

ap_list = set()

for w in words:
    if "'" in w:
        ap_list.add(w)

print(ap_list)

file.close()
