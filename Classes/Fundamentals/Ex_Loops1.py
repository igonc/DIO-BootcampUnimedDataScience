# EXEMPLO DE FOR COM ITERAÇÃO
# EXIBINDO AS VOGAIS DE UM TEXTO
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'
i = 0
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
        i += 1

if i == 0:
        print('Não existem vogais no texto')
print()