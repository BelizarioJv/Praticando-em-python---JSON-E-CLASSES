import json
caminhoArquivo = 'arquivo.json'
class Pessoa :
    year = 2025

    def __init__(self,nome,sobrenome,idade,email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
    
User1 = Pessoa("Joao","Victor",22,"joaovictor.fera@hotmail.com")
User2= Pessoa("Paulo","Antonio",42,"pauloantonio@hotmail.com")
User3 = Pessoa("Davidson","Santos",35,"davidsonsantos@hotmail.com")

listaUsuarios = [vars(User1),vars(User2),vars(User3)]


with open  (caminhoArquivo,"w") as arquivo :
    json.dump(listaUsuarios,arquivo,ensure_ascii=False,indent=2)

    
