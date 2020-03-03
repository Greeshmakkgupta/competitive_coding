t=input()
d = au = al = sc = 0
if len(t)>=8:
    for i in t:
            if ord(i) > 64 and  ord(i) < 91:
              au += 1
            elif  ord(i) >= 97 and  ord(i) <= 122:
              al += 1
            elif ord(i) >= 48 and ord(i) <= 57:
              d += 1
            else:
                sc += 1

else:
    print('length is short ')

if al != 0 and sc != 0 and au != 0 and d != 0:
    print("valid password ")
else:
    print('not a valid password ')