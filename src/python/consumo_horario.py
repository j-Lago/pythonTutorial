import pandas as pd
import matplotlib.pyplot as plt
from project_paths import *


if __name__ == '__main__':

    # importa dados
    df = pd.read_csv(data_dir / 'subestacao.csv',
                     index_col='time',
                     parse_dates=['time'],
                     date_format='%Y-%m-%d %H:%M:%S')

    # exclui finais de semana
    df = df[df.index.weekday < 5]

    # calcula potência total
    df['P [W]'] = df['Pa [W]'] + df['Pb [W]'] + df['Pc [W]']

    # adiciona coluna com hora cheia
    df['hour'] = df.index.hour

    # cria lista com potência média horária
    mean_power = [0.0] * 24
    argmax = 0
    for h in range(len(mean_power)):
        locs = df.index[df['hour'] == h]
        mean_power[h] += df['P [W]'].loc[locs].loc[locs].sum() / len(locs) / 1000
        if mean_power[h] > mean_power[argmax]:
            argmax = h

    # plot
    plt.rcParams.update({'text.usetex': True, 'font.family': 'serif'})    # comente se não tiver latex instalado
    plt.figure(figsize=(5.6, 2.5))

    plt.bar(range(len(mean_power)), mean_power, zorder=3, label='consumo médio horário', color='#8080E6')
    plt.bar(argmax, mean_power[argmax], zorder=4, label='consumo médio no horário de pico',
            color='#664DE6', edgecolor='#8080E6', hatch='////')

    plt.ylim(0, 450)
    plt.xlim(-0.5, 23.5)
    plt.xlabel(r'hora~do~dia')
    plt.ylabel(r'consumo~[kWh]')

    plt.xticks(list(range(0, len(mean_power), 2)))
    plt.grid(visible=True, alpha=0.3)

    plt.legend(loc='lower center',
               framealpha=0,
               ncol=2,
               bbox_to_anchor=(0.5, 1.01))
    plt.tight_layout()

    plt.savefig(figs_dir / 'subestacao.pdf', format='pdf')
    plt.show()
