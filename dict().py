#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
           7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

min_key = min(my_dict.keys())
max_key = max(my_dict.keys())

print(min_key + max_key)

#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
{'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
{'name': 'Olivia', 'phone': '449-3141', 'email': ''},
{'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
{'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
{'name': 'John', 'phone': '233-421-32', 'email': ''},
{'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
{'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
{'name': 'Robert', 'phone': '420-2011', 'email': ''},
{'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
{'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
{'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
{'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
{'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
{'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
{'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

names = []

for u in users:
    phone = u['phone']
    if phone[-1] == '8': 
        names.append(u['name'])

names.sort()
print(*names)

#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
{'name': 'Helga', 'phone': '555-1618'},
{'name': 'Olivia', 'phone': '449-3141', 'email': ''},
{'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
{'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
{'name': 'John', 'phone': '233-421-32', 'email': ''},
{'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
{'name': 'Alina', 'phone': '+7948-799-2434'},
{'name': 'Robert', 'phone': '420-2011', 'email': ''},
{'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
{'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
{'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
{'name': 'Roman', 'phone': '+7459-145-8059'},
{'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
{'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
{'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

names = []

for u in users:
    if 'email' not in u or u['email'] == '':
        names.append(u['name'])

names.sort()
print(*names)

#4
num = input()

d = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

res = []

for ch in num:
    res.append(d[ch])

print(*res)

#8
result = {}

for i in range(11, 16):
    result[i] = i ** 2

#9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]

#10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for ch in text:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1


#11
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

words = s.split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
max_count = max(count.values())
most_common = []
for w in count:
    if count[w] == max_count:
        most_common.append(w)
most_common.sort()
print(most_common[0])

#12
result = {}

for pet in pets:
    dog, name, surname, age = pet
    owner = (name, surname, age)
    if owner not in result:
        result[owner] = []
    result[owner].append(dog)

#13
s = input().lower()

for ch in '.,!?:;-':
    s = s.replace(ch, '')

words = s.split()
count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

min_count = min(count.values())
rare_words = [w for w in count if count[w] == min_count]
rare_words.sort()
print(rare_words[0])

#14
ids = input().split()
count = {}
result = []

for i in ids:
    if i in count:
        count[i] += 1
        result.append(f"{i}_{count[i]-1}")
    else:
        count[i] = 1
        result.append(i)

print(*result)
