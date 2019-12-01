import re
n = int(input())

final = []

templ = r'(^\$[A-Z]{1}[a-z]{2,}\$:[ ](\[[0-9]+\]\|){3}$)|(^\%[A-Z]{1}[a-z]{2,}\%:[ ](\[[0-9]+\]\|){3}$)'

for x in range(n):
    line = input()
    found = re.findall(templ, line)
    if found:
        line = line.split(': ')
        word = line[0][1:-1]
        lett = line[1].split('|')
        lett.pop()
        for y in lett:
            y = int(y[1:-1])
            y = chr(y)
            final.append(y)
        print(f"{word}: {''.join(final)}")
        final = []
    else:
        print('Valid message not found!')
