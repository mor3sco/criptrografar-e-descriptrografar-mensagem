alfabeto = 'abcdefghijklmnopqrstuvwxyz'
chave = 3
novaMensagem = ''
  
mensagem = input('Por favor digite uma mensagem: ')

chave = input('Digite uma chave (1-26): ')
chave = int(chave)

for caractere in mensagem:
  if caractere in alfabeto:
    posicao = alfabeto.find(caractere)
    novaPosicao = (posicao + chave) % 26
    novoCaractere = alfabeto[novaPosicao]
    novaMensagem += novoCaractere


print('Sua nova mensagem é: ', novaMensagem)