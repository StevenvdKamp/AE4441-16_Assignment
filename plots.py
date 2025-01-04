import matplotlib.pyplot as plt
import numpy as np

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
    ax.set_xlabel('Increase in Maintenance Speed (%)')
    ax.set_ylabel('Score')
    # ax.set_title('Score vs Increase in Speed')  # Title was commented out
    # Add a legend
    # ax.legend()  # Legend was commented out

    # Save the plot to a PNG file
    fig.tight_layout()
    fig.savefig('work_duration_vs_score_plot.png', format='png', dpi=300)

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
    ax.set_ylabel('Score')
    # ax.set_xlabel('Machine Configuration')
    # ax.set_title('Score Comparison with Different Machine Configurations')

    # Save the plot to a PNG file
    fig.tight_layout()
    fig.savefig('machine_configuration_score_comparison.png', format='png', dpi=300)

    # Show the plot
    plt.show()


def plot_score_vs_travel_times():
    adjusted_travel_times = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2]) * 100
    adjusted_travel_times_result = [753, 753, 797, 797, 797, 835, 836, 853, 853, 870, 870, 901]

    plt.scatter(adjusted_travel_times, adjusted_travel_times_result, color='b', s=20, zorder=3)

    #plt.title("Travel Costs Change vs Total Costs")
    plt.xlabel("Travel Time (% of original)")
    plt.ylabel("Total Costs")

    # Enable minor ticks
    plt.minorticks_on()

    # Add major grid
    plt.grid(which='major', linewidth=0.3, zorder=1)

    # Add minor grid
    plt.grid(which='minor', linewidth=0.2, zorder=1)

    plt.show()

def plot_score_vs_travel_costs():
    adjusted_travel_costs = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2]) * 100
    adjusted_travel_costs_result = [587.5, 637.2, 686.9, 736.6, 786.3, 835, 876.5, 915, 953.5, 992, 1030.5, 1223]

    plt.scatter(adjusted_travel_costs, adjusted_travel_costs_result, color='b', s=20, zorder=3)

    plt.xlabel("Travel Costs (% of original)")
    plt.ylabel("Total Costs")

    # Enable minor ticks
    plt.minorticks_on()

    # Add major grid
    plt.grid(which='major', linewidth=0.3, zorder=1)

    # Add minor grid
    plt.grid(which='minor', linewidth=0.2, zorder=1)

    plt.show()

# Example function calls to generate the plots
plot_score_vs_travel_times()
# plot_score_vs_speed_increase()

