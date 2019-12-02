import operator
followers = dict()


while True:
    command = input()
    if command == 'Log out':
        break
    tokens = command.split(': ')
    if tokens[0] == 'New follower':
        username = tokens[1]
        if username not in followers:
            followers[username] = [0, 0]
    elif tokens[0] == 'Like':
        username = tokens[1]
        count = int(tokens[2])
        if username in followers:
            followers[username][0] += count
        else:
            followers[username] = [count, 0]
    elif tokens[0] == 'Comment':
        username = tokens[1]
        if username in followers:
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]
    elif tokens[0] == 'Blocked':
        username = tokens[1]
        if username in followers:
            followers.pop(username)
        else:
            print(f"{username} doesn't exist")

print(f'{len(followers)} followers')
# TODO - Sort dictionary using lambda!!!
#
#
#
#
#
