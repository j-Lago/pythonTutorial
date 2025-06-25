import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import atan2
from project_paths import *


def rms(path: str) -> tuple[float, float]:
        df = pd.read_csv(path)
        df.head()
        t = df['time'].to_numpy()
        phase = df['phase'].to_numpy()
        v = df['voltage'].to_numpy()

        period = t[-1] - t[0]
        n = 1
        p0 = phase[0]
        for p in phase:
            if p0 > np.pi > p:
                n += 1
            p0 = p

        vrms = np.sqrt((v**2/len(v)).sum())
        return vrms, n/period


if __name__ == '__main__':

    # contantes das eq. a diferenças
    k0 = 0.7
    k1 = 2.84e-6
    k2 = 0.385715277950311
    k3 = -0.385713293478261
    w0 = 376.9911184307752

    # importa dados
    df = pd.read_csv(data_dir / 'grid_voltage.csv', index_col='time')

    t = df.index.to_numpy()
    v = df['voltage'].to_numpy()

    # inicialização dos arrays
    N = len(v)
    a = np.zeros(N)
    b = np.zeros(N)
    e = np.zeros(N)
    d = np.zeros(N)
    q = np.zeros(N)
    delta = np.zeros(N)
    w = np.full(N, w0)
    th = np.zeros(N)

    # cruzamentos pode zero
    sync_cross_ids = []
    nosync_cross_ids = []

    # resolve eq. a diferenças
    for n in range(1, N):
        e[n] = k0 * (v[n] - a[n - 1]) - b[n - 1]
        a[n] = w[n - 1] * k1 * (e[n] + e[n - 1]) + a[n - 1]
        b[n] = w[n - 1] * k1 * (a[n] + a[n - 1]) + b[n - 1]
        q[n] = a[n] * np.cos(th[n - 1]) + b[n] * np.sin(th[n - 1])
        d[n] = a[n] * np.sin(th[n - 1]) - b[n] * np.cos(th[n - 1])
        delta[n] = k2 * q[n] + k3 * q[n-1] + delta[n-1]
        w[n] = w0 + delta[n]
        th[n] = (k1 * (w[n] + w[n - 1]) + th[n - 1]) % (2 * np.pi)

        # cruzamento por zero
        if th[n - 1] > np.pi >= th[n]:
            if abs(atan2(q[n], d[n])) < 0.03 and d[n] > 250:
                sync_cross_ids.append(n)
            else:
                nosync_cross_ids.append(n)


    # etapa 2
    vsync_filename = 'grid_sync.csv'
    if len(sync_cross_ids) > 1:
        locked = slice(sync_cross_ids[0], sync_cross_ids[-1] - 1, None)
        out = pd.DataFrame(index=t[locked], data={'phase': th[locked], 'voltage': v[locked]})
        out.to_csv(data_dir / vsync_filename, index_label='time')
        print(out.head())


    vrms, f1 = rms(data_dir / vsync_filename)
    print(f"A amostra de tensão possui valor rms de {vrms:.2f} V e frequência {f1:.2f} Hz")


    plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})  # comente se não tiver Latex instalado

    # gráficos
    fig, axs = plt.subplots(2, 1, figsize=(5.5, 4), sharex=True)

    for ax in axs:
        for n in sync_cross_ids:
            ax.axvline(t[n], linewidth=1, linestyle='-.', color='seagreen', alpha=0.5)
        for n in nosync_cross_ids:
            ax.axvline(t[n], linewidth=1, linestyle='-.', color='gray', alpha=0.5)
    axs[0].axhline(0, linewidth=1, linestyle='-', color='gray', alpha=0.3)

    axs[0].plot(t, v, linewidth=2, color='steelblue', alpha=0.3, label=r'$v$')
    axs[0].plot(t, a, linewidth=1, color='steelblue', label=r'$\alpha$')
    axs[0].plot(t, d, linewidth=1, color='olivedrab', label=r'$d$')
    axs[0].plot(t, q, linewidth=1, color='darkorange', label=r'$q$')

    for n in sync_cross_ids:
        axs[0].plot(t[n],0, marker='s', markersize=6, markerfacecolor='none', markeredgecolor='seagreen')
    for n in nosync_cross_ids:
        axs[0].plot(t[n],0, marker='x', markersize=6, color='palevioletred')
    axs[0].set_ylabel(r'voltages [V]')

    axs[1].plot(t, th, linewidth=1, color='pink', alpha=1, label=r'$\theta_{unlocked}$', zorder=-2)
    if len(sync_cross_ids) > 1:
        axs[1].plot(t[sync_cross_ids[0]:], th[sync_cross_ids[0]:], linewidth=1, color='olivedrab', label=r'$\theta_{locked}$', zorder=-1)
    axs[1].set_xlabel('time [s]')
    axs[1].set_ylabel('PLL phase [rad]')

    for ax in axs:
        ax.legend(loc='lower right', ncol=2)
        ax.set_xlim(t[0], t[-1])

    plt.tight_layout()
    plt.savefig(figs_dir / 'plot_pll.pdf', format="pdf")
    plt.show()



