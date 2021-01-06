import collections

# named touple
Point = collections.namedtuple('Point', 'x y')
p1 = Point(10,20)
p2 = Point(30,50)

print(p1, p2)
print(p1.x, p2.y)

p1 = p1._replace(x=100)
print(p1)

# default dict
list_01 = ['0', '1', '12', '0', '0', '0', '1', '12']

counted_dict = collections.defaultdict(int)

for item in list_01:
    counted_dict[item] += 1

counted_dict

# counter
nums = collections.Counter(list_01)

nums.update(collections.Counter(list_01))

#ordered dict
teams = [("fradi", 8), ("ujpest", 12), ("mtk", 10), ("debrecen", 9)]

sorted_teams = sorted(teams, key=lambda t: t[1], reverse=True)
teams
sorted_teams

d1 = collections.OrderedDict(teams)
d1

# deque
import string
d = collections.deque(string.ascii_lowercase)
len(d)

d.pop()
d
len(d)
d.popleft()
d
len(d)
d.append(2)
d
len(d)
d.appendleft(3)
d
len(d)
d.rotate(10)
d