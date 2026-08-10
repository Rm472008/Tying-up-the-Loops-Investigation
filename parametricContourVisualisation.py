import numpy as np
import matplotlib.pyplot as plt
def F(x, y):
    return x * np.log(x**2) + y * np.log(y**2)
x = np.linspace(-0.5, 1.5, 1000)
y = np.linspace(-0.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
with np.errstate(divide="ignore", invalid="ignore"):
    Z = F(X, Y)
Z[~np.isfinite(Z)] = np.nan
lambda_min = float(input("Lambda min approx(4/e): "))
lambda_max = float(input("Lambda man approx(3): "))
n = int(input("nLines: "))
t = np.linspace(0, 1, n)
levels = lambda_min + (lambda_max - lambda_min) * t**2
fig, ax = plt.subplots(figsize=(9, 9))
contours = ax.contour(
    X,
    Y,
    Z,
    levels=levels,
    cmap="turbo",
    linewidths=1.2
)
ax.axhline(
    0,
    linewidth=1.5
)
ax.axvline(
    0,
    linewidth=1.5
)
ax.set_axisbelow(True)
ax.grid(
    True,
    linewidth=0.7,
    alpha=0.5
)
ax.set_xlabel(
    r"$x$",
    fontsize=14
)
ax.set_ylabel(
    r"$y$",
    fontsize=14
)
ax.set_title(
    r"$x\ln(x^2)+y\ln(y^2)=\lambda$",
    fontsize=16
)
cbar = fig.colorbar(
    contours,
    ax=ax
)
cbar.set_label(
    r"$\lambda$",
    fontsize=14
)
ax.set_aspect(
    "equal",
    adjustable="box"
)
ax.set_xlim(
    -0.5,
    1.5
)
ax.set_ylim(
    -0.5,
    1.5
)
ax.tick_params(
    labelsize=11
)
plt.tight_layout()
plt.savefig(
    "lambda_level_curves.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
