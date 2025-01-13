# Manual de Configuração do Ambiente - Data Football Analytics

Este guia foi desenvolvido para **usuários iniciantes** em programação e criação de projetos. Ele descreve de forma detalhada e passo a passo como configurar o ambiente de desenvolvimento para o projeto *Data Football Analytics*. Abaixo, você encontrará explicações sobre cada comando e ação necessária.

---

## **1. Pré-requisitos**

Antes de iniciar, certifique-se de que os seguintes softwares estão instalados no seu computador:

- **Python**: Versão 3.8 ou superior (verifique no terminal com `python --version`).
- **Visual Studio Code (VS Code)**: Última versão estável.
- **Git**: Ferramenta de controle de versão (verifique no terminal com `git --version`).
- **Sistema Operacional**: Windows 10/11.

Se algum desses itens não estiver instalado, procure tutoriais online para instalação antes de continuar.

---

## **2. Estrutura do Projeto**

### **Passo 1: Criar o diretório principal**

1. Abra o **Explorador de Arquivos** e navegue até o local onde deseja salvar o projeto.
2. Clique com o botão direito e escolha "Abrir no Terminal" ou abra o terminal do VS Code (atalho: `Ctrl + ```) e vá até o local desejado com:

   ```bash
   cd "E:\Profissional\Science\01_DataFootball"
   ```

3. Crie a pasta principal do projeto:

   ```bash
   mkdir 01_data_football_analytics
   cd 01_data_football_analytics
   ```

### **Passo 2: Criar a estrutura de pastas**

No terminal do VS Code ou no Prompt de Comando, execute os comandos abaixo para criar as pastas necessárias:

```bash
mkdir data notebooks src tests documentation reports
mkdir data\raw data\processed
```

**Explicação das pastas:**

- `data`: Armazena os dados brutos (`raw`) e processados (`processed`).
- `notebooks`: Contém os notebooks Jupyter para análises exploratórias.
- `src`: Contém os scripts Python organizados por função (coleta, processamento, visualização).
- `tests`: Scripts para testes e validação.
- `documentation`: Documentação técnica e análises do projeto.
- `reports`: Relatórios finais em PDF ou HTML.

---

## **3. Configuração do Ambiente Virtual**

### **Passo 1: Criar o ambiente virtual**

No terminal do VS Code, execute:

```bash
python -m venv .venv
```

Isso criará uma pasta chamada `.venv` dentro do projeto, onde todas as dependências serão instaladas.

### **Passo 2: Ativar o ambiente virtual**

No Windows, ative o ambiente virtual com:

```bash
.\.venv\Scripts\activate
```

Após ativar, você verá algo como `(.venv)` no início da linha do terminal, indicando que o ambiente virtual está ativo.

---

## **4. Instalação das Dependências**

Com o ambiente virtual ativo, instale as bibliotecas necessárias executando os comandos abaixo:

### **Bibliotecas para análise de dados**

```bash
pip install pandas numpy matplotlib seaborn plotly pip soccerdata mplsoccer
```

### **Bibliotecas para desenvolvimento**

```bash
pip install black flake8 pylint isort jupyter notebook ipykernel
```

### **Bibliotecas para relatórios**

```bash
pip install pdfkit streamlit
```

### **Salvar dependências instaladas**

Crie um arquivo `requirements.txt` contendo todas as bibliotecas instaladas:

```bash
pip freeze > requirements.txt
```

---

## **5. Extensões do VS Code**

Para melhorar a produtividade e facilitar o desenvolvimento, recomendamos instalar as seguintes extensões no Visual Studio Code. Para instalá-las, siga os passos abaixo:

1. Abra o VS Code.
2. Clique no ícone de Extensões na barra lateral esquerda (ou use o atalho `Ctrl+Shift+X`).
3. Pesquise pelo nome da extensão e clique em **Instalar**.

### **Extensões para Python e Data Science**

- **Python (Microsoft)**: Suporte completo para Python, incluindo execução de scripts e depuração.
- **Jupyter (Microsoft)**: Permite trabalhar com notebooks Jupyter diretamente no VS Code.
- **Pylance**: Fornece autocompletar avançado e verificação de tipos para Python.
- **GitHub Copilot**: Assistente de programação baseado em IA que sugere códigos.
- **GitHub Copilot Chat**: Chat interativo para suporte com IA dentro do VS Code.
- **Data Wrangler (Microsoft)**: Ferramenta para visualização, limpeza e preparação de dados tabulares.

### **Extensões para Visualização**

- **Excel Viewer**: Permite abrir e visualizar arquivos Excel diretamente no VS Code.
- **Rainbow CSV**: Facilita a leitura e manipulação de arquivos CSV, destacando colunas por cores.
- **Jupyter Notebook Renderers (Microsoft)**: Suporte a renderizações avançadas em notebooks Jupyter, como gráficos interativos com Plotly.
- **Jupyter Slide Show (Microsoft)**: Criação de apresentações interativas a partir de notebooks Jupyter.

### **Extensões para Documentação**

- **Markdown All in One**: Adiciona suporte avançado para edição de arquivos Markdown, incluindo atalhos e tabelas.
- **Markdown Preview Enhanced**: Permite visualizar arquivos Markdown com gráficos, tabelas e diagramas.
- **markdownlint**: Verifica boas práticas e estilo em arquivos Markdown.

### **Extensões de Produtividade**

- **autoDocstring**: Gera automaticamente docstrings para funções Python.
- **Python Indent**: Melhora a indentação automática em arquivos Python.
- **Git Graph**: Visualiza o histórico do Git em formato gráfico.
- **GitLens**: Exibe detalhes sobre commits diretamente no código.
- **Better Comments**: Facilita a criação de comentários organizados e coloridos no código.
- **Error Lens**: Destaca erros e avisos diretamente no editor.
- **Material Icon Theme**: Adiciona ícones personalizados às pastas e arquivos no VS Code.
- **Path Intellisense**: Autocompleta caminhos de arquivos ao escrevê-los no código.
- **Code Spell Checker**: Verifica erros ortográficos no código, útil para nomes de variáveis ou comentários.

---

## Configurações do Workspace

Após instalar as extensões acima, configure o workspace do VS Code para otimizar sua experiência com o projeto. Siga os passos abaixo:

1. Na raiz do projeto, crie uma pasta chamada `.vscode`.
2. Dentro da pasta `.vscode`, crie um arquivo chamado `settings.json`.
3. Cole o seguinte conteúdo no arquivo:

```json
{
    "editor.formatOnSave": true,
    "editor.rulers": [
        80,
        100
    ],
    "editor.renderWhitespace": "all",
    "editor.minimap.enabled": false,
    "editor.wordWrap": "on",
    "files.trimTrailingWhitespace": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    // Configurações específicas para Python
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": true,
    // Configurações específicas para Jupyter Notebooks
    "jupyter.notebookFileRoot": "${workspaceFolder}",
    "jupyter.askForKernelRestart": false,
    "jupyter.enableCellCodeLens": true,
    // Configurações específicas para Markdownlint e cSpell
    "[markdown]": {
        "editor.defaultFormatter": "yzhang.markdown-all-in-one",
        "editor.formatOnSave": true
    },
    "cSpell.words": [
        "Better",
        "Copilot",
        "docstrings",
        "documentaion",
        "Excel",
        "fbref",
        "flake8",
        "football",
        "Football",
        "freeze",
        "heatmaps",
        "Indent",
        "indentação",
        "ipykernel",
        "ipynb",
        "isort",
        "jupyter",
        "matplotlib",
        "mplsoccer",
        "numpy",
        "plotly",
        "pycache",
        "Pylance",
        "pylint",
        "pyplot",
        "Rainbow",
        "Renderers",
        "requirements",
        "seaborn",
        "Shift",
        "soccerdata",
        "streamlit",
        "Studio",
        "venv",
        "Viewer",
        "whoscored",
        "Wrangler",
        "yzhang"
    ]
}
```

### Explicação das Configurações

1. **`editor.formatOnSave`**: Formata automaticamente o código ao salvar o arquivo.
2. **`python.defaultInterpreterPath`**: Define o interpretador Python usado no projeto (o ambiente virtual criado).
3. **`python.linting`**: Ativa ferramentas como `pylint` e `flake8` para verificar erros no código.
4. **`jupyter.notebookFileRoot`**: Define a raiz dos notebooks como sendo a pasta do projeto.
5. **`files.autoSave`**: Salva automaticamente os arquivos após um pequeno atraso.

---

## **6. Configuração do Git**

### **Passo 1: Inicializar repositório**

No terminal, execute os comandos abaixo para configurar o Git no projeto:

```bash
git init
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### **Passo 2: Criar arquivo `.gitignore`**

Crie um arquivo chamado `.gitignore` na raiz do projeto com o seguinte conteúdo:

```bash
# Ambiente Virtual
.venv/
__pycache__/
*.pyc

# Dados e relatórios
data/raw/*
data/processed/*
reports/*

# Notebooks e logs
.ipynb_checkpoints/
*.log

# Configurações locais
.vscode/
.env
```

---

## **7. Verificação da Instalação**

Crie um arquivo chamado `tests/test_environment.py` com o seguinte código para verificar se tudo está configurado corretamente:

```bash
def test_imports():
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import plotly.express as px
        import soccerdata

        print("✅ Todas as bibliotecas foram importadas com sucesso!")
    except ImportError as e:
        print(f"❌ Erro ao importar biblioteca: {e}")

if __name__ == "__main__":
    test_imports()
```

Execute o script no terminal com:

```bash
python tests/test_environment.py
```

---

## **8. Primeiro Commit**

Após configurar tudo, faça seu primeiro commit no Git:

1. Adicione os arquivos ao repositório:

   ```bash
   git add .
   ```

2. Faça um commit inicial:

   ```bash
   git commit -m "Configuração inicial do projeto Data Football Analytics"
   ```

3. Vincule ao repositório remoto no GitHub (substitua pelo link do seu repositório):

   ```bash
   git remote add origin https://github.com/vipessoabarbosa/data_football_analytics.git
   git push -u origin main
   ```
