import polars as pl #Importando biblioteca Polars e apelidando ela de "pl"

df = pl.read_csv("winemag-data_first150k.csv") #Utiliazndo o polars (pl.read_csv) para ler o arquivo 

#df = pl.scan_csv("winemag-data_first150k.csv") #Diferente o Read_csv, o Scan_csv irá realizar um carregamento preguiçoso de dados, sendo uma grande vantagem para conjuntos de dados grandes, permitindo que o polars otimize as consultas antes de ler o conjunto de dados completo.

print(df.head()) #Exibe um DataFrame com as colunas e as 5 primeiras linhas do dataframe, podendo alterar a exibição de acordo com o desejavel, por exemplo: 
#print(df.head(10)) -> Irá mostrar as 10 primeiras linhas. 

print(df.tail()) #Exibe um DataFrame com as colunas e as 5 ultimas linhas do DataFrame

pl.set_random_seed(42) #Serve para que possa setar uma Seed no código, mantendo a reprodutividade. 

print(df.describe()) #Irá mostrar as estatísticas resumidas de todas as colunas do DataFrame

print(df.schema()) #Um dos comandos mais importantes para EDA, pois irá mostrar os nomes das colunas ou séries para os tipos de dados, como String, Date, Float64 e outros... Algo muito necessário para o Pre-Processamento.

