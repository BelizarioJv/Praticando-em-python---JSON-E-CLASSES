import json

from criandoClasse import caminhoArquivo , Pessoa

with open (caminhoArquivo,"r") as arquivo:
    pessoas = json.load(arquivo)
    User1 = Pessoa(**pessoas[0])
    User2 = Pessoa(**pessoas[1])
    User3 = Pessoa(**pessoas[2])

print(vars(User1))
print(vars(User2))
print(vars(User3))