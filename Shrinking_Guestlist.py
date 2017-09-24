guest = ['Kendall Jenner ','Kylie Jenner','Kendrick Lamar','Calvin Harris']
mail = ', You are invited to a dinner'
guest.insert(0, "Rihanna, ")
guest.insert(1, "Drake, ")
guest.append('Travis Scott, ')
print(guest[0] + mail)
print(guest[1] + mail)
print(guest[2] + mail)
print(guest[3] + mail)
print(guest[4] + mail)
print(guest[5] + mail)
print(guest[6] + mail)

message = 'I found a bigger table for us'
print(message)

text = 'I am sorry that i cannot invite you to dinner because there is no more table left'
print(text)
guest.pop()
guest.pop()
guest.pop()
guest.pop()
print(guest)

message = 'You are still invited to dinner'
print(guest[0] + message)
print(guest[1] + message)
print(guest[2] + message)

del guest[0]
del guest[0]
del guest[0]
print(guest)
