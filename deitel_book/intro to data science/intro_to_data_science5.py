import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


rolls = [random.randrange(1, 7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)
print(values)
print(frequencies)

# f-string includes the number of die rolls in the bar plot's title.
# The comma (,) format specifier in {len(rolls):, } displays the number
# with thousands separators. so, 60000 would be displayed as 60,000
title = f"Rolling a six-sided die {len(rolls) } times"
sns.set_style("whitegrid")
axes = sns.barplot(x=values, y=frequencies, palette="bright")
