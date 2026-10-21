from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_boxplot.csv")
plt.figure(figsize=(9, 5))
departamentos = dados["departamento"].dropna().unique()
valores = [dados.loc[dados["departamento"] == d, "salario"].dropna() for d in departamentos]
plt.boxplot(valores, labels=departamentos, showmeans=True)
plt.title("Distribuição de salários por departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
saida = BASE / "graficos" / "grafico_boxplot.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
