# cSpell:disable

import os
import soccerdata as sd
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from typing import Optional, Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do ChromeDriver
driver_path = r"C:\Users\pesso\chromedriver-win64\chromedriver.exe"
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Inicializando o driver
driver = webdriver.Chrome(service=service, options=options)

pd.set_option('display.max_columns', None)

# Configurações
LEAGUE = 'BRA-Serie A'
SEASON = '2024'
TEAM = 'Cruzeiro'
MATCH_ID_FBREF = "9650b0b3"  # Exemplo de ID de partida
MATCH_ID_WHOSCORED = 1806973
BASE_DIR = r'E:\Desenvolvimento Profissional\Data Science\Python\Projetos\01_DataFootball\01_data_football_analytics\data\raw'

league_season_dir = os.path.join(BASE_DIR, 'fbref', f'{LEAGUE}_{SEASON}')

if not os.path.exists(league_season_dir):
    os.makedirs(league_season_dir)

# Lista de tipos de estatísticas para cada categoria
TEAM_SEASON_TYPES = [
    "standard", "keeper", "keeper_adv", "shooting", "passing",
    "passing_types", "goal_shot_creation", "defense", "possession",
    "playing_time", "misc"
]
TEAM_MATCH_TYPES = [
    "schedule", "keeper", "shooting", "passing", "passing_types",
    "goal_shot_creation", "defense", "possession", "misc"
]
PLAYER_SEASON_TYPES = [
    "standard", "keeper", "keeper_adv", "shooting", "passing",
    "passing_types", "goal_shot_creation", "defense", "possession",
    "playing_time", "misc"
]
PLAYER_MATCH_TYPES = [
    "summary", "keepers", "passing", "passing_types", "defense",
    "possession", "misc"
]

# Função para criar o FBref reader
def setup_fbref():
    """
    Cria e retorna um objeto FBref para leitura de dados.

    Returns:
        FBref: Instância do objeto FBref.
    """
    return sd.FBref(leagues=[LEAGUE], seasons=[SEASON])

# Função para criar o WhoScored reader
def setup_whoscored():
    """
    Instancia a classe WhoScored para a Série A do Brasileirão,
    tentando temporada 2024; se não estiver disponível, usa 2023.
    """
    try:
        return sd.WhoScored(leagues=LEAGUE, seasons=SEASON, headless=False)
    except ValueError:
        return sd.WhoScored(leagues='BRA-Serie A', seasons='2023', headless=False)

# Função para salvar DataFrame
def save_dataframe(df, filename, source='fbref'):
    """
    Salva um DataFrame em um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        filename (str): Nome do arquivo CSV.
        source (str): Fonte dos dados ('fbref' ou 'whoscored').
    """
    if df is not None and not df.empty:
        output_dir = os.path.join(BASE_DIR, source, f"{LEAGUE}_{SEASON}")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        if os.path.exists(filepath):
            print(f"Arquivo já existe: {filepath}")
        else:
            df.to_csv(filepath, index=False)
            print(f"Arquivo salvo: {filepath}")
    else:
        print(f"Dados não disponíveis para: {filename}")

def fetch_data_in_parallel(functions, *args):
    """
    Executa funções em paralelo.

    Args:
        functions (list): Lista de funções a serem executadas.
        args (tuple): Argumentos para as funções.

    Returns:
        list: Lista de resultados das funções.
    """
    results = []
    with ThreadPoolExecutor() as executor:
        future_to_function = {executor.submit(func, *args): func for func in functions}
        for future in as_completed(future_to_function):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Erro na execução paralela: {e}")
    return results

def exibir_tabela(df, nome_tabela):
    """
    Exibe uma tabela de DataFrame com um título específico.

    Args:
        df (pd.DataFrame): DataFrame a ser exibido.
        nome_tabela (str): Nome da tabela.
    """
    if df is not None and not df.empty:
        print(f"\n## {nome_tabela}")
        print(df.head())

def main():
    """
    Função principal para coletar e salvar dados do FBref e WhoScored.
    """
    fbref = setup_fbref()
    if fbref is None:
        print("Erro: o objeto fbref não foi inicializado corretamente.")
        return

    whoscored = setup_whoscored()
    tabelas_fbref = {}
    tabelas_whoscored = {}

    # Coleta de dados do FBref
    # 1) Schedule (cronograma de jogos)
    try:
        df = fbref.read_schedule()
        save_dataframe(df, "schedule.csv")
    except Exception as e:
        print(f"Erro em read_schedule: {e}")

    # 2) Estatísticas de Equipe por Temporada
    for stat_type in tqdm(TEAM_SEASON_TYPES, desc="Estatísticas de Equipe por Temporada"):
        # 2a) Sem opponent_stats
        try:
            df = fbref.read_team_season_stats(stat_type=stat_type, opponent_stats=False)
            key_no_opp = f"team_season_{stat_type}_for.csv"
            tabelas_fbref[key_no_opp] = df
            save_dataframe(df, key_no_opp)
        except Exception as e:
            print(f"Erro em team_season_{stat_type}_for: {e}")

        # 2b) Com opponent_stats
        try:
            df_opp = fbref.read_team_season_stats(stat_type=stat_type, opponent_stats=True)
            key_opp = f"team_season_{stat_type}_against.csv"
            tabelas_fbref[key_opp] = df_opp
            save_dataframe(df_opp, key_opp)
        except Exception as e:
            print(f"Erro em team_season_{stat_type}_against: {e}")

    # 3) Estatísticas de Equipe por Partida
    for stat_type in tqdm(TEAM_MATCH_TYPES, desc="Estatísticas de Equipe por Partida"):
        # 'schedule' não possui opponent_stats=True
        if stat_type == "schedule":
            try:
                df_match = fbref.read_team_match_stats(stat_type="schedule", team=TEAM)
                tabelas_fbref["team_match_schedule"] = df_match
                save_dataframe(df_match, f"team_match_schedule_{TEAM}.csv")
            except Exception as e:
                print(f"Erro em team_match_schedule: {e}")
        else:
            for opp in [False, True]:
                try:
                    df_tm = fbref.read_team_match_stats(
                        stat_type=stat_type,
                        opponent_stats=opp,
                        team=TEAM
                    )
                    tm_key = f"team_match_{stat_type}_{'against' if opp else 'for'}.csv"
                    tabelas_fbref[tm_key] = df_tm
                    save_dataframe(df_tm, tm_key)
                except Exception as e:
                    print(f"Erro em team_match_{stat_type}_{opp}: {e}")

    # 4) Estatísticas de Jogadores por Temporada
    for stat_type in tqdm(PLAYER_SEASON_TYPES, desc="Estatísticas de Jogadores por Temporada"):
        try:
            df_ps = fbref.read_player_season_stats(stat_type=stat_type)
            ps_key = f"player_season_{stat_type}.csv"
            tabelas_fbref[ps_key] = df_ps
            save_dataframe(df_ps, ps_key)
        except Exception as e:
            print(f"Erro em player_season_{stat_type}: {e}")

    # 5) Estatísticas de Jogadores por Partida (para um match_id de exemplo)
    for stat_type in tqdm(PLAYER_MATCH_TYPES, desc="Estatísticas de Jogadores por Partida"):
        try:
            df_pm = fbref.read_player_match_stats(stat_type=stat_type, match_id=MATCH_ID_FBREF)
            pm_key = f"player_match_{stat_type}.csv"
            tabelas_fbref[pm_key] = df_pm
            save_dataframe(df_pm, pm_key)
        except Exception as e:
            print(f"Erro em player_match_{stat_type}: {e}")

    # 6) Escalações, Eventos e Finalizações do MATCH_ID
    try:
        lineups = fbref.read_lineup(match_id=MATCH_ID_FBREF)
        tabelas_fbref["lineups"] = lineups
        save_dataframe(lineups, "lineups.csv")

        events = fbref.read_events(match_id=MATCH_ID_FBREF)
        tabelas_fbref["events"] = events
        save_dataframe(events, "events.csv")

        shots = fbref.read_shot_events(match_id=MATCH_ID_FBREF)
        tabelas_fbref["shot_events"] = shots
        save_dataframe(shots, "shot_events.csv")

    except Exception as e:
        print(f"Erro em lineups/events/shot_events: {e}")

       # Coleta de dados do WhoScored
    # 1) Leagues
    try:
        df_leagues = whoscored.read_leagues()
        tabelas_whoscored["leagues"] = df_leagues
        save_dataframe(df_leagues, "leagues.csv", source='whoscored')
    except Exception as e:
        print(f"Erro em read_leagues: {e}")

    # 2) Seasons
    try:
        df_seasons = whoscored.read_seasons()
        tabelas_whoscored["seasons"] = df_seasons
        save_dataframe(df_seasons, "seasons.csv", source='whoscored')
    except Exception as e:
        print(f"Erro em read_seasons: {e}")

    # 3) Season Stages
    try:
        df_stages = whoscored.read_season_stages()
        tabelas_whoscored["season_stages"] = df_stages
        save_dataframe(df_stages, "season_stages.csv", source='whoscored')
    except Exception as e:
        print(f"Erro em read_season_stages: {e}")

    # 4) Schedule (Jogos)
    try:
        df_schedule = whoscored.read_schedule()
        tabelas_whoscored["schedule"] = df_schedule
        save_dataframe(df_schedule, "schedule.csv", source='whoscored')
    except Exception as e:
        print(f"Erro em read_schedule: {e}")

    # 5) Missing Players (Jogadores indisponíveis)
    if "schedule" in tabelas_whoscored and not tabelas_whoscored["schedule"].empty:
        try:
            example_game_ids = MATCH_ID_WHOSCORED
            df_missing = whoscored.read_missing_players(match_id=example_game_ids)
            tabelas_whoscored["missing_players"] = df_missing
            save_dataframe(df_missing, "missing_players.csv", source='whoscored')
        except Exception as e:
            print(f"Erro em read_missing_players: {e}")

    # 6) Events - Testando todos os formatos possíveis
    if "schedule" in tabelas_whoscored and not tabelas_whoscored["schedule"].empty:
        try:

            # 6.1 Events (formato padrão)
            try:
                tabelas_whoscored['events'] = whoscored.read_events(match_id=[MATCH_ID_WHOSCORED])
                save_dataframe(tabelas_whoscored['events'], "events.csv", source='whoscored')
            except Exception as e:
                print(f"Erro ao carregar Events (Padrão): {e}")

            # 6.2 Events (raw)
            try:
                events_raw = whoscored.read_events(match_id=[MATCH_ID_WHOSCORED], output_fmt="raw")
                print("\n## Events (raw) - Exemplo do primeiro evento:")
                print(json.dumps(events_raw[MATCH_ID_WHOSCORED][0], indent=2)) # type: ignore
            except Exception as e:
                print(f"Erro ao carregar Events (raw): {e}")

            # 6.3 Events (SPADL)
            try:
                tabelas_whoscored['events_spadl'] = whoscored.read_events(match_id=[MATCH_ID_WHOSCORED], output_fmt='spadl')
                save_dataframe(tabelas_whoscored['events_spadl'], "events_spadl.csv", source='whoscored')
            except Exception as e:
                print(f"Erro ao carregar Events (SPADL): {e}")

            # 6.4 Events (atomic-spadl)
            try:
                tabelas_whoscored['events_atomic'] = whoscored.read_events(match_id=[MATCH_ID_WHOSCORED], output_fmt='atomic-spadl')
                save_dataframe(tabelas_whoscored['events_atomic'], "events_atomic.csv", source='whoscored')
            except Exception as e:
                print(f"Erro ao carregar Events (Atomic-SPADL): {e}")

            # Seção do WhoScored - Events Loader
            try:
                # Inicialização do loader
                loader = whoscored.read_events(output_fmt='loader', match_id=[MATCH_ID_WHOSCORED])

                # Carregamento dos dados usando as funções do loader
                tabelas_whoscored['games'] = loader.games(competition_id=LEAGUE,season_id=SEASON) # type: ignore

                tabelas_whoscored['teams'] = loader.teams(game_id=MATCH_ID_WHOSCORED) # type: ignore

                tabelas_whoscored['players'] = loader.players(game_id=MATCH_ID_WHOSCORED) # type: ignore

                tabelas_whoscored['events_loader'] = loader.events(game_id=MATCH_ID_WHOSCORED) # type: ignore

                # Salvamento dos dados
                for key, df in tabelas_whoscored.items():
                    if df is not None and not df.empty:
                        save_dataframe(df, f"{key}.csv", source='whoscored')

            except Exception as e:
                print(f"Erro ao processar dados do WhoScored - Events Loader: {e}")


        except Exception as e:
            print(f"Erro geral na coleta de eventos: {e}")

    print("\n[Info] Coleta de dados concluída. Consulte os dicionários 'tabelas_fbref' e 'tabelas_whoscored' para acesso completo.")

if __name__ == "__main__":
    main()

