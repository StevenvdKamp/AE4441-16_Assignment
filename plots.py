import matplotlib.pyplot as plt

# Function to plot the scatter graph for "Score vs Speed Increase"
def plot_score_vs_speed_increase():
    # Data for the plot
    data = [200, 167, 143, 125, 111, 100, 91, 83, 77, 71, 67, 50]
    score = [574, 603, 671, 714, 753, 835, 853, 875, 895, 895, 908, 987]

    # Set up the figure and axes
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
    ax.set_xlabel('Maintenance Speed (% of original)')
    ax.set_ylabel('Total Cost')
    # ax.set_title('Score vs Increase in Speed')  # Title was commented out
    # Add a legend
    # ax.legend()  # Legend was commented out

    # Save the plot to a pdf file
    fig.tight_layout()
    fig.savefig('figures/work_duration_vs_score_plot.pdf', format='pdf', dpi=300)

    # Show the plot
    plt.show()

# Function to plot the bar graph for the given scores with different machine configurations
def plot_score_comparison():
    # Data for the bar graph
    labels = ['2 Machines', 'Extra Machine at Depot 1', 'Extra Machine at Depot 2']
    scores = [835.0, 628, 638]

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Set font and style for readability
    plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

    # Add gridlines
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
    ax.minorticks_on()
    ax.grid(True, which='minor', axis='y', linestyle=':', linewidth=0.5, color='gray', alpha=0.5)

    # Plot the data as a bar graph
    ax.bar(labels, scores, color='skyblue')

    # Labels and title
    ax.set_ylabel('Total Cost')
    # ax.set_xlabel('Machine Configuration')
    # ax.set_title('Score Comparison with Different Machine Configurations')

    # Save the plot to a pdf file
    fig.tight_layout()
    fig.savefig('figures/machine_configuration_score_comparison.pdf', format='pdf', dpi=300)

    # Show the plot
    plt.show()

# Example function calls to generate the plots
plot_score_comparison()
plot_score_vs_speed_increase()

