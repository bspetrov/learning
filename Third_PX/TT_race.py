encrypted_sentence = input()

reg_ex = r'^([#$%*&])([a-zA-Z]+)\1=([0-9]+)!!(.+){16}'

#This function is for getting the length for one of the groups from the RegEx
def group_len(encrypted_sentence):
    for i in range(len(encrypted_sentence)):
        if encrypted_sentence[i] == '!':
            main_key = f'{encrypted_sentence[i-2]}{encrypted_sentence[i-1]}'
            try:
                main_key = int(main_key)
                return main_key
            except:
                main_key = int(encrypted_sentence[i-1])
                return main_key


print(group_len(encrypted_sentence))
