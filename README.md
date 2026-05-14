# Law of Large Numbers — Snakemake Pipeline

Demonstrates the **Law of Large Numbers**: if you repeatedly sample from a range (1 to n), the mean of those samples converges to the true mean `(n+1)/2` as the number of draws increases. For example, for n=2000 the true mean is 1000.5 — the more you draw, the closer your sample mean gets to that value.

---

## File Structure

```
BET_105_Assignment_2/
├── Snakefile               # Pipeline definition (rules, dependencies)
├── config.yaml             # Parameters: n, k_values, n_repeats
├── scripts/
│   ├── sample_means.py     # Samples k integers from 1..n, repeats n_repeats times, saves means to TSV
│   └── plot_means.py       # Reads all TSVs and generates the box plot PNG
├── results/
│   └── law_of_large_numbers_n2000.png   # Final output plot
└── README.md
```

---

## How It Works

For each value of k in `k_values`:
1. Draw k random integers from 1 to n
2. Compute their mean
3. Repeat `n_repeats` times → produces a distribution of means
4. Plot all distributions as side-by-side box plots

As k increases, the spread of the box narrows — the sample mean converges to the true mean.

---

## Setup

### Prerequisites

- [Conda](https://docs.conda.io/) with a Snakemake environment, or any Python environment with:
  - `snakemake`
  - `matplotlib`

### Install dependencies (if not already available)

```bash
conda install -c bioconda -c conda-forge snakemake matplotlib
```

### Clone the repository

```bash
git clone https://github.com/moodyadi2006/BET-104_Assignment_2.git
cd BET-104_Assignment_2
```

---

## Running the Pipeline

```bash
snakemake --cores 4
```

The output plot is saved to:
```
results/law_of_large_numbers_n2000.png
```

To do a dry run (see what Snakemake would execute without running it):
```bash
snakemake --cores 4 -n
```

---

## Configuration (`config.yaml`)

```yaml
n: 2000
k_values: [5, 10, 25, 50, 100, 200, 1000, 2000]
n_repeats: 10
```

| Parameter   | Default | Description |
|-------------|---------|-------------|
| `n`         | 2000    | Upper bound of the sampling range (1 to n) |
| `k_values`  | [5, 10, 25, 50, 100, 200, 1000, 2000] | Number of draws per experiment (one box per value) |
| `n_repeats` | 10      | Number of experiments per k |

### Change n (e.g. test range 1 to 1000)

Edit `config.yaml`:
```yaml
n: 1000
```

### Add a new k value (e.g. k=5000)

Edit `config.yaml`:
```yaml
k_values: [5, 10, 25, 50, 100, 200, 1000, 2000, 5000]
```

Then re-run `snakemake --cores 4`. Snakemake will only generate the new TSV and replot — existing outputs are reused.

---

## Inspecting Intermediate TSV Files

By default, the per-k TSV files (e.g. `results/means_k25.tsv`) are marked as `temp()` in the Snakefile and are **automatically deleted** after the plot is generated.

To keep them for inspection, open `Snakefile` and remove the `temp()` wrapper in the `sample_means` rule:

**Before:**
```python
rule sample_means:
    output:
        temp("results/means_k{k}.tsv")
```

**After:**
```python
rule sample_means:
    output:
        "results/means_k{k}.tsv"
```

Each TSV has this structure (one row per experiment):
```
k       mean
25      987.4
25      1023.1
...
```

Re-run the pipeline and the TSV files will be retained in `results/`.

---

## Results

![Law of Large Numbers](results/law_of_large_numbers_n2000.png)
