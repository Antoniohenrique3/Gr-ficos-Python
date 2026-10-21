from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_frequencia.csv")
frequencias = dados["tipo_atendimento"].dropna().value_counts().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
barras = plt.bar(frequencias.index, frequencias.values, edgecolor="black")
plt.title("Frequência por tipo de atendimento")
plt.xlabel("Tipo de atendimento")
plt.ylabel("Quantidade de chamados")
plt.bar_label(barras, padding=3)
plt.grid(axis="y", linestyle="--", alpha=0.35)
plt.tight_layout()
saida = BASE / "graficos" / "grafico_frequencia.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
