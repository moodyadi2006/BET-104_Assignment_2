import random
import csv

k = int(snakemake.wildcards.k)
n = snakemake.params.n
n_repeats = snakemake.params.n_repeats

means = [sum(random.randint(1, n) for _ in range(k)) / k for _ in range(n_repeats)]

with open(snakemake.output[0], "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["k", "mean"])
    for m in means:
        writer.writerow([k, m])
