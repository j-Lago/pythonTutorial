import numpy as np
import matplotlib.pyplot as plt
from project_paths import *

if __name__ == '__main__':

    # parâmetros
    T = 0.05
    L = 1024
    fs = L / T  # frequência de amostragem (1024 amostras em 50ms)
    f1 = 60.0  # Hz
    noise_amp = 300

    t = np.linspace(0, T, L, endpoint=False)

    # sinal com componente fundamental, 5a harmônica e ruído
    v1 = np.sqrt(2) * 220 * np.sin(2 * np.pi * f1 * t)
    v5 = np.sqrt(2) * 40 * np.sin(2 * np.pi * 5 * f1 * t + np.deg2rad(128.4))
    noise = noise_amp * (np.random.rand(len(t)) - 0.5)
    v_orig = v1 + v5 + noise

    # fft
    V_fft = np.fft.fft(v_orig)
    freqs = np.fft.fftfreq(len(t), 1/fs)

    # filtra componentes de baixa magnitude
    threshold = 10 * L
    V_fft_filt = V_fft.copy()
    V_fft_filt[np.abs(V_fft) < threshold] = 0

    # sinal reconstruído
    v_filt = np.fft.ifft(V_fft_filt).real

    # plot
    plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})
    plt.figure(figsize=(5.0, 2.8))

    plt.plot(t, v_orig, label='$v_o$', linewidth=1, alpha=0.3, color='steelblue')
    plt.plot(t, v_filt, label='$v_{f}$', linewidth=1, color='steelblue')
    plt.xlim(t[0], t[-1])
    plt.ylim(-500, 500)
    plt.xlabel('time [s]')
    plt.ylabel('voltage [V]')
    plt.legend(ncol=1, loc='upper right')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(figs_dir / 'fft.pdf', format='pdf')
    plt.show()