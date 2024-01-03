pessoa = {
    'nome' : 'Wendell',
    'sobrenome' : 'Santos',
    'idade' : '19',
}

print(pessoa)
print('------------------------')
print(pessoa['nome'])
print('------------------------')
newkey = 'altura'
pessoa[newkey] = '1,72'

print(pessoa)
print('------------------------')

del pessoa['idade']

print(pessoa)