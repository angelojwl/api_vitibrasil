🚀 Visão Geral do Projeto

Objetivo: Fornecer uma API pública que permita consultar, em tempo real, os dados de vitivinicultura do site da Embrapa e documentação interativa via Swagger.  


Funcionalidades Principais:  
	•	Raspagem de dados em tempo real do site da Embrapa das categorias: Produção, Processamento, Comercialização, Importação e Exportação.  
	•	Documentação automática e interativa com Swagger UI.  
	•	Fallback para arquivos CSV local em caso de falha na raspagem.  


🗂️ Estrutura do Projeto
```plaintext
api_vitibrasil/
├── app/
│   ├── routes/
|   |   ├── 
│   │   └── vitibrasil.py
│   ├── services/
|   |   ├── __init__.py
│   │   └── scraper.py
│   ├── utils/
|   |   ├── __init__.py
│   |   └── fallback.py
|   ├── __init__.py
|   └── main.py
├── data/
│   ├── comercio.csv
│   ├── exportacao.csv
│   ├── importacao.csv
│   ├── processamento.csv
│   └── producao.csv
├── Procfile
├── README.md
└── requirements.txt
```
`app/`: Diretório principal do aplicativo.
`routes/`: Contém a rota para obter os dados.
`services/`: Serviços para lógica de negócios, como scraping.
`data/`: Arquivos CSV para fallback
`utils/`: Utilitários, fallback para caso scrap falhe.
`main.py`: Ponto de entrada para iniciar o aplicativo.
`README.md`: Documentação do projeto.
`requirements.txt`: Lista de dependências do projeto.


📄 Documentação com Swagger

A documentação interativa da API está disponível em /docs, fornecida automaticamente pelo FastAPI utilizando Swagger UI. Isso permite que os usuários explorem e testem os endpoints diretamente pelo navegador.  


🛠️ Raspagem de Dados com BeautifulSoup

A raspagem dos dados é realizada utilizando a biblioteca BeautifulSoup. A função scrape_data no módulo scraper.py acessa as páginas específicas do site da Embrapa, extrai as tabelas de interesse e as converte para o formato JSON. Em caso de falha na raspagem, a função load_fallback_data no módulo fallback.py fornece os dados a partir dos arquivos CSV local.  


🔄 Fallback para Arquivos Locais

Caso a raspagem em tempo real falhe (por exemplo, devido a mudanças na estrutura do site ou problemas de conectividade), a API utiliza arquivos CSV local como fonte de dados alternativa. Isso garante a continuidade do serviço mesmo em situações adversas.  


🔗 Repositório e Link de Deploy  
	•	Repositório GitHub: https://github.com/angelojwl/api_vitibrasil  
	•	Link de Deploy (Heroku): https://vitibrasil-api.herokuapp.com  



🖼️ Diagrama de Arquitetura
```plaintext
┌────────────┐       ┌──────────────┐       ┌──────────────┐
│  Cliente   │ ───▶  │     API      │ ───▶  │   Embrapa    │
|            │       │  (FastAPI)   │       │(Web Scraping)|
└────────────┘       └────┬─────────┘       └────┬─────────┘
                          │                      │
                          ▼                      ▼
                   ┌──────────────┐       ┌──────────────┐
                   │ Autenticação │       │ Fallback CSV │
                   │    JWT       │       │   Local      │
                   └──────────────┘       └──────────────┘
```


⚙️ Como executar o projeto

1. Clone o Repositório
```bash
git clone https://github.com/angelojwl/api_vitibrasil
cd api_vitibrasil
```

2. Crie um Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# No Windows: venv\Scripts\activate
```

3. Instale as Dependências
```bash
pip install -r requirements.txt
```

4. Execute o Aplicativo
```bash
python3 app/main.py
```

