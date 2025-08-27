
import math
import numpy as np

# Base periods (z values from the 24 primitives)
base_periods = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91]

# Function to compute LCM of two numbers using GCD
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Generate the 24x24 matrix of shared periods (LCMs)
matrix = [[lcm(z_i, z_j) for z_j in base_periods] for z_i in base_periods]

# Compute average overlap rate (1/LCM for i != j)
overlap_rates = [1 / lcm(z_i, z_j) for i, z_i in enumerate(base_periods) for j, z_j in enumerate(base_periods) if i != j]
average_overlap = sum(overlap_rates) / len(overlap_rates) if overlap_rates else 0

# Print text-based table
print("Shared Periods Matrix (LCM of Base Periods):")
print("-" * 80)
header = "     " + " ".join(f"{z:4}" for z in base_periods)
print(header)
print("-" * 80)
for i, row in enumerate(matrix):
    print(f"{base_periods[i]:4} | " + " ".join(f"{val:4}" for val in row))
print("-" * 80)
print(f"Average overlap rate (1/LCM for i != j): {average_overlap:.6f}")

# Generate LaTeX table code
latex_table = """
\\begin{table}[h]
\\centering
\\begin{tabular}{c|""" + "c" * len(base_periods) + """}
\\toprule
 & """ + " & ".join(str(z) for z in base_periods) + """ \\\\
\\midrule
"""
for i, row in enumerate(matrix):
    latex_table += f"{base_periods[i]} & " + " & ".join(str(val) for val in row) + " \\\\\n"
latex_table += """\\bottomrule
\\end{tabular}
\\caption{Shared Periods Matrix (LCM of Base Periods). Rows and columns are labeled by the base periods \( z \).}
\\label{tab:shared_periods}
\\end{table}
"""

# Output LaTeX code to file
with open("shared_periods_matrix.tex", "w") as f:
    f.write(latex_table)

print("\nLaTeX table code written to 'shared_periods_matrix.tex'")
