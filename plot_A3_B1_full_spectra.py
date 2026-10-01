"""Plot the complete A3/B1 transmission and absorbance export."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "YbYAG_A3_B1_last_spectra.csv"
OUTPUT = ROOT / "figures"


def main() -> None:
    data = pd.read_csv(SOURCE).sort_values("Wavelength (nm)")
    wavelength = data["Wavelength (nm)"].to_numpy()
    assert len(data) == 361 and np.all(np.diff(wavelength) > 0)

    for sample in ("A3", "B1"):
        transmission = data[f"{sample} Transmittance"].to_numpy()
        np.testing.assert_allclose(
            data[f"{sample} Transmittance (%)"].to_numpy(),
            100 * transmission,
            atol=1e-12,
        )
        np.testing.assert_allclose(
            data[f"{sample} Abs"].to_numpy(),
            -np.log10(transmission),
            atol=1e-10,
        )

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "savefig.facecolor": "white",
    })
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 6.5), sharex=True,
                             constrained_layout=True)
    colors = {"A3": "#1f5aa6", "B1": "#c46b1a"}
    for sample in ("A3", "B1"):
        axes[0].plot(wavelength, data[f"{sample} Transmittance (%)"],
                     color=colors[sample], linewidth=1.7, label=sample)
        axes[1].plot(wavelength, data[f"{sample} Abs"],
                     color=colors[sample], linewidth=1.7, label=sample)

    axes[0].set(ylabel="Transmittance (%)",
                title="A3 and B1: full exported spectra")
    axes[1].set(xlabel="Wavelength (nm)", ylabel="Absorbance, −log₁₀(T)")
    axes[1].set_xlim(wavelength[0], wavelength[-1])
    for axis in axes:
        axis.grid(color="0.87", linewidth=0.6)
        axis.legend(frameon=False, loc="best")

    OUTPUT.mkdir(exist_ok=True)
    for extension in ("png", "pdf"):
        path = OUTPUT / f"A3_B1_full_spectra.{extension}"
        fig.savefig(path, dpi=220)
        print(path)
    plt.close(fig)


if __name__ == "__main__":
    main()
