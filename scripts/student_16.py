"""Student 16: draw a unit circle in a square frame."""
import matplotlib.pyplot as plt

CIRCLE_COLOR = "red"
OUTPUT_FILE = "student_16_circle.png"

fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
ax.set_facecolor("white")
circle = plt.Circle((0, 0), 1, fill=False, color=CIRCLE_COLOR, linewidth=4)
ax.add_patch(circle)
ax.set(xlim=(-2, 2), ylim=(-2, 2), xlabel="x", ylabel="y", title="Unit circle")
ax.set_aspect("equal", adjustable="box")
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUTPUT_FILE, dpi=150, facecolor="white")
print(f"Wrote {OUTPUT_FILE}")
