#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Line Graph
y0 = np.arange(0, 11) ** 3
x0 = np.arange(0, 11)

# Scatter
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

# Explonential Decay of Decay of C-14
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

# Exponnetial Decay of Radioactive Elements
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

# Histogram
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Combined
fig = plt.figure(figsize=(10, 8))
gs = GridSpec(3, 2, height_ratios=[1, 1, 1])

axs = np.array([fig.add_subplot(gs[0, 0]),
                fig.add_subplot(gs[1, 0]),
                fig.add_subplot(gs[0, 1]),
                fig.add_subplot(gs[1, 1]),
                fig.add_subplot(gs[2, :])])

fig.suptitle("All in One")
# Line Graph#
axs[0].plot(x0, y0, color="red")
axs[0].set_xlim(0, 10)
axs[0].set_yticks(np.arange(0, 1001, 500))

# Exponetial Decay of C14
axs[1].plot(x2, y2)
axs[1].set_yscale('log')
axs[1].set_title("Explonetial Decay of C-14")
axs[1].set_xlabel("Time (years)")
axs[1].set_ylabel("Fraction Remaining")
axs[1].set_xlim(0, 28650)
axs[1].set_xticks([0, 10000, 20000])

# Scatter
axs[2].scatter(x1, y1, color="magenta")
axs[2].set_title("Men`s Height Vs Weight")
axs[2].set_ylabel("Weight (lbs)")
axs[2].set_xlabel("Height (in)")
axs[2].set_xticks([60, 70, 80])

# Exponetial Decay of Radioactive Elements
axs[3].plot(x3, y31, '--', color='red', label="C-14")
axs[3].plot(x3, y32, color='green', label="Ra-226")
axs[3].legend()
axs[3].set_xticks([0, 5000, 10000, 15000, 20000])
axs[3].set_xlim(0, 20000)

# histogram
axs[4].set_title("Project A")
axs[4].set_xlabel("Grades")
axs[4].set_ylabel("Number of Students")
axs[4].hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
axs[4].set_xticks(np.arange(0, 101, 10))
axs[4].set_ylim(0, 30)

fig.tight_layout()
plt.show()
