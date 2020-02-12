import xml.etree.ElementTree as ET
import pandas as pd

receitas = ET.parse("receita.xml")
root = receitas.getroot()
print(root.tag) # nome da tag: receita
print(root.attrib) # atributos: {'nome': 'pão', 'tempo_de_preparo': '5 minutos', 'tempo_de_cozimento': '1 hora'}

# Buscar os subelementos de root
for child in root:
    print(child.tag)
    #titulo, ingredientes, instrucoes

# Percorrendo todos elementos do arquivo
print([elem.tag for elem in root.iter()])

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

dados = []
for ingrediente in root.iter('ingrediente'):
    dado = {}
    dado[ingrediente.tag] = ingrediente.text
    dado['atributos'] = ingrediente.attrib
    dados.append(dado)


#print(dados)
df = pd.DataFrame(dados)
print(f"df: {df}")

