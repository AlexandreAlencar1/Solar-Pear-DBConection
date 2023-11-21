from pymongo import MongoClient

# Conectar ao MongoDB sem senha
client = MongoClient('mongodb://admin:admin@localhost:27017/')

# Selecionar o banco de dados
db = client['nome_do_banco']

# Selecionar a coleção
collection = db['nome_da_colecao']

# Inserir um documento
documento = {'chave': 'valor'}
resultado_insercao = collection.insert_one(documento)
print(f'ID do documento inserido: {resultado_insercao.inserted_id}')

# Consultar dados
resultados_consulta = collection.find({'chave': 'valor'})
for doc in resultados_consulta:
    print(doc)
