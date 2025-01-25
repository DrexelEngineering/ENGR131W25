import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_stiffness_line(transform_stiffness, Q_local):
    """
    Line plot of stiffness components over fiber orientation.
    """
    angles_deg = np.linspace(0, 360, 100)
    angles_rad = np.radians(angles_deg)

    Q11_values = []
    Q22_values = []
    G12_values = []

    for theta in angles_rad:
        Q_bar = transform_stiffness(Q_local, theta)
        Q11_values.append(Q_bar[0, 0])
        Q22_values.append(Q_bar[1, 1])
        G12_values.append(Q_bar[2, 2])

    plt.figure(figsize=(10, 6))
    plt.plot(angles_deg, Q11_values, label="$Q_{11}$", linewidth=2)
    plt.plot(angles_deg, Q22_values, label="$Q_{22}$", linewidth=2)
    plt.plot(angles_deg, G12_values, label="$G_{12}$", linewidth=2)
    plt.xlabel("Orientation (degrees)")
    plt.ylabel("Stiffness")
    plt.title("Stiffness Components vs Fiber Orientation")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()


def plot_stiffness_polar(transform_stiffness, Q_local):
    """
    Polar plot of stiffness components as a function of fiber orientation.
    """
    angles_deg = np.linspace(0, 360, 100)  # 100 angles from 0 to 360 degrees
    angles_rad = np.radians(angles_deg)

    Q11_values = []
    Q22_values = []
    G12_values = []

    for theta in angles_rad:
        Q_bar = transform_stiffness(Q_local, theta)
        Q11_values.append(Q_bar[0, 0])  # Extract Q11
        Q22_values.append(Q_bar[1, 1])  # Extract Q22
        G12_values.append(Q_bar[2, 2])  # Extract G12

    # Create polar plot
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(8, 8))
    ax.plot(angles_rad, Q11_values, label="$Q_{11}$", linewidth=2)
    ax.plot(angles_rad, Q22_values, label="$Q_{22}$", linewidth=2)
    ax.plot(angles_rad, G12_values, label="$G_{12}$", linewidth=2)

    ax.set_title("Stiffness Components vs Orientation ($\\theta$)", va="bottom")
    ax.legend(loc="upper right")
    plt.show()


def plot_volume_fractions(angles_deg, phis):
    """
    Bar plot of volume fractions for each orientation.
    """
    plt.figure(figsize=(8, 6))
    plt.bar(
        angles_deg,
        phis,
        width=10,
        align="center",
        alpha=0.7,
        color="skyblue",
        edgecolor="k",
    )
    plt.xlabel("Orientation (degrees)")
    plt.ylabel("Volume Fraction")
    plt.title("Volume Fractions for Different Fiber Orientations")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def plot_stiffness_matrix(Q, title="Stiffness Matrix Heatmap"):
    """
    Heatmap of a stiffness matrix.
    """
    plt.figure(figsize=(6, 5))
    sns.heatmap(Q, annot=True, fmt=".2f", cmap="viridis", cbar=True)
    plt.title(title)
    plt.xlabel("Matrix Columns")
    plt.ylabel("Matrix Rows")
    plt.show()
