#função IMC com acréscimo do nome

def imc(peso, altura, nome):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O imc de {nome} é {meu_imc:.2f}')
  return meu_imc

meu_imc = imc(106, 1.75, 'Léo')