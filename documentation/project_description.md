# **Documento Descritivo do Projeto de Análise de Dados no Futebol**

Este documento tem como finalidade apresentar, de forma detalhada, as principais características e o planejamento para um projeto de análise de dados na área do futebol. O projeto está sendo desenvolvido em Python, utilizando o Visual Studio Code como IDE, e fará uso da biblioteca `soccerdata` para extração de estatísticas de sites especializados (FBref e WhoScored).
Parte da inspiração vem de projetos como o [**CruzeiroData*](https://cruzeirodata.substack.com), que mostram como dados avançados podem gerar insights sobre o desempenho de times e atletas de futebol, sobretudo no contexto brasileiro.

---

## **Revisão do Documento**

| Data       | Versão | Descrição da Alteração                     | Autor               |
| ---------- | ------ | ------------------------------------------ | ------------------- |
| 12-01-2025 | 1.0    | Criação do documento com estrutura inicial | Vinícius P. Barbosa |

---

## **1. Objetivo do Projeto**

1. **Objetivo Geral**: Desenvolver um sistema capaz de coletar, processar e analisar dados de futebol, gerando insights relevantes sobre o desempenho do Cruzeiro (ou de outros clubes) e de seus jogadores.
2. **Objetivos Específicos**:
   - **Coletar e padronizar dados** usando a biblioteca `soccerdata`, extraindo informações do FBref e WhoScored.
   - **Limpar e transformar** os dados, padronizando colunas e nomes.
   - **Criar análises e métricas** (xG, xA, passes, gols, etc.).
   - **Visualizar e reportar** resultados de forma simplificada para tomada de decisão.

---

## **2. Ambiente e Ferramentas**

- **Linguagem:** Python (versão ≥ 3.8)
- **IDE:** Visual Studio Code
- **Bibliotecas Principais:**
  - `pandas`, `numpy` (manipulação de dados)
  - `soccerdata` (coleta de dados de FBref e WhoScored)
  - `matplotlib`, `seaborn`, `mplsoccer`, `plotly` (visualizações)
- **Controle de Versão:** Git + GitHub
- **Sistema Operacional:** Windows (caminho de trabalho definido)

---

## **3. Estrutura do Projeto**

O diretório principal do projeto será:

E:\Desenvolvimento Profissional\Data Science\Python\Projetos\01_DataFootball\01_data_football_analytics

### **3.1 Estrutura de Diretórios**

data_football_analytics/
│
├── data/
│   ├── raw/                 # Dados brutos extraídos via `soccerdata`
│   └── processed/           # Dados limpos e prontos para análise
│
├── notebooks/               # Notebooks Jupyter de exploração e protótipos
│   ├── Exploratory.ipynb    # Primeiras análises e testes de visualização
│   └── ...
│
├── src/                     # Códigos-fonte do projeto
│   ├── data_collection.py   # Rotinas de coleta (web scraping) com `soccerdata`
│   ├── data_processing.py   # Processamento e limpeza (tratamento de nulos, normalizações)
│   ├── analysis.py          # Cálculo de métricas e análises exploratórias
│   └── visualization.py     # Funções para gerar gráficos e relatórios
│
├── reports/                 # Local para salvar gráficos e relatórios finais (PDF, HTML)
│
├── tests/ (opcional)        # Scripts de teste para lidar com dados e validação
│
├── documentation/            # Pasta dedicada à documentação do projeto
│   ├── project_description.md
│   └── setup_guide.md
│
├── README.md                # Descrição geral do projeto
├── requirements.txt         # Lista de dependências (versões das bibliotecas)
└── .gitignore               # Arquivos e pastas a serem ignorados pelo Git

### **3.2 Destaques de cada arquivo e pasta:**

- **`src/data_collection.py`**
  - **Função**: conterá scripts que utilizam `soccerdata` para extrair estatísticas (jogos, jogadores, eventos) do FBref e WhoScored.
  - **Sugestão**: configurar funções como `collect_fbref_data()` e `collect_whoscored_data()` para obter dados brutos e armazenar em `data/raw/`.

- **`src/data_processing.py`**
  - **Função**: limpar dados, tratar valores ausentes, padronizar colunas e nomes de equipes/jogadores.

- **`src/analysis.py`**
  - **Função**: calcular métricas avançadas (por exemplo, percentual de acerto de passes, gols prevenidos pelo goleiro, etc.) e preparar tabelas de comparação entre jogadores.

- **`src/visualization.py`**
  - **Função**: criar gráficos de linha, barras, “heatmaps” (com `mplsoccer` ou similar), além de exportar relatórios em PDF/HTML.

- **`notebooks/`**
  - Local ideal para testes ou prototipagem das análises e geração de insights rápidos. Exemplo: `Exploratory.ipynb`.

- **`documentaion/`** (grafia proposital para diferenciar)
  - `project_description.md`: visão geral do propósito, público-alvo, principais funcionalidades.
  - `setup_guide.md`: passo a passo de instalação das dependências, configuração de ambiente Python, ativação de ambiente virtual, etc.

---

## **4. Etapas do Projeto**

1. **Configuração Inicial**
   - Criação de ambiente virtual e instalação das dependências listadas em `requirements.txt`.
   - Ajustes na biblioteca `soccerdata` (definição de ligas, temporadas, etc.).

2. **Coleta de Dados**
   - Coletar dados de FBref e WhoScored usando `data_collection.py`.
   - Armazenar arquivos na pasta `data/raw/`.

3. **Limpeza e Processamento**
   - Padronizar nomes de colunas, corrigir valores ausentes e tipos de dados em `data_processing.py`.
   - Salvar versões processadas em `data/processed/`.

4. **Análise**
   - Desenvolver métricas e comparações em `analysis.py` e/ou notebooks.
   - Criar tabelas consolidadas por temporada, jogador, equipe etc.

5. **Visualização e Relatórios**
   - Usar `visualization.py` ou notebooks para gerar gráficos e relatórios.
   - Salvar relatórios em PDF ou HTML na pasta `reports/`.

6. **Validação e Testes**
   - (Opcional) Scripts em `tests/` para garantir a integridade dos dados e do pipeline.

---

## **5. Ferramentas Utilizadas**

- **Linguagem e IDE**: Python (versão ≥ 3.8) e Visual Studio Code
- **Manipulação de Dados**: `pandas`, `numpy`
- **Visualização**: `matplotlib`, `seaborn`, `mplsoccer`, `plotly`
- **Coleta de Dados**: `soccerdata`
- **Outras**: Jupyter Notebook, bibliotecas de exportação para PDF (por exemplo, `pdfkit`)

---

## **6. Exemplos de Análises Planejadas**

| Tipo de Análise                | Descrição                                                    |
| ------------------------------ | ------------------------------------------------------------ |
| Mapas de Finalizações          | Mostra onde os chutes foram realizados no campo/gol          |
| Comparação Entre Goleiros      | Avaliação baseada em PSxG+/- (gols prevenidos)               |
| Evolução Rodada a Rodada       | Exibe xG, pontos ou desempenho em diferentes rodadas         |
| Fluxo de Passes                | Mapeia os passes mais frequentes entre os jogadores          |
| Ranking dos Melhores Jogadores | Baseado em métricas como xG, xA, desarmes, finalizações etc. |

---

## **7. Exemplos de Visualizações Planejadas**

| Tipo de Visualização              | Descrição                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------- |
| Mapas de Finalizações (Shot Maps) | Mostrar a localização dos chutes no campo, utilizando *WhoScored* para coordenadas.   |
| Heatmaps de Movimentação          | Evidenciar as regiões do campo onde os jogadores mais atuam.                          |
| Gráficos de Radar (Spider Charts) | Comparar múltiplas métricas simultaneamente (ex.: passes, finalizações, dribles).     |
| Linhas de Tendência               | Ilustrar a evolução de métricas como xG ou pontos ao longo das rodadas.               |
| Gráficos de Barras                | Destacar os principais jogadores em termos de gols, assistências ou passes decisivos. |

---

## **8. Cronograma Estimado**

| Etapa                  | Duração Estimada | Período (Previsto)      |
| ---------------------- | ---------------- | ----------------------- |
| Configuração Inicial   | 1 semana         | 13/01/2025 a 19/01/2025 |
| Coleta dos Dados       | 1 semana         | 20/01/2025 a 26/01/2025 |
| Limpeza dos Dados      | 2 semanas        | 27/01/2025 a 09/02/2025 |
| Análises Estatísticas  | 3 semanas        | 10/02/2025 a 01/03/2025 |
| Visualizações Gráficas | 3 semanas        | 02/03/2025 a 22/03/2025 |
| Relatórios             | 2 semanas        | 23/03/2025 a 05/04/2025 |

---

## **9. Possíveis Evoluções e Modularidade**

Embora este projeto seja planejado para alguém com pouca experiência na área de análise de dados, a estrutura permite uma evolução contínua:

- **Integração com Bancos de Dados**: Futuramente, migrar para PostgreSQL ou MySQL para lidar com grandes volumes.
- **Dashboards Interativos**: Adicionar ferramentas como Streamlit ou Dash para consultas dinâmicas.
- **Machine Learning**: Incorporar previsões de desempenho individual ou de resultados de partidas conforme a experiência do autor aumentar.
- **Automação de Rotinas**: Agendar tarefas de coleta de dados e geração de relatórios via ferramentas de CI/CD (ex.: GitHub Actions).

---

Este projeto combina ferramentas modernas e acessíveis para análise de futebol, fornecendo uma **base sólida** para adentrar o universo de dados esportivos. A estrutura modular e a documentação clara possibilitam **crescimento gradativo**, permitindo que o(a) desenvolvedor(a) implemente novas métricas e gráficos conforme for ganhando experiência. Espera-se que este trabalho sirva como ponto de partida para análises estatísticas cada vez mais ricas, gerando insights estratégicos para o esporte e contribuindo para o desenvolvimento profissional na área de Ciência de Dados.

---

**Autor: Vinícius P. Barbosa**
*Última atualização: 10 de janeiro de 2025*