from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def in_unit_circle(pt):
    return pt[0] ** 2 + pt[1] ** 2 < 1


fig, ax1 = plt.subplots(1, figsize=(5, 5))

ax1.set_xlim((-1.1, 1.1))
ax1.set_ylim((-1.1, 1.1))

unit_circle = plt.Circle((0, 0), 1, ec='black', fc='none')
unit_square = plt.Rectangle((-1, -1), 2, 2, ec='black', fc='none')
ax1.add_artist(unit_circle)
ax1.add_artist(unit_square)

in_pts = np.array([[0, 0]])
out_pts = np.array([[0, 0]])
in_scatter = ax1.scatter([], [], c='g', s=1)
out_scatter = ax1.scatter([], [], c='r', s=1)
scatters = [in_scatter, out_scatter]
in_count, out_count = 0, 0

def update(frame):
    pt = np.random.uniform(-1, 1, (1, 2))

    global in_count, out_count
    if in_unit_circle(pt[0]):
        in_count += 1

        global in_pts
        in_pts = np.concatenate((in_pts, pt))
        scatters[0].set_offsets(in_pts[1:])
    else:
        out_count += 1

        global out_pts
        out_pts = np.concatenate((out_pts, pt))
        scatters[1].set_offsets(out_pts[1:])

    if in_count > 0 and out_count > 0:
        est_pi =  4 * in_count / (in_count + out_count)
        print(f'{frame:3d}: {est_pi:0.2f} | {np.pi - est_pi:0.3e}')

    return scatters


max_iter = 100000
ani = FuncAnimation(fig, update, frames=max_iter, blit=True, interval=0, repeat=False)

plt.show()