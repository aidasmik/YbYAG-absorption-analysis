# Yb:YAG absorption from reflection and transmission spectra

This repository contains the measured spectra and the executed [analysis notebook](YbYAG_measurement_to_cross_section.ipynb). The notebook plots the raw measurements, applies the documented reflectance corrections, separates the coated samples' two-pass attenuation into one-pass absorbance, estimates absorption cross sections, and compares the results with literature points. It also plots the uncoated A3 transmission, the available photoluminescence (PL) spectra, and separately acquired spatial PL-ratio maps.

## Samples and assigned thicknesses

| Specimen | Nominal Yb | Thickness | Measurement used |
| --- | ---: | ---: | --- |
| Coated sample 5 | 5 at.% | 502 µm | Paired A/B reflectance; A is the coated face |
| Coated sample 10 | 10 at.% | 463 µm | Paired A/B reflectance; B is the coated face |
| Coated sample 15 | 15 at.% | 472 µm | Paired A/B reflectance; B is the coated face |
| Uncoated A3 | 5 at.% | 509 µm | Single-pass transmission |

The **509 µm, nominal 5 at.%** values were assigned to A3 from the user's description of an uncoated 5% sample. The source export identifies A3 as uncoated but does not independently establish that concentration. The PL file labeled *uncoated/unknown, 300 K* is likewise **not identified as A3**.

## Run the notebook

Use Python 3.11 from this repository's root directory:

```bash
python -m pip install -r requirements.txt
python -m jupyter lab YbYAG_measurement_to_cross_section.ipynb
```

Run all cells in order. They write derived CSVs and PDF/PNG plots to `figures_academic/`. Those products are excluded from Git because the executed notebook already contains its plots and the cells regenerate them. The bundled aluminum-reference CSV is a **NIST example curve**, not a measurement of the mirror used in the lab. The shared smooth reflectance compensation is a relative visualization; the absolute cross sections remain conditional on the simplified optical model and nominal concentrations.

The [full A3/B1 export plot](figures/A3_B1_full_spectra.png) shows both samples' raw transmittance and absorbance from 800 to 1200 nm, without optical corrections or smoothing. Regenerate the PNG and PDF with `python plot_A3_B1_full_spectra.py`.

## Input data

| Files | Content |
| --- | --- |
| `reflection/YbYag_{5,10,15}_{A,B}_R.txt` | Six measured face-reflectance scans |
| `YbYag_T.csv`, `YbYag_ABS.csv` | Published transmission and derived absorbance exports |
| `YbYAG_A3_B1_last_spectra.csv` | A3 and B1 transmission and absorbance; the main absorption analysis uses A3 only |
| `YbYAG_A3_spectra.csv` | A3-only copy of the wavelength, absorbance, and transmittance columns, with source values unchanged |
| `pl_reference/*.csv` | Cleaned PL spectra and reported concentration ratios |
| `pl_reference/spatial_maps/*.csv`, `pair_selection.json` | Selected coordinate-resolved 5%, 10%, and 15% PL-ratio maps and scan provenance |
| `aluminum_reference_nist_example.csv` | Illustrative mirror reference used by the notebook |
| `literature_reference_values.csv` | Reference values and citations |

The reflection spectra and spectral PL tables were copied from [`aidasmik/YbYAG`](https://github.com/aidasmik/YbYAG/tree/d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3) at commit `d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3`. The original source repository provides the [reflection files](https://github.com/aidasmik/YbYAG/tree/d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3/data/reflection), [A3/B1 spectral export](https://github.com/aidasmik/YbYAG/blob/d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3/data/YbYAG_A3_B1_last_spectra.csv), [PL files](https://github.com/aidasmik/YbYAG/tree/d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3/data/pl), and [literature table](https://github.com/aidasmik/YbYAG/blob/d626e35938bf3ccce9c83d8cf133b6b7aa52a0a3/data/analysis_2026_09_17/literature_reference_values.csv). The spatial PL maps are separate lab measurements archived in `pl_reference/spatial_maps/`; they are not used to derive absorption cross sections.
