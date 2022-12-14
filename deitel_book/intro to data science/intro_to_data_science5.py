# plotting a graph
import matplotlib.pyplot as plt  # contains the Matplotlib library's graphing capabilities that we use.
                                # This module typically is imported with the name plt
import numpy as np  #includes the function "unique" that we will use to summarize the die rolls
import random #contains Python's random-number-generation functions
import seaborn as sns #contains the Seaborn library's graphing capabilities we use.
                    #This module typically is imported with the name sns.

nr_of_rolls = 600

rolls = [random.randrange(1, 7) for i in range(nr_of_rolls)]
values, frequencies = np.unique(rolls, return_counts=True)
# print(values)
# print(frequencies)

# f-string includes the number of die rolls in the bar plot's title.
# The comma (,) format specifier in {len(rolls):, } displays the number
# with thousands separators. so, 60000 would be displayed as 60,000
title = f"Rolling a six-sided die {len(rolls)} times"
sns.set_style("whitegrid")
axes = sns.barplot(x=values, y=frequencies, palette="bright")
axes.set_title(title)
axes.set(xlabel="Die value", ylabel="Frequency")
axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  # calculates the center x coordinate where the text will appear
    text_y = bar.get_height()  # gets the y coordinate where the text will appear
    text = f"{frequency:,}\n {frequency / len(rolls):.3%}"
    axes.text(text_x, text_y, text, fontsize=11, ha="center", va="bottom")
plt.show()



# frame_number = The next value from FuncAnimation 's frames argument.
# rolls = The number of die rolls for animation frame
# faces = The die face values used as labels allong the graph's x-axis
# frequencies - The list in which we summarize the die frequencies.
