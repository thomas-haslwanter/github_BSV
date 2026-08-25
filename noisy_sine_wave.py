"""Plot a noisy sine wave using the requested parameters."""

import numpy as np
import matplotlib.pyplot as plt


AMPLITUDE = 2.0
OFFSET = 0.5
PHASE = 0.3  # radians
DURATION = 10.0
DT = 0.05
NOISE_MEAN = 0.0
NOISE_STD = 0.5


def main() -> None:
    time = np.arange(0.0, DURATION + DT / 2, DT)
    clean_signal = OFFSET + AMPLITUDE * np.sin(time + PHASE)
    noise = np.random.normal(NOISE_MEAN, NOISE_STD, size=time.shape)
    noisy_signal = clean_signal + noise

    plt.plot(time, noisy_signal, label="Noisy sine wave", linewidth=1.2)
    plt.plot(time, clean_signal, label="Clean sine wave", linewidth=2)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Noisy Sine Wave")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
