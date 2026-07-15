with open('output.txt','w') as fh1:
    text1=input('Enter text to write to file:')
    fh1.write(text1 +'\n')
    print('Data successfully written to output.txt')

with open('output.txt' ,'a') as fh2:
    text2=input('Enter additional text to append:')
    fh2.write(text2 + '\n')
    print('Data successfully appended to output.txt')
    print('Data successfully appended')

print('final content of ouput.txt')
with open('output.txt','r') as fh3:
    text3=fh3.read()
    print(text3)