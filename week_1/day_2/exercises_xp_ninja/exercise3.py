Morse_dict = {
    'a' : ".-",'b' : "-...",'c' : "-.-.",'d' : "-..",'e' : ".",'f' : "..-.",'g' : "--.",'h' : "....",'i' : "..",'j' : ".---",'k' : "-.-",'l' : ".-..",'m' : "--",'n' : "-.",'o' : "---",'p' : ".--.",'q' : "--.-",'r' : ".-.",'s' : "...",'t' : "-",'u' : "..-",'v' : "...-",'w' : ".--",'x' : "-..-",'y' : "-.--",'z' : "--..", ' ' : "/"
}
'''
user_word = input("enter a word: ").lower()

each_word = user_word.split()
print(each_word)

letter_list = []
for word in each_word:
    words = list(word)
    letter_list.append(words)

for letter in letter_list:
    if letter in Morse_dict:
        for value in Morse_dict:
            print(f"{letter} : {Morse_dict[letter]}")
            break


'''