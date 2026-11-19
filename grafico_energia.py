import matplotlib.pyplot as plt

# nome do arquivo
arquivo = "energia_potencial.png"

# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9   # N·m²/C²
q1 = 1e-6    # 1 µC
q2 = 1e-6    # 1 µC

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = [0.10 + i * 0.01 for i in range(91)]
energia = [k * abs(q1 * q2) / r for r in distancias]

plt.figure(figsize=(6, 4))
plt.plot(distancias, energia, color="tab:blue", linewidth=2)
plt.title("Energia Potencial vs. Distância (Lei de Coulomb)")
plt.xlabel("Distância r (m)")
plt.ylabel("Energia U (J)")
plt.grid(True)
plt.tight_layout()
plt.savefig(arquivo, dpi=150)
print("Gráfico salvo em ",arquivo,"")
