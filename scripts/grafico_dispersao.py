from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_dispersao.csv")
plt.figure(figsize=(8, 5))
for sexo, grupo in dados.groupby("sexo", dropna=False):
    plt.scatter(grupo["altura_cm"], grupo["peso_kg"], label=str(sexo), alpha=0.75)
plt.title("Relação entre altura e peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend(title="Sexo")
plt.grid(True, linestyle="--", alpha=0.35)
plt.tight_layout()
saida = BASE / "graficos" / "grafico_dispersao.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
