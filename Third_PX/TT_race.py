encrypted_sentence = input()

reg_ex = r'^([#$%*&])([a-zA-Z]+)\1=([0-9]+)!!(.+){16}'

#This function is for getting the length for one of the groups from the RegEx
def group_len(encrypted_sentence):
    for i in range(len(encrypted_sentence)):
        if encrypted_sentence[i] == '!':
            main_key = f'{encrypted_sentence[i-2]}{encrypted_sentence[i-1]}'
            print(main_key)
            break

group_len(encrypted_sentence)
