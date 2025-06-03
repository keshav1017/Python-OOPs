# lst = [1, 2, 3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

# lst.clear()
# print(lst)

# my_str.capitalize()
# print(my_str)

from oops_proj import chatbook

user1 = chatbook()
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

print(user1.id)
# using static method directly from class rather than obj

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)


user3 = chatbook()
print(user3.id)

# function
# a1 = len(lst)
# print(a1)

# user1.send_message()