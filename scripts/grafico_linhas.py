from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_linhas.csv", parse_dates=["data"])
dados = dados.sort_values("data")
plt.figure(figsize=(10, 5))
for loja, grupo in dados.groupby("loja"):
    plt.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3, label=loja)
plt.title("Vendas ao longo do tempo por loja")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.legend(title="Loja")
plt.grid(True, linestyle="--", alpha=0.35)
plt.xticks(rotation=45)
plt.tight_layout()
saida = BASE / "graficos" / "grafico_linhas.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
