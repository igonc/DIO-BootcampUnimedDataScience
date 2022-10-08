nome = 'Rodrigo'
idade = 42
profissao = 'Data Scientist'
periodo = 10
linguagem1 = 'Python'
linguagem2 = 'R'

print('Olá, me chamo %s e tenho %d anos de idade. Possuo experiência como %s há cerca de %d anos, com expertise utilizando as linguagens %s e %s.' % (nome, idade, profissao, periodo, linguagem1, linguagem2))
print('Olá, me chamo {0} e tenho {1} anos de idade. Possuo experiência como {2} há cerca de {3} anos, com expertise utilizando as linguagens {4} e {5}.'.format(nome, idade, profissao, periodo, linguagem1, linguagem2))
print('Olá, me chamo {} e tenho {} anos de idade. Possuo experiência como {} há cerca de {} anos, com expertise utilizando as linguagens {} e {}.'.format(nome, idade, profissao, periodo, linguagem1, linguagem2))
print('Olá, me chamo {nome} e tenho {idade} anos de idade. Possuo experiência como {profissao} há cerca de {periodo} anos, com expertise utilizando as linguagens {linguagem1} e {linguagem2}.'.format(nome=nome, idade=idade, profissao=profissao, periodo=periodo, linguagem1=linguagem1, linguagem2=linguagem2))
print(f'Olá, me chamo {nome} e tenho {idade} anos de idade. Possuo experiência como {profissao} há cerca de {periodo} anos, com expertise utilizando as linguagens {linguagem1} e {linguagem2}.')

pessoa = {'nome': nome, 'idade': idade, 'profissao': profissao, 'periodo': periodo, 'linguagem1': linguagem1, 'linguagem2': linguagem2}
print('Olá, me chamo {nome} e tenho {idade} anos de idade. Possuo experiência como {profissao} há cerca de {periodo} anos, com expertise utilizando as linguagens {linguagem1} e {linguagem2}.'.format(**pessoa))
