```markdown
# cSpell:disable
```

# Dicionário de Dados - Campeonato Brasileiro Série A 2024

Este documento contém informações detalhadas sobre as tabelas e dados coletados para o Campeonato Brasileiro Série A de 2024, utilizando as plataformas FBref e WhoScored. O objetivo é fornecer uma referência completa para pesquisadores, analistas e entusiastas do futebol que desejam trabalhar com esses dados.

O dicionário está organizado em duas seções principais:

1. Tabelas do FBref
2. Tabelas do WhoScored

Cada seção inclui uma lista completa das tabelas disponíveis, seguida por descrições detalhadas de cada tabela, incluindo suas colunas, tipos de dados e exemplos de valores.

Este documento serve como um guia essencial para entender a estrutura e o conteúdo dos dados coletados, facilitando análises estatísticas, visualizações e pesquisas sobre o futebol brasileiro.

## Tabelas do FBref

# Dicionário de Colunas FBref

| ID                        | Categoria         | Nome Col.      | Tipo           | tabela                                 | Descrição                                                                             |
| :------------------------ | :---------------- | :------------- | :------------- | :------------------------------------- | :------------------------------------------------------------------------------------ |
| event_type                | nan               | event_type     | object         | events                                 | Tipo de evento ocorrido na partida                                                    |
| minute                    | nan               | minute         | object         | events                                 | Minuto em que o evento ocorreu                                                        |
| player1                   | nan               | player1        | object         | events                                 | Jogador principal envolvido no evento                                                 |
| player2                   | nan               | player2        | object         | events                                 | Jogador secundário envolvido no evento (quando aplicável)                             |
| score                     | nan               | score          | object         | events                                 | Placar da partida no momento do evento                                                |
| team                      | nan               | team           | object         | events                                 | Time envolvido no evento                                                              |
| is_starter                | nan               | is_starter     | object         | lineups                                | Indica se o jogador é titular                                                         |
| jersey_number             | nan               | jersey_number  | Int64          | lineups                                | Número da camisa do jogador                                                           |
| minutes_played            | nan               | minutes_played | Int64          | lineups                                | Minutos jogados pelo jogador                                                          |
| player                    | nan               | player         | string         | lineups                                | Nome do jogador                                                                       |
| position                  | nan               | position       | string         | lineups                                | Posição do jogador                                                                    |
| team                      | nan               | team           | object         | lineups                                | Time envolvido no evento                                                              |
| Clr                       | nan               | Clr            | Int64          | player_match_defense                   | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | player_match_defense                   | Erros que resultaram em finalização do adversário                                     |
| Int                       | nan               | Int            | Int64          | player_match_defense                   | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | player_match_defense                   | Soma de desarmes e interceptações                                                     |
| age                       | nan               | age            | string         | player_match_defense                   | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_defense                   | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_defense                   | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_defense                   | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_defense                   | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_defense                   | Posição do jogador (abreviada)                                                        |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | player_match_defense                   | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | player_match_defense                   | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | player_match_defense                   | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | player_match_defense                   | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | player_match_defense                   | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | player_match_defense                   | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | player_match_defense                   | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | player_match_defense                   | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | player_match_defense                   | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | player_match_defense                   | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | player_match_defense                   | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | player_match_defense                   | Desarmes bem-sucedidos                                                                |
| age                       | nan               | age            | string         | player_match_keepers                   | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_keepers                   | Identificador único da partida                                                        |
| min                       | nan               | min            | Int64          | player_match_keepers                   | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_keepers                   | Nacionalidade do jogador                                                              |
| Crosses_Opp               | Crosses           | Opp            | Int64          | player_match_keepers                   | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | player_match_keepers                   | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Int64          | player_match_keepers                   | Porcentagem de cruzamentos interceptados                                              |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | player_match_keepers                   | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | player_match_keepers                   | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | player_match_keepers                   | Porcentagem de tiros de meta longos                                                   |
| Launched_Att              | Launched          | Att            | Int64          | player_match_keepers                   | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | player_match_keepers                   | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | player_match_keepers                   | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | player_match_keepers                   | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | player_match_keepers                   | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | player_match_keepers                   | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | player_match_keepers                   | Passes realizados com as mãos                                                         |
| Shot Stopping_GA          | Shot Stopping     | GA             | Int64          | player_match_keepers                   | Gols sofridos                                                                         |
| Shot Stopping_PSxG        | Shot Stopping     | PSxG           | Float64        | player_match_keepers                   | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Shot Stopping_Save%       | Shot Stopping     | Save%          | Float64        | player_match_keepers                   | Porcentagem de defesas realizadas                                                     |
| Shot Stopping_Saves       | Shot Stopping     | Saves          | Int64          | player_match_keepers                   | Defesas realizadas                                                                    |
| Shot Stopping_SoTA        | Shot Stopping     | SoTA           | Int64          | player_match_keepers                   | Chutes no alvo enfrentados                                                            |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | player_match_keepers                   | Ações defensivas fora da área                                                         |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | player_match_keepers                   | Distância média das ações                                                             |
| age                       | nan               | age            | string         | player_match_misc                      | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_misc                      | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_misc                      | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_misc                      | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_misc                      | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_misc                      | Posição do jogador (abreviada)                                                        |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | player_match_misc                      | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | player_match_misc                      | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | player_match_misc                      | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | player_match_misc                      | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | player_match_misc                      | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | player_match_misc                      | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | player_match_misc                      | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | player_match_misc                      | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | player_match_misc                      | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | player_match_misc                      | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | player_match_misc                      | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | player_match_misc                      | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | player_match_misc                      | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | player_match_misc                      | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | player_match_misc                      | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | player_match_misc                      | Desarmes bem-sucedidos                                                                |
| 1/3                       | nan               | 1/3            | Int64          | player_match_passing                   | Passes para o terço final do campo                                                    |
| Ast                       | nan               | Ast            | Int64          | player_match_passing                   | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | player_match_passing                   | Cruzamentos para área de pênalti                                                      |
| KP                        | nan               | KP             | Int64          | player_match_passing                   | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | player_match_passing                   | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | player_match_passing                   | Passes progressivos realizados                                                        |
| age                       | nan               | age            | string         | player_match_passing                   | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_passing                   | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_passing                   | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_passing                   | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_passing                   | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_passing                   | Posição do jogador (abreviada)                                                        |
| xA                        | nan               | xA             | Float64        | player_match_passing                   | Expected Assists                                                                      |
| xAG                       | nan               | xAG            | Float64        | player_match_passing                   | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Long_Att                  | Long              | Att            | Int64          | player_match_passing                   | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | player_match_passing                   | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | player_match_passing                   | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | player_match_passing                   | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | player_match_passing                   | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | player_match_passing                   | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | player_match_passing                   | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | player_match_passing                   | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | player_match_passing                   | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | player_match_passing                   | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | player_match_passing                   | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | player_match_passing                   | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | player_match_passing                   | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | player_match_passing                   | Distância total percorrida                                                            |
| Att                       | nan               | Att            | Int64          | player_match_passing_types             | Tentativas de ação (contexto específico da categoria)                                 |
| age                       | nan               | age            | string         | player_match_passing_types             | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_passing_types             | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_passing_types             | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_passing_types             | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_passing_types             | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_passing_types             | Posição do jogador (abreviada)                                                        |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | player_match_passing_types             | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | player_match_passing_types             | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | player_match_passing_types             | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | player_match_passing_types             | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | player_match_passing_types             | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | player_match_passing_types             | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | player_match_passing_types             | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | player_match_passing_types             | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | player_match_passing_types             | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | player_match_passing_types             | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | player_match_passing_types             | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | player_match_passing_types             | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | player_match_passing_types             | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | player_match_passing_types             | Arremessos laterais                                                                   |
| age                       | nan               | age            | string         | player_match_possession                | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_possession                | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_possession                | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_possession                | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_possession                | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_possession                | Posição do jogador (abreviada)                                                        |
| Carries_1/3               | Carries           | 1/3            | Int64          | player_match_possession                | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | player_match_possession                | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | player_match_possession                | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | player_match_possession                | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | player_match_possession                | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | player_match_possession                | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | player_match_possession                | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | player_match_possession                | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | player_match_possession                | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | player_match_possession                | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | player_match_possession                | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | player_match_possession                | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | player_match_possession                | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | player_match_possession                | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | player_match_possession                | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | player_match_possession                | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | player_match_possession                | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | player_match_possession                | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | player_match_possession                | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | player_match_possession                | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | player_match_possession                | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | player_match_possession                | Total de toques na bola                                                               |
| age                       | nan               | age            | string         | player_match_summary                   | Idade do jogador                                                                      |
| game_id                   | nan               | game_id        | object         | player_match_summary                   | Identificador único da partida                                                        |
| jersey_number             | nan               | jersey_number  | Int64          | player_match_summary                   | Número da camisa do jogador                                                           |
| min                       | nan               | min            | Int64          | player_match_summary                   | Minutos jogados                                                                       |
| nation                    | nan               | nation         | string         | player_match_summary                   | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_match_summary                   | Posição do jogador (abreviada)                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | player_match_summary                   | Conduções de bola realizadas                                                          |
| Carries_PrgC              | Carries           | PrgC           | Int64          | player_match_summary                   | Conduções progressivas                                                                |
| Expected_npxG             | Expected          | npxG           | Float64        | player_match_summary                   | Expected Goals excluindo pênaltis                                                     |
| Expected_xAG              | Expected          | xAG            | Float64        | player_match_summary                   | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_xG               | Expected          | xG             | Float64        | player_match_summary                   | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Passes_Att                | Passes            | Att            | Int64          | player_match_summary                   | Tentativas de ação (contexto específico da categoria)                                 |
| Passes_Cmp                | Passes            | Cmp            | Int64          | player_match_summary                   | Passes completados                                                                    |
| Passes_Cmp%               | Passes            | Cmp%           | Float64        | player_match_summary                   | Porcentagem de passes completados                                                     |
| Passes_PrgP               | Passes            | PrgP           | Int64          | player_match_summary                   | Passes progressivos realizados                                                        |
| Performance_Ast           | Performance       | Ast            | Int64          | player_match_summary                   | Assistências para gol                                                                 |
| Performance_Blocks        | Performance       | Blocks         | Int64          | player_match_summary                   | Total de bloqueios realizados                                                         |
| Performance_CrdR          | Performance       | CrdR           | Int64          | player_match_summary                   | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | player_match_summary                   | Cartões amarelos                                                                      |
| Performance_Gls           | Performance       | Gls            | Int64          | player_match_summary                   | Gols marcados                                                                         |
| Performance_Int           | Performance       | Int            | Int64          | player_match_summary                   | Interceptações realizadas                                                             |
| Performance_PK            | Performance       | PK             | Int64          | player_match_summary                   | Pênaltis convertidos                                                                  |
| Performance_PKatt         | Performance       | PKatt          | Int64          | player_match_summary                   | Pênaltis cobrados                                                                     |
| Performance_Sh            | Performance       | Sh             | Int64          | player_match_summary                   | Chutes bloqueados                                                                     |
| Performance_SoT           | Performance       | SoT            | Int64          | player_match_summary                   | Chutes no alvo                                                                        |
| Performance_Tkl           | Performance       | Tkl            | Int64          | player_match_summary                   | Desarmes realizados                                                                   |
| Performance_Touches       | Performance       | Touches        | Int64          | player_match_summary                   | Total de toques na bola                                                               |
| SCA_GCA                   | SCA               | GCA            | Int64          | player_match_summary                   | Ações que geraram gols                                                                |
| SCA_SCA                   | SCA               | SCA            | Int64          | player_match_summary                   | Ações que geraram chutes                                                              |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | player_match_summary                   | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | player_match_summary                   | Dribles bem-sucedidos                                                                 |
| 90s                       | nan               | 90s            | Float64        | player_season_defense                  | Número de partidas completas (90 minutos)                                             |
| Clr                       | nan               | Clr            | Int64          | player_season_defense                  | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | player_season_defense                  | Erros que resultaram em finalização do adversário                                     |
| Int                       | nan               | Int            | Int64          | player_season_defense                  | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | player_season_defense                  | Soma de desarmes e interceptações                                                     |
| age                       | nan               | age            | Int64          | player_season_defense                  | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_defense                  | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_defense                  | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_defense                  | Posição do jogador (abreviada)                                                        |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | player_season_defense                  | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | player_season_defense                  | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | player_season_defense                  | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | player_season_defense                  | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | player_season_defense                  | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | player_season_defense                  | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | player_season_defense                  | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | player_season_defense                  | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | player_season_defense                  | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | player_season_defense                  | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | player_season_defense                  | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | player_season_defense                  | Desarmes bem-sucedidos                                                                |
| 90s                       | nan               | 90s            | Float64        | player_season_goal_shot_creation       | Número de partidas completas (90 minutos)                                             |
| age                       | nan               | age            | Int64          | player_season_goal_shot_creation       | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_goal_shot_creation       | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_goal_shot_creation       | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_goal_shot_creation       | Posição do jogador (abreviada)                                                        |
| GCA_GCA                   | GCA               | GCA            | Int64          | player_season_goal_shot_creation       | Ações que geraram gols                                                                |
| GCA_GCA90                 | GCA               | GCA90          | Float64        | player_season_goal_shot_creation       | Ações que geraram gols por 90 minutos                                                 |
| GCA Types_Def             | GCA Types         | Def            | Int64          | player_season_goal_shot_creation       | Ações defensivas que geraram gol                                                      |
| GCA Types_Fld             | GCA Types         | Fld            | Int64          | player_season_goal_shot_creation       | Faltas sofridas                                                                       |
| GCA Types_PassDead        | GCA Types         | PassDead       | Int64          | player_season_goal_shot_creation       | Ações de bola parada para criação de chance                                           |
| GCA Types_PassLive        | GCA Types         | PassLive       | Int64          | player_season_goal_shot_creation       | Ações de bola em movimento para criação de chance                                     |
| GCA Types_Sh              | GCA Types         | Sh             | Int64          | player_season_goal_shot_creation       | Chutes bloqueados                                                                     |
| GCA Types_TO              | GCA Types         | TO             | Int64          | player_season_goal_shot_creation       | Dribles que geraram chance                                                            |
| SCA_SCA                   | SCA               | SCA            | Int64          | player_season_goal_shot_creation       | Ações que geraram chutes                                                              |
| SCA_SCA90                 | SCA               | SCA90          | Float64        | player_season_goal_shot_creation       | Ações que geraram chutes por 90 minutos                                               |
| SCA Types_Def             | SCA Types         | Def            | Int64          | player_season_goal_shot_creation       | Ações defensivas que geraram chute                                                    |
| SCA Types_Fld             | SCA Types         | Fld            | Int64          | player_season_goal_shot_creation       | Faltas sofridas                                                                       |
| SCA Types_PassDead        | SCA Types         | PassDead       | Int64          | player_season_goal_shot_creation       | Ações de bola parada para criação de chance                                           |
| SCA Types_PassLive        | SCA Types         | PassLive       | Int64          | player_season_goal_shot_creation       | Ações de bola em movimento para criação de chance                                     |
| SCA Types_Sh              | SCA Types         | Sh             | Int64          | player_season_goal_shot_creation       | Chutes bloqueados                                                                     |
| SCA Types_TO              | SCA Types         | TO             | Int64          | player_season_goal_shot_creation       | Dribles que geraram chance                                                            |
| age                       | nan               | age            | Int64          | player_season_keeper                   | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_keeper                   | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_keeper                   | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_keeper                   | Posição do jogador (abreviada)                                                        |
| Penalty Kicks_PKA         | Penalty Kicks     | PKA            | Int64          | player_season_keeper                   | Pênaltis convertidos                                                                  |
| Penalty Kicks_PKatt       | Penalty Kicks     | PKatt          | Int64          | player_season_keeper                   | Pênaltis cobrados                                                                     |
| Penalty Kicks_PKm         | Penalty Kicks     | PKm            | Int64          | player_season_keeper                   | Pênaltis perdidos                                                                     |
| Penalty Kicks_PKsv        | Penalty Kicks     | PKsv           | Int64          | player_season_keeper                   | Pênaltis defendidos                                                                   |
| Penalty Kicks_Save%       | Penalty Kicks     | Save%          | Float64        | player_season_keeper                   | Porcentagem de defesas realizadas                                                     |
| Performance_CS            | Performance       | CS             | Int64          | player_season_keeper                   | Clean sheets (jogos sem sofrer gol)                                                   |
| Performance_CS%           | Performance       | CS%            | Float64        | player_season_keeper                   | Porcentagem de jogos sem sofrer gol                                                   |
| Performance_D             | Performance       | D              | Int64          | player_season_keeper                   | Empates                                                                               |
| Performance_GA            | Performance       | GA             | Int64          | player_season_keeper                   | Gols sofridos                                                                         |
| Performance_GA90          | Performance       | GA90           | Float64        | player_season_keeper                   | Gols sofridos por 90 minutos                                                          |
| Performance_L             | Performance       | L              | Int64          | player_season_keeper                   | Derrotas                                                                              |
| Performance_Save%         | Performance       | Save%          | Float64        | player_season_keeper                   | Porcentagem de defesas realizadas                                                     |
| Performance_Saves         | Performance       | Saves          | Int64          | player_season_keeper                   | Defesas realizadas                                                                    |
| Performance_SoTA          | Performance       | SoTA           | Int64          | player_season_keeper                   | Chutes no alvo enfrentados                                                            |
| Performance_W             | Performance       | W              | Int64          | player_season_keeper                   | Vitórias                                                                              |
| Playing Time_90s          | Playing Time      | 90s            | Float64        | player_season_keeper                   | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | player_season_keeper                   | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | player_season_keeper                   | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | player_season_keeper                   | Partidas iniciadas como titular                                                       |
| 90s                       | nan               | 90s            | Float64        | player_season_keeper_adv               | Número de partidas completas (90 minutos)                                             |
| age                       | nan               | age            | Int64          | player_season_keeper_adv               | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_keeper_adv               | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_keeper_adv               | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_keeper_adv               | Posição do jogador (abreviada)                                                        |
| Crosses_Opp               | Crosses           | Opp            | Int64          | player_season_keeper_adv               | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | player_season_keeper_adv               | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Float64        | player_season_keeper_adv               | Porcentagem de cruzamentos interceptados                                              |
| Expected_/90              | Expected          | /90            | Float64        | player_season_keeper_adv               | Métrica normalizada por 90 minutos                                                    |
| Expected_PSxG             | Expected          | PSxG           | Float64        | player_season_keeper_adv               | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Expected_PSxG+/-          | Expected          | PSxG+/-        | Float64        | player_season_keeper_adv               | Diferença entre gols sofridos e PSxG                                                  |
| Expected_PSxG/SoT         | Expected          | PSxG/SoT       | Float64        | player_season_keeper_adv               | PSxG por chute no alvo                                                                |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | player_season_keeper_adv               | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | player_season_keeper_adv               | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | player_season_keeper_adv               | Porcentagem de tiros de meta longos                                                   |
| Goals_CK                  | Goals             | CK             | Int64          | player_season_keeper_adv               | Cobranças de escanteio                                                                |
| Goals_FK                  | Goals             | FK             | Int64          | player_season_keeper_adv               | Cobranças de falta                                                                    |
| Goals_GA                  | Goals             | GA             | Int64          | player_season_keeper_adv               | Gols sofridos                                                                         |
| Goals_OG                  | Goals             | OG             | Int64          | player_season_keeper_adv               | Gols contra                                                                           |
| Goals_PKA                 | Goals             | PKA            | Int64          | player_season_keeper_adv               | Pênaltis convertidos                                                                  |
| Launched_Att              | Launched          | Att            | Int64          | player_season_keeper_adv               | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | player_season_keeper_adv               | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | player_season_keeper_adv               | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | player_season_keeper_adv               | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | player_season_keeper_adv               | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | player_season_keeper_adv               | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | player_season_keeper_adv               | Passes realizados com as mãos                                                         |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | player_season_keeper_adv               | Ações defensivas fora da área                                                         |
| Sweeper_#OPA/90           | Sweeper           | #OPA/90        | Float64        | player_season_keeper_adv               | Ações defensivas fora da área por 90 minutos                                          |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | player_season_keeper_adv               | Distância média das ações                                                             |
| 90s                       | nan               | 90s            | Float64        | player_season_misc                     | Número de partidas completas (90 minutos)                                             |
| age                       | nan               | age            | Int64          | player_season_misc                     | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_misc                     | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_misc                     | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_misc                     | Posição do jogador (abreviada)                                                        |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | player_season_misc                     | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | player_season_misc                     | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | player_season_misc                     | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | player_season_misc                     | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | player_season_misc                     | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | player_season_misc                     | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | player_season_misc                     | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | player_season_misc                     | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | player_season_misc                     | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | player_season_misc                     | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | player_season_misc                     | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | player_season_misc                     | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | player_season_misc                     | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | player_season_misc                     | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | player_season_misc                     | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | player_season_misc                     | Desarmes bem-sucedidos                                                                |
| 1/3                       | nan               | 1/3            | Int64          | player_season_passing                  | Passes para o terço final do campo                                                    |
| 90s                       | nan               | 90s            | Float64        | player_season_passing                  | Número de partidas completas (90 minutos)                                             |
| Ast                       | nan               | Ast            | Int64          | player_season_passing                  | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | player_season_passing                  | Cruzamentos para área de pênalti                                                      |
| KP                        | nan               | KP             | Int64          | player_season_passing                  | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | player_season_passing                  | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | player_season_passing                  | Passes progressivos realizados                                                        |
| age                       | nan               | age            | Int64          | player_season_passing                  | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_passing                  | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_passing                  | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_passing                  | Posição do jogador (abreviada)                                                        |
| xAG                       | nan               | xAG            | Float64        | player_season_passing                  | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_A-xAG            | Expected          | A-xAG          | Float64        | player_season_passing                  | Diferença entre assistências e expectativas de assistência esperadas                  |
| Expected_xA               | Expected          | xA             | Float64        | player_season_passing                  | Expected Assists                                                                      |
| Long_Att                  | Long              | Att            | Int64          | player_season_passing                  | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | player_season_passing                  | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | player_season_passing                  | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | player_season_passing                  | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | player_season_passing                  | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | player_season_passing                  | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | player_season_passing                  | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | player_season_passing                  | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | player_season_passing                  | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | player_season_passing                  | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | player_season_passing                  | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | player_season_passing                  | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | player_season_passing                  | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | player_season_passing                  | Distância total percorrida                                                            |
| 90s                       | nan               | 90s            | Float64        | player_season_passing_types            | Número de partidas completas (90 minutos)                                             |
| Att                       | nan               | Att            | Int64          | player_season_passing_types            | Tentativas de ação (contexto específico da categoria)                                 |
| age                       | nan               | age            | Int64          | player_season_passing_types            | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_passing_types            | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_passing_types            | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_passing_types            | Posição do jogador (abreviada)                                                        |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | player_season_passing_types            | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | player_season_passing_types            | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | player_season_passing_types            | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | player_season_passing_types            | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | player_season_passing_types            | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | player_season_passing_types            | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | player_season_passing_types            | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | player_season_passing_types            | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | player_season_passing_types            | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | player_season_passing_types            | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | player_season_passing_types            | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | player_season_passing_types            | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | player_season_passing_types            | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | player_season_passing_types            | Arremessos laterais                                                                   |
| age                       | nan               | age            | Int64          | player_season_playing_time             | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_playing_time             | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_playing_time             | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_playing_time             | Posição do jogador (abreviada)                                                        |
| Playing Time_90s          | Playing Time      | 90s            | Float64        | player_season_playing_time             | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | player_season_playing_time             | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | player_season_playing_time             | Minutos jogados                                                                       |
| Playing Time_Min%         | Playing Time      | Min%           | Float64        | player_season_playing_time             | Porcentagem de minutos possíveis jogados                                              |
| Playing Time_Mn/MP        | Playing Time      | Mn/MP          | Int64          | player_season_playing_time             | Média de minutos por partida                                                          |
| Starts_Compl              | Starts            | Compl          | Int64          | player_season_playing_time             | Partidas completas                                                                    |
| Starts_Mn/Start           | Starts            | Mn/Start       | Int64          | player_season_playing_time             | Média de minutos por titularidade                                                     |
| Starts_Starts             | Starts            | Starts         | Int64          | player_season_playing_time             | Partidas iniciadas como titular                                                       |
| Subs_Mn/Sub               | Subs              | Mn/Sub         | Int64          | player_season_playing_time             | Média de minutos como substituto                                                      |
| Subs_Subs                 | Subs              | Subs           | Int64          | player_season_playing_time             | Entradas como substituto                                                              |
| Subs_unSub                | Subs              | unSub          | Int64          | player_season_playing_time             | Jogos não utilizados como substituto                                                  |
| Team Success_+/-          | Team Success      | +/-            | Int64          | player_season_playing_time             | Saldo de gols com o jogador em campo                                                  |
| Team Success_+/-90        | Team Success      | +/-90          | Float64        | player_season_playing_time             | Saldo de gols por 90 minutos                                                          |
| Team Success_On-Off       | Team Success      | On-Off         | Float64        | player_season_playing_time             | Diferença no desempenho da equipe quando o jogador está em campo versus fora dele     |
| Team Success_PPM          | Team Success      | PPM            | Float64        | player_season_playing_time             | Pontos por partida                                                                    |
| Team Success_onG          | Team Success      | onG            | Int64          | player_season_playing_time             | Gols marcados com o jogador em campo                                                  |
| Team Success_onGA         | Team Success      | onGA           | Int64          | player_season_playing_time             | Gols sofridos com o jogador em campo                                                  |
| Team Success (xG)_On-Off  | Team Success (xG) | On-Off         | Float64        | player_season_playing_time             | Diferença no Expected Goals da equipe quando o jogador está em campo versus fora dele |
| Team Success (xG)_onxG    | Team Success (xG) | onxG           | Float64        | player_season_playing_time             | xG com jogador em campo                                                               |
| Team Success (xG)_onxGA   | Team Success (xG) | onxGA          | Float64        | player_season_playing_time             | xGA com jogador em campo                                                              |
| Team Success (xG)_xG+/-   | Team Success (xG) | xG+/-          | Float64        | player_season_playing_time             | Saldo de xG                                                                           |
| Team Success (xG)_xG+/-90 | Team Success (xG) | xG+/-90        | Float64        | player_season_playing_time             | Saldo de xG por 90 minutos                                                            |
| 90s                       | nan               | 90s            | Float64        | player_season_possession               | Número de partidas completas (90 minutos)                                             |
| age                       | nan               | age            | Int64          | player_season_possession               | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_possession               | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_possession               | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_possession               | Posição do jogador (abreviada)                                                        |
| Carries_1/3               | Carries           | 1/3            | Int64          | player_season_possession               | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | player_season_possession               | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | player_season_possession               | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | player_season_possession               | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | player_season_possession               | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | player_season_possession               | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | player_season_possession               | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | player_season_possession               | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | player_season_possession               | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | player_season_possession               | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | player_season_possession               | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | player_season_possession               | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | player_season_possession               | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | player_season_possession               | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | player_season_possession               | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | player_season_possession               | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | player_season_possession               | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | player_season_possession               | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | player_season_possession               | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | player_season_possession               | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | player_season_possession               | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | player_season_possession               | Total de toques na bola                                                               |
| 90s                       | nan               | 90s            | Float64        | player_season_shooting                 | Número de partidas completas (90 minutos)                                             |
| age                       | nan               | age            | Int64          | player_season_shooting                 | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_shooting                 | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_shooting                 | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_shooting                 | Posição do jogador (abreviada)                                                        |
| Expected_G-xG             | Expected          | G-xG           | Float64        | player_season_shooting                 | Diferença entre gols e xG                                                             |
| Expected_np:G-xG          | Expected          | np:G-xG        | Float64        | player_season_shooting                 | Diferença entre gols sem pênalti e xG                                                 |
| Expected_npxG             | Expected          | npxG           | Float64        | player_season_shooting                 | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG/Sh          | Expected          | npxG/Sh        | Float64        | player_season_shooting                 | npxG por chute                                                                        |
| Expected_xG               | Expected          | xG             | Float64        | player_season_shooting                 | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Standard_Dist             | Standard          | Dist           | Float64        | player_season_shooting                 | Distância média dos chutes                                                            |
| Standard_FK               | Standard          | FK             | Int64          | player_season_shooting                 | Cobranças de falta                                                                    |
| Standard_G/Sh             | Standard          | G/Sh           | Float64        | player_season_shooting                 | Média de gols por chute                                                               |
| Standard_G/SoT            | Standard          | G/SoT          | Float64        | player_season_shooting                 | Média de gols por chute no alvo                                                       |
| Standard_Gls              | Standard          | Gls            | Int64          | player_season_shooting                 | Gols marcados                                                                         |
| Standard_PK               | Standard          | PK             | Int64          | player_season_shooting                 | Pênaltis convertidos                                                                  |
| Standard_PKatt            | Standard          | PKatt          | Int64          | player_season_shooting                 | Pênaltis cobrados                                                                     |
| Standard_Sh               | Standard          | Sh             | Int64          | player_season_shooting                 | Chutes bloqueados                                                                     |
| Standard_Sh/90            | Standard          | Sh/90          | Float64        | player_season_shooting                 | Média de chutes por 90 minutos                                                        |
| Standard_SoT              | Standard          | SoT            | Int64          | player_season_shooting                 | Chutes no alvo                                                                        |
| Standard_SoT%             | Standard          | SoT%           | Float64        | player_season_shooting                 | Porcentagem de chutes no alvo                                                         |
| Standard_SoT/90           | Standard          | SoT/90         | Float64        | player_season_shooting                 | Chutes no alvo por 90 minutos                                                         |
| age                       | nan               | age            | Int64          | player_season_standard                 | Idade do jogador                                                                      |
| born                      | nan               | born           | Int64          | player_season_standard                 | Data de nascimento                                                                    |
| nation                    | nan               | nation         | string         | player_season_standard                 | Nacionalidade do jogador                                                              |
| pos                       | nan               | pos            | string         | player_season_standard                 | Posição do jogador (abreviada)                                                        |
| Expected_npxG             | Expected          | npxG           | Float64        | player_season_standard                 | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG+xAG         | Expected          | npxG+xAG       | Float64        | player_season_standard                 | Soma de npxG e xAG                                                                    |
| Expected_xAG              | Expected          | xAG            | Float64        | player_season_standard                 | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_xG               | Expected          | xG             | Float64        | player_season_standard                 | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_Ast        | Per 90 Minutes    | Ast            | Float64        | player_season_standard                 | Assistências para gol                                                                 |
| Per 90 Minutes_G+A        | Per 90 Minutes    | G+A            | Float64        | player_season_standard                 | Soma de gols e assistências                                                           |
| Per 90 Minutes_G+A-PK     | Per 90 Minutes    | G+A-PK         | Float64        | player_season_standard                 | Soma de gols e assistências, excluindo pênaltis                                       |
| Per 90 Minutes_G-PK       | Per 90 Minutes    | G-PK           | Float64        | player_season_standard                 | Gols excluindo pênaltis                                                               |
| Per 90 Minutes_Gls        | Per 90 Minutes    | Gls            | Float64        | player_season_standard                 | Gols marcados                                                                         |
| Per 90 Minutes_npxG       | Per 90 Minutes    | npxG           | Float64        | player_season_standard                 | Expected Goals excluindo pênaltis                                                     |
| Per 90 Minutes_npxG+xAG   | Per 90 Minutes    | npxG+xAG       | Float64        | player_season_standard                 | Soma de npxG e xAG                                                                    |
| Per 90 Minutes_xAG        | Per 90 Minutes    | xAG            | Float64        | player_season_standard                 | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Per 90 Minutes_xG         | Per 90 Minutes    | xG             | Float64        | player_season_standard                 | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_xG+xAG     | Per 90 Minutes    | xG+xAG         | Float64        | player_season_standard                 | Soma de xG e xAG                                                                      |
| Performance_Ast           | Performance       | Ast            | Int64          | player_season_standard                 | Assistências para gol                                                                 |
| Performance_CrdR          | Performance       | CrdR           | Int64          | player_season_standard                 | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | player_season_standard                 | Cartões amarelos                                                                      |
| Performance_G+A           | Performance       | G+A            | Int64          | player_season_standard                 | Soma de gols e assistências                                                           |
| Performance_G-PK          | Performance       | G-PK           | Int64          | player_season_standard                 | Gols excluindo pênaltis                                                               |
| Performance_Gls           | Performance       | Gls            | Int64          | player_season_standard                 | Gols marcados                                                                         |
| Performance_PK            | Performance       | PK             | Int64          | player_season_standard                 | Pênaltis convertidos                                                                  |
| Performance_PKatt         | Performance       | PKatt          | Int64          | player_season_standard                 | Pênaltis cobrados                                                                     |
| Playing Time_90s          | Playing Time      | 90s            | Float64        | player_season_standard                 | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | player_season_standard                 | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | player_season_standard                 | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | player_season_standard                 | Partidas iniciadas como titular                                                       |
| Progression_PrgC          | Progression       | PrgC           | Int64          | player_season_standard                 | Conduções progressivas                                                                |
| Progression_PrgP          | Progression       | PrgP           | Int64          | player_season_standard                 | Passes progressivos realizados                                                        |
| Progression_PrgR          | Progression       | PrgR           | Int64          | player_season_standard                 | Recebimentos progressivos                                                             |
| attendance                | nan               | attendance     | Int64          | schedule                               | Público presente                                                                      |
| away_team                 | nan               | away_team      | string         | schedule                               | Time visitante                                                                        |
| away_xg                   | nan               | away_xg        | Float64        | schedule                               | Expected Goals do time visitante                                                      |
| date                      | nan               | date           | datetime64[ns] | schedule                               | Data da partida                                                                       |
| day                       | nan               | day            | string         | schedule                               | Dia da semana                                                                         |
| game_id                   | nan               | game_id        | object         | schedule                               | Identificador único da partida                                                        |
| home_team                 | nan               | home_team      | string         | schedule                               | Time mandante                                                                         |
| home_xg                   | nan               | home_xg        | Float64        | schedule                               | Expected Goals do time mandante                                                       |
| match_report              | nan               | match_report   | object         | schedule                               | Link para relatório da partida                                                        |
| notes                     | nan               | notes          | Int64          | schedule                               | Observações adicionais                                                                |
| referee                   | nan               | referee        | string         | schedule                               | Árbitro da partida                                                                    |
| score                     | nan               | score          | string         | schedule                               | Placar da partida no momento do evento                                                |
| time                      | nan               | time           | string         | schedule                               | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | schedule                               | Local da partida                                                                      |
| week                      | nan               | week           | Int64          | schedule                               | Semana da temporada                                                                   |
| PSxG                      | nan               | PSxG           | Float64        | shot_events                            | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| body_part                 | nan               | body_part      | string         | shot_events                            | Parte do corpo usada no chute                                                         |
| distance                  | nan               | distance       | Int64          | shot_events                            | Distância do chute                                                                    |
| minute                    | nan               | minute         | string         | shot_events                            | Minuto em que o evento ocorreu                                                        |
| notes                     | nan               | notes          | string         | shot_events                            | Observações adicionais                                                                |
| outcome                   | nan               | outcome        | string         | shot_events                            | Resultado do chute                                                                    |
| player                    | nan               | player         | string         | shot_events                            | Nome do jogador                                                                       |
| team                      | nan               | team           | string         | shot_events                            | Time envolvido no evento                                                              |
| xG                        | nan               | xG             | Float64        | shot_events                            | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| SCA 1_event               | SCA 1             | event          | string         | shot_events                            | Tipo do primeiro evento que gerou uma chance de finalização                           |
| SCA 1_player              | SCA 1             | player         | string         | shot_events                            | Nome do jogador                                                                       |
| SCA 2_event               | SCA 2             | event          | string         | shot_events                            | Tipo do segundo evento que gerou uma chance de finalização                            |
| SCA 2_player              | SCA 2             | player         | string         | shot_events                            | Nome do jogador                                                                       |
| Clr                       | nan               | Clr            | Int64          | team_match_defense_against             | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | team_match_defense_against             | Erros que resultaram em finalização do adversário                                     |
| GA                        | nan               | GA             | string         | team_match_defense_against             | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_defense_against             | Gols marcados                                                                         |
| Int                       | nan               | Int            | Int64          | team_match_defense_against             | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | team_match_defense_against             | Soma de desarmes e interceptações                                                     |
| date                      | nan               | date           | datetime64[ns] | team_match_defense_against             | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_defense_against             | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_defense_against             | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_defense_against             | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_defense_against             | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_defense_against             | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_defense_against             | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_defense_against             | Local da partida                                                                      |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | team_match_defense_against             | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | team_match_defense_against             | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | team_match_defense_against             | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | team_match_defense_against             | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | team_match_defense_against             | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | team_match_defense_against             | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | team_match_defense_against             | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | team_match_defense_against             | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | team_match_defense_against             | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | team_match_defense_against             | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | team_match_defense_against             | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | team_match_defense_against             | Desarmes bem-sucedidos                                                                |
| Clr                       | nan               | Clr            | Int64          | team_match_defense_for                 | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | team_match_defense_for                 | Erros que resultaram em finalização do adversário                                     |
| GA                        | nan               | GA             | string         | team_match_defense_for                 | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_defense_for                 | Gols marcados                                                                         |
| Int                       | nan               | Int            | Int64          | team_match_defense_for                 | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | team_match_defense_for                 | Soma de desarmes e interceptações                                                     |
| date                      | nan               | date           | datetime64[ns] | team_match_defense_for                 | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_defense_for                 | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_defense_for                 | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_defense_for                 | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_defense_for                 | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_defense_for                 | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_defense_for                 | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_defense_for                 | Local da partida                                                                      |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | team_match_defense_for                 | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | team_match_defense_for                 | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | team_match_defense_for                 | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | team_match_defense_for                 | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | team_match_defense_for                 | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | team_match_defense_for                 | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | team_match_defense_for                 | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | team_match_defense_for                 | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | team_match_defense_for                 | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | team_match_defense_for                 | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | team_match_defense_for                 | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | team_match_defense_for                 | Desarmes bem-sucedidos                                                                |
| GA                        | nan               | GA             | string         | team_match_goal_shot_creation_against  | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_goal_shot_creation_against  | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_goal_shot_creation_against  | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_goal_shot_creation_against  | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_goal_shot_creation_against  | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_goal_shot_creation_against  | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_goal_shot_creation_against  | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_goal_shot_creation_against  | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_goal_shot_creation_against  | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_goal_shot_creation_against  | Local da partida                                                                      |
| GCA Types_Def             | GCA Types         | Def            | Int64          | team_match_goal_shot_creation_against  | Ações defensivas que geraram gol                                                      |
| GCA Types_Fld             | GCA Types         | Fld            | Int64          | team_match_goal_shot_creation_against  | Faltas sofridas                                                                       |
| GCA Types_GCA             | GCA Types         | GCA            | Int64          | team_match_goal_shot_creation_against  | Ações que geraram gols                                                                |
| GCA Types_PassDead        | GCA Types         | PassDead       | Int64          | team_match_goal_shot_creation_against  | Ações de bola parada para criação de chance                                           |
| GCA Types_PassLive        | GCA Types         | PassLive       | Int64          | team_match_goal_shot_creation_against  | Ações de bola em movimento para criação de chance                                     |
| GCA Types_Sh              | GCA Types         | Sh             | Int64          | team_match_goal_shot_creation_against  | Chutes bloqueados                                                                     |
| GCA Types_TO              | GCA Types         | TO             | Int64          | team_match_goal_shot_creation_against  | Dribles que geraram chance                                                            |
| SCA Types_Def             | SCA Types         | Def            | Int64          | team_match_goal_shot_creation_against  | Ações defensivas que geraram chute                                                    |
| SCA Types_Fld             | SCA Types         | Fld            | Int64          | team_match_goal_shot_creation_against  | Faltas sofridas                                                                       |
| SCA Types_PassDead        | SCA Types         | PassDead       | Int64          | team_match_goal_shot_creation_against  | Ações de bola parada para criação de chance                                           |
| SCA Types_PassLive        | SCA Types         | PassLive       | Int64          | team_match_goal_shot_creation_against  | Ações de bola em movimento para criação de chance                                     |
| SCA Types_SCA             | SCA Types         | SCA            | Int64          | team_match_goal_shot_creation_against  | Ações que geraram chutes                                                              |
| SCA Types_Sh              | SCA Types         | Sh             | Int64          | team_match_goal_shot_creation_against  | Chutes bloqueados                                                                     |
| SCA Types_TO              | SCA Types         | TO             | Int64          | team_match_goal_shot_creation_against  | Dribles que geraram chance                                                            |
| GA                        | nan               | GA             | string         | team_match_goal_shot_creation_for      | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_goal_shot_creation_for      | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_goal_shot_creation_for      | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_goal_shot_creation_for      | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_goal_shot_creation_for      | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_goal_shot_creation_for      | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_goal_shot_creation_for      | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_goal_shot_creation_for      | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_goal_shot_creation_for      | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_goal_shot_creation_for      | Local da partida                                                                      |
| GCA Types_Def             | GCA Types         | Def            | Int64          | team_match_goal_shot_creation_for      | Ações defensivas que geraram gol                                                      |
| GCA Types_Fld             | GCA Types         | Fld            | Int64          | team_match_goal_shot_creation_for      | Faltas sofridas                                                                       |
| GCA Types_GCA             | GCA Types         | GCA            | Int64          | team_match_goal_shot_creation_for      | Ações que geraram gols                                                                |
| GCA Types_PassDead        | GCA Types         | PassDead       | Int64          | team_match_goal_shot_creation_for      | Ações de bola parada para criação de chance                                           |
| GCA Types_PassLive        | GCA Types         | PassLive       | Int64          | team_match_goal_shot_creation_for      | Ações de bola em movimento para criação de chance                                     |
| GCA Types_Sh              | GCA Types         | Sh             | Int64          | team_match_goal_shot_creation_for      | Chutes bloqueados                                                                     |
| GCA Types_TO              | GCA Types         | TO             | Int64          | team_match_goal_shot_creation_for      | Dribles que geraram chance                                                            |
| SCA Types_Def             | SCA Types         | Def            | Int64          | team_match_goal_shot_creation_for      | Ações defensivas que geraram chute                                                    |
| SCA Types_Fld             | SCA Types         | Fld            | Int64          | team_match_goal_shot_creation_for      | Faltas sofridas                                                                       |
| SCA Types_PassDead        | SCA Types         | PassDead       | Int64          | team_match_goal_shot_creation_for      | Ações de bola parada para criação de chance                                           |
| SCA Types_PassLive        | SCA Types         | PassLive       | Int64          | team_match_goal_shot_creation_for      | Ações de bola em movimento para criação de chance                                     |
| SCA Types_SCA             | SCA Types         | SCA            | Int64          | team_match_goal_shot_creation_for      | Ações que geraram chutes                                                              |
| SCA Types_Sh              | SCA Types         | Sh             | Int64          | team_match_goal_shot_creation_for      | Chutes bloqueados                                                                     |
| SCA Types_TO              | SCA Types         | TO             | Int64          | team_match_goal_shot_creation_for      | Dribles que geraram chance                                                            |
| GA                        | nan               | GA             | string         | team_match_keeper_against              | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_keeper_against              | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_keeper_against              | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_keeper_against              | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_keeper_against              | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_keeper_against              | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_keeper_against              | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_keeper_against              | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_keeper_against              | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_keeper_against              | Local da partida                                                                      |
| Crosses_Opp               | Crosses           | Opp            | Int64          | team_match_keeper_against              | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | team_match_keeper_against              | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Float64        | team_match_keeper_against              | Porcentagem de cruzamentos interceptados                                              |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | team_match_keeper_against              | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | team_match_keeper_against              | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | team_match_keeper_against              | Porcentagem de tiros de meta longos                                                   |
| Launched_Att              | Launched          | Att            | Int64          | team_match_keeper_against              | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | team_match_keeper_against              | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | team_match_keeper_against              | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | team_match_keeper_against              | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | team_match_keeper_against              | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | team_match_keeper_against              | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | team_match_keeper_against              | Passes realizados com as mãos                                                         |
| Penalty Kicks_PKA         | Penalty Kicks     | PKA            | Int64          | team_match_keeper_against              | Pênaltis convertidos                                                                  |
| Penalty Kicks_PKatt       | Penalty Kicks     | PKatt          | Int64          | team_match_keeper_against              | Pênaltis cobrados                                                                     |
| Penalty Kicks_PKm         | Penalty Kicks     | PKm            | Int64          | team_match_keeper_against              | Pênaltis perdidos                                                                     |
| Penalty Kicks_PKsv        | Penalty Kicks     | PKsv           | Int64          | team_match_keeper_against              | Pênaltis defendidos                                                                   |
| Performance_CS            | Performance       | CS             | Int64          | team_match_keeper_against              | Clean sheets (jogos sem sofrer gol)                                                   |
| Performance_GA            | Performance       | GA             | Int64          | team_match_keeper_against              | Gols sofridos                                                                         |
| Performance_PSxG          | Performance       | PSxG           | Float64        | team_match_keeper_against              | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Performance_PSxG+/-       | Performance       | PSxG+/-        | Float64        | team_match_keeper_against              | Diferença entre gols sofridos e PSxG                                                  |
| Performance_Save%         | Performance       | Save%          | Float64        | team_match_keeper_against              | Porcentagem de defesas realizadas                                                     |
| Performance_Saves         | Performance       | Saves          | Int64          | team_match_keeper_against              | Defesas realizadas                                                                    |
| Performance_SoTA          | Performance       | SoTA           | Int64          | team_match_keeper_against              | Chutes no alvo enfrentados                                                            |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | team_match_keeper_against              | Ações defensivas fora da área                                                         |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | team_match_keeper_against              | Distância média das ações                                                             |
| GA                        | nan               | GA             | string         | team_match_keeper_for                  | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_keeper_for                  | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_keeper_for                  | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_keeper_for                  | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_keeper_for                  | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_keeper_for                  | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_keeper_for                  | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_keeper_for                  | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_keeper_for                  | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_keeper_for                  | Local da partida                                                                      |
| Crosses_Opp               | Crosses           | Opp            | Int64          | team_match_keeper_for                  | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | team_match_keeper_for                  | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Float64        | team_match_keeper_for                  | Porcentagem de cruzamentos interceptados                                              |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | team_match_keeper_for                  | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | team_match_keeper_for                  | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | team_match_keeper_for                  | Porcentagem de tiros de meta longos                                                   |
| Launched_Att              | Launched          | Att            | Int64          | team_match_keeper_for                  | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | team_match_keeper_for                  | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | team_match_keeper_for                  | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | team_match_keeper_for                  | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | team_match_keeper_for                  | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | team_match_keeper_for                  | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | team_match_keeper_for                  | Passes realizados com as mãos                                                         |
| Penalty Kicks_PKA         | Penalty Kicks     | PKA            | Int64          | team_match_keeper_for                  | Pênaltis convertidos                                                                  |
| Penalty Kicks_PKatt       | Penalty Kicks     | PKatt          | Int64          | team_match_keeper_for                  | Pênaltis cobrados                                                                     |
| Penalty Kicks_PKm         | Penalty Kicks     | PKm            | Int64          | team_match_keeper_for                  | Pênaltis perdidos                                                                     |
| Penalty Kicks_PKsv        | Penalty Kicks     | PKsv           | Int64          | team_match_keeper_for                  | Pênaltis defendidos                                                                   |
| Performance_CS            | Performance       | CS             | Int64          | team_match_keeper_for                  | Clean sheets (jogos sem sofrer gol)                                                   |
| Performance_GA            | Performance       | GA             | Int64          | team_match_keeper_for                  | Gols sofridos                                                                         |
| Performance_PSxG          | Performance       | PSxG           | Float64        | team_match_keeper_for                  | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Performance_PSxG+/-       | Performance       | PSxG+/-        | Float64        | team_match_keeper_for                  | Diferença entre gols sofridos e PSxG                                                  |
| Performance_Save%         | Performance       | Save%          | Float64        | team_match_keeper_for                  | Porcentagem de defesas realizadas                                                     |
| Performance_Saves         | Performance       | Saves          | Int64          | team_match_keeper_for                  | Defesas realizadas                                                                    |
| Performance_SoTA          | Performance       | SoTA           | Int64          | team_match_keeper_for                  | Chutes no alvo enfrentados                                                            |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | team_match_keeper_for                  | Ações defensivas fora da área                                                         |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | team_match_keeper_for                  | Distância média das ações                                                             |
| GA                        | nan               | GA             | string         | team_match_misc_against                | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_misc_against                | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_misc_against                | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_misc_against                | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_misc_against                | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_misc_against                | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_misc_against                | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_misc_against                | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_misc_against                | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_misc_against                | Local da partida                                                                      |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | team_match_misc_against                | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | team_match_misc_against                | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | team_match_misc_against                | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | team_match_misc_against                | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_match_misc_against                | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_match_misc_against                | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | team_match_misc_against                | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | team_match_misc_against                | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | team_match_misc_against                | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | team_match_misc_against                | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | team_match_misc_against                | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | team_match_misc_against                | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | team_match_misc_against                | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | team_match_misc_against                | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | team_match_misc_against                | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | team_match_misc_against                | Desarmes bem-sucedidos                                                                |
| GA                        | nan               | GA             | string         | team_match_misc_for                    | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_misc_for                    | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_misc_for                    | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_misc_for                    | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_misc_for                    | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_misc_for                    | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_misc_for                    | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_misc_for                    | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_misc_for                    | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_misc_for                    | Local da partida                                                                      |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | team_match_misc_for                    | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | team_match_misc_for                    | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | team_match_misc_for                    | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | team_match_misc_for                    | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_match_misc_for                    | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_match_misc_for                    | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | team_match_misc_for                    | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | team_match_misc_for                    | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | team_match_misc_for                    | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | team_match_misc_for                    | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | team_match_misc_for                    | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | team_match_misc_for                    | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | team_match_misc_for                    | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | team_match_misc_for                    | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | team_match_misc_for                    | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | team_match_misc_for                    | Desarmes bem-sucedidos                                                                |
| 1/3                       | nan               | 1/3            | Int64          | team_match_passing_against             | Passes para o terço final do campo                                                    |
| Ast                       | nan               | Ast            | Int64          | team_match_passing_against             | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | team_match_passing_against             | Cruzamentos para área de pênalti                                                      |
| GA                        | nan               | GA             | string         | team_match_passing_against             | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_passing_against             | Gols marcados                                                                         |
| KP                        | nan               | KP             | Int64          | team_match_passing_against             | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | team_match_passing_against             | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | team_match_passing_against             | Passes progressivos realizados                                                        |
| date                      | nan               | date           | datetime64[ns] | team_match_passing_against             | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_passing_against             | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_passing_against             | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_passing_against             | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_passing_against             | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_passing_against             | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_passing_against             | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_passing_against             | Local da partida                                                                      |
| xA                        | nan               | xA             | Float64        | team_match_passing_against             | Expected Assists                                                                      |
| xAG                       | nan               | xAG            | Float64        | team_match_passing_against             | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Long_Att                  | Long              | Att            | Int64          | team_match_passing_against             | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | team_match_passing_against             | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | team_match_passing_against             | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | team_match_passing_against             | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | team_match_passing_against             | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | team_match_passing_against             | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | team_match_passing_against             | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | team_match_passing_against             | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | team_match_passing_against             | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | team_match_passing_against             | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | team_match_passing_against             | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | team_match_passing_against             | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | team_match_passing_against             | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | team_match_passing_against             | Distância total percorrida                                                            |
| 1/3                       | nan               | 1/3            | Int64          | team_match_passing_for                 | Passes para o terço final do campo                                                    |
| Ast                       | nan               | Ast            | Int64          | team_match_passing_for                 | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | team_match_passing_for                 | Cruzamentos para área de pênalti                                                      |
| GA                        | nan               | GA             | string         | team_match_passing_for                 | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_passing_for                 | Gols marcados                                                                         |
| KP                        | nan               | KP             | Int64          | team_match_passing_for                 | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | team_match_passing_for                 | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | team_match_passing_for                 | Passes progressivos realizados                                                        |
| date                      | nan               | date           | datetime64[ns] | team_match_passing_for                 | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_passing_for                 | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_passing_for                 | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_passing_for                 | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_passing_for                 | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_passing_for                 | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_passing_for                 | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_passing_for                 | Local da partida                                                                      |
| xA                        | nan               | xA             | Float64        | team_match_passing_for                 | Expected Assists                                                                      |
| xAG                       | nan               | xAG            | Float64        | team_match_passing_for                 | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Long_Att                  | Long              | Att            | Int64          | team_match_passing_for                 | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | team_match_passing_for                 | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | team_match_passing_for                 | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | team_match_passing_for                 | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | team_match_passing_for                 | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | team_match_passing_for                 | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | team_match_passing_for                 | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | team_match_passing_for                 | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | team_match_passing_for                 | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | team_match_passing_for                 | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | team_match_passing_for                 | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | team_match_passing_for                 | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | team_match_passing_for                 | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | team_match_passing_for                 | Distância total percorrida                                                            |
| Att                       | nan               | Att            | Int64          | team_match_passing_types_against       | Tentativas de ação (contexto específico da categoria)                                 |
| GA                        | nan               | GA             | string         | team_match_passing_types_against       | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_passing_types_against       | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_passing_types_against       | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_passing_types_against       | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_passing_types_against       | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_passing_types_against       | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_passing_types_against       | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_passing_types_against       | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_passing_types_against       | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_passing_types_against       | Local da partida                                                                      |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | team_match_passing_types_against       | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | team_match_passing_types_against       | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | team_match_passing_types_against       | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | team_match_passing_types_against       | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | team_match_passing_types_against       | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | team_match_passing_types_against       | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | team_match_passing_types_against       | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | team_match_passing_types_against       | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | team_match_passing_types_against       | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | team_match_passing_types_against       | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | team_match_passing_types_against       | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | team_match_passing_types_against       | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | team_match_passing_types_against       | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | team_match_passing_types_against       | Arremessos laterais                                                                   |
| Att                       | nan               | Att            | Int64          | team_match_passing_types_for           | Tentativas de ação (contexto específico da categoria)                                 |
| GA                        | nan               | GA             | string         | team_match_passing_types_for           | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_passing_types_for           | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_passing_types_for           | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_passing_types_for           | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_passing_types_for           | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_passing_types_for           | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_passing_types_for           | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_passing_types_for           | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_passing_types_for           | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_passing_types_for           | Local da partida                                                                      |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | team_match_passing_types_for           | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | team_match_passing_types_for           | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | team_match_passing_types_for           | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | team_match_passing_types_for           | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | team_match_passing_types_for           | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | team_match_passing_types_for           | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | team_match_passing_types_for           | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | team_match_passing_types_for           | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | team_match_passing_types_for           | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | team_match_passing_types_for           | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | team_match_passing_types_for           | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | team_match_passing_types_for           | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | team_match_passing_types_for           | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | team_match_passing_types_for           | Arremessos laterais                                                                   |
| GA                        | nan               | GA             | string         | team_match_possession_against          | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_possession_against          | Gols marcados                                                                         |
| Poss                      | nan               | Poss           | Int64          | team_match_possession_against          | Percentual de posse de bola                                                           |
| date                      | nan               | date           | datetime64[ns] | team_match_possession_against          | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_possession_against          | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_possession_against          | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_possession_against          | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_possession_against          | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_possession_against          | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_possession_against          | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_possession_against          | Local da partida                                                                      |
| Carries_1/3               | Carries           | 1/3            | Int64          | team_match_possession_against          | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | team_match_possession_against          | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | team_match_possession_against          | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | team_match_possession_against          | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | team_match_possession_against          | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | team_match_possession_against          | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | team_match_possession_against          | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | team_match_possession_against          | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | team_match_possession_against          | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | team_match_possession_against          | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | team_match_possession_against          | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | team_match_possession_against          | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | team_match_possession_against          | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | team_match_possession_against          | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | team_match_possession_against          | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | team_match_possession_against          | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | team_match_possession_against          | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | team_match_possession_against          | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | team_match_possession_against          | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | team_match_possession_against          | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | team_match_possession_against          | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | team_match_possession_against          | Total de toques na bola                                                               |
| GA                        | nan               | GA             | string         | team_match_possession_for              | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_possession_for              | Gols marcados                                                                         |
| Poss                      | nan               | Poss           | Int64          | team_match_possession_for              | Percentual de posse de bola                                                           |
| date                      | nan               | date           | datetime64[ns] | team_match_possession_for              | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_possession_for              | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_possession_for              | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_possession_for              | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_possession_for              | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_possession_for              | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_possession_for              | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_possession_for              | Local da partida                                                                      |
| Carries_1/3               | Carries           | 1/3            | Int64          | team_match_possession_for              | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | team_match_possession_for              | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | team_match_possession_for              | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | team_match_possession_for              | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | team_match_possession_for              | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | team_match_possession_for              | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | team_match_possession_for              | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | team_match_possession_for              | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | team_match_possession_for              | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | team_match_possession_for              | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | team_match_possession_for              | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | team_match_possession_for              | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | team_match_possession_for              | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | team_match_possession_for              | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | team_match_possession_for              | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | team_match_possession_for              | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | team_match_possession_for              | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | team_match_possession_for              | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | team_match_possession_for              | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | team_match_possession_for              | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | team_match_possession_for              | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | team_match_possession_for              | Total de toques na bola                                                               |
| Attendance                | nan               | Attendance     | Int64          | team_match_schedule                    | nan                                                                                   |
| Captain                   | nan               | Captain        | string         | team_match_schedule                    | Capitão da equipe                                                                     |
| Formation                 | nan               | Formation      | string         | team_match_schedule                    | Formação tática                                                                       |
| GA                        | nan               | GA             | string         | team_match_schedule                    | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_schedule                    | Gols marcados                                                                         |
| Notes                     | nan               | Notes          | string         | team_match_schedule                    | nan                                                                                   |
| Opp Formation             | nan               | Opp Formation  | string         | team_match_schedule                    | Formação tática do adversário                                                         |
| Poss                      | nan               | Poss           | Int64          | team_match_schedule                    | Percentual de posse de bola                                                           |
| Referee                   | nan               | Referee        | string         | team_match_schedule                    | nan                                                                                   |
| date                      | nan               | date           | datetime64[ns] | team_match_schedule                    | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_schedule                    | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_schedule                    | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_schedule                    | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_schedule                    | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_schedule                    | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_schedule                    | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_schedule                    | Local da partida                                                                      |
| xG                        | nan               | xG             | Float64        | team_match_schedule                    | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| xGA                       | nan               | xGA            | Float64        | team_match_schedule                    | Expected Goals Against                                                                |
| GA                        | nan               | GA             | string         | team_match_shooting_against            | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_shooting_against            | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_shooting_against            | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_shooting_against            | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_shooting_against            | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_shooting_against            | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_shooting_against            | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_shooting_against            | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_shooting_against            | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_shooting_against            | Local da partida                                                                      |
| Expected_G-xG             | Expected          | G-xG           | Float64        | team_match_shooting_against            | Diferença entre gols e xG                                                             |
| Expected_np:G-xG          | Expected          | np:G-xG        | Float64        | team_match_shooting_against            | Diferença entre gols sem pênalti e xG                                                 |
| Expected_npxG             | Expected          | npxG           | Float64        | team_match_shooting_against            | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG/Sh          | Expected          | npxG/Sh        | Float64        | team_match_shooting_against            | npxG por chute                                                                        |
| Expected_xG               | Expected          | xG             | Float64        | team_match_shooting_against            | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Standard_Dist             | Standard          | Dist           | Float64        | team_match_shooting_against            | Distância média dos chutes                                                            |
| Standard_FK               | Standard          | FK             | Int64          | team_match_shooting_against            | Cobranças de falta                                                                    |
| Standard_G/Sh             | Standard          | G/Sh           | Float64        | team_match_shooting_against            | Média de gols por chute                                                               |
| Standard_G/SoT            | Standard          | G/SoT          | Float64        | team_match_shooting_against            | Média de gols por chute no alvo                                                       |
| Standard_Gls              | Standard          | Gls            | Int64          | team_match_shooting_against            | Gols marcados                                                                         |
| Standard_PK               | Standard          | PK             | Int64          | team_match_shooting_against            | Pênaltis convertidos                                                                  |
| Standard_PKatt            | Standard          | PKatt          | Int64          | team_match_shooting_against            | Pênaltis cobrados                                                                     |
| Standard_Sh               | Standard          | Sh             | Int64          | team_match_shooting_against            | Chutes bloqueados                                                                     |
| Standard_SoT              | Standard          | SoT            | Int64          | team_match_shooting_against            | Chutes no alvo                                                                        |
| Standard_SoT%             | Standard          | SoT%           | Float64        | team_match_shooting_against            | Porcentagem de chutes no alvo                                                         |
| GA                        | nan               | GA             | string         | team_match_shooting_for                | Gols sofridos                                                                         |
| GF                        | nan               | GF             | string         | team_match_shooting_for                | Gols marcados                                                                         |
| date                      | nan               | date           | datetime64[ns] | team_match_shooting_for                | Data da partida                                                                       |
| day                       | nan               | day            | string         | team_match_shooting_for                | Dia da semana                                                                         |
| match_report              | nan               | match_report   | object         | team_match_shooting_for                | Link para relatório da partida                                                        |
| opponent                  | nan               | opponent       | string         | team_match_shooting_for                | Time adversário                                                                       |
| result                    | nan               | result         | string         | team_match_shooting_for                | Resultado do jogo (W/D/L)                                                             |
| round                     | nan               | round          | string         | team_match_shooting_for                | Rodada da competição                                                                  |
| time                      | nan               | time           | object         | team_match_shooting_for                | Horário da partida                                                                    |
| venue                     | nan               | venue          | string         | team_match_shooting_for                | Local da partida                                                                      |
| Expected_G-xG             | Expected          | G-xG           | Float64        | team_match_shooting_for                | Diferença entre gols e xG                                                             |
| Expected_np:G-xG          | Expected          | np:G-xG        | Float64        | team_match_shooting_for                | Diferença entre gols sem pênalti e xG                                                 |
| Expected_npxG             | Expected          | npxG           | Float64        | team_match_shooting_for                | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG/Sh          | Expected          | npxG/Sh        | Float64        | team_match_shooting_for                | npxG por chute                                                                        |
| Expected_xG               | Expected          | xG             | Float64        | team_match_shooting_for                | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Standard_Dist             | Standard          | Dist           | Float64        | team_match_shooting_for                | Distância média dos chutes                                                            |
| Standard_FK               | Standard          | FK             | Int64          | team_match_shooting_for                | Cobranças de falta                                                                    |
| Standard_G/Sh             | Standard          | G/Sh           | Float64        | team_match_shooting_for                | Média de gols por chute                                                               |
| Standard_G/SoT            | Standard          | G/SoT          | Float64        | team_match_shooting_for                | Média de gols por chute no alvo                                                       |
| Standard_Gls              | Standard          | Gls            | Int64          | team_match_shooting_for                | Gols marcados                                                                         |
| Standard_PK               | Standard          | PK             | Int64          | team_match_shooting_for                | Pênaltis convertidos                                                                  |
| Standard_PKatt            | Standard          | PKatt          | Int64          | team_match_shooting_for                | Pênaltis cobrados                                                                     |
| Standard_Sh               | Standard          | Sh             | Int64          | team_match_shooting_for                | Chutes bloqueados                                                                     |
| Standard_SoT              | Standard          | SoT            | Int64          | team_match_shooting_for                | Chutes no alvo                                                                        |
| Standard_SoT%             | Standard          | SoT%           | Float64        | team_match_shooting_for                | Porcentagem de chutes no alvo                                                         |
| 90s                       | nan               | 90s            | Int64          | team_season_defense_against            | Número de partidas completas (90 minutos)                                             |
| Clr                       | nan               | Clr            | Int64          | team_season_defense_against            | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | team_season_defense_against            | Erros que resultaram em finalização do adversário                                     |
| Int                       | nan               | Int            | Int64          | team_season_defense_against            | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | team_season_defense_against            | Soma de desarmes e interceptações                                                     |
| players_used              | nan               | players_used   | Int64          | team_season_defense_against            | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_defense_against            | Link para página de estatísticas                                                      |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | team_season_defense_against            | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | team_season_defense_against            | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | team_season_defense_against            | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | team_season_defense_against            | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | team_season_defense_against            | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | team_season_defense_against            | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | team_season_defense_against            | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | team_season_defense_against            | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | team_season_defense_against            | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | team_season_defense_against            | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | team_season_defense_against            | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | team_season_defense_against            | Desarmes bem-sucedidos                                                                |
| 90s                       | nan               | 90s            | Int64          | team_season_defense_for                | Número de partidas completas (90 minutos)                                             |
| Clr                       | nan               | Clr            | Int64          | team_season_defense_for                | Cortes/Afastamentos defensivos                                                        |
| Err                       | nan               | Err            | Int64          | team_season_defense_for                | Erros que resultaram em finalização do adversário                                     |
| Int                       | nan               | Int            | Int64          | team_season_defense_for                | Interceptações realizadas                                                             |
| Tkl+Int                   | nan               | Tkl+Int        | Int64          | team_season_defense_for                | Soma de desarmes e interceptações                                                     |
| players_used              | nan               | players_used   | Int64          | team_season_defense_for                | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_defense_for                | Link para página de estatísticas                                                      |
| Blocks_Blocks             | Blocks            | Blocks         | Int64          | team_season_defense_for                | Total de bloqueios realizados                                                         |
| Blocks_Pass               | Blocks            | Pass           | Int64          | team_season_defense_for                | Bloqueios de passes realizados                                                        |
| Blocks_Sh                 | Blocks            | Sh             | Int64          | team_season_defense_for                | Chutes bloqueados                                                                     |
| Challenges_Att            | Challenges        | Att            | Int64          | team_season_defense_for                | Tentativas de ação (contexto específico da categoria)                                 |
| Challenges_Lost           | Challenges        | Lost           | Int64          | team_season_defense_for                | Desarmes perdidos                                                                     |
| Challenges_Tkl            | Challenges        | Tkl            | Int64          | team_season_defense_for                | Desarmes realizados                                                                   |
| Challenges_Tkl%           | Challenges        | Tkl%           | Float64        | team_season_defense_for                | Porcentagem de desarmes bem-sucedidos                                                 |
| Tackles_Att 3rd           | Tackles           | Att 3rd        | Int64          | team_season_defense_for                | Ações no terço ofensivo                                                               |
| Tackles_Def 3rd           | Tackles           | Def 3rd        | Int64          | team_season_defense_for                | Ações no terço defensivo                                                              |
| Tackles_Mid 3rd           | Tackles           | Mid 3rd        | Int64          | team_season_defense_for                | Ações no terço médio                                                                  |
| Tackles_Tkl               | Tackles           | Tkl            | Int64          | team_season_defense_for                | Desarmes realizados                                                                   |
| Tackles_TklW              | Tackles           | TklW           | Int64          | team_season_defense_for                | Desarmes bem-sucedidos                                                                |
| 90s                       | nan               | 90s            | Int64          | team_season_goal_shot_creation_against | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_goal_shot_creation_against | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_goal_shot_creation_against | Link para página de estatísticas                                                      |
| GCA_GCA                   | GCA               | GCA            | Int64          | team_season_goal_shot_creation_against | Ações que geraram gols                                                                |
| GCA_GCA90                 | GCA               | GCA90          | Float64        | team_season_goal_shot_creation_against | Ações que geraram gols por 90 minutos                                                 |
| GCA Types_Def             | GCA Types         | Def            | Int64          | team_season_goal_shot_creation_against | Ações defensivas que geraram gol                                                      |
| GCA Types_Fld             | GCA Types         | Fld            | Int64          | team_season_goal_shot_creation_against | Faltas sofridas                                                                       |
| GCA Types_PassDead        | GCA Types         | PassDead       | Int64          | team_season_goal_shot_creation_against | Ações de bola parada para criação de chance                                           |
| GCA Types_PassLive        | GCA Types         | PassLive       | Int64          | team_season_goal_shot_creation_against | Ações de bola em movimento para criação de chance                                     |
| GCA Types_Sh              | GCA Types         | Sh             | Int64          | team_season_goal_shot_creation_against | Chutes bloqueados                                                                     |
| GCA Types_TO              | GCA Types         | TO             | Int64          | team_season_goal_shot_creation_against | Dribles que geraram chance                                                            |
| SCA_SCA                   | SCA               | SCA            | Int64          | team_season_goal_shot_creation_against | Ações que geraram chutes                                                              |
| SCA_SCA90                 | SCA               | SCA90          | Float64        | team_season_goal_shot_creation_against | Ações que geraram chutes por 90 minutos                                               |
| SCA Types_Def             | SCA Types         | Def            | Int64          | team_season_goal_shot_creation_against | Ações defensivas que geraram chute                                                    |
| SCA Types_Fld             | SCA Types         | Fld            | Int64          | team_season_goal_shot_creation_against | Faltas sofridas                                                                       |
| SCA Types_PassDead        | SCA Types         | PassDead       | Int64          | team_season_goal_shot_creation_against | Ações de bola parada para criação de chance                                           |
| SCA Types_PassLive        | SCA Types         | PassLive       | Int64          | team_season_goal_shot_creation_against | Ações de bola em movimento para criação de chance                                     |
| SCA Types_Sh              | SCA Types         | Sh             | Int64          | team_season_goal_shot_creation_against | Chutes bloqueados                                                                     |
| SCA Types_TO              | SCA Types         | TO             | Int64          | team_season_goal_shot_creation_against | Dribles que geraram chance                                                            |
| 90s                       | nan               | 90s            | Int64          | team_season_goal_shot_creation_for     | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_goal_shot_creation_for     | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_goal_shot_creation_for     | Link para página de estatísticas                                                      |
| GCA_GCA                   | GCA               | GCA            | Int64          | team_season_goal_shot_creation_for     | Ações que geraram gols                                                                |
| GCA_GCA90                 | GCA               | GCA90          | Float64        | team_season_goal_shot_creation_for     | Ações que geraram gols por 90 minutos                                                 |
| GCA Types_Def             | GCA Types         | Def            | Int64          | team_season_goal_shot_creation_for     | Ações defensivas que geraram gol                                                      |
| GCA Types_Fld             | GCA Types         | Fld            | Int64          | team_season_goal_shot_creation_for     | Faltas sofridas                                                                       |
| GCA Types_PassDead        | GCA Types         | PassDead       | Int64          | team_season_goal_shot_creation_for     | Ações de bola parada para criação de chance                                           |
| GCA Types_PassLive        | GCA Types         | PassLive       | Int64          | team_season_goal_shot_creation_for     | Ações de bola em movimento para criação de chance                                     |
| GCA Types_Sh              | GCA Types         | Sh             | Int64          | team_season_goal_shot_creation_for     | Chutes bloqueados                                                                     |
| GCA Types_TO              | GCA Types         | TO             | Int64          | team_season_goal_shot_creation_for     | Dribles que geraram chance                                                            |
| SCA_SCA                   | SCA               | SCA            | Int64          | team_season_goal_shot_creation_for     | Ações que geraram chutes                                                              |
| SCA_SCA90                 | SCA               | SCA90          | Float64        | team_season_goal_shot_creation_for     | Ações que geraram chutes por 90 minutos                                               |
| SCA Types_Def             | SCA Types         | Def            | Int64          | team_season_goal_shot_creation_for     | Ações defensivas que geraram chute                                                    |
| SCA Types_Fld             | SCA Types         | Fld            | Int64          | team_season_goal_shot_creation_for     | Faltas sofridas                                                                       |
| SCA Types_PassDead        | SCA Types         | PassDead       | Int64          | team_season_goal_shot_creation_for     | Ações de bola parada para criação de chance                                           |
| SCA Types_PassLive        | SCA Types         | PassLive       | Int64          | team_season_goal_shot_creation_for     | Ações de bola em movimento para criação de chance                                     |
| SCA Types_Sh              | SCA Types         | Sh             | Int64          | team_season_goal_shot_creation_for     | Chutes bloqueados                                                                     |
| SCA Types_TO              | SCA Types         | TO             | Int64          | team_season_goal_shot_creation_for     | Dribles que geraram chance                                                            |
| 90s                       | nan               | 90s            | Int64          | team_season_keeper_adv_against         | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_keeper_adv_against         | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_keeper_adv_against         | Link para página de estatísticas                                                      |
| Crosses_Opp               | Crosses           | Opp            | Int64          | team_season_keeper_adv_against         | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | team_season_keeper_adv_against         | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Float64        | team_season_keeper_adv_against         | Porcentagem de cruzamentos interceptados                                              |
| Expected_/90              | Expected          | /90            | Float64        | team_season_keeper_adv_against         | Métrica normalizada por 90 minutos                                                    |
| Expected_PSxG             | Expected          | PSxG           | Float64        | team_season_keeper_adv_against         | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Expected_PSxG+/-          | Expected          | PSxG+/-        | Float64        | team_season_keeper_adv_against         | Diferença entre gols sofridos e PSxG                                                  |
| Expected_PSxG/SoT         | Expected          | PSxG/SoT       | Float64        | team_season_keeper_adv_against         | PSxG por chute no alvo                                                                |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | team_season_keeper_adv_against         | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | team_season_keeper_adv_against         | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | team_season_keeper_adv_against         | Porcentagem de tiros de meta longos                                                   |
| Goals_CK                  | Goals             | CK             | Int64          | team_season_keeper_adv_against         | Cobranças de escanteio                                                                |
| Goals_FK                  | Goals             | FK             | Int64          | team_season_keeper_adv_against         | Cobranças de falta                                                                    |
| Goals_GA                  | Goals             | GA             | Int64          | team_season_keeper_adv_against         | Gols sofridos                                                                         |
| Goals_OG                  | Goals             | OG             | Int64          | team_season_keeper_adv_against         | Gols contra                                                                           |
| Goals_PKA                 | Goals             | PKA            | Int64          | team_season_keeper_adv_against         | Pênaltis convertidos                                                                  |
| Launched_Att              | Launched          | Att            | Int64          | team_season_keeper_adv_against         | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | team_season_keeper_adv_against         | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | team_season_keeper_adv_against         | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | team_season_keeper_adv_against         | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | team_season_keeper_adv_against         | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | team_season_keeper_adv_against         | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | team_season_keeper_adv_against         | Passes realizados com as mãos                                                         |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | team_season_keeper_adv_against         | Ações defensivas fora da área                                                         |
| Sweeper_#OPA/90           | Sweeper           | #OPA/90        | Float64        | team_season_keeper_adv_against         | Ações defensivas fora da área por 90 minutos                                          |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | team_season_keeper_adv_against         | Distância média das ações                                                             |
| 90s                       | nan               | 90s            | Int64          | team_season_keeper_adv_for             | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_keeper_adv_for             | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_keeper_adv_for             | Link para página de estatísticas                                                      |
| Crosses_Opp               | Crosses           | Opp            | Int64          | team_season_keeper_adv_for             | Cruzamentos enfrentados                                                               |
| Crosses_Stp               | Crosses           | Stp            | Int64          | team_season_keeper_adv_for             | Cruzamentos interceptados                                                             |
| Crosses_Stp%              | Crosses           | Stp%           | Float64        | team_season_keeper_adv_for             | Porcentagem de cruzamentos interceptados                                              |
| Expected_/90              | Expected          | /90            | Float64        | team_season_keeper_adv_for             | Métrica normalizada por 90 minutos                                                    |
| Expected_PSxG             | Expected          | PSxG           | Float64        | team_season_keeper_adv_for             | Post-Shot Expected Goals - Qualidade dos chutes enfrentados                           |
| Expected_PSxG+/-          | Expected          | PSxG+/-        | Float64        | team_season_keeper_adv_for             | Diferença entre gols sofridos e PSxG                                                  |
| Expected_PSxG/SoT         | Expected          | PSxG/SoT       | Float64        | team_season_keeper_adv_for             | PSxG por chute no alvo                                                                |
| Goal Kicks_Att            | Goal Kicks        | Att            | Int64          | team_season_keeper_adv_for             | Tentativas de ação (contexto específico da categoria)                                 |
| Goal Kicks_AvgLen         | Goal Kicks        | AvgLen         | Float64        | team_season_keeper_adv_for             | Comprimento médio dos tiros de meta                                                   |
| Goal Kicks_Launch%        | Goal Kicks        | Launch%        | Float64        | team_season_keeper_adv_for             | Porcentagem de tiros de meta longos                                                   |
| Goals_CK                  | Goals             | CK             | Int64          | team_season_keeper_adv_for             | Cobranças de escanteio                                                                |
| Goals_FK                  | Goals             | FK             | Int64          | team_season_keeper_adv_for             | Cobranças de falta                                                                    |
| Goals_GA                  | Goals             | GA             | Int64          | team_season_keeper_adv_for             | Gols sofridos                                                                         |
| Goals_OG                  | Goals             | OG             | Int64          | team_season_keeper_adv_for             | Gols contra                                                                           |
| Goals_PKA                 | Goals             | PKA            | Int64          | team_season_keeper_adv_for             | Pênaltis convertidos                                                                  |
| Launched_Att              | Launched          | Att            | Int64          | team_season_keeper_adv_for             | Tentativas de ação (contexto específico da categoria)                                 |
| Launched_Cmp              | Launched          | Cmp            | Int64          | team_season_keeper_adv_for             | Passes completados                                                                    |
| Launched_Cmp%             | Launched          | Cmp%           | Float64        | team_season_keeper_adv_for             | Porcentagem de passes completados                                                     |
| Passes_Att (GK)           | Passes            | Att (GK)       | Int64          | team_season_keeper_adv_for             | Lançamentos tentados pelo goleiro                                                     |
| Passes_AvgLen             | Passes            | AvgLen         | Float64        | team_season_keeper_adv_for             | Comprimento médio dos passes                                                          |
| Passes_Launch%            | Passes            | Launch%        | Float64        | team_season_keeper_adv_for             | Porcentagem de passes longos                                                          |
| Passes_Thr                | Passes            | Thr            | Int64          | team_season_keeper_adv_for             | Passes realizados com as mãos                                                         |
| Sweeper_#OPA              | Sweeper           | #OPA           | Int64          | team_season_keeper_adv_for             | Ações defensivas fora da área                                                         |
| Sweeper_#OPA/90           | Sweeper           | #OPA/90        | Float64        | team_season_keeper_adv_for             | Ações defensivas fora da área por 90 minutos                                          |
| Sweeper_AvgDist           | Sweeper           | AvgDist        | Float64        | team_season_keeper_adv_for             | Distância média das ações                                                             |
| players_used              | nan               | players_used   | Int64          | team_season_keeper_against             | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_keeper_against             | Link para página de estatísticas                                                      |
| Penalty Kicks_PKA         | Penalty Kicks     | PKA            | Int64          | team_season_keeper_against             | Pênaltis convertidos                                                                  |
| Penalty Kicks_PKatt       | Penalty Kicks     | PKatt          | Int64          | team_season_keeper_against             | Pênaltis cobrados                                                                     |
| Penalty Kicks_PKm         | Penalty Kicks     | PKm            | Int64          | team_season_keeper_against             | Pênaltis perdidos                                                                     |
| Penalty Kicks_PKsv        | Penalty Kicks     | PKsv           | Int64          | team_season_keeper_against             | Pênaltis defendidos                                                                   |
| Penalty Kicks_Save%       | Penalty Kicks     | Save%          | Float64        | team_season_keeper_against             | Porcentagem de defesas realizadas                                                     |
| Performance_CS            | Performance       | CS             | Int64          | team_season_keeper_against             | Clean sheets (jogos sem sofrer gol)                                                   |
| Performance_CS%           | Performance       | CS%            | Float64        | team_season_keeper_against             | Porcentagem de jogos sem sofrer gol                                                   |
| Performance_D             | Performance       | D              | Int64          | team_season_keeper_against             | Empates                                                                               |
| Performance_GA            | Performance       | GA             | Int64          | team_season_keeper_against             | Gols sofridos                                                                         |
| Performance_GA90          | Performance       | GA90           | Float64        | team_season_keeper_against             | Gols sofridos por 90 minutos                                                          |
| Performance_L             | Performance       | L              | Int64          | team_season_keeper_against             | Derrotas                                                                              |
| Performance_Save%         | Performance       | Save%          | Float64        | team_season_keeper_against             | Porcentagem de defesas realizadas                                                     |
| Performance_Saves         | Performance       | Saves          | Int64          | team_season_keeper_against             | Defesas realizadas                                                                    |
| Performance_SoTA          | Performance       | SoTA           | Int64          | team_season_keeper_against             | Chutes no alvo enfrentados                                                            |
| Performance_W             | Performance       | W              | Int64          | team_season_keeper_against             | Vitórias                                                                              |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_keeper_against             | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_keeper_against             | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_keeper_against             | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | team_season_keeper_against             | Partidas iniciadas como titular                                                       |
| players_used              | nan               | players_used   | Int64          | team_season_keeper_for                 | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_keeper_for                 | Link para página de estatísticas                                                      |
| Penalty Kicks_PKA         | Penalty Kicks     | PKA            | Int64          | team_season_keeper_for                 | Pênaltis convertidos                                                                  |
| Penalty Kicks_PKatt       | Penalty Kicks     | PKatt          | Int64          | team_season_keeper_for                 | Pênaltis cobrados                                                                     |
| Penalty Kicks_PKm         | Penalty Kicks     | PKm            | Int64          | team_season_keeper_for                 | Pênaltis perdidos                                                                     |
| Penalty Kicks_PKsv        | Penalty Kicks     | PKsv           | Int64          | team_season_keeper_for                 | Pênaltis defendidos                                                                   |
| Penalty Kicks_Save%       | Penalty Kicks     | Save%          | Float64        | team_season_keeper_for                 | Porcentagem de defesas realizadas                                                     |
| Performance_CS            | Performance       | CS             | Int64          | team_season_keeper_for                 | Clean sheets (jogos sem sofrer gol)                                                   |
| Performance_CS%           | Performance       | CS%            | Float64        | team_season_keeper_for                 | Porcentagem de jogos sem sofrer gol                                                   |
| Performance_D             | Performance       | D              | Int64          | team_season_keeper_for                 | Empates                                                                               |
| Performance_GA            | Performance       | GA             | Int64          | team_season_keeper_for                 | Gols sofridos                                                                         |
| Performance_GA90          | Performance       | GA90           | Float64        | team_season_keeper_for                 | Gols sofridos por 90 minutos                                                          |
| Performance_L             | Performance       | L              | Int64          | team_season_keeper_for                 | Derrotas                                                                              |
| Performance_Save%         | Performance       | Save%          | Float64        | team_season_keeper_for                 | Porcentagem de defesas realizadas                                                     |
| Performance_Saves         | Performance       | Saves          | Int64          | team_season_keeper_for                 | Defesas realizadas                                                                    |
| Performance_SoTA          | Performance       | SoTA           | Int64          | team_season_keeper_for                 | Chutes no alvo enfrentados                                                            |
| Performance_W             | Performance       | W              | Int64          | team_season_keeper_for                 | Vitórias                                                                              |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_keeper_for                 | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_keeper_for                 | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_keeper_for                 | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | team_season_keeper_for                 | Partidas iniciadas como titular                                                       |
| 90s                       | nan               | 90s            | Int64          | team_season_misc_against               | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_misc_against               | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_misc_against               | Link para página de estatísticas                                                      |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | team_season_misc_against               | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | team_season_misc_against               | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | team_season_misc_against               | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | team_season_misc_against               | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_season_misc_against               | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_season_misc_against               | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | team_season_misc_against               | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | team_season_misc_against               | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | team_season_misc_against               | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | team_season_misc_against               | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | team_season_misc_against               | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | team_season_misc_against               | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | team_season_misc_against               | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | team_season_misc_against               | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | team_season_misc_against               | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | team_season_misc_against               | Desarmes bem-sucedidos                                                                |
| 90s                       | nan               | 90s            | Int64          | team_season_misc_for                   | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_misc_for                   | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_misc_for                   | Link para página de estatísticas                                                      |
| Aerial Duels_Lost         | Aerial Duels      | Lost           | Int64          | team_season_misc_for                   | Duelos aéreos perdidos                                                                |
| Aerial Duels_Won          | Aerial Duels      | Won            | Int64          | team_season_misc_for                   | Duelos aéreos vencidos                                                                |
| Aerial Duels_Won%         | Aerial Duels      | Won%           | Float64        | team_season_misc_for                   | Porcentagem de duelos aéreos vencidos                                                 |
| Performance_2CrdY         | Performance       | 2CrdY          | Int64          | team_season_misc_for                   | Segundo cartão amarelo recebido                                                       |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_season_misc_for                   | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_season_misc_for                   | Cartões amarelos                                                                      |
| Performance_Crs           | Performance       | Crs            | Int64          | team_season_misc_for                   | Cruzamentos                                                                           |
| Performance_Fld           | Performance       | Fld            | Int64          | team_season_misc_for                   | Faltas sofridas                                                                       |
| Performance_Fls           | Performance       | Fls            | Int64          | team_season_misc_for                   | Faltas cometidas                                                                      |
| Performance_Int           | Performance       | Int            | Int64          | team_season_misc_for                   | Interceptações realizadas                                                             |
| Performance_OG            | Performance       | OG             | Int64          | team_season_misc_for                   | Gols contra                                                                           |
| Performance_Off           | Performance       | Off            | Int64          | team_season_misc_for                   | Impedimentos                                                                          |
| Performance_PKcon         | Performance       | PKcon          | Int64          | team_season_misc_for                   | Pênaltis concedidos                                                                   |
| Performance_PKwon         | Performance       | PKwon          | Int64          | team_season_misc_for                   | Pênaltis conquistados                                                                 |
| Performance_Recov         | Performance       | Recov          | Int64          | team_season_misc_for                   | Bolas recuperadas                                                                     |
| Performance_TklW          | Performance       | TklW           | Int64          | team_season_misc_for                   | Desarmes bem-sucedidos                                                                |
| 1/3                       | nan               | 1/3            | Int64          | team_season_passing_against            | Passes para o terço final do campo                                                    |
| 90s                       | nan               | 90s            | Int64          | team_season_passing_against            | Número de partidas completas (90 minutos)                                             |
| Ast                       | nan               | Ast            | Int64          | team_season_passing_against            | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | team_season_passing_against            | Cruzamentos para área de pênalti                                                      |
| KP                        | nan               | KP             | Int64          | team_season_passing_against            | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | team_season_passing_against            | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | team_season_passing_against            | Passes progressivos realizados                                                        |
| players_used              | nan               | players_used   | Int64          | team_season_passing_against            | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_passing_against            | Link para página de estatísticas                                                      |
| xAG                       | nan               | xAG            | Float64        | team_season_passing_against            | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_A-xAG            | Expected          | A-xAG          | Float64        | team_season_passing_against            | Diferença entre assistências e expectativas de assistência esperadas                  |
| Expected_xA               | Expected          | xA             | Float64        | team_season_passing_against            | Expected Assists                                                                      |
| Long_Att                  | Long              | Att            | Int64          | team_season_passing_against            | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | team_season_passing_against            | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | team_season_passing_against            | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | team_season_passing_against            | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | team_season_passing_against            | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | team_season_passing_against            | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | team_season_passing_against            | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | team_season_passing_against            | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | team_season_passing_against            | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | team_season_passing_against            | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | team_season_passing_against            | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | team_season_passing_against            | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | team_season_passing_against            | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | team_season_passing_against            | Distância total percorrida                                                            |
| 1/3                       | nan               | 1/3            | Int64          | team_season_passing_for                | Passes para o terço final do campo                                                    |
| 90s                       | nan               | 90s            | Int64          | team_season_passing_for                | Número de partidas completas (90 minutos)                                             |
| Ast                       | nan               | Ast            | Int64          | team_season_passing_for                | Assistências para gol                                                                 |
| CrsPA                     | nan               | CrsPA          | Int64          | team_season_passing_for                | Cruzamentos para área de pênalti                                                      |
| KP                        | nan               | KP             | Int64          | team_season_passing_for                | Passes-chave que resultaram em finalização                                            |
| PPA                       | nan               | PPA            | Int64          | team_season_passing_for                | Passes para área de pênalti                                                           |
| PrgP                      | nan               | PrgP           | Int64          | team_season_passing_for                | Passes progressivos realizados                                                        |
| players_used              | nan               | players_used   | Int64          | team_season_passing_for                | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_passing_for                | Link para página de estatísticas                                                      |
| xAG                       | nan               | xAG            | Float64        | team_season_passing_for                | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_A-xAG            | Expected          | A-xAG          | Float64        | team_season_passing_for                | Diferença entre assistências e expectativas de assistência esperadas                  |
| Expected_xA               | Expected          | xA             | Float64        | team_season_passing_for                | Expected Assists                                                                      |
| Long_Att                  | Long              | Att            | Int64          | team_season_passing_for                | Tentativas de ação (contexto específico da categoria)                                 |
| Long_Cmp                  | Long              | Cmp            | Int64          | team_season_passing_for                | Passes completados                                                                    |
| Long_Cmp%                 | Long              | Cmp%           | Float64        | team_season_passing_for                | Porcentagem de passes completados                                                     |
| Medium_Att                | Medium            | Att            | Int64          | team_season_passing_for                | Tentativas de ação (contexto específico da categoria)                                 |
| Medium_Cmp                | Medium            | Cmp            | Int64          | team_season_passing_for                | Passes completados                                                                    |
| Medium_Cmp%               | Medium            | Cmp%           | Float64        | team_season_passing_for                | Porcentagem de passes completados                                                     |
| Short_Att                 | Short             | Att            | Int64          | team_season_passing_for                | Tentativas de ação (contexto específico da categoria)                                 |
| Short_Cmp                 | Short             | Cmp            | Int64          | team_season_passing_for                | Passes completados                                                                    |
| Short_Cmp%                | Short             | Cmp%           | Float64        | team_season_passing_for                | Porcentagem de passes completados                                                     |
| Total_Att                 | Total             | Att            | Int64          | team_season_passing_for                | Tentativas de ação (contexto específico da categoria)                                 |
| Total_Cmp                 | Total             | Cmp            | Int64          | team_season_passing_for                | Passes completados                                                                    |
| Total_Cmp%                | Total             | Cmp%           | Float64        | team_season_passing_for                | Porcentagem de passes completados                                                     |
| Total_PrgDist             | Total             | PrgDist        | Int64          | team_season_passing_for                | Distância progressiva percorrida                                                      |
| Total_TotDist             | Total             | TotDist        | Int64          | team_season_passing_for                | Distância total percorrida                                                            |
| 90s                       | nan               | 90s            | Int64          | team_season_passing_types_against      | Número de partidas completas (90 minutos)                                             |
| Att                       | nan               | Att            | Int64          | team_season_passing_types_against      | Tentativas de ação (contexto específico da categoria)                                 |
| players_used              | nan               | players_used   | Int64          | team_season_passing_types_against      | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_passing_types_against      | Link para página de estatísticas                                                      |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | team_season_passing_types_against      | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | team_season_passing_types_against      | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | team_season_passing_types_against      | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | team_season_passing_types_against      | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | team_season_passing_types_against      | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | team_season_passing_types_against      | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | team_season_passing_types_against      | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | team_season_passing_types_against      | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | team_season_passing_types_against      | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | team_season_passing_types_against      | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | team_season_passing_types_against      | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | team_season_passing_types_against      | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | team_season_passing_types_against      | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | team_season_passing_types_against      | Arremessos laterais                                                                   |
| 90s                       | nan               | 90s            | Int64          | team_season_passing_types_for          | Número de partidas completas (90 minutos)                                             |
| Att                       | nan               | Att            | Int64          | team_season_passing_types_for          | Tentativas de ação (contexto específico da categoria)                                 |
| players_used              | nan               | players_used   | Int64          | team_season_passing_types_for          | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_passing_types_for          | Link para página de estatísticas                                                      |
| Corner Kicks_In           | Corner Kicks      | In             | Int64          | team_season_passing_types_for          | Escanteios para dentro da área                                                        |
| Corner Kicks_Out          | Corner Kicks      | Out            | Int64          | team_season_passing_types_for          | Escanteios para fora da área                                                          |
| Corner Kicks_Str          | Corner Kicks      | Str            | Int64          | team_season_passing_types_for          | Escanteios rasteiros                                                                  |
| Outcomes_Blocks           | Outcomes          | Blocks         | Int64          | team_season_passing_types_for          | Total de bloqueios realizados                                                         |
| Outcomes_Cmp              | Outcomes          | Cmp            | Int64          | team_season_passing_types_for          | Passes completados                                                                    |
| Outcomes_Off              | Outcomes          | Off            | Int64          | team_season_passing_types_for          | Impedimentos                                                                          |
| Pass Types_CK             | Pass Types        | CK             | Int64          | team_season_passing_types_for          | Cobranças de escanteio                                                                |
| Pass Types_Crs            | Pass Types        | Crs            | Int64          | team_season_passing_types_for          | Cruzamentos                                                                           |
| Pass Types_Dead           | Pass Types        | Dead           | Int64          | team_season_passing_types_for          | Bolas paradas                                                                         |
| Pass Types_FK             | Pass Types        | FK             | Int64          | team_season_passing_types_for          | Cobranças de falta                                                                    |
| Pass Types_Live           | Pass Types        | Live           | Int64          | team_season_passing_types_for          | Bolas em movimento                                                                    |
| Pass Types_Sw             | Pass Types        | Sw             | Int64          | team_season_passing_types_for          | Passes longos diagonais                                                               |
| Pass Types_TB             | Pass Types        | TB             | Int64          | team_season_passing_types_for          | Passes em profundidade                                                                |
| Pass Types_TI             | Pass Types        | TI             | Int64          | team_season_passing_types_for          | Arremessos laterais                                                                   |
| Age                       | nan               | Age            | Float64        | team_season_playing_time_against       | nan                                                                                   |
| players_used              | nan               | players_used   | Int64          | team_season_playing_time_against       | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_playing_time_against       | Link para página de estatísticas                                                      |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_playing_time_against       | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_playing_time_against       | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_playing_time_against       | Minutos jogados                                                                       |
| Playing Time_Min%         | Playing Time      | Min%           | Int64          | team_season_playing_time_against       | Porcentagem de minutos possíveis jogados                                              |
| Playing Time_Mn/MP        | Playing Time      | Mn/MP          | Int64          | team_season_playing_time_against       | Média de minutos por partida                                                          |
| Starts_Compl              | Starts            | Compl          | Int64          | team_season_playing_time_against       | Partidas completas                                                                    |
| Starts_Mn/Start           | Starts            | Mn/Start       | Int64          | team_season_playing_time_against       | Média de minutos por titularidade                                                     |
| Starts_Starts             | Starts            | Starts         | Int64          | team_season_playing_time_against       | Partidas iniciadas como titular                                                       |
| Subs_Mn/Sub               | Subs              | Mn/Sub         | Int64          | team_season_playing_time_against       | Média de minutos como substituto                                                      |
| Subs_Subs                 | Subs              | Subs           | Int64          | team_season_playing_time_against       | Entradas como substituto                                                              |
| Subs_unSub                | Subs              | unSub          | Int64          | team_season_playing_time_against       | Jogos não utilizados como substituto                                                  |
| Team Success_+/-          | Team Success      | +/-            | Int64          | team_season_playing_time_against       | Saldo de gols com o jogador em campo                                                  |
| Team Success_+/-90        | Team Success      | +/-90          | Float64        | team_season_playing_time_against       | Saldo de gols por 90 minutos                                                          |
| Team Success_PPM          | Team Success      | PPM            | Float64        | team_season_playing_time_against       | Pontos por partida                                                                    |
| Team Success_onG          | Team Success      | onG            | Int64          | team_season_playing_time_against       | Gols marcados com o jogador em campo                                                  |
| Team Success_onGA         | Team Success      | onGA           | Int64          | team_season_playing_time_against       | Gols sofridos com o jogador em campo                                                  |
| Team Success (xG)_onxG    | Team Success (xG) | onxG           | Float64        | team_season_playing_time_against       | xG com jogador em campo                                                               |
| Team Success (xG)_onxGA   | Team Success (xG) | onxGA          | Float64        | team_season_playing_time_against       | xGA com jogador em campo                                                              |
| Team Success (xG)_xG+/-   | Team Success (xG) | xG+/-          | Float64        | team_season_playing_time_against       | Saldo de xG                                                                           |
| Team Success (xG)_xG+/-90 | Team Success (xG) | xG+/-90        | Float64        | team_season_playing_time_against       | Saldo de xG por 90 minutos                                                            |
| Age                       | nan               | Age            | Float64        | team_season_playing_time_for           | nan                                                                                   |
| players_used              | nan               | players_used   | Int64          | team_season_playing_time_for           | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_playing_time_for           | Link para página de estatísticas                                                      |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_playing_time_for           | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_playing_time_for           | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_playing_time_for           | Minutos jogados                                                                       |
| Playing Time_Min%         | Playing Time      | Min%           | Int64          | team_season_playing_time_for           | Porcentagem de minutos possíveis jogados                                              |
| Playing Time_Mn/MP        | Playing Time      | Mn/MP          | Int64          | team_season_playing_time_for           | Média de minutos por partida                                                          |
| Starts_Compl              | Starts            | Compl          | Int64          | team_season_playing_time_for           | Partidas completas                                                                    |
| Starts_Mn/Start           | Starts            | Mn/Start       | Int64          | team_season_playing_time_for           | Média de minutos por titularidade                                                     |
| Starts_Starts             | Starts            | Starts         | Int64          | team_season_playing_time_for           | Partidas iniciadas como titular                                                       |
| Subs_Mn/Sub               | Subs              | Mn/Sub         | Int64          | team_season_playing_time_for           | Média de minutos como substituto                                                      |
| Subs_Subs                 | Subs              | Subs           | Int64          | team_season_playing_time_for           | Entradas como substituto                                                              |
| Subs_unSub                | Subs              | unSub          | Int64          | team_season_playing_time_for           | Jogos não utilizados como substituto                                                  |
| Team Success_+/-          | Team Success      | +/-            | Int64          | team_season_playing_time_for           | Saldo de gols com o jogador em campo                                                  |
| Team Success_+/-90        | Team Success      | +/-90          | Float64        | team_season_playing_time_for           | Saldo de gols por 90 minutos                                                          |
| Team Success_PPM          | Team Success      | PPM            | Float64        | team_season_playing_time_for           | Pontos por partida                                                                    |
| Team Success_onG          | Team Success      | onG            | Int64          | team_season_playing_time_for           | Gols marcados com o jogador em campo                                                  |
| Team Success_onGA         | Team Success      | onGA           | Int64          | team_season_playing_time_for           | Gols sofridos com o jogador em campo                                                  |
| Team Success (xG)_onxG    | Team Success (xG) | onxG           | Float64        | team_season_playing_time_for           | xG com jogador em campo                                                               |
| Team Success (xG)_onxGA   | Team Success (xG) | onxGA          | Float64        | team_season_playing_time_for           | xGA com jogador em campo                                                              |
| Team Success (xG)_xG+/-   | Team Success (xG) | xG+/-          | Float64        | team_season_playing_time_for           | Saldo de xG                                                                           |
| Team Success (xG)_xG+/-90 | Team Success (xG) | xG+/-90        | Float64        | team_season_playing_time_for           | Saldo de xG por 90 minutos                                                            |
| 90s                       | nan               | 90s            | Int64          | team_season_possession_against         | Número de partidas completas (90 minutos)                                             |
| Poss                      | nan               | Poss           | Float64        | team_season_possession_against         | Percentual de posse de bola                                                           |
| players_used              | nan               | players_used   | Int64          | team_season_possession_against         | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_possession_against         | Link para página de estatísticas                                                      |
| Carries_1/3               | Carries           | 1/3            | Int64          | team_season_possession_against         | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | team_season_possession_against         | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | team_season_possession_against         | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | team_season_possession_against         | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | team_season_possession_against         | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | team_season_possession_against         | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | team_season_possession_against         | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | team_season_possession_against         | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | team_season_possession_against         | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | team_season_possession_against         | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | team_season_possession_against         | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | team_season_possession_against         | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | team_season_possession_against         | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | team_season_possession_against         | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | team_season_possession_against         | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | team_season_possession_against         | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | team_season_possession_against         | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | team_season_possession_against         | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | team_season_possession_against         | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | team_season_possession_against         | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | team_season_possession_against         | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | team_season_possession_against         | Total de toques na bola                                                               |
| 90s                       | nan               | 90s            | Int64          | team_season_possession_for             | Número de partidas completas (90 minutos)                                             |
| Poss                      | nan               | Poss           | Float64        | team_season_possession_for             | Percentual de posse de bola                                                           |
| players_used              | nan               | players_used   | Int64          | team_season_possession_for             | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_possession_for             | Link para página de estatísticas                                                      |
| Carries_1/3               | Carries           | 1/3            | Int64          | team_season_possession_for             | Conduções para o terço final                                                          |
| Carries_CPA               | Carries           | CPA            | Int64          | team_season_possession_for             | Conduções para área de pênalti                                                        |
| Carries_Carries           | Carries           | Carries        | Int64          | team_season_possession_for             | Conduções de bola realizadas                                                          |
| Carries_Dis               | Carries           | Dis            | Int64          | team_season_possession_for             | Conduções perdidas                                                                    |
| Carries_Mis               | Carries           | Mis            | Int64          | team_season_possession_for             | Controles mal-sucedidos                                                               |
| Carries_PrgC              | Carries           | PrgC           | Int64          | team_season_possession_for             | Conduções progressivas                                                                |
| Carries_PrgDist           | Carries           | PrgDist        | Int64          | team_season_possession_for             | Distância progressiva percorrida                                                      |
| Carries_TotDist           | Carries           | TotDist        | Int64          | team_season_possession_for             | Distância total percorrida                                                            |
| Receiving_PrgR            | Receiving         | PrgR           | Int64          | team_season_possession_for             | Recebimentos progressivos                                                             |
| Receiving_Rec             | Receiving         | Rec            | Int64          | team_season_possession_for             | Bolas recebidas                                                                       |
| Take-Ons_Att              | Take-Ons          | Att            | Int64          | team_season_possession_for             | Tentativas de ação (contexto específico da categoria)                                 |
| Take-Ons_Succ             | Take-Ons          | Succ           | Int64          | team_season_possession_for             | Dribles bem-sucedidos                                                                 |
| Take-Ons_Succ%            | Take-Ons          | Succ%          | Float64        | team_season_possession_for             | Porcentagem de dribles bem-sucedidos                                                  |
| Take-Ons_Tkld             | Take-Ons          | Tkld           | Int64          | team_season_possession_for             | Vezes desarmado                                                                       |
| Take-Ons_Tkld%            | Take-Ons          | Tkld%          | Float64        | team_season_possession_for             | Porcentagem de vezes desarmado                                                        |
| Touches_Att 3rd           | Touches           | Att 3rd        | Int64          | team_season_possession_for             | Ações no terço ofensivo                                                               |
| Touches_Att Pen           | Touches           | Att Pen        | Int64          | team_season_possession_for             | Toques na área adversária                                                             |
| Touches_Def 3rd           | Touches           | Def 3rd        | Int64          | team_season_possession_for             | Ações no terço defensivo                                                              |
| Touches_Def Pen           | Touches           | Def Pen        | Int64          | team_season_possession_for             | Toques na própria área                                                                |
| Touches_Live              | Touches           | Live           | Int64          | team_season_possession_for             | Bolas em movimento                                                                    |
| Touches_Mid 3rd           | Touches           | Mid 3rd        | Int64          | team_season_possession_for             | Ações no terço médio                                                                  |
| Touches_Touches           | Touches           | Touches        | Int64          | team_season_possession_for             | Total de toques na bola                                                               |
| 90s                       | nan               | 90s            | Int64          | team_season_shooting_against           | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_shooting_against           | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_shooting_against           | Link para página de estatísticas                                                      |
| Expected_G-xG             | Expected          | G-xG           | Float64        | team_season_shooting_against           | Diferença entre gols e xG                                                             |
| Expected_np:G-xG          | Expected          | np:G-xG        | Float64        | team_season_shooting_against           | Diferença entre gols sem pênalti e xG                                                 |
| Expected_npxG             | Expected          | npxG           | Float64        | team_season_shooting_against           | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG/Sh          | Expected          | npxG/Sh        | Float64        | team_season_shooting_against           | npxG por chute                                                                        |
| Expected_xG               | Expected          | xG             | Float64        | team_season_shooting_against           | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Standard_Dist             | Standard          | Dist           | Float64        | team_season_shooting_against           | Distância média dos chutes                                                            |
| Standard_FK               | Standard          | FK             | Int64          | team_season_shooting_against           | Cobranças de falta                                                                    |
| Standard_G/Sh             | Standard          | G/Sh           | Float64        | team_season_shooting_against           | Média de gols por chute                                                               |
| Standard_G/SoT            | Standard          | G/SoT          | Float64        | team_season_shooting_against           | Média de gols por chute no alvo                                                       |
| Standard_Gls              | Standard          | Gls            | Int64          | team_season_shooting_against           | Gols marcados                                                                         |
| Standard_PK               | Standard          | PK             | Int64          | team_season_shooting_against           | Pênaltis convertidos                                                                  |
| Standard_PKatt            | Standard          | PKatt          | Int64          | team_season_shooting_against           | Pênaltis cobrados                                                                     |
| Standard_Sh               | Standard          | Sh             | Int64          | team_season_shooting_against           | Chutes bloqueados                                                                     |
| Standard_Sh/90            | Standard          | Sh/90          | Float64        | team_season_shooting_against           | Média de chutes por 90 minutos                                                        |
| Standard_SoT              | Standard          | SoT            | Int64          | team_season_shooting_against           | Chutes no alvo                                                                        |
| Standard_SoT%             | Standard          | SoT%           | Float64        | team_season_shooting_against           | Porcentagem de chutes no alvo                                                         |
| Standard_SoT/90           | Standard          | SoT/90         | Float64        | team_season_shooting_against           | Chutes no alvo por 90 minutos                                                         |
| 90s                       | nan               | 90s            | Int64          | team_season_shooting_for               | Número de partidas completas (90 minutos)                                             |
| players_used              | nan               | players_used   | Int64          | team_season_shooting_for               | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_shooting_for               | Link para página de estatísticas                                                      |
| Expected_G-xG             | Expected          | G-xG           | Float64        | team_season_shooting_for               | Diferença entre gols e xG                                                             |
| Expected_np:G-xG          | Expected          | np:G-xG        | Float64        | team_season_shooting_for               | Diferença entre gols sem pênalti e xG                                                 |
| Expected_npxG             | Expected          | npxG           | Float64        | team_season_shooting_for               | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG/Sh          | Expected          | npxG/Sh        | Float64        | team_season_shooting_for               | npxG por chute                                                                        |
| Expected_xG               | Expected          | xG             | Float64        | team_season_shooting_for               | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Standard_Dist             | Standard          | Dist           | Float64        | team_season_shooting_for               | Distância média dos chutes                                                            |
| Standard_FK               | Standard          | FK             | Int64          | team_season_shooting_for               | Cobranças de falta                                                                    |
| Standard_G/Sh             | Standard          | G/Sh           | Float64        | team_season_shooting_for               | Média de gols por chute                                                               |
| Standard_G/SoT            | Standard          | G/SoT          | Float64        | team_season_shooting_for               | Média de gols por chute no alvo                                                       |
| Standard_Gls              | Standard          | Gls            | Int64          | team_season_shooting_for               | Gols marcados                                                                         |
| Standard_PK               | Standard          | PK             | Int64          | team_season_shooting_for               | Pênaltis convertidos                                                                  |
| Standard_PKatt            | Standard          | PKatt          | Int64          | team_season_shooting_for               | Pênaltis cobrados                                                                     |
| Standard_Sh               | Standard          | Sh             | Int64          | team_season_shooting_for               | Chutes bloqueados                                                                     |
| Standard_Sh/90            | Standard          | Sh/90          | Float64        | team_season_shooting_for               | Média de chutes por 90 minutos                                                        |
| Standard_SoT              | Standard          | SoT            | Int64          | team_season_shooting_for               | Chutes no alvo                                                                        |
| Standard_SoT%             | Standard          | SoT%           | Float64        | team_season_shooting_for               | Porcentagem de chutes no alvo                                                         |
| Standard_SoT/90           | Standard          | SoT/90         | Float64        | team_season_shooting_for               | Chutes no alvo por 90 minutos                                                         |
| Age                       | nan               | Age            | Float64        | team_season_standard_against           | nan                                                                                   |
| Poss                      | nan               | Poss           | Float64        | team_season_standard_against           | Percentual de posse de bola                                                           |
| players_used              | nan               | players_used   | Int64          | team_season_standard_against           | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_standard_against           | Link para página de estatísticas                                                      |
| Expected_npxG             | Expected          | npxG           | Float64        | team_season_standard_against           | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG+xAG         | Expected          | npxG+xAG       | Float64        | team_season_standard_against           | Soma de npxG e xAG                                                                    |
| Expected_xAG              | Expected          | xAG            | Float64        | team_season_standard_against           | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_xG               | Expected          | xG             | Float64        | team_season_standard_against           | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_Ast        | Per 90 Minutes    | Ast            | Float64        | team_season_standard_against           | Assistências para gol                                                                 |
| Per 90 Minutes_G+A        | Per 90 Minutes    | G+A            | Float64        | team_season_standard_against           | Soma de gols e assistências                                                           |
| Per 90 Minutes_G+A-PK     | Per 90 Minutes    | G+A-PK         | Float64        | team_season_standard_against           | Soma de gols e assistências, excluindo pênaltis                                       |
| Per 90 Minutes_G-PK       | Per 90 Minutes    | G-PK           | Float64        | team_season_standard_against           | Gols excluindo pênaltis                                                               |
| Per 90 Minutes_Gls        | Per 90 Minutes    | Gls            | Float64        | team_season_standard_against           | Gols marcados                                                                         |
| Per 90 Minutes_npxG       | Per 90 Minutes    | npxG           | Float64        | team_season_standard_against           | Expected Goals excluindo pênaltis                                                     |
| Per 90 Minutes_npxG+xAG   | Per 90 Minutes    | npxG+xAG       | Float64        | team_season_standard_against           | Soma de npxG e xAG                                                                    |
| Per 90 Minutes_xAG        | Per 90 Minutes    | xAG            | Float64        | team_season_standard_against           | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Per 90 Minutes_xG         | Per 90 Minutes    | xG             | Float64        | team_season_standard_against           | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_xG+xAG     | Per 90 Minutes    | xG+xAG         | Float64        | team_season_standard_against           | Soma de xG e xAG                                                                      |
| Performance_Ast           | Performance       | Ast            | Int64          | team_season_standard_against           | Assistências para gol                                                                 |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_season_standard_against           | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_season_standard_against           | Cartões amarelos                                                                      |
| Performance_G+A           | Performance       | G+A            | Int64          | team_season_standard_against           | Soma de gols e assistências                                                           |
| Performance_G-PK          | Performance       | G-PK           | Int64          | team_season_standard_against           | Gols excluindo pênaltis                                                               |
| Performance_Gls           | Performance       | Gls            | Int64          | team_season_standard_against           | Gols marcados                                                                         |
| Performance_PK            | Performance       | PK             | Int64          | team_season_standard_against           | Pênaltis convertidos                                                                  |
| Performance_PKatt         | Performance       | PKatt          | Int64          | team_season_standard_against           | Pênaltis cobrados                                                                     |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_standard_against           | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_standard_against           | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_standard_against           | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | team_season_standard_against           | Partidas iniciadas como titular                                                       |
| Progression_PrgC          | Progression       | PrgC           | Int64          | team_season_standard_against           | Conduções progressivas                                                                |
| Progression_PrgP          | Progression       | PrgP           | Int64          | team_season_standard_against           | Passes progressivos realizados                                                        |
| Age                       | nan               | Age            | Float64        | team_season_standard_for               | nan                                                                                   |
| Poss                      | nan               | Poss           | Float64        | team_season_standard_for               | Percentual de posse de bola                                                           |
| players_used              | nan               | players_used   | Int64          | team_season_standard_for               | Número de jogadores utilizados                                                        |
| url                       | nan               | url            | object         | team_season_standard_for               | Link para página de estatísticas                                                      |
| Expected_npxG             | Expected          | npxG           | Float64        | team_season_standard_for               | Expected Goals excluindo pênaltis                                                     |
| Expected_npxG+xAG         | Expected          | npxG+xAG       | Float64        | team_season_standard_for               | Soma de npxG e xAG                                                                    |
| Expected_xAG              | Expected          | xAG            | Float64        | team_season_standard_for               | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Expected_xG               | Expected          | xG             | Float64        | team_season_standard_for               | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_Ast        | Per 90 Minutes    | Ast            | Float64        | team_season_standard_for               | Assistências para gol                                                                 |
| Per 90 Minutes_G+A        | Per 90 Minutes    | G+A            | Float64        | team_season_standard_for               | Soma de gols e assistências                                                           |
| Per 90 Minutes_G+A-PK     | Per 90 Minutes    | G+A-PK         | Float64        | team_season_standard_for               | Soma de gols e assistências, excluindo pênaltis                                       |
| Per 90 Minutes_G-PK       | Per 90 Minutes    | G-PK           | Float64        | team_season_standard_for               | Gols excluindo pênaltis                                                               |
| Per 90 Minutes_Gls        | Per 90 Minutes    | Gls            | Float64        | team_season_standard_for               | Gols marcados                                                                         |
| Per 90 Minutes_npxG       | Per 90 Minutes    | npxG           | Float64        | team_season_standard_for               | Expected Goals excluindo pênaltis                                                     |
| Per 90 Minutes_npxG+xAG   | Per 90 Minutes    | npxG+xAG       | Float64        | team_season_standard_for               | Soma de npxG e xAG                                                                    |
| Per 90 Minutes_xAG        | Per 90 Minutes    | xAG            | Float64        | team_season_standard_for               | Expected Assisted Goals - Probabilidade de uma assistência resultar em gol            |
| Per 90 Minutes_xG         | Per 90 Minutes    | xG             | Float64        | team_season_standard_for               | Expected Goals - Probabilidade de gol baseada na qualidade do chute                   |
| Per 90 Minutes_xG+xAG     | Per 90 Minutes    | xG+xAG         | Float64        | team_season_standard_for               | Soma de xG e xAG                                                                      |
| Performance_Ast           | Performance       | Ast            | Int64          | team_season_standard_for               | Assistências para gol                                                                 |
| Performance_CrdR          | Performance       | CrdR           | Int64          | team_season_standard_for               | Cartões vermelhos diretos                                                             |
| Performance_CrdY          | Performance       | CrdY           | Int64          | team_season_standard_for               | Cartões amarelos                                                                      |
| Performance_G+A           | Performance       | G+A            | Int64          | team_season_standard_for               | Soma de gols e assistências                                                           |
| Performance_G-PK          | Performance       | G-PK           | Int64          | team_season_standard_for               | Gols excluindo pênaltis                                                               |
| Performance_Gls           | Performance       | Gls            | Int64          | team_season_standard_for               | Gols marcados                                                                         |
| Performance_PK            | Performance       | PK             | Int64          | team_season_standard_for               | Pênaltis convertidos                                                                  |
| Performance_PKatt         | Performance       | PKatt          | Int64          | team_season_standard_for               | Pênaltis cobrados                                                                     |
| Playing Time_90s          | Playing Time      | 90s            | Int64          | team_season_standard_for               | Número de partidas completas (90 minutos)                                             |
| Playing Time_MP           | Playing Time      | MP             | Int64          | team_season_standard_for               | Partidas jogadas                                                                      |
| Playing Time_Min          | Playing Time      | Min            | Int64          | team_season_standard_for               | Minutos jogados                                                                       |
| Playing Time_Starts       | Playing Time      | Starts         | Int64          | team_season_standard_for               | Partidas iniciadas como titular                                                       |
| Progression_PrgC          | Progression       | PrgC           | Int64          | team_season_standard_for               | Conduções progressivas                                                                |
| Progression_PrgP          | Progression       | PrgP           | Int64          | team_season_standard_for               | Passes progressivos realizados                                                        |

## Tabelas do WhoScored

### 1. **Leagues (Ligas)**

- **Origem:** WhoScored
- **Método:** `whoscored.read_leagues()`
- **Descrição:** Identificação das ligas disponíveis no WhoScored.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** 1, **Colunas:** 3
- **Colunas:**
  - `league` (string): Identificador da liga
  - `region_id` (int): ID da região
  - `region` (string): Nome da região
  - `league_id` (int): ID da liga
- **Exemplo:**

  | league      | region_id | region | league_id |
  | ----------- | --------- | ------ | --------- |
  | BRA-Serie A | 31        | Brazil | 95        |

### 2. **Seasons (Temporadas)**

- **Origem:** WhoScored
- **Método:** `whoscored.read_seasons()`
- **Descrição:** Temporadas disponíveis para cada liga.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** 1, **Colunas:** 3
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `region_id` (int): ID da região
  - `league_id` (int): ID da liga
  - `season_id` (int): ID da temporada
- **Exemplo:**

  | league      | season | region_id | league_id | season_id |
  | ----------- | ------ | --------- | --------- | --------- |
  | BRA-Serie A | 2024   | 31        | 95        | 10003     |

### 3. Season Stages (Fases da Temporada)

- **Origem:** WhoScored
- **Método:** `whoscored.read_season_stages()`
- **Descrição:** Fases ou rodadas da competição.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** 1, **Colunas:** 5
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `region_id` (int): ID da região
  - `league_id` (int): ID da liga
  - `season_id` (int): ID da temporada
  - `stage_id` (int): ID da fase
  - `stage` (string): Nome da fase
- **Exemplo:**

  | league      | season | region_id | league_id | season_id | stage_id | stage |
  | ----------- | ------ | --------- | --------- | --------- | -------- | ----- |
  | BRA-Serie A | 2024   | 31        | 95        | 10003     | 22961    | None  |

### 4. Schedule (Cronograma de Jogos)

- **Origem:** WhoScored
- **Método:** `whoscored.read_schedule()`
- **Descrição:** Calendário completo com detalhes dos jogos da temporada.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** 380, **Colunas:** 43
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `game` (string): Identificador único do jogo
  - `stage_id` (int): ID da fase ou rodada
  - `game_id` (int): ID único do jogo
  - `status` (int): Status do jogo
  - `start_time` (datetime): Data e hora de início do jogo
  - `home_team_id` (int): ID do time da casa
  - `home_team` (string): Nome do time da casa
  - `home_yellow_cards` (int): Cartões amarelos do time da casa
  - `home_red_cards` (int): Cartões vermelhos do time da casa
  - `away_team_id` (int): ID do time visitante
  - `away_team` (string): Nome do time visitante
  - `away_yellow_cards` (int): Cartões amarelos do time visitante
  - `away_red_cards` (int): Cartões vermelhos do time visitante
  - `has_incidents_summary` (bool): Indica se há resumo de incidentes
  - `has_preview` (bool): Indica se há prévia do jogo
  - `score_changed_at` (datetime): Última atualização do placar
  - `elapsed` (string): Tempo decorrido de jogo
  - `last_scorer` (float): Último jogador a marcar
  - `is_top_match` (bool): Indica se é um jogo de destaque
  - `home_team_country_code` (string): Código do país do time da casa
  - `away_team_country_code` (string): Código do país do time visitante
  - `comment_count` (int): Número de comentários
  - `is_lineup_confirmed` (bool): Indica se a escalação está confirmada
  - `is_stream_available` (bool): Indica se há transmissão disponível
  - `match_is_opta` (bool): Indica se o jogo é Opta
  - `home_team_country_name` (string): Nome do país do time da casa
  - `away_team_country_name` (string): Nome do país do time visitante
  - `date` (datetime): Data do jogo
  - `home_score` (int): Gols do time da casa
  - `away_score` (int): Gols do time visitante
  - `incidents` (list): Lista de incidentes do jogo
  - `bets` (object): Informações de apostas
  - `aggregate_winner_field` (object): Campo do vencedor agregado
  - `winner_field` (float): Campo do vencedor
  - `period` (int): Período do jogo
  - `extra_result_field` (object): Campo de resultado extra
  - `home_extratime_score` (object): Placar da prorrogação do time da casa
  - `away_extratime_score` (object): Placar da prorrogação do time visitante
  - `home_penalty_score` (object): Placar dos pênaltis do time da casa
  - `away_penalty_score` (object): Placar dos pênaltis do time visitante
  - `started_at_utc` (datetime): Horário de início em UTC
  - `first_half_ended_at_utc` (datetime): Horário de término do primeiro tempo em UTC
  - `second_half_started_at_utc` (datetime): Horário de início do segundo tempo em UTC
  - `stage` (object): Fase ou estágio do jogo
- **Exemplo:**

  | league      | season | game                          | stage_id | game_id | status | start_time          | home_team_id | home_team | home_yellow_cards | home_red_cards | away_team_id | away_team | away_yellow_cards | away_red_cards | has_incidents_summary | has_preview | score_changed_at     | elapsed | last_scorer | is_top_match | home_team_country_code | away_team_country_code | comment_count | is_lineup_confirmed | is_stream_available | match_is_opta | home_team_country_name | away_team_country_name | date                      | home_score | away_score | incidents                                          | bets | aggregate_winner_field | winner_field | period | extra_result_field | home_extratime_score | away_extratime_score | home_penalty_score | away_penalty_score | started_at_utc       | first_half_ended_at_utc | second_half_started_at_utc | stage |
  | ----------- | ------ | ----------------------------- | -------- | ------- | ------ | ------------------- | ------------ | --------- | ----------------- | -------------- | ------------ | --------- | ----------------- | -------------- | --------------------- | ----------- | -------------------- | ------- | ----------- | ------------ | ---------------------- | ---------------------- | ------------- | ------------------- | ------------------- | ------------- | ---------------------- | ---------------------- | ------------------------- | ---------- | ---------- | -------------------------------------------------- | ---- | ---------------------- | ------------ | ------ | ------------------ | -------------------- | -------------------- | ------------------ | ------------------ | -------------------- | ----------------------- | -------------------------- | ----- |
  | BRA-Serie A | 2024   | 2024-04-13 Criciuma-Juventude | 22961    | 1806862 | 6      | 2024-04-13T22:30:00 | 2066         | Criciuma  | 4                 | 0              | 1220         | Juventude | 6                 | 0              | True                  | True        | 2024-04-14 00:02:16Z | FT      | 1.0         | False        | br                     | br                     | 0             | True                | False               | False         | Brazil                 | Brazil                 | 2024-04-13 21:30:00+00:00 | 1          | 1          | [{'minute': '36', 'type': 1, 'subType': 1, 'pl...] | None | None                   | NaN          | 7      | None               | None                 | None                 | None               | None               | 2024-04-13T21:33:41Z | 2024-04-13T22:25:48Z    | 2024-04-13T22:42:18Z       | None  |

### 5. Missing Players (Jogadores Indisponíveis)

- **Origem:** WhoScored
- **Método:** `whoscored.read_missing_players()`
- **Descrição:** Lista de jogadores lesionados ou suspensos.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** Variável, **Colunas:** 8
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `team` (string): Nome da equipe
  - `player` (string): Nome do jogador
  - `reason` (string): Motivo da indisponibilidade
  - `status` (string): Status do jogador
  - `return_date` (date): Data prevista de retorno
  - `last_updated` (datetime): Data da última atualização
- **Exemplo:**

  | league      | season | team     | player         | reason | status   | return_date | last_updated        |
  | ----------- | ------ | -------- | -------------- | ------ | -------- | ----------- | ------------------- |
  | BRA-Serie A | 2024   | Flamengo | Bruno Henrique | Lesão  | Duvidoso | 2024-04-20  | 2024-01-14 20:00:00 |

### 6. Events (Padrão)

- **Origem:** WhoScored
- **Método:** `whoscored.read_events()`
- **Descrição:** Eventos detalhados como passes, finalizações e faltas.
- **Parâmetros Utilizados:** Nenhum parâmetro adicional.
- **Linhas:** 1565, **Colunas:** 26
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `game` (string): Identificador da partida
  - `game_id` (int): ID único da partida
  - `period` (string): Período do jogo (FirstHalf, SecondHalf)
  - `minute` (int): Minuto do evento
  - `second` (float): Segundo do evento
  - `expanded_minute` (float): Minuto expandido do evento
  - `type` (string): Tipo de evento
  - `outcome_type` (string): Resultado do evento
  - `team_id` (int): ID da equipe
  - `team` (string): Nome da equipe
  - `player_id` (float): ID do jogador
  - `player` (string): Nome do jogador
  - `x` (float): Coordenada X do evento
  - `y` (float): Coordenada Y do evento
  - `end_x` (float): Coordenada X final do evento
  - `end_y` (float): Coordenada Y final do evento
  - `goal_mouth_y` (float): Coordenada Y da boca do gol
  - `goal_mouth_z` (float): Coordenada Z da boca do gol
  - `blocked_x` (float): Coordenada X do bloqueio
  - `blocked_y` (float): Coordenada Y do bloqueio
  - `qualifiers` (list): Qualificadores adicionais do evento
  - `is_touch` (bool): Indica se houve toque na bola
  - `is_shot` (bool): Indica se foi um chute
  - `is_goal` (bool): Indica se resultou em gol
- **Exemplo:**

  | league      | season | game                          | game_id | period    | minute | second | expanded_minute | type | outcome_type | team_id | team      | player_id | player   | x    | y    | end_x | end_y | goal_mouth_y | goal_mouth_z | blocked_x | blocked_y | qualifiers                                         | is_touch | is_shot | is_goal |
  | ----------- | ------ | ----------------------------- | ------- | --------- | ------ | ------ | --------------- | ---- | ------------ | ------- | --------- | --------- | -------- | ---- | ---- | ----- | ----- | ------------ | ------------ | --------- | --------- | -------------------------------------------------- | -------- | ------- | ------- |
  | BRA-Serie A | 2024   | 2024-04-13 Criciuma-Juventude | 1806862 | FirstHalf | 0      | 1.0    | 0               | Pass | Successful   | 1220    | Juventude | 101698.0  | Gilberto | 50.2 | 50.0 | 36.9  | 41.9  | NaN          | NaN          | NaN       | NaN       | [{'type': {'displayName': 'Angle', 'value': 21...] | True     | NaN     | NaN     |

### 7. Events (Raw)

- **Origem:** WhoScored
- **Método:** `whoscored.read_events(raw=True)`
- **Descrição:** Dados brutos em formato JSON dos eventos.
- **Parâmetros Utilizados:** `raw=True`
- **Linhas:** Variável, **Colunas:** 3
- **Colunas:**
  - `league` (string): Identificador da liga
  - `season` (int): Ano da temporada
  - `game_id` (int): ID do jogo
  - `events` (json): Dados brutos dos eventos em formato JSON
- **Exemplo:**

  | league      | season | game_id | events                                               |
  | ----------- | ------ | ------- | ---------------------------------------------------- |
  | BRA-Serie A | 2024   | 1806862 | {"event_id": 1234, "minute": 23, "second": 15, ... } |

### 8. Events (SPADL)

- **Origem:** WhoScored
- **Método:** `whoscored.read_events(match_id=example_game_ids, type='spadl')`
- **Descrição:** Eventos formatados no modelo SPADL para análises avançadas.
- **Parâmetros Utilizados:** `match_id`,`type='spadl'`
- **Linhas:** 1586, **Colunas:** 16
- **Colunas:**
  - `game_id` (int): ID único do jogo
  - `original_event_id` (float): ID do evento original
  - `period_id` (int): ID do período do jogo
  - `time_seconds` (float): Tempo do evento em segundos
  - `team_id` (int): ID da equipe
  - `player_id` (float): ID do jogador
  - `start_x` (float): Coordenada X inicial
  - `end_x` (float): Coordenada X final
  - `start_y` (float): Coordenada Y inicial
  - `end_y` (float): Coordenada Y final
  - `type_id` (int): ID do tipo de evento
  - `result_id` (int): ID do resultado do evento
  - `bodypart_id` (int): ID da parte do corpo usada
  - `action_id` (int): ID da ação
  - `player` (string): Nome do jogador
  - `team` (string): Nome da equipe
- **Exemplo:**

  | game_id | original_event_id | period_id | time_seconds | team_id | player_id | start_x | end_x  | start_y | end_y  | type_id | result_id | bodypart_id | action_id | player   | team      |
  | ------- | ----------------- | --------- | ------------ | ------- | --------- | ------- | ------ | ------- | ------ | ------- | --------- | ----------- | --------- | -------- | --------- |
  | 1806862 | 2672232031        | 1         | 1.0          | 1220    | 101698.0  | 52.290  | 66.255 | 34.000  | 39.508 | 0       | 1         | 0           | 0         | Gilberto | Juventude |
  | 1806862 | 2672232097        | 1         | 3.0          | 1220    | 514437.0  | 64.155  | 75.810 | 38.352  | 55.012 | 0       | 1         | 0           | 1         | Caíque   | Juventude |
  | 1806862 | NaN               | 1         | 3.5          | 1220    | 114096.0  | 75.810  | 68.775 | 55.012  | 54.604 | 21      | 1         | 0           | 2         | Jádson   | Juventude |

### 9. Events (Atomic-SPADL)

- **Origem:** WhoScored
- **Método:** `whoscored.read_events(match_id=example_game_ids, type='atomic-spadl')`
- **Descrição:** Versão atomizada dos eventos SPADL para análises avançadas.
- **Parâmetros Utilizados:** `match_id`, `type='atomic-spadl'`
- **Linhas:** 2600, **Colunas:** 15
- **Colunas:**
  - `game_id` (int): ID único do jogo
  - `original_event_id` (float): ID do evento original
  - `action_id` (int): ID da ação
  - `period_id` (int): ID do período do jogo
  - `time_seconds` (float): Tempo do evento em segundos
  - `team_id` (int): ID da equipe
  - `player_id` (float): ID do jogador
  - `x` (float): Coordenada X da ação
  - `y` (float): Coordenada Y da ação
  - `dx` (float): Mudança na coordenada X
  - `dy` (float): Mudança na coordenada Y
  - `type_id` (int): ID do tipo de ação
  - `bodypart_id` (int): ID da parte do corpo usada
  - `player` (string): Nome do jogador
  - `team` (string): Nome da equipe
- **Exemplo:**

  | game_id | original_event_id | action_id | period_id | time_seconds | team_id | player_id | x      | y      | dx     | dy     | type_id | bodypart_id | player   | team      |
  | ------- | ----------------- | --------- | --------- | ------------ | ------- | --------- | ------ | ------ | ------ | ------ | ------- | ----------- | -------- | --------- |
  | 1806862 | 2672232031        | 0         | 1         | 1.00         | 1220    | 101698.0  | 52.290 | 34.000 | 13.965 | 5.508  | 0       | 0           | Gilberto | Juventude |
  | 1806862 | 2672232031        | 1         | 1         | 2.00         | 1220    | 514437.0  | 66.255 | 39.508 | 0.000  | 0.000  | 23      | 0           | Caíque   | Juventude |
  | 1806862 | 2672232097        | 2         | 1         | 3.00         | 1220    | 514437.0  | 64.155 | 38.352 | 11.655 | 16.660 | 0       | 0           | Caíque   | Juventude |

### 10. Games Loader

- **Origem:** WhoScored
- **Método:** `loader.games(competition_id="BRA-Serie A", season_id="2024")`
- **Descrição:** Informações detalhadas sobre os jogos da temporada.
- **Parâmetros Utilizados:** `competition_id`, `season_id`
- **Linhas:** 1, **Colunas:** 15
- **Colunas:**
  - `game_id` (int): ID único do jogo
  - `season_id` (int): ID da temporada
  - `competition_id` (string): Identificador da competição
  - `game_day` (string): Dia do jogo
  - `game_date` (datetime): Data e hora do jogo
  - `home_team_id` (int): ID do time da casa
  - `away_team_id` (int): ID do time visitante
  - `home_score` (int): Gols marcados pelo time da casa
  - `away_score` (int): Gols marcados pelo time visitante
  - `duration` (int): Duração do jogo em minutos
  - `referee` (string): Nome do árbitro
  - `venue` (string): Nome do estádio onde o jogo foi realizado
  - `attendance` (int): Número de espectadores presentes
  - `home_manager` (string): Nome do treinador do time da casa
  - `away_manager` (string): Nome do treinador do time visitante
- **Exemplo:**

  | game_id | season_id | competition_id | game_day | game_date           | home_team_id | away_team_id | home_score | away_score | duration | referee                   | venue                   | attendance | home_manager    | away_manager          |
  | ------- | --------- | -------------- | -------- | ------------------- | ------------ | ------------ | ---------- | ---------- | -------- | ------------------------- | ----------------------- | ---------- | --------------- | --------------------- |
  | 1806862 | 2024      | BRA-Serie A    | None     | 2024-04-13T22:30:00 | 2066         | 1220         | 1          | 1          | 105      | Bruno Pereira Vasconcelos | Estádio Heriberto Hülse | 12408      | Cláudio Tencati | Roger Machado Marques |

### 11. Teams Loader

- **Origem:** WhoScored
- **Método:** `loader.teams(game_id=example_game_id)`
- **Descrição:** Identificação das equipes participantes em uma partida específica.
- **Parâmetros Utilizados:** `game_id`
- **Linhas:** 2, **Colunas:** 2
- **Colunas:**
  - `team_id` (int): ID único da equipe
  - `team_name` (string): Nome da equipe
- **Exemplo:**

  | team_id | team_name |
  | ------- | --------- |
  | 2066    | Criciuma  |
  | 1220    | Juventude |

### 12. Players Loader

- **Origem:** WhoScored
- **Método:** `loader.players(game_id=example_game_id)`
- **Descrição:** Dados dos jogadores em uma partida específica.
- **Parâmetros Utilizados:** `game_id`
- **Linhas:** 46, **Colunas:** 8
- **Colunas:**
  - `game_id` (int): ID único do jogo
  - `team_id` (int): ID da equipe do jogador
  - `player_id` (int): ID único do jogador
  - `player_name` (string): Nome do jogador
  - `is_starter` (bool): Indica se o jogador foi titular
  - `minutes_played` (int): Minutos jogados
  - `jersey_number` (int): Número da camisa
  - `starting_position` (string): Posição inicial do jogador
- **Exemplo:**

  | game_id | team_id | player_id | player_name | is_starter | minutes_played | jersey_number | starting_position |
  | ------- | ------- | --------- | ----------- | ---------- | -------------- | ------------- | ----------------- |
  | 1806862 | 2066    | 321245    | Alisson     | True       | 105            | 25            | GK                |
  | 1806862 | 2066    | 513492    | Claudinho   | True       | 85             | 27            | DR                |

### 13. Events Loader

- **Origem:** WhoScored
- **Método:** `loader.events(game_id=example_game_id)`
- **Descrição:** Eventos estruturados para análises específicas de uma partida.
- **Parâmetros Utilizados:** `game_id`
- **Linhas:** 1565, **Colunas:** 20
- **Colunas:**
  - `game_id` (int): ID único do jogo
  - `event_id` (int): ID único do evento
  - `period_id` (int): ID do período do jogo
  - `team_id` (int): ID da equipe envolvida no evento
  - `player_id` (float): ID do jogador envolvido no evento
  - `type_id` (float): ID do tipo de evento
  - `timestamp` (datetime): Data e hora do evento
  - `minute` (int): Minuto do evento
  - `second` (int): Segundo do evento
  - `outcome` (bool): Resultado do evento (sucesso ou falha)
  - `start_x` (float): Coordenada X inicial do evento
  - `start_y` (float): Coordenada Y inicial do evento
  - `end_x` (float): Coordenada X final do evento
  - `end_y` (float): Coordenada Y final do evento
  - `qualifiers` (dict): Qualificadores adicionais do evento
  - `related_player_id` (float): ID do jogador relacionado ao evento
  - `touch` (bool): Indica se houve toque na bola
  - `goal` (bool): Indica se resultou em gol
  - `shot` (bool): Indica se foi um chute
  - `type_name` (string): Nome do tipo de evento
- **Exemplo:**

  | game_id | event_id   | period_id | team_id | player_id | type_id | timestamp           | minute | second | outcome | start_x | start_y | end_x | end_y | qualifiers | related_player_id | touch | goal  | shot  | type_name |
  | ------- | ---------- | --------- | ------- | --------- | ------- | ------------------- | ------ | ------ | ------- | ------- | ------- | ----- | ----- | ---------- | ----------------- | ----- | ----- | ----- | --------- |
  | 1806862 | 2672227645 | 1         | 2066    | NaN       | 32      | 2024-04-13 22:30:00 | 0      | 0      | True    | 0.0     | 0.0     | 0.0   | 0.0   | {}         | NaN               | False | False | False | start     |
