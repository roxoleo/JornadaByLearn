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