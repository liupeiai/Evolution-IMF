# Observational properties of high-z galaxies from semi-analytical models

## 🖥️ Simulation data

This repository provides predictions from the L-Galaxies2020
for five stellar IMF models (`Salpeter`, `TopHeavy`, `Chon2022`, `Evolution_z`,
`Evolution_metal`) at redshifts `z = 5.08 – 19.92`:

- 📊 `UVLF_*.txt` — UV luminosity function `phi(M_1500)` [Mpc^-3 mag^-1]
- ✨ `rho_UV_*.txt` — UV luminosity density `rho_UV` [erg s^-1 Hz^-1 Mpc^-3, log10]
- ⭐ `rho_SFR_*.txt` — star-formation-rate density `rho_SFR` [M_sun yr^-1 Mpc^-3, log10]
- 🌍 `rho_star_*.txt` — stellar-mass density `rho_*` [M_sun Mpc^-3, log10]
- ⚡ `n_ion_z_*.txt` — Ionizing photon number density `log10(N_ion)` [cMpc^-3]
- 🎯 `eta_ion_*.txt` — Ionizing efficiency `log10(ζ_ion)` [erg^-1 Hz]

### 📁 `Metal` 

Contains mass-metallicity relations and gas/stellar metallicities.

- 🧬 `Metal/MZR_*.txt` — Mass–metallicity relation `12 + log(O/H)` vs `log M_*` [M_sun].
  Each redshift occupies **4 columns**: `logM_center`, `median`, `p16`, `p84`.
- 🔬 `Metal/metal_z_*.txt` — `log10(Z)` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- 🔭 `Metal/O_H_z_*.txt` — `12 + log(O/H)` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- ⚛️ `Metal/Fe_H_z_*.txt` — `[Fe/H]` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.
- 🔥 `Metal/O_Fe_z_*.txt` — `[O/Fe]` as a function of redshift. Columns: `z`, `Gas`, `Stellar`.

## 📖 Source

The data are taken from:

> Liu et al. 2026, *[Journal / arXiv]*

## ✉️ Contact

If you are interested in these data, please feel free to contact the authors.
- 👨‍🔬 Peiai Liu (刘培爱)
- <p align="left">
    <a href="https://orcid.org/0009-0001-8640-9012" target="_blank">
      <img src="https://img.shields.io/badge/ORCID-0009--0001--8640--9012-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"/>
    </a>
  </p>
- <p align="left">
    <a href="mailto:peiailiu@qq.com">
      <img src="https://img.shields.io/badge/Email-peiailiu@qq.com-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/>
    </a>
  </p>
- 🔭 Institute for Astrophysics, Zhengzhou University
