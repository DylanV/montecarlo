from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1)

np.random.seed(1123)
max_iter = 10000
total_n = 0
count_n = 0
x = np.arange(1, max_iter)
e = np.exp(1)
y = np.full(x.shape, e)

ax1.plot(x, y)
ln = ax1.plot([], [])
ln2 = ax2.plot([], [])
lines = [ln[0], ln2[0]]
ax2.set_xlim(0, max_iter)
ax2.set_ylim(-0.001, 0.1)
ax1.set_xlim(0, max_iter)
ax1.set_ylim(e-0.05, e+0.05)

y_hist = []
x_hist = []
err_hist = []

def update(frame):
    total = 0
    n = 0
    while total < 1:
        total += np.random.uniform(0, 1)
        n += 1

    global total_n, count_n
    total_n = total_n + n
    count_n = count_n + 1
    e_est = total_n/count_n
    print(frame, e_est, e_est-e)
    y_hist.append(total_n/count_n)
    x_hist.append(count_n)
    err_hist.append(np.abs( e_est - e ))

    lines[0].set_data(x_hist, y_hist)
    lines[1].set_data(x_hist, err_hist)
    return lines

ani = FuncAnimation(fig, update, frames=max_iter, blit=True, interval=0, repeat=False)

plt.show()