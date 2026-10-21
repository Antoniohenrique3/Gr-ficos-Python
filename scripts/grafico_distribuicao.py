from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_distribuicao.csv")
idades = dados["idade"].dropna()
plt.figure(figsize=(8, 5))
plt.hist(idades, bins=12, edgecolor="black")
plt.title("Distribuição das idades dos clientes")
plt.xlabel("Idade (anos)")
plt.ylabel("Quantidade de clientes")
plt.grid(axis="y", linestyle="--", alpha=0.35)
plt.tight_layout()
saida = BASE / "graficos" / "grafico_distribuicao.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
