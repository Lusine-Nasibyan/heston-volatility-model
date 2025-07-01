import numpy as np
import matplotlib.pyplot as plt

def stimulate_brownian_motion(T=1.0, N=1000):
    dt = T / N
    t = np.linspace(0, T, N)
    dW = np.random.normal(0.0, np.sqrt(dt), size=N-1)
    W = np.concatenate(([0], np.cumsum(dW)))
    return t, W

t, W = stimulate_brownian_motion()
plt.plot(t,W)
plt.title('Brownian Motion')
plt.xlabel('Time')
plt.ylabel('W(t)')
plt.grid(True)
plt.show()

