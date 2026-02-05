import pandas as pd

soft_path = "data/GDS6063_full.soft"      
out_csv = "data/gds6063_expression.csv"

data_lines = []
header = None
in_table = False

with open(soft_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line = line.strip()
        if line.startswith("!dataset_table_begin"):
            in_table = True
            continue
        if in_table:
            if header is None:
                header = line.split("\t")
            else:
                if line == "" or line.startswith("!"):
                    break
                data_lines.append(line.split("\t"))

df = pd.DataFrame(data_lines, columns=header)

sample_cols = [c for c in df.columns if c.startswith("GSM")]
df_clean = df[["ID_REF"] + sample_cols]

df_clean.replace("null", pd.NA, inplace=True)
df_clean[sample_cols] = df_clean[sample_cols].astype(float)

# save as CSV
df_clean.to_csv(out_csv, index=False)

print(f"Saved cleaned expression matrix to {out_csv}")

