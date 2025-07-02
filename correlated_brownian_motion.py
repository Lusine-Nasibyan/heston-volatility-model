import numpy as np
import matplotlib.pyplot as plt

def simulate_correlated_brownian_motion(T=1.0, N=1000, rho=-0.7):
    dt = T / N
    t = np.linspace(0, T, N)

    # Simulate two independent Brownian motions
    dW1 = np.random.normal(0.0, np.sqrt(dt), size=N-1)
    dW2 = np.random.normal(0.0, np.sqrt(dt), size=N-1)

    # Build correlated Brownian motions
    W1 = np.concatenate(([0], np.cumsum(dW1)))  # Brownian motion for stock
    W2 = np.concatenate(([0], np.cumsum(rho * dW1 + np.sqrt(1 - rho**2) * dW2)))  # Brownian motion for variance

    return t, W1, W2

# Run the simulation
t, W_stock, W_variance = simulate_correlated_brownian_motion()

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(t, W_stock, label="Brownian Motion for Stock (W^S)")
plt.plot(t, W_variance, label="Brownian Motion for Variance (W^v)")
plt.title("Two Correlated Brownian Motions")
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.legend()
plt.grid(True)
plt.show()
