# ==========================================================================================================================================
# ==========================================================================================================================================
# 1. Make a table or figure of average tree errors for each of the five methods for the two methods
# 2. For 1000M1 and 1000M2
#   (a) Which method is the most accurate?
#   (b) Does changing the estimation method for FastTree impact accuracy? If so, how?
#   (c) Does changing the distance correction for Neighbor Joining impact accuracy? If so, how?
#   (d) Do any of the trends above change as you change method conditions?
#   (e) Does the relative accuracy of methods remain the same between the method conditions?
#   (f) One of the method conditions is "easier" (in that the methods have higher accuracy); which one? 
#       And what is it about the method condition (i.e., numeric parameters and/or empirical statistics of the sequences that are produced) 
#       that suggests why that method condition is easier than the other?
#  3. Describe how the data were generated; what sequence evolution method was used?
#  4. Which of the methods that you ran is statistically consistent for the method that generated the data? Justify your answers.
#  5. Did the statistically consistent methods always produce more accurate trees than the methods not guaranteed to be consistent?
# ==========================================================================================================================================
# ==========================================================================================================================================

import pandas as pd
import numpy as np

# ==========================================================================================================================================
#   1.  (printing out statistics as pandas dataframe)
# ==========================================================================================================================================

replicates = 5
methods = [
        "FastTreeGTR",
        "FastTreeJC",
        "NeighborJoinGM",
        "NeighborJoinHam",
        "NeighborJoinJC",
]
models = [
        "Gamma/1000M1",
        "Gamma/1000M4",
]

# columns: method, FN/FP R0..., FP/FN average
data = {}
data["Method"] = []
data["Model"] = []
data[f"FN (avg)"] = []
data[f"FP (avg)"] = []
for r in range(replicates):
    data[f"FN (R{r})"] = []
    data[f"FP (R{r})"] = []

for d in models:
    for m in methods:
        data["Method"].append(m)
        data["Model"].append(d)
        sum_FN = 0
        sum_FP = 0
        for r in range(replicates):
            filename = f"~/hw6/output/{d}/{m}_R{r}/error.csv"
            df = pd.read_csv(filename)
            data[f"FN (R{r})"].append(df["rf_FN"][0])
            data[f"FP (R{r})"].append(df["rf_FP"][0])
            sum_FN += df["rf_FN"][0]
            sum_FP += df["rf_FP"][0]
        data[f"FN (avg)"].append(sum_FN / replicates)
        data[f"FP (avg)"].append(sum_FP / replicates)

df = pd.DataFrame.from_dict(data)
df.to_csv("summary_Gamma.csv", index=False)
