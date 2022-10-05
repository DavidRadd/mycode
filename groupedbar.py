#! /usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


labels = ['Inches of rainfall', '> 80', '> 90', '> 100', '> 110']
seattle_means = [156, 39, 8, 3, 0 ]
phoenix_means = [12.9,300, 191, 111, 22]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, seattle_means, width, label='Seattle')
rects2 = ax.bar(x + width/2, phoenix_means, width, label='Phoenix')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by State')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig("/home/student/static/groupedbar.png")
#plt.savefig("/home/student/mycode/groupedbar.png")

