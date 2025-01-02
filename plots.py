import matplotlib.pyplot as plt

# Data
data = [200, 167, 143, 125, 111, 100, 91, 83, 77, 71, 67, 50]
score = [574, 603, 671, 714, 753, 835, 853, 875, 895, 895, 908, 987]

# Set up the figure and axes using the function provided earlier
fig, ax = plt.subplots(figsize=(8, 6))

# Set font and style for readability
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Add gridlines
ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
ax.minorticks_on()
ax.grid(True, which='minor', axis='both', linestyle=':', linewidth=0.5, color='gray', alpha=0.5)

# Plot the data
ax.scatter(data, score, label='Score vs Speed Increase', color='blue', marker='o')

# Labels and title
ax.set_xlabel('Increase in Maintenance Speed (%)')
ax.set_ylabel('Score')
# ax.set_title('Score vs Increase in Speed')

# Add a legend
# ax.legend()

# Save the plot to a PNG file
fig.tight_layout()
fig.savefig('work_duration_vs_score_plot.png', format='png', dpi=300)

# Show the plot
plt.show()
