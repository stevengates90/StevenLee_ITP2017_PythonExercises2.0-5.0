Cities = ('Boston','Las Vegas','Los Angeles','Seattle','New York')
print(Cities)
print(Cities[2])
print(Cities[0].title())
print(Cities[-1])
message = "I've been to " + Cities[2].title() + "."
print(message)
Cities = ['Boston','Las Vegas','Los Angeles','Seattle','New York']
print(Cities)
Cities[3] = 'Miami'
print(Cities)
Cities.append('Detroit')
print(Cities)
Cities.insert(1, "San Diego")
print(Cities)
del Cities[3]
print(Cities)
popped_Cities = Cities.pop()
print(Cities)
print(popped_Cities)
last_owned = Cities.pop()
print("Finally, we went to " + last_owned.title() + ".")
first_owned = Cities.pop(0)
print("First, we went to " + first_owned.title()+ ".")
Cities = ['Boston','Las Vegas','Los Angeles','Seattle','New York']
print(Cities)
Cities.remove("New York")
print(Cities)
too_expensive = 'Las Vegas'
Cities.remove(too_expensive)
print(Cities)
print("Las Vegas " + "is too far from where i live.")
Cities = ['Boston','Las Vegas','Los Angeles','Seattle','New York']
Cities.sort()
print(Cities)
Cities = ['Boston','Las Vegas','Los Angeles','Seattle','New York']
Cities.sort(reverse=True)
print(Cities)
Cities.reverse()
print(Cities)
Cities = ['Boston','Las Vegas','Los Angeles','Seattle','New York']
c= len(Cities)
print(c)







