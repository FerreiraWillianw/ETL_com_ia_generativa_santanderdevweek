# Santander Dev Week 2023: Geração de Mensagens de Marketing Personalizadas com IA

## 🎯 Objetivo do Projeto

Este projeto demonstra a integração de dados de clientes obtidos através da API oficial da **Santander Dev Week 2023 (SDW2023)** com a capacidade de geração de texto da **OpenAI (GPT-4)**. O objetivo final é criar e atribuir mensagens de marketing altamente personalizadas sobre a importância de investimentos para cada cliente, utilizando seus dados cadastrais.

A solução automatiza um pipeline de dados e processamento, transformando uma lista simples de IDs de clientes em um conjunto de mensagens customizadas prontas para serem veiculadas em aplicativos bancários ou canais de comunicação.

## ⚙️ Tecnologias Utilizadas

* **Python:** Linguagem principal para o desenvolvimento do script.
* **Pandas:** Utilizado para a leitura e manipulação inicial dos dados a partir do arquivo CSV.
* **Requests:** Biblioteca para a realização de consultas HTTP e consumo da API da SDW2023.
* **API Santander Dev Week 2023:** Fonte de dados simulada para informações de contas bancárias de clientes.
* **API OpenAI (GPT-4):** Motor de Inteligência Artificial para gerar as mensagens de marketing com base nas informações do cliente (usando *prompts* de sistema e usuário).
* **JSON:** Formato de serialização de dados usado para manipular as respostas das APIs.

## 🛠️ Funcionalidades Chave

1.  **Leitura de Dados (CSV):** O script inicia lendo o arquivo `SDW2023.csv` para extrair uma lista de `UserIDs`.
2.  **Consulta à API Externa:**
    * Itera sobre a lista de IDs.
    * Utiliza a função `get_user(id)` para consultar o endpoint da API `https://sdw-2023-prd.up.railway.app/users/{id}`.
    * Filtra e coleta apenas os dados de clientes que retornam um status `200 OK`.
3.  **Geração de Conteúdo Personalizado com IA:**
    * A função `generate_ai_news(user)` utiliza o modelo **GPT-4** para gerar uma mensagem.
    * Um *prompt* de **"System Role"** define o comportamento da IA como um **"especialista em marketing bancário"**.
    * O *prompt* de **"User Role"** passa o nome do cliente e a instrução clara para criar uma mensagem concisa (máximo de 100 caracteres) sobre investimentos.
4.  **Enriquecimento dos Dados:** As mensagens geradas pela IA são inseridas de volta na estrutura de dados de cada cliente, simulando o enriquecimento de um perfil de usuário com um novo item de **"news"**.
5.  **Output e Visualização:** O processo finaliza com a impressão dos resultados e a estrutura de dados atualizada, demonstrando o sucesso da integração.

## 📂 Estrutura do Código

O código segue um fluxo lógico de processamento:

1.  **Configuração de APIs:** Definição das URLs e chaves de acesso (`sdw2023_api_url`, `openai_api_key`).
2.  **Extração de IDs:** `pd.read_csv('SDW2023.csv')` e conversão para lista.
3.  **Função de Conexão com SDW2023:** `get_user(id)` para buscar dados do cliente.
4.  **Função de Geração com OpenAI:** `generate_ai_news(user)` para criar a mensagem de marketing.
5.  **Loop Principal:** Iteração sobre os usuários, chamada das APIs e atualização do objeto `user`.

## 📈 Lições Aprendidas e Destaques

* **Orquestração de Múltiplas APIs:** Demonstração prática de como integrar e encadear o uso de APIs de dados (SDW2023) e APIs de processamento/serviço (OpenAI).
* **Prompt Engineering Básico:** Utilização de *System Role* para direcionar a personalidade e a especialidade do modelo de IA (marketing bancário), garantindo a relevância do output.
* **Automação de Marketing:** Criação de um MVP (Produto Mínimo Viável) para personalização em escala, um conceito central em *FinTech* moderna.
