username = input()

while True:
    command = input()
    if command == 'Sign up':
        break
    tokens = command.split()
    if tokens[0] == 'Case':
        if tokens[1] == 'lower':
            username = username.lower()
            print(username)
        elif tokens[1] == 'upper':
            username = username.upper()
            print(username)
    elif tokens[0] == 'Reverse':
        start = int(tokens[1])
        end = int(tokens[2])
        if start <= len(username) and end <= len(username):
            sub = username[start:end+1]
            print(''.join(reversed(sub)))
    elif tokens[0] == 'Cut':
        sub = tokens[1]
        if sub in username:
            username = username.replace(sub, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {sub}.")
    elif tokens[0] == 'Replace':
        chr = tokens[1]
        for x in range(len(username)):
            if username[x] == chr:
                username = username.replace(username[x], '*')
        print(username)
    elif tokens[0] == 'Check':
        chr = tokens[1]
        if chr in username:
            print('Valid')
        else:
            print(f'Your username must contain {chr}.')
