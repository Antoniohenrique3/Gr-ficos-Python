from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE = Path(__file__).resolve().parent.parent
dados = pd.read_csv(BASE / "dados" / "dados_heatmap.csv")
tabela = dados.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = tabela.reindex(ordem_dias)
fig, ax = plt.subplots(figsize=(9, 5))
imagem = ax.imshow(tabela, aspect="auto")
ax.set_xticks(range(len(tabela.columns)), labels=tabela.columns)
ax.set_yticks(range(len(tabela.index)), labels=tabela.index)
ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
fig.colorbar(imagem, ax=ax, label="Movimento de clientes")
for i in range(tabela.shape[0]):
    for j in range(tabela.shape[1]):
        valor = tabela.iloc[i, j]
        if pd.notna(valor):
            ax.text(j, i, f"{valor:.0f}", ha="center", va="center", fontsize=8)
fig.tight_layout()
saida = BASE / "graficos" / "grafico_heatmap.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em: {saida}")
plt.show()
