import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
def F(x, y):
    return x * np.log(x**2) + y * np.log(y**2)
resolution = 1200
x = np.linspace(-3, 3, resolution)
y = np.linspace(-3, 3, resolution)
X, Y = np.meshgrid(x, y)
with np.errstate(divide="ignore", invalid="ignore"):
    Z = F(X, Y)
Z[~np.isfinite(Z)] = np.nan
z_min = -3
z_max = 3
Z_plot = np.where(
    (Z >= z_min) & (Z <= z_max),
    Z,
    np.nan
)
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(
    111,
    projection="3d"
)
norm = Normalize(
    vmin=z_min,
    vmax=z_max
)
surface = ax.plot_surface(
    X,
    Y,
    Z_plot,
    cmap="turbo",
    norm=norm,
    rcount=1200,
    ccount=1200,
    linewidth=0,
    antialiased=True
)
ax.set_xlabel(
    r"$x$",
    fontsize=15,
    labelpad=12
)
ax.set_ylabel(
    r"$y$",
    fontsize=15,
    labelpad=12
)
ax.set_zlabel(
    r"$\lambda$",
    fontsize=15,
    labelpad=12
)
ax.set_title(
    r"$z=x\ln(x^2)+y\ln(y^2)$",
    fontsize=18,
    pad=25
)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_box_aspect(
    (1, 1, 1)
)
ax.grid(
    True,
    linewidth=0.6,
    alpha=0.5
)
cbar = fig.colorbar(
    surface,
    ax=ax,
    shrink=0.7,
    pad=0.1
)
cbar.set_label(
    r"$\lambda$",
    fontsize=15
)
ax.view_init(
    elev=30,
    azim=-135
)
plt.tight_layout()
plt.savefig(
    "lambda_3d_high_quality.png",
    dpi=600,
    bbox_inches="tight"
)
plt.show() 
