from collections import deque, defaultdict, namedtuple

d = deque([1, 2, 3])
d.appendleft(5)
d.append(4)
print(deque)

notes="walk HW Eat"
notesCount = defaultdict(lambda : 0)

for note in notes.split(" "):
    notesCount[note] += 1

print( notesCount )
user = namedtuple("User", "name age gender")
user1 = user(name="bob", age= 45, gender= 'male')
print(user1)