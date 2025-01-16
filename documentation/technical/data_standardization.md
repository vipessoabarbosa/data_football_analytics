```# cSpell:disable```

# Plano de Documentação: Padronização de Dados

Este documento estabelece as diretrizes e processos para normalização e padronização dos dados do projeto, garantindo consistência, qualidade na integração das informações e clareza na hora de combinar diferentes tabelas. Ele complementa o project_description.md no que se refere às definições técnicas, além de referenciar o data_dictionary.md para consultar tipos de dados e descrições originais.

## 1. Introdução

### 1.1 Objetivo do Documento

Estabelecer diretrizes técnicas e processuais para padronização dos dados de futebol, garantindo consistência na integração entre FBref e WhoScored.

### 1.2 Escopo

- Padronização de métricas e estatísticas de futebol
- Processos de ETL específicos para dados esportivos
- Definição de tabelas e métricas prioritárias
- Regras de combinação de fontes de dados

### 1.3 Documentos Relacionados

- project_description.md
- data_dictionary.md

## 2. Definições Técnicas

### 2.1 Padrões de Nomenclatura

A padronização de nomenclatura é essencial para garantir a consistência e a clareza na integração de dados entre diferentes plataformas. Aqui estão as convenções recomendadas:

- **Campos**: Utilize snake_case para nomes de campos. Exemplo: `home_team`, `away_xg`. Isso facilita a leitura e a compreensão, especialmente em linguagens de programação que utilizam underscore para separar palavras.

  **Uso Correto**: `home_team`, `away_xg`

  **Uso Incorreto**: `homeTeam`, `awayXG`

- **Tabelas**: Utilize PascalCase para nomes de tabelas. Exemplo: `TeamStats`, `PlayerEvents`. Este padrão é comum em bancos de dados relacionais e ajuda a distinguir tabelas de campos.

  **Uso Correto**: `TeamStats`, `PlayerEvents`

  **Uso Incorreto**: `team_stats`, `player_events`

- **Constantes**: Utilize UPPER_CASE para constantes. Exemplo: `MAX_PLAYERS`. Isso indica que o valor não deve ser alterado durante a execução do programa.

  **Uso Correto**: `MAX_PLAYERS`

  **Uso Incorreto**: `max_players`, `MaxPlayers`

**Importância**: A padronização de nomenclatura evita confusões, facilita a manutenção do código e a integração de dados entre diferentes fontes. Por exemplo, ao integrar dados de FBref e WhoScored, a consistência nos nomes de campos e tabelas garante que as correspondências sejam feitas corretamente.

### 2.2 Tipos de Dados

A definição correta dos tipos de dados é crucial para a integridade e a eficiência do sistema de dados. Aqui estão os tipos de dados recomendados:

- **Identificadores**: Utilize UUID ou strings únicas para identificadores. Exemplo: `game_id`. UUIDs são ideais para garantir a unicidade global dos registros.

  **Exemplo**: `game_id` como UUID: `123e4567-e89b-12d3-a456-426614174000`

- **Datas**: Utilize o formato ISO 8601 (`YYYY-MM-DD`) para datas. Exemplo: `2023-05-15`. Este formato é universalmente reconhecido e evita ambiguidades.

  **Exemplo**: `date` como `2023-05-15`

- **Horários**: Utilize a notação `HH:MM` (24h) para horários. Exemplo: `14:30`. Isso evita confusões entre AM e PM.

  **Exemplo**: `time` como `14:30`

- **Números**: Utilize `Decimal(10,2)` para estatísticas que requerem precisão decimal. Exemplo: `xg` (Expected Goals) como `2.50`.

  **Exemplo**: `xg` como `2.50`

- **Booleanos**: Utilize 0/1 para representar valores booleanos. Exemplo: `is_home_team` como `1` para verdadeiro e `0` para falso.

  **Exemplo**: `is_home_team` como `1`

**Importância**: A escolha correta dos tipos de dados garante a integridade dos dados, evita erros de conversão e facilita a análise e a manipulação dos dados. Por exemplo, ao integrar dados de FBref e WhoScored, a consistência nos tipos de dados permite a correspondência correta entre as fontes.

### 2.3 Formatos de Arquivo

A escolha do formato de arquivo é fundamental para a eficiência na transferência e armazenamento de dados:

- **CSV**: Ideal para dados tabulares. Utilize codificação UTF-8 e vírgula (,) como delimitador. Exemplo:

  ```csv
  game_id,date,home_team,away_team
  123e4567-e89b-12d3-a456-426614174000,2023-05-15,Cruzeiro,Atlético-MG
  ```

- **JSON**: Ideal para dados estruturados e hierárquicos. Exemplo:

  ```json
  {
    "game_id": "123e4567-e89b-12d3-a456-426614174000",
    "date": "2023-05-15",
    "teams": {
      "home": "Cruzeiro",
      "away": "Atlético-MG"
    }
  }
  ```

**Importância**: A escolha do formato de arquivo correto facilita a leitura, a escrita e a integração de dados entre diferentes sistemas. CSV é simples e amplamente suportado, enquanto JSON permite estruturas de dados mais complexas e hierárquicas.

### 2.4 Validações Obrigatórias

Para garantir a qualidade e a integridade dos dados, são necessárias validações específicas:

- **Campos Obrigatórios**: Verifique a presença de campos críticos como `game_id`, `date`, `home_team`, `away_team`. Exemplo:

  ```python
  if not game_id or not date or not home_team or not away_team:
      raise ValueError("Campos obrigatórios ausentes")
  ```

- **Intervalos Permitidos**: Valide valores dentro de intervalos específicos. Exemplo: valores de posse de bola entre 0 e 100.

  ```python
  if not 0 <= possession <= 100:
      raise ValueError("Posse de bola fora do intervalo permitido")
  ```

- **Máscaras de Formatação**: Verifique se os dados seguem formatos específicos. Exemplo: data em `YYYY-MM-DD`.

  ```python
  if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
      raise ValueError("Formato de data inválido")
  ```

**Importância**: As validações garantem que os dados sejam consistentes e confiáveis, evitando erros de entrada e facilitando a integração entre diferentes fontes de dados.

## 3. Normalização

A normalização de dados é um processo crucial para garantir a consistência e a integridade dos dados coletados de diferentes fontes, como FBref e WhoScored. Aqui estão as diretrizes detalhadas para a normalização dos dados de futebol:

### Regras por Fonte de Dados

**FBref:**

- **Remoção de Caracteres Especiais**: Nomes de times devem ser limpos de caracteres especiais, como acentos, para evitar problemas de codificação e consistência. Exemplo: "Cruzeiro EC" deve ser padronizado para "Cruzeiro".

- **Conversão de Métricas**: Métricas como `xG` (Expected Goals) devem ser convertidas para o tipo `Decimal(10,2)` para garantir precisão decimal. Isso é importante para análises estatísticas e comparações entre jogos.

- **Alinhamento de Colunas**: As colunas devem ser alinhadas com o `data_dictionary.md` para garantir que os dados sejam consistentes com a estrutura definida. Isso inclui verificar se todas as colunas necessárias estão presentes e se os tipos de dados estão corretos.

**WhoScored:**

- **Consistência de Coordenadas**: As coordenadas de eventos devem ser padronizadas para um intervalo de 0 a 100, garantindo que todas as posições no campo sejam representadas de maneira uniforme.

- **Padronização de Nomes**: Nomes de jogadores e IDs de eventos devem ser padronizados para evitar duplicatas e inconsistências. Por exemplo, "Alan Patrick" deve ser o mesmo em todas as tabelas.

### Processos de Transformação

- **Limpeza de Caracteres Especiais e Espaços em Branco**: Remover caracteres especiais e espaços em branco desnecessários para garantir a consistência dos dados. Exemplo: "Marquinhos Gabriel" deve ser "MarquinhosGabriel".

- **Conversão Unificada de Tipos**: Converter tipos de dados para um formato unificado. Por exemplo, o minuto do evento deve ser sempre um inteiro.

- **Padronização de Formatos de Data e Hora**: Utilizar o formato ISO 8601 (`YYYY-MM-DD` para datas e `HH:MM` para horários) para garantir a consistência temporal.

### Tratamento de Valores Nulos/Ausentes

- **Estratégia por Tipo de Campo**:
  - `float` -> 0.0 ou `NaN` (Not a Number) para valores ausentes.
  - `string` -> vazio (`""`) para valores ausentes.
  - `boolean` -> 0 para falso e 1 para verdadeiro.

- **Definição de *Defaults***: Quando não houver dados, definir valores padrão. Por exemplo, `attendance = 0` quando não houver informações de público.

- **Regras de Preenchimento**: Quando possível, preencher valores ausentes a partir de colunas correlatas. Por exemplo, se um jogador não tiver minutos jogados registrados, mas estiver na escalação, pode-se inferir que jogou 90 minutos.

### Padronização de Unidades

- **Medidas**: Utilizar o Sistema Internacional (SI) para todas as medidas. Exemplo: distâncias em metros, tempo em minutos/segundos.

- **Tempo de Partida**: Padronizar o tempo de partida em minutos e segundos. Exemplo: 90 minutos para um jogo completo.

### Exemplos Práticos

- **FBref**:

  ```python
  # Remoção de caracteres especiais
  team_name = team_name.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

  # Conversão de métricas
  xg = Decimal(xg).quantize(Decimal('0.01'))
  ```

- **WhoScored**:

  ```python
  # Padronização de coordenadas
  if 'x' in event:
      event['x'] = min(max(event['x'], 0), 100)
  if 'y' in event:
      event['y'] = min(max(event['y'], 0), 100)

  # Padronização de nomes
  player_name = player_name.strip().replace(" ", "")
  ```

## 4. Integração de Dados

### 4.1 Estratégias de Mapeamento entre Fontes

#### 4.1.1 Identificadores Principais

**game_id**: Chave primária para correlação entre diferentes fontes

- **Objetivo**: Garantir correspondência unívoca entre registros de FBref e WhoScored
- **Características**:
  - Formato UUID (Universally Unique Identifier)
  - Gerado de forma consistente entre plataformas
  - Deve ser imutável durante todo o processo de integração

**Exemplo de Implementação**:

```python
def generate_game_id(home_team, away_team, date):
    unique_string = f"{home_team}_{away_team}_{date}"
    return hashlib.md5(unique_string.encode()).hexdigest()
```

#### 4.1.2 Chaves de Relacionamento

**player_id**:

- Consolidar identificadores de jogadores entre plataformas
- Critérios de unificação:
  1. Nome completo
  2. Data de nascimento
  3. Time atual
  4. Posição em campo

**team_id**:

- Padronizar nomes de times
- Remover variações (ex: "Cruzeiro EC" -> "Cruzeiro")
- Criar tabela de mapeamento centralizada

### 4.2 Processos de Correspondência

#### 4.2.1 Algoritmo de Matching

**Etapas de Correspondência**:

1. Identificação de chaves primárias
2. Validação de consistência
3. Tratamento de divergências
4. Registro de exceções

**Exemplo de Pseudocódigo**:

```python
def match_game_records(fbref_data, whoscored_data):
    matched_records = []
    for fbref_record in fbref_data:
        for whoscored_record in whoscored_data:
            if is_same_game(fbref_record, whoscored_record):
                merged_record = merge_records(fbref_record, whoscored_record)
                matched_records.append(merged_record)
    return matched_records
```

### 4.3 Resolução de Conflitos

#### 4.3.1 Critérios de Priorização

**Hierarquia de Fontes**:

1. WhoScored (prioridade para eventos e coordenadas)
2. FBref (prioridade para estatísticas agregadas)

**Exemplo de Resolução**:

- Divergência em número de chutes: priorizar dados do WhoScored
- Estatísticas de temporada: priorizar FBref

#### 4.3.2 Estratégias de Merge

**Regras para Combinação**:

- Preservar metadados originais
- Criar colunas com sufixo da fonte (`_fbref`, `_whoscored`)
- Registrar fonte original em metadados

**Exemplo de Merge**:

```python
def merge_player_stats(player1, player2):
    merged_stats = {
        'goals_fbref': player1.get('goals', 0),
        'goals_whoscored': player2.get('goals', 0),
        'goals_final': max(player1.get('goals', 0), player2.get('goals', 0))
    }
    return merged_stats
```

### 4.4 Validação de Integridade

#### 4.4.1 Checagens Automáticas

**Validações Obrigatórias**:

- Consistência de datas
- Correspondência de times
- Integridade de estatísticas

**Exemplo de Validação**:

```python
def validate_game_integrity(game_record):
    checks = [
        check_date_consistency(game_record),
        check_team_names(game_record),
        check_score_integrity(game_record)
    ]
    return all(checks)
```

### 4.5 Tratamento de Exceções

#### 4.5.1 Registro de Inconsistências

**Log de Erros**:

- Arquivo de log detalhado
- Registro de cada inconsistência
- Informações para auditoria posterior

**Estrutura de Log**:

```json
{
    "timestamp": "2023-05-20T14:30:00",
    "game_id": "unique_identifier",
    "source": "FBref/WhoScored",
    "error_type": "data_mismatch",
    "details": "Divergência no número de chutes"
}
```

### 4.6 Considerações Finais

**Princípios Fundamentais**:

- Transparência no processo de integração
- Preservação da rastreabilidade
- Minimização de perda de informação

**Recomendações**:

- Documentar cada decisão de merge
- Manter flexibilidade no processo
- Revisar periodicamente as estratégias de integração

## 5. Qualidade

### 5.1 Critérios de Validação

#### **Completude de Dados**

**Objetivo**: Garantir que todos os campos essenciais estejam preenchidos e sejam significativos.

**Validações Específicas**:

- **Campos Obrigatórios**:

  ```python
  def validar_completude(registro):
      campos_criticos = [
          'game_id',
          'date',
          'home_team',
          'away_team',
          'home_score',
          'away_score'
      ]

      for campo in campos_criticos:
          if pd.isna(registro[campo]) or registro[campo] == '':
              raise ValueError(f"Campo crítico '{campo}' não pode ser nulo")
  ```

- **Percentual Mínimo de Preenchimento**:

  ```python
  def verificar_preenchimento(dataframe, limite_minimo=0.9):
      preenchimento = dataframe.notna().mean()
      campos_incompletos = preenchimento[preenchimento < limite_minimo]

      if not campos_incompletos.empty:
          raise ValueError(f"Campos com baixo preenchimento: {campos_incompletos}")
  ```

#### **Consistência de Dados**

**Objetivo**: Assegurar que os dados sigam padrões e regras predefinidas.

**Validações Específicas**:

- **Padronização de Nomes**:

  ```python
  def normalizar_nome_time(nome):
      return re.sub(r'[^\w\s]', '', nome).lower().strip()

  def validar_consistencia_times(dataframe):
      times_validos = set(['cruzeiro', 'flamengo', 'palmeiras'])

      for time in dataframe['home_team']:
          if normalizar_nome_time(time) not in times_validos:
              raise ValueError(f"Time inválido: {time}")
  ```

- **Intervalos de Valores**:

  ```python
  def validar_intervalos(dataframe):
      validacoes = {
          'possession': (0, 100),
          'xg': (0, 5),
          'shots_on_target': (0, 30)
      }

      for coluna, (min_val, max_val) in validacoes.items():
          fora_intervalo = dataframe[
              (dataframe[coluna] < min_val) |
              (dataframe[coluna] > max_val)
          ]

          if not fora_intervalo.empty:
              raise ValueError(f"Valores fora do intervalo em {coluna}")
  ```

### 5.2 Processos de Verificação

#### **Validação Automática**

**Estratégias**:

- Execução de scripts de validação antes de cada inserção/atualização
- Logs detalhados de inconsistências
- Bloqueio de inserções com dados inválidos

**Exemplo de Implementação**:

```python
def validacao_pre_insercao(dados):
    try:
        # Validações sequenciais
        validar_completude(dados)
        validar_consistencia_times(dados)
        validar_intervalos(dados)

        # Se passar por todas, dados são considerados válidos
        return True

    except ValueError as erro:
        # Registra erro em log
        logging.error(f"Erro de validação: {erro}")
        return False
```

### 5.3 Tratamento de Exceções

#### **Estratégias de Correção**

1. **Correção Automática**:
   - Preencher valores nulos com defaults
   - Normalizar strings
   - Ajustar valores para dentro de intervalos permitidos

2. **Intervenção Manual**:
   - Gerar relatórios de inconsistências
   - Sinalizar registros para revisão humana

**Exemplo de Tratamento**:

```python
def tratar_excecoes(registro):
    # Preenche valores nulos
    registro['home_xg'] = registro['home_xg'] or 0
    registro['away_xg'] = registro['away_xg'] or 0

    # Normaliza nomes
    registro['home_team'] = normalizar_nome_time(registro['home_team'])

    # Ajusta intervalos
    registro['possession'] = max(0, min(registro['possession'], 100))

    return registro
```

### 5.4 Fluxo de Notificação

**Componentes**:

- Sistema de alertas para falhas críticas
- Relatórios periódicos de qualidade dos dados
- Mecanismo de rastreabilidade de correções

### 5.5 Considerações Finais

**Princípios Fundamentais**:

- Tolerância zero para dados comprometidos
- Transparência no processo de validação
- Flexibilidade para correções

**Recomendações**:

- Documentar cada regra de validação
- Revisar periodicamente as estratégias
- Manter histórico de correções

## 6. Definição das Tabelas Principais

### 6.1 Visão Geral das Tabelas Fundamentais

As tabelas principais representam a espinha dorsal do projeto de análise de dados do Campeonato Brasileiro, integrando informações das plataformas FBref e WhoScored. Cada tabela desempenha um papel crucial na compreensão abrangente do futebol brasileiro.

### 6.2 Tabelas Essenciais

#### 6.2.1 Cronograma de Jogos (schedule)

**Características Principais**:

- **Função**: Base para relacionar partidas e eventos
- **Colunas Críticas**:
  - `game_id`: Identificador único
  - `date`: Data do jogo
  - `home_team`: Time mandante
  - `away_team`: Time visitante
  - `home_score`: Placar do time mandante
  - `away_score`: Placar do time visitante

**Exemplo de Estrutura**:

```python
schedule = {
    'game_id': 'uuid_único',
    'date': '2024-04-14',
    'home_team': 'Cruzeiro',
    'away_team': 'Botafogo',
    'home_score': 3,
    'away_score': 2
}
```

#### 6.2.2 Estatísticas das Equipes (team_season_*)

**Categorias de Estatísticas**:

1. **Padrão (`standard`)**:
   - Desempenho geral da equipe
   - Métricas como gols, assistências, posse de bola

2. **Goleiros (`keeper`)**:
   - Estatísticas de defesas
   - Gols sofridos, defesas, expected goals

3. **Chutes (`shooting`)**:
   - Análise ofensiva
   - Chutes, gols, expected goals

4. **Passes (`passing`)**:
   - Precisão e progressão
   - Passes completados, distância progressiva

#### 6.2.3 Estatísticas Individuais (player_season_*)

**Tipos de Estatísticas**:

- **Padrão**: Desempenho geral do jogador
- **Defesa**: Desarmes, interceptações
- **Passes**: Precisão, progressão
- **Posse de Bola**: Conduções, dribles
- **Goleiros**: Desempenho específico para goleiros

#### 6.2.4 Estatísticas no Nível de Partida (team_match_*)

**Características**:

- Dados detalhados jogo a jogo
- Métricas granulares de desempenho
- Permite análise de variação de performance

#### 6.2.5 Eventos Avançados (WhoScored)

**Componentes**:

- Coordenadas de eventos
- Tipos de ações
- Detalhes de passes, chutes, dribles
- Informações posicionais

### 6.3 Estratégias de Integração

#### 6.3.1 Mapeamento de Identificadores

- **game_id**: Chave primária para correlação
- **player_id**: Identificador único de jogadores
- **team_id**: Identificador consistente entre plataformas

#### 6.3.2 Padronização de Métricas

- Conversão para tipos de dados uniformes
- Normalização de escalas e intervalos
- Tratamento de valores ausentes

### 6.4 Considerações Importantes

**Princípios Fundamentais**:

- Consistência entre fontes
- Preservação da granularidade dos dados
- Facilidade de integração e análise

**Recomendações**:

- Documentar mapeamentos
- Criar tabelas de referência
- Implementar validações rigorosas

### 6.5 Exemplo de Integração

```python
def integrar_estatisticas(fbref_data, whoscored_data):
    # Lógica de mapeamento e consolidação
    dados_integrados = {
        'game_id': mapear_game_id(fbref_data, whoscored_data),
        'metricas_consolidadas': {
            'passes': consolidar_passes(fbref_data, whoscored_data),
            'chutes': consolidar_chutes(fbref_data, whoscored_data)
        }
    }
    return dados_integrados
```

### 6.6 Conclusão

A definição cuidadosa das tabelas principais garante uma base sólida para análises complexas, permitindo insights profundos sobre o desempenho de equipes e jogadores no Campeonato Brasileiro.

## 7. Tabelas Derivadas e Combinação

### 7.1 Estratégias de Criação de Tabelas Derivadas

#### Tabela de Integração de Partidas

**Objetivo**: Consolidar informações de jogos do FBref e WhoScored em uma única estrutura unificada.

**Processo de Criação**:

```python
def criar_tabela_integracao_partidas(fbref_schedule, whoscored_schedule):
    tabela_integrada = pd.merge(
        fbref_schedule,
        whoscored_schedule,
        on=['game_id', 'date', 'home_team', 'away_team'],
        how='outer',
        suffixes=('_fbref', '_whoscored')
    )

    # Tratamento de campos duplicados
    tabela_integrada['home_score'] = tabela_integrada['home_score_fbref'].fillna(tabela_integrada['home_score_whoscored'])
    tabela_integrada['away_score'] = tabela_integrada['away_score_fbref'].fillna(tabela_integrada['away_score_whoscored'])

    return tabela_integrada
```

#### Tabela de Eventos Enriquecida

**Características**:

- Combinar eventos de WhoScored com estatísticas pontuais do FBref
- Adicionar campos calculados e métricas avançadas

**Implementação**:

```python
def enriquecer_eventos(events_whoscored, stats_fbref):
    eventos_enriquecidos = events_whoscored.copy()

    # Adicionar métricas do FBref
    eventos_enriquecidos['xG'] = stats_fbref['xG']
    eventos_enriquecidos['expected_assist'] = stats_fbref['xAG']
    eventos_enriquecidos['possession'] = stats_fbref['possession']

    return eventos_enriquecidos
```

### 7.2 Métricas Compostas

#### Tabela de Performance Avançada

**Desenvolvimento de Índices Compostos**:

```python
def calcular_indice_performance(dados_chutes, dados_posse, dados_finalizacao):
    indice_performance = {
        'eficiencia_ataque': (
            dados_chutes['shots_on_target'] / dados_chutes['total_shots']
        ),
        'progressao_jogo': (
            dados_posse['progressive_carries'] +
            dados_posse['progressive_passes']
        ),
        'criatividade_ofensiva': (
            dados_finalizacao['key_passes'] *
            dados_finalizacao['expected_assists']
        )
    }

    return indice_performance
```

### 7.3 Considerações para Combinação de Dados

**Princípios Fundamentais**:

- Preservar a granularidade original dos dados
- Minimizar perda de informação
- Garantir consistência entre fontes

**Estratégias de Merge**:

1. Identificadores únicos (`game_id`, `player_id`)
2. Correspondência por data e times
3. Tratamento de campos nulos
4. Priorização de fontes

### 7.4 Tratamento de Campos Complexos

**Exemplo de Normalização**:

```python
def normalizar_campos_multi_indice(dataframe):
    # Remover hierarquias complexas
    dataframe.columns = [
        '_'.join(col).strip()
        for col in dataframe.columns.values
    ]

    return dataframe
```

### 7.5 Validações de Integridade

**Checagens Automáticas**:

```python
def validar_tabela_derivada(tabela_derivada):
    validacoes = [
        # Verificar campos obrigatórios
        tabela_derivada['game_id'].notna().all(),

        # Checar intervalos de valores
        (tabela_derivada['xG'] >= 0).all(),
        (tabela_derivada['xG'] <= 5).all(),

        # Consistência entre colunas
        tabela_derivada['home_score'] >= 0,
        tabela_derivada['away_score'] >= 0
    ]

    return all(validacoes)
```

### 7.6 Conclusão

A criação de tabelas derivadas é um processo crítico que requer:

- Atenção aos detalhes
- Compreensão profunda das fontes de dados
- Implementação de validações rigorosas

**Recomendações Finais**:

- Documentar cada transformação
- Manter flexibilidade no processo
- Validar constantemente a integridade dos dados

## 8. Padronização Avançada de Colunas

### 8.1 Estratégias de Normalização de Campos Complexos

#### Tratamento de Multi-Índices

**Objetivo**: Simplificar estruturas de dados complexas e garantir consistência na representação.

**Exemplo de Implementação**:

```python
def normalizar_multi_indice(dataframe):
    # Achatamento de colunas multi-índice
    dataframe.columns = [
        '_'.join(str(col).strip() for col in col_tuple)
        if isinstance(col_tuple, tuple)
        else str(col_tuple)
        for col_tuple in dataframe.columns
    ]
    return dataframe
```

#### Estratégias de Conversão

**Técnicas de Transformação**:

1. **Renomeação Consistente**
2. **Conversão de Tipos**
3. **Padronização de Formatos**

**Exemplo Prático**:

```python
def padronizar_colunas(df):
    mapeamento_colunas = {
        'home_xG': 'expected_goals_home',
        'away_xG': 'expected_goals_away',
        'possession': 'ball_possession_percentage'
    }

    # Renomear colunas
    df.rename(columns=mapeamento_colunas, inplace=True)

    # Conversão de tipos
    conversoes = {
        'expected_goals_home': float,
        'expected_goals_away': float,
        'ball_possession_percentage': float
    }

    for coluna, tipo in conversoes.items():
        df[coluna] = df[coluna].astype(tipo)

    return df
```

### 8.2 Tratamento de Colunas Aninhadas

**Estratégias de Desnormalização**:

- Expandir colunas complexas
- Criar colunas simples e diretas
- Preservar informações originais

**Exemplo de Implementação**:

```python
def desaninhar_colunas(dataframe):
    # Expandir colunas de eventos
    if 'qualifiers' in dataframe.columns:
        # Extrair informações específicas dos qualificadores
        dataframe['pass_angle'] = dataframe['qualifiers'].apply(
            lambda x: next((q['value'] for q in x if q.get('type', {}).get('displayName') == 'Angle'), None)
        )

        dataframe['pass_zone'] = dataframe['qualifiers'].apply(
            lambda x: next((q['value'] for q in x if q.get('type', {}).get('displayName') == 'Zone'), None)
        )

    return dataframe
```

### 8.3 Validações de Integridade

**Checagens Automáticas**:

```python
def validar_colunas_normalizadas(dataframe):
    validacoes = [
        # Verificar tipos de dados
        dataframe.dtypes.apply(lambda x: x in [float, int, str]),

        # Checar valores nulos
        dataframe.isnull().sum() == 0,

        # Intervalos de valores
        (dataframe['expected_goals_home'] >= 0).all(),
        (dataframe['expected_goals_home'] <= 5).all()
    ]

    return all(validacoes)
```

### 8.4 Considerações Finais

**Princípios Fundamentais**:

- Simplicidade na representação
- Preservação de informações originais
- Facilidade de manipulação

**Recomendações**:

- Documentar cada transformação
- Manter flexibilidade no processo
- Validar constantemente a integridade dos dados

### Exemplo Completo de Aplicação

```python
def processar_dados_futebol(df_fbref, df_whoscored):
    # Normalização de colunas
    df_fbref = normalizar_multi_indice(df_fbref)
    df_whoscored = normalizar_multi_indice(df_whoscored)

    # Padronização
    df_fbref = padronizar_colunas(df_fbref)
    df_whoscored = padronizar_colunas(df_whoscored)

    # Desnormalização
    df_fbref = desaninhar_colunas(df_fbref)
    df_whoscored = desaninhar_colunas(df_whoscored)

    # Validação
    assert validar_colunas_normalizadas(df_fbref)
    assert validar_colunas_normalizadas(df_whoscored)

    return df_fbref, df_whoscored
```

## 9. Tratamento de Índices e Multi-Índices

### 9.1 Estratégias de Simplificação de Estruturas Complexas

#### Princípios Fundamentais

**Objetivo**: Transformar estruturas de dados hierárquicas em formatos simples e diretamente manipuláveis.

**Estratégias de Desnormalização**:

```python
def desanimar_multi_indice(dataframe):
    # Achatamento de colunas multi-índice
    dataframe.columns = [
        '_'.join(str(nivel).strip() for nivel in col_tuple)
        if isinstance(col_tuple, tuple)
        else str(col_tuple)
        for col_tuple in dataframe.columns
    ]
    return dataframe
```

#### Técnicas de Conversão

**Exemplos de Transformação**:

1. **Renomeação Hierárquica**
2. **Simplificação de Níveis**
3. **Padronização de Nomes**

```python
def padronizar_colunas_complexas(df):
    # Mapeamento de colunas hierárquicas
    mapeamento = {
        ('passes', 'total'): 'passes_total',
        ('passes', 'curtos'): 'passes_curtos',
        ('chutes', 'gols'): 'chutes_gols'
    }

    # Renomear colunas
    df.columns = [
        mapeamento.get(col, '_'.join(map(str, col)) if isinstance(col, tuple) else col)
        for col in df.columns
    ]

    return df
```

### 9.2 Validação de Estruturas Simplificadas

**Checagens Automáticas**:

```python
def validar_estrutura_simplificada(dataframe):
    validacoes = [
        # Verificar ausência de multi-índices
        len(dataframe.columns.names) <= 1,

        # Garantir nomes de colunas únicos
        len(dataframe.columns) == len(set(dataframe.columns)),

        # Tipos de dados consistentes
        all(
            df[col].dtype in [float, int, str, object]
            for col in dataframe.columns
        )
    ]

    return all(validacoes)
```

### 9.3 Considerações Específicas para Dados de Futebol

**Exemplos de Aplicação**:

```python
def processar_dados_futebol(df_fbref, df_whoscored):
    # Desanimação de multi-índices
    df_fbref = desanimar_multi_indice(df_fbref)
    df_whoscored = desanimar_multi_indice(df_whoscored)

    # Padronização de colunas
    df_fbref = padronizar_colunas_complexas(df_fbref)
    df_whoscored = padronizar_colunas_complexas(df_whoscored)

    # Validação das estruturas
    assert validar_estrutura_simplificada(df_fbref)
    assert validar_estrutura_simplificada(df_whoscored)

    return df_fbref, df_whoscored
```

### 9.4 Recomendações Finais

**Princípios Fundamentais**:

- Simplicidade na representação
- Preservação da informação original
- Facilidade de manipulação

**Boas Práticas**:

1. Documentar cada transformação
2. Manter flexibilidade no processo
3. Validar constantemente a integridade dos dados

### 9.5 Casos Especiais

**Tratamento de Índices Específicos**:

- Manter `game_id` como chave principal
- Preservar informações de `player_id` e `team_id`
- Garantir consistência entre fontes

### 9.6 Conclusão

O tratamento de índices e multi-índices é um processo crítico que requer:

- Atenção aos detalhes
- Compreensão profunda da estrutura dos dados
- Implementação de transformações consistentes

**Exemplo Completo de Aplicação**:

```python
def integrar_dados_futebol(df_fbref, df_whoscored):
    # Tratamento de multi-índices
    df_processado_fbref = processar_dados_futebol(df_fbref)[0]
    df_processado_whoscored = processar_dados_futebol(df_whoscored)[0]

    # Merge baseado em identificadores
    df_integrado = pd.merge(
        df_processado_fbref,
        df_processado_whoscored,
        on=['game_id', 'player_id'],
        how='outer'
    )

    return df_integrado
```

## Controle de Versão

Versão: 1.2
Data: 2025-01-15
Autor: Vinicius P Barbosa
