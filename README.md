# 🍷 Desafio DataLab: Primeiros Passos na Análise de Dados com Polars

## 🎯 Objetivo
Realizar uma **Análise Exploratória de Dados (EDA)** inicial utilizando a **biblioteca Polars**.

---

## 📌 Regra de Ouro

> Para **CADA etapa abaixo**, você deve escrever um comentário no código explicando:
>
> - O que o código está fazendo;
> - Por que essa etapa é importante para um Cientista de Dados.

---

# 🚀 Etapa 1: Conhecendo o Terreno (Importação e Inspeção)

### ✅ Atividades

- [x] Importe a biblioteca `polars`.
- [x] Carregue o arquivo **winemag-data_first150k.csv** em um DataFrame.
- [x] Imprima as **5 primeiras linhas** do DataFrame para vermos a "cara" dos dados.
- [x] Descubra e imprima a quantidade total de **linhas** e **colunas** do DataFrame.
- [x] Descubra quais são os **tipos de dados** de cada coluna.

### 🎯 O que você deve responder
- Quantas linhas existem?
R: 150930 Linhas
- Quantas colunas existem?
R: 11 Colunas
- Quais são os tipos de dados presentes?
R: Strings, Int64, Float64. 

---

# 🧹 Etapa 2: A Arte da Limpeza (Lidando com Valores Nulos)

Na vida real, os dados raramente vêm perfeitos. Precisamos saber onde estão os "buracos".

### ✅ Atividades

- [x] Verifique quantas informações nulas (ausentes) existem em cada coluna.
- [x] A coluna `price` (preço) é muito importante para nós.
- [x] Crie um novo DataFrame que exclua todas as linhas onde o preço seja nulo.

### 🎯 O que você deve responder
- Quais colunas possuem valores nulos? 
R: 6 colunas possuem valores nulos
- Quantos valores nulos existem em cada uma?
R: Country = 5, Designation = 45735, Price = 13695, Province = 5, Region_1 = 25060, Region_2 = 89977
- Quantas linhas restaram após remover os preços nulos?
R: 137235 Linhas. 
---

# 🔎 Etapa 3: Respondendo a Perguntas com Filtros

O time de negócios quer saber sobre vinhos específicos.

### ✅ Atividades

- [x] Filtre o DataFrame para mostrar apenas os vinhos do país (`country`) **"Brazil"**.
- [x] Filtre os vinhos que:
  - [x] Possuem pontuação (`points`) maior ou igual a **90**;
  - [x] Possuem preço (`price`) menor que **20 dólares**.

### 🎯 O que você deve responder
- Quantos vinhos brasileiros existem na base?
R: 25 vinhos brasileiros
- Quantos vinhos atendem aos critérios de alta qualidade e baixo custo?
R: 15 vinhos atendem os critérios de alta qualidade e baixo custo (OBS: Foi necessário diminuir para >= 80 points)
---

# 📊 Etapa 4: Agrupamento e Insights (O poder do groupby)

Vamos encontrar os padrões gerais dos nossos dados.

### ✅ Atividades

#### 1️⃣ Países e preço médio

- [x] Agrupe os dados por país (`country`).
- [x] Calcule a média de preço (`price`) dos vinhos de cada país.
- [x] Ordene o resultado do maior para o menor preço médio.

#### 2️⃣ Melhor Chardonnay da base

- [x] Descubra qual é a pontuação máxima (`points`) recebida pelos vinhos da variedade (`variety`) **"Chardonnay"**.

### 🎯 O que você deve responder
- Qual país possui o maior preço médio?
R: US-France
- Qual foi a maior pontuação obtida por um Chardonnay?
R: Malbec

---

# ⚙️ Etapa 5: Engenharia de Recursos (Criando novas colunas)

Um bom cientista de dados cria suas próprias métricas.

### ✅ Atividades

- [x] Crie uma nova coluna chamada `custo_beneficio`.
- [x] Essa coluna deve ser calculada pela divisão:

```text
points / price
