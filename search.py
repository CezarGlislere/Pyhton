## importando o módulo re (regular expression)
import re

## lista de termos para a busca
pesquisa = ['taxa','crescimento']

## texto para analisar 
texto = 'O conceito de derivada está intimamente relacionado à taxa de variação instantânea de uma'\
    'função, o qual está presente no cotidiano das pessoas, através, por exemplo, da determinação da'\
    'taxa de crescimento de uma certa população, da taxa de crescimento econômico do país, da taxa de'\
    'redução da mortalidade infantil, da taxa de variação de temperaturas, da velocidade de corpos ou '\
    'objetos em movimento, enfim, poderíamos ilustrar inúmeros exemplos que apresentam uma função '\
    'variando e que a medida desta variação se faz necessária em um determinado momento. Para'\
    'entendermos como isso se dá, inicialmente vejamos a definição matemática da derivada de uma '\
    'função em um ponto:'

## Exemplo basico de Data Mining
for item in pesquisa:
    print('Buscando por "%s" em: \n\n"%s"' % (item,texto))

## Verifica se o termo da pesquisa existe no texto
    if re.search(item,texto):
       print('\n')
       print('Palavra encontrada. \n')
       print('\n')

    else:
       print('\n')
       print('Palavra não encontrada')
       print('\n')





