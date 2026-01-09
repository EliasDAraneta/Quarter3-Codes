import numpy as np

names = ["Me", "Lia", "Jake"]
np.steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

for i in range(len(names)):
    total_steps = np.sum(np.steps[i])
    average_steps = np.mean(np.steps[i])
    min_steps = np.min(np.steps[i])
    max_steps = np.max(np.steps[i])
    print(
        f"{names[i]} - Total Steps: {total_steps} | "
        f"Average: {average_steps:.1f} | "
        f"Min: {min_steps} | Max: {max_steps}"
    )