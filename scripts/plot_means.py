import csv
import matplotlib.pyplot as plt

n = snakemake.params.n
k_values = snakemake.params.k_values

data_by_k = {k: [] for k in k_values}
for filepath in snakemake.input:
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            data_by_k[int(row["k"])].append(float(row["mean"]))

data = [data_by_k[k] for k in k_values]
labels = [f"k={k}" for k in k_values]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(data, labels=labels)
ax.set_xlabel("Number of Draws (k)")
ax.set_ylabel("Mean")
ax.set_title(f"Testing Draws for {n}")
ax.axhline(y=(n + 1) / 2, color="red", linestyle="--", linewidth=0.8, alpha=0.6,
           label=f"True mean = {(n + 1) / 2}")
ax.legend()

plt.tight_layout()
plt.savefig(snakemake.output[0], dpi=150)
plt.close()
