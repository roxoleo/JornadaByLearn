# JornadaByLearn
Repositório Teste da Jornada Python Faixa Preta ByLearn - com Zarcky

Códigos-Testes para treinar Python

Projeto para aprender a usar Git e Github

#função IMC com acréscimo do nome

def imc(peso, altura, nome):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O imc de {nome} é {meu_imc:.2f}')
  return meu_imc

meu_imc = imc(106, 1.75, 'Léo')

#Função calcular média com acréscimo do nome do aluno

def calcular_media(notas, nome):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print(f'{nome} tirou', media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno Aprovado :)')
  else:
    print('Aluno Reprovado :(')

calcular_media([10, 9, 8, 7], 'Léo')
