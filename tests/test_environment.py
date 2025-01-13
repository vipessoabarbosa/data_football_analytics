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