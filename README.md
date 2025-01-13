# Data Football Analytics

![Logo do Projeto](https://github.com/vipessoabarbosa/data_football_analytics/blob/main/assets/images/logo.png)

## 📖 Descrição do Projeto

O **Data Football Analytics** é um projeto de análise de dados focado no futebol brasileiro. Ele utiliza ferramentas de ciência de dados para coletar, processar e visualizar informações relevantes sobre partidas, jogadores e times, fornecendo insights valiosos para torcedores, analistas e profissionais da área.

---

## 🚀 Status do Projeto

  🟢 Data Football Analytics 🚀 Em desenvolvimento... 🟢

---

## 📋 Índice

- [Data Football Analytics](#data-football-analytics)
  - [📖 Descrição do Projeto](#-descrição-do-projeto)
  - [🚀 Status do Projeto](#-status-do-projeto)
  - [📋 Índice](#-índice)
  - [✨ Funcionalidades Principais](#-funcionalidades-principais)
  - [🛠️ Pré-requisitos e Configuração](#️-pré-requisitos-e-configuração)
    - [Configuração do Ambiente Virtual](#configuração-do-ambiente-virtual)
  - [▶️ Como Rodar o Projeto](#️-como-rodar-o-projeto)
  - [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
    - [Linguagens e Ferramentas](#linguagens-e-ferramentas)
    - [Bibliotecas](#bibliotecas)
  - [🤝 Contribuição](#-contribuição)
  - [👨‍💻 Autor](#-autor)
  - [📜 Licença](#-licença)

---

## ✨ Funcionalidades Principais

✔️ Coleta de dados estatísticos de partidas e jogadores.
✔️ Processamento e limpeza de dados brutos.
✔️ Visualização interativa de métricas e gráficos.
✔️ Análise avançada utilizando Machine Learning (em desenvolvimento).
✔️ Exportação de relatórios em PDF e dashboards interativos.

---

## 🛠️ Pré-requisitos e Configuração

Antes de começar, certifique-se de que você possui os seguintes itens instalados no seu ambiente:

1. **Python 3.8 ou superior**
   Verifique a instalação com o comando:

   ```bash
   python --version
   ```

2. **Visual Studio Code (VS Code)**
   Instale as extensões recomendadas no guia de configuração.

3. **Git**
   Verifique a instalação com o comando:

   ```bash
   git --version
   ```

4. **Dependências do projeto**
   Instale as bibliotecas listadas no arquivo `requirements.txt` após configurar o ambiente virtual.

### Configuração do Ambiente Virtual

1. Crie o ambiente virtual:

   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente virtual (Windows):

   ```bash
   .\.venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Rodar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/data_football_analytics.git
   cd data_football_analytics
   ```

2. Configure o ambiente virtual conforme descrito acima.

3. Execute um notebook Jupyter para análises exploratórias:

   ```bash
   jupyter notebook
   ```

4. Para rodar scripts Python diretamente:

   ```bash
   python src/main.py
   ```

5. Para gerar relatórios interativos com Streamlit:

   ```bash
   streamlit run src/visualization/dashboard.py
   ```

---

## 💻 Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto incluem:

### Linguagens e Ferramentas

- **Python**: Linguagem principal para análise e processamento.
- **Jupyter Notebook**: Ferramenta para análise exploratória.
- **Streamlit**: Criação de dashboards interativos.

### Bibliotecas

- **Pandas**: Manipulação de dados.
- **NumPy**: Operações matemáticas.
- **Matplotlib/Seaborn/Plotly**: Visualização de dados.
- **SoccerData/Mplsoccer**: Coleta e visualização específica para futebol.
- **Flake8/Pylint/Black**: Linting e formatação de código.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir com o projeto:

1. Faça um fork deste repositório.
2. Crie uma nova branch com a sua funcionalidade ou correção:

   ```bash
   git checkout -b minha-feature
   ```

3. Faça commit das suas alterações:

   ```bash
   git commit -m "Minha nova feature"
   ```

4. Envie as alterações para a sua branch remota:

   ```bash
   git push origin minha-feature
   ```

5. Abra um Pull Request explicando suas alterações.

---

## 👨‍💻 Autor

Desenvolvido por [Vinícius P. Barbosa](https://github.com/vipessoabarbosa).

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
