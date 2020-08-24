import sys
lines = sys.stdin.readlines()


words = []
word = ''
out_text = ''

for text in lines:
    for i in text:        
        if i.isalnum():
            word += i
        else:                    
            if word == '0':
                break      
            if word.isnumeric():
                temp_word = words[int(word)*-1]
                words.remove(temp_word)
                words.append(temp_word)
                out_text += temp_word                                          
            if word.isalpha() and word != '':
                words.append(word)
                out_text += word
            out_text += i                       
            word = ''            

print(out_text[:-1])


