
num1 = 23
num2 = 23.4
x = False
first_name = 'paul'
FIRST_NAME = 'JOHN'
SECOND_NAME = 'PETER'
print(first_name, FIRST_NAME, SECOND_NAME)

#ESCAPE CHARACTER
word = 'we\'re brothers from the other side of the town'
print(word)

#NEWLINE
word2 = 'python is fun,\npython is easy,\npython is good'
print(word2)

#MULTILINE STRING
print('\n')
word3 = '''python is fun
python is easy
python is good
'''
print(word3)

#STRING CONCATENATION
print('my name is' + ' '+ first_name)

#STRING FORMATTING
price1 = 1000
price2 = 2000
price3 = 3000

report = 'i sold a jacket for {}, a shirt for {} and a suit for {}'
print(report.format(price1,price2,price3))

print(f'i sold a jacket for {price1}, a shirt for{price2} and a suit for {price3}')

#STRING METHOD
word1 = 'python'
word2 = 'PYTHON'
word3 = 'python is fun'
word4 = '  info@gmail.com'
print(word1.upper())
print(word2.lower())
print(word3.title())
print(word3.capitalize())
print(word3.split())
print(word4.strip())


