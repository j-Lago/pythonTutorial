import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import math
import pandas as pd
from project_paths import *

if __name__ == '__main__':
    df = pd.read_csv(data_dir / 'grid_sync.csv')
    vg = df['voltage'].to_numpy()
    th = df['phase'].to_numpy()
    t = df['time'].to_numpy()


    # T = 0.2
    # Ts = 0.000005
    # t = np.linspace(0,T, int(T//Ts)+1)
    # th = np.fmod(t*(2*np.pi*60), 2*np.pi)

    print(len(t))

    print(len(th))

    Vi = 250
    phi = .4
    Vdc = 400
    fc = 600

    k0 = 3.3333e-4
    k1 = 0.99963

    print(k0)
    print(k1)


    vg = np.sqrt(2)*220 * np.sin(th)
    vm = np.sqrt(2)* Vi * np.sin(th+phi)

    vc = Vdc * (4 * np.abs(np.fmod(fc*t, 1)-1/2)-1)

    sp = (vm >= vc)*1
    sn = (vm <= -vc)*1

    vi = Vdc * (sp-sn)

    vl = vi - vg

    ig = np.zeros_like(vl)
    for k in range(1, len(ig)):
        ig[k] = k0*vl[k] + k1*ig[k-1]

    plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})  # comente se não tiver Latex instalado

    # gráficos
    fig, axs = plt.subplots(2, 1, figsize=(5.5, 4), sharex=True)

    axs[0].plot(t, vg, color='darkorange', label='$v_g$', alpha=1.0)
    axs[0].plot(t, vc, color='gray', label='$v_c$', alpha=0.3)
    axs[0].plot(t, vm, color='olivedrab', label='$v_m$', linestyle='-.')

    axs[0].set_ylabel(r'$v$ [V]')

    ax1s = axs[1].twinx()
    ax1s.set_ylim(-25, 25)
    ln_vg, = axs[1].plot(t, vg, color='darkorange', label='$v_g$', alpha=1.0)
    ln_vi, = axs[1].plot(t, vi, linewidth=1.0, color='cornflowerblue', label=r'$v_i$', alpha=0.4)
    ln_ig, = ax1s.plot(t, ig, color='steelblue', label=r'$i_g$')

    ax1s.set_ylabel(r'$i$ [A]', color='steelblue')
    ax1s.tick_params(axis='y', colors='steelblue')
    axs[1].set_ylabel(r'$v$ [V]')
    axs[1].set_xlabel(r'$t$ [s]')

    lines = [ln_vi, ln_vg, ln_ig]
    labels = [line.get_label() for line in lines]
    axs[1].legend(lines, labels, loc='lower right', handlelength=1)

    axs[0].legend(loc='lower right', ncol=1, handlelength=1)
    axs[0].set_xlim(t[0], t[len(t)//2])

    plt.tight_layout()
    plt.savefig(figs_dir / 'inv1.pdf', format="pdf")
    plt.show()



