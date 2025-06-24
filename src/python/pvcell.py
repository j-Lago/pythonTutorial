import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import math
import pandas as pd
from project_paths import *

def i_cell(v: float) -> float:
    i = 0.0  # chute inicial
    while True:
        arg = (v - i * Rs) / T
        fi = I - S * math.exp(arg - 1) - (v - i * Rs) / Rp - i
        dfi = - 1 -S * Rs / T * math.exp(arg)  - Rs / Rp
        delta = fi / dfi
        i -= delta
        if abs(delta) < epsilon:
            break
    return i



if __name__ == '__main__':

    # constantes
    Rs = 0.002
    Rp = 10
    I = 8
    S = 0.02
    T = 0.085
    epsilon = 0.001

    # etapa 1
    print(f"{i_cell(0.4) = }")
    print(f"{i_cell(0.5) = }")

    plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})   # comente se não tiver latex instalado

    # etapa 2
    v = np.linspace(0,0.6, 100)
    p = np.zeros_like(v)
    i = np.zeros_like(v)

    for k in range(len(v)):
        i[k] = i_cell(v[k])
        p[k] = v[k] * i[k]

    plt.figure(1, figsize=(5, 2.8))
    plt.plot(v, i, color='steelblue')
    plt.xlabel(r'$v_{cell}$ [V]')
    plt.ylabel(r'$i_{cell}$ [A]')
    plt.xlim(v[0], v[-1])
    plt.ylim(-1, 9)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(figs_dir / "pvcell.pdf", format="pdf")

    # etapa 3
    res = minimize_scalar(lambda v: -v * i_cell(v), bounds=(0.0, 0.6), method='bounded')
    votp = res.x
    potp = -res.fun
    print(votp, potp)

    plt.figure(2, figsize=(5, 2.8))
    plt.plot(v, p, color='olivedrab')
    plt.plot(votp, potp, color='darkorange', marker='*', markersize=10)
    plt.xlabel(r'$v_{cell}$ [V]')
    plt.ylabel(r'$p_{cell}$ [W]')
    plt.xlim(v[0], v[-1])
    plt.ylim(-1, 4)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(figs_dir / "pvcellotp.pdf", format="pdf")

    plt.show()