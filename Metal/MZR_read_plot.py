import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

data_dir = r"./imf_fig"   # 
z_list = [5.08, 5.96, 6.99, 7.88, 8.91, 10.07, 10.94, 11.90, 12.94, 14.09, 14.70]

# 
n_z = len(z_list)
n_cols_expected = 4 * n_z          # = 44

models = [
    ("Salpeter",    r'$\mathrm{Salpeter \, IMF}$',                'k', '-',  1.5),
    ("TopHeavy",    r'$\mathrm{TopHeavy \, IMF}$',                'b', '--', 1.0),
    ("Chon2022",    r'$\mathrm{Chon2022 \, IMF}$',                'm', '-.', 1.0),
    ("Evolution_z", r'$\mathrm{Evolution}(z) \, \mathrm{IMF}$',   'c', '-',  1.0),
    ("Evolution_Z", r'$\mathrm{Evolution}(Z) \, \mathrm{IMF}$',   'r', ':',  1.0),
]

data_all = {}
for key, *_ in models:
    fpath = os.path.join(data_dir, f"MZR_{key}.txt")
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"no find file: {fpath}")
 
    arr = np.loadtxt(fpath, comments='#', usecols=range(n_cols_expected))
    data_all[key] = arr

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['font.size'] = 9

fig, axes = plt.subplots(3, 4, figsize=(8., 4.95), sharex=True, sharey=True,
                         gridspec_kw={'hspace': 0, 'wspace': 0})
axes = axes.flatten()
ax_legend = axes[-1]
ax_legend.axis('off')

xlim = (4.35, 9.85)
ylim = (5.5, 9.5)

for idx, z in enumerate(z_list):
    if idx >= len(axes) - 1:
        break
    ax = axes[idx]

    # 4*idx (logM), +1 (median), +2 (p16), +3 (p84)
    col_logM = idx * 4
    col_med  = col_logM + 1
    col_p16  = col_logM + 2
    col_p84  = col_logM + 3

    for key, label, color, ls, lw in models:
        x_model = data_all[key][:, col_logM]
        med = data_all[key][:, col_med]
        
        valid_med = ~np.isnan(med)
        ax.plot(x_model[valid_med], med[valid_med], 
                color=color, ls=ls, lw=lw, label=label, alpha=0.8)

        # Salpeter 1σ 
        if key == "Salpeter":
            p16 = data_all[key][:, col_p16]
            p84 = data_all[key][:, col_p84]
            valid_shade = ~np.isnan(p16) & ~np.isnan(p84)
            ax.fill_between(x_model[valid_shade], p16[valid_shade], p84[valid_shade], 
                            color='gray', alpha=0.2, zorder=0)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks([5, 6, 7, 8, 9])
    ax.text(0.05, 0.8, f"$z={z:.2f}$", transform=ax.transAxes,
            va='bottom', ha='left', fontsize=11)

for i in [0, 4, 8]:
    axes[i].set_ylabel(r'$12+\log({\rm O/H})$', fontsize=12)
for i in [7, 8, 9, 10]:
    axes[i].set_xlabel(r'$\log\,M_{*}[\rm M_{\odot}]$', fontsize=12)
    if i == 7:
        axes[7].tick_params(labelbottom=True)

legend_elements = [
    Line2D([0], [0], color=c, linestyle=ls, linewidth=lw, label=lab)
    for key, lab, c, ls, lw in models
]
ax_legend.legend(handles=legend_elements, loc='lower center',
                 frameon=False, fontsize=8.)

plt.tight_layout()

out_fig = os.path.join(data_dir, "MZR_from_txt_fixed.pdf")
plt.savefig(out_fig, dpi=300, bbox_inches='tight')
print(f"Saved figure: {out_fig}")

plt.show()
