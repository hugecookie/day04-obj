7-1
years_list = [2000, 2001, 2002, 2003, 2004]

7-2
# print(years_list[2])

7-3
# print(years_list[4])

7-4
things = ["mozzarella", "cinderella", "salmonella"]


7-5
# print(things[-2].title())

7-6
# print(things[-3].upper())

7-7
# print(f'Delete the {things.pop()} from things, get Nobel price')

7-8
surprise = ['Groucho', 'Chico', 'Harpo']

7-9
# surprise[2] = surprise[2].lower()
# surprise.reverse()
# surprise[0] = surprise[0].title()
# print(surprise)

7-10
# even = [a for a in range(1, 10) if a % 2 == 0]
# print(even)

7-11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we are done")
]
start2 = 'someone better'

# for i in range(7):
#     first = start1 + list(rhymes[0])
#     del first[-1]
#     start2 = start2[0].title() + start2[1:]
#     for j in range(4):
#         first[j] = (first[j].title())
#     print('! '.join(first) + '!')
#     print(start2 + ' ' + rhymes[i][1])

8-1
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

8-2
# print(e2f['walrus'])

8-3
ch = list(e2f.items())
f2e = {ch[0][1]:ch[0][0], ch[1][1]:ch[1][0], ch[2][1]:ch[2][0]}
# print(f2e)

8-4
# for i in range(3):
#     if list(e2f.values())[i] == 'chien':
#         print(list(e2f.keys())[i])

8-5
# print(f2e.values())

8-6

