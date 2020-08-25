import sys

lines = sys.stdin.readlines()
vowel = "AaEeIiOoUu"
word = ''
out_text = ''

for text in lines:
    for i in text:
        if i.isalpha():
            word += i            
        else:            
            if word != '':            
                if word[0] in vowel:
                    word += "ay"
                else:
                    word = word[1:]+word[0]+"ay"
            out_text += word + i            
            word = ''

print(out_text[:-1])

        




