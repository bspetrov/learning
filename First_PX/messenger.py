max = int(input())

records = dict()

while True:
    command = input()
    if command == 'Statistics':
        break
    tokens = command.split('=')
    if tokens[0] == 'Add':
        username = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])
        if username not in records:
            records[username] = [sent, received]
    elif tokens[0] == 'Message':
        sender = tokens[1]
        receiver = tokens[2]
        if sender in records and receiver in records:
            records[sender][0] += 1
            records[receiver][1] += 1
            if sum(records[sender]) >= max:
                records.pop(sender)
                print(f'{sender} reached the capacity!')
            if sum(records[receiver]) >= max:
                records.pop(receiver)
                print(f'{receiver} reached the capacity!')
    elif tokens[0] == 'Empty':
        username = tokens[1]
        if username == 'All':
            records = {}
        else:
            if username in records:
                records.pop(username)
records = dict(sorted(records.items(), key=lambda x: (-x[1][1], x[0])))
print(f'Users count: {len(records)}')
for key, value in records.items():
    print(f'{key} - {sum(value)}')
