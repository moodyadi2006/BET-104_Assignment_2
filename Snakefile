configfile: "config.yaml"

N = config["n"]
K_VALUES = config["k_values"]
N_REPEATS = config["n_repeats"]

rule all:
    input:
        f"results/law_of_large_numbers_n{N}.png"

rule sample_means:
    output:
        temp("results/means_k{k}.tsv")
    params:
        n=N,
        n_repeats=N_REPEATS
    script:
        "scripts/sample_means.py"

rule plot_means:
    input:
        expand("results/means_k{k}.tsv", k=K_VALUES)
    output:
        f"results/law_of_large_numbers_n{N}.png"
    params:
        n=N,
        k_values=K_VALUES
    script:
        "scripts/plot_means.py"
