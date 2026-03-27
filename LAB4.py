num_users = int(input("Enter number of users: "))
users = {}

for i in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))

    user_items = []
    for j in range(num_items):
        item_name = input(f"Item {j + 1}: ")
        user_items.append(item_name)

    users[username] = user_items

print("\nUSER DATA:")
for user in users:
    print(user, "->", users[user])

all_unique_items_set = set()
for items_list in users.values():
    for item in items_list:
        all_unique_items_set.add(item)

common_items = []
unique_items = []
most_popular_items = []
max_count = 0

for item in all_unique_items_set:
    count = 0
    for items_list in users.values():
        if item in items_list:
            count += 1

    if count > 1:
        common_items.append(item)
    else:
        unique_items.append(item)

    if count > max_count:
        max_count = count

for item in all_unique_items_set:
    count = 0
    for items_list in users.values():
        if item in items_list:
            count += 1

    if count == max_count and max_count > 0:
        most_popular_items.append(item)

print("COMMON ITEMS:")
for item in common_items:
    print(item)

print("UNIQUE ITEMS:")
for item in unique_items:
    print(item)

print("MOST POPULAR ITEM:")
for item in most_popular_items:
    print(item)