# Observational properties of high-z galaxies from semi-analytical models

## Data included

This repository provides predictions from the L-Galaxies2020
for five stellar IMF models (`Salpeter`, `TopHeavy`, `Chon2022`, `Evolution_z`,
`Evolution_metal`) at redshifts `z = 5.08 – 19.92`:

- `UVLF_*.txt` — UV luminosity function `phi(M_1500)` [Mpc^-3 mag^-1]
- `rho_UV_*.txt` — UV luminosity density [erg s^-1 Hz^-1 Mpc^-3, log10]
- `rho_SFR_*.txt` — star-formation-rate density [M_sun yr^-1 Mpc^-3, log10]
- `rho_star_*.txt` — stellar-mass density [M_sun Mpc^-3, log10]
- `n_ion_z_*.txt` — Ionizing photon number density `log10(N_ion)` [cMpc^-3]
- `eta_ion_*.txt` — Ionizing efficiency `log10(ζ_ion)` [erg^-1 Hz]

### `Metal/` directory

Contains mass-metallicity relations and gas/stellar metallicities.

- `Metal/MZR_*.txt` — Mass–metallicity relation `12 + log(O/H)` vs `log M_*` [M_sun].
  Each redshift occupies **4 columns**: `logM_center`, `median`, `p16`, `p84`.
- `Metal/metal_z_*.txt` — `log10(Z)` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- `Metal/O_H_z_*.txt` — `12 + log(O/H)` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- `Metal/Fe_H_z_*.txt` — `[Fe/H]` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- `Metal/O_Fe_z_*.txt` — `[O/Fe]` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.

## Source

The data are taken from:

> Liu et al. 2026, *[Journal / arXiv]*

## Contact

If you are interested in these data, please feel free to contact the authors.

## Citation

If you use these data, please cite Liu et al. 2026.
