
main = input()

while True:
    line = input()
    if line == 'Done':
        break
    command = line.split()
    if command[0] == 'Change':
        counter = 0
        current_char = command[1]
        replacement = command[2]
        for each in main:
            if each == current_char:
                counter += 1
        main = main.replace(current_char, replacement, counter)
        print(main)
    elif command[0] == 'Includes':
        chr = command[1]
        if chr in main:
            print('True')
        else:
            print('False')
    elif command[0] == 'End':
        chr = command[1]
        if main.endswith(chr):
            print('True')
        else:
            print('False')
    elif command[0] == 'Uppercase':
        main = main.upper()
        print(main)
    elif command[0] == 'FindIndex':
        chr = command[1]
        idx = 0
        for x in range(len(main)):
            if main[x] == chr:
                idx = x
                break
        print(idx)
    elif command[0] == 'Cut':
        start = int(command[1])
        length = int(command[2])
        main = main[start:start + length]
        print(main)

