# Assuming Python 3
s = "Кустарев И. П."
encoded = s.encode('cp1251')
print('исходное сообщение: ' + s)
print('в шестнадцатеричном коде: ', end='')
for b in encoded:
    print(str(hex(b)[2:]).upper(), end=' ')
print()
print('в двоичном коде: ', end='')
for b in encoded:
    print(bin(b)[2:], end='')
print()
print('длина сообщения: {0} байт ({1} бит)'.format(len(s), len(s)*8))