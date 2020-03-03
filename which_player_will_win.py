t = eval(input())
even_words = 0
odd_words = 0

for i in t:
    if len(i) % 2 == 0:
        even_words += 1
    else:
        odd_words += 1

p1 = 'greeshma'
p2 = 'manali'

if even_words > odd_words:
    print(f'{p1} always win ')
elif even_words < odd_words:
    print(f'{p2} win always win')
else:
    print('tie match ')    
    
