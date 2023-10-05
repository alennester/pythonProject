for a in range(1, 150):
    for b in range(a, 150):
        for c in range(b, 150):
            for d in range(c, 150):
                for e in range(d, 150):
                    if(a**5 + b**5 + c**5 + d**5 < e**5):
                        break
                    if (a**5 + b**5 + c**5 + d**5 == e**5):
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d,  'e =', e)
                        print(a + b + c + d + e)