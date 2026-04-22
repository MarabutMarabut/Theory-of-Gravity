-----

# Marabūt's Theory of Gravity: The Electron Flow Model (EFM)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19672868.svg)](https://doi.org/10.5281/zenodo.19672868)
[![Live Simulation](https://img.shields.io/badge/Live_Demo-Volumetric_Profiler-success.svg)](https://marabutmarabut.github.io/Theory-of-Gravity/)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the official computational repository for **Marabūt's Theory of Gravity**. This repository hosts the mathematical engines, 3D fluid-dynamic visualization tools, and structural data validating the **Electron Flow Model (EFM)**.

Traditional astrophysics treats gravity as a static geometric property of mass, retroactively assigning mass to celestial bodies to balance orbital equations. The EFM introduces a definitive paradigm shift in computational astrophysics: **gravity is a continuous, hydrodynamic pressure gradient driven by the consumption of vacuum flux.**

## 🌌 The Electron Flow Model (EFM)

In the EFM framework, a celestial core acts as a negative sink, initiating an **Electron Jump Cascade**. This radial inward flow of vacuum flux imparts microscopic momentum to atomic nuclei—a process defined as **Micro-Kinetic Transfer**. The macroscopic synchronization of this subatomic push-pull mechanism is the physical pressure we experience as gravity.

### Key Features of this Repository:

  * **The Volumetric Profiler (The Mara Scale):** A dynamic 11-point coordinate system mapping gravitational flux density from the deep-space boundary (Mara10) straight down to the core sink (Mara0).
  * **The Grand Computational Atlas:** Validation of the model against **64 celestial bodies**—including main sequence stars, circumbinary exoplanets, degenerate stellar remnants, and ultramassive black holes—with sub-2% variances from observed NASA data.
  * **Resolving Anomalies natively:** The framework demonstrates mathematical stability across extreme cosmological bounds, offering fluid-dynamic resolutions to the "Final Parsec Problem" and providing a deterministic alternative to "dark matter" halos.
  * **`efm_engine.py`:** The core Python driver for generating 3D hydrodynamic vacuum flux vector maps based on localized impedance and ambient flux constraints.

-----

## 🧮 The Unified Master Equation

Classical physics patches different mathematical rules together for different celestial bodies. The EFM abandons this for a single, elegant fluid-dynamic algorithm. This formula calculates the raw power of the local engine and dynamically tests it against the environment using the **Environmental Superposition Factor** ($\Omega_{shield}$).

$$g_{surf}=[(\alpha G)\cdot\rho_{eff}\cdot R_{surf}\cdot\tau(T)-\frac{v_{rot}^{2}}{R_{surf}}]\cdot\Omega_{shield}$$

  * **Self-Shielded Primary Bodies:** For massive bodies like Jupiter or Earth that secure their own boundary against the solar wind, $\Omega_{shield}$ locks at **$1.000$**.
  * **Ambient-Dependent Small Bodies:** For moons or dwarf planets whose boundaries are breached by the rushing flux of a parent star or planet, $\Omega_{shield}$ activates as the Ambient Flux Multiplier $(D_{ref})^{0.21}$, scaling the body's gravity based on the density of the river it is swimming in.

*Where $\alpha G$ is the baseline geometric vacuum resistance, $\rho_{eff}$ is effective density, $R_{surf}$ is volumetric radius, $\tau(T)$ is the structural/thermodynamic impedance, and $v_{rot}$ accounts for centrifugal exhaust.*

-----

## 🚀 Getting Started

To visualize the hydrodynamic flow of vacuum flux cascading into a core sink, run the core mathematical engine.

### Prerequisites

Ensure you have Python 3.x installed along with `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
```

### Running the EFM Engine

```bash
python efm_engine.py
```

This script will output a 3D vector quiver plot (`marabut_3d_flow.png`) demonstrating the continuous, multiaxial inward acceleration of vacuum flux toward a negative core sink.

*(Note: Ensure your code editor utilizes a strict 2-space indentation rule to maintain alignment with the repository's source code standards).*

-----

## 📖 The Official Manuscript & LaTeX Source

For full transparency and editorial review, the complete source code and compiled manuscript are included in this repository:

  * **LaTeX Source:** `2026-04-20-v41-Marabuts-Theory-of-Gravity.tex`
  * **Compiled PDF:** `2026-04-20-v41-Marabuts-Theory-of-Gravity.pdf`

These files contain the complete theoretical framework, derivations, quantum mechanical implications (including the resolution of the Energy-Thermal Paradox and Vibronic Coupling), and the full 64-body Computational Atlas.

For the officially published and archived version, our paper is hosted on CERN's Zenodo:

**Marabūt, C. B., & Marabūt, A. L. (2026).** *Marabūt's Theory of Gravity: The Push-Pull Mechanics of Vacuum Flux* (v41).  
[Read the full paper on Zenodo](https://doi.org/10.5281/zenodo.19672868)

-----

## 👥 About the Authors

**Christopher Berry Marabūt** [![ORCID](https://img.shields.io/badge/ORCID-0009--0001--9759--9587-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0001-9759-9587)  
Is an Associate Director of Infrastructure and Cloud Architecture at Kyndryl Holdings, Inc., and an independent researcher specializing in computational physics and complex systems. Holding elite credentials as a Microsoft Certified Azure Solution Architect Expert and fluent in over 14 programming languages, he leverages advanced architectural logic to investigate fundamental cosmological mechanisms. Driven by the ultimate question of *how* gravity mechanically works, he developed the Unified Master Equation—a framework capable of calculating gravity continuously from the crushing core of an ultramassive black hole all the way out into the vacuum of deep space.

**Angelina Lopez Marabūt** [![ORCID](https://img.shields.io/badge/ORCID-0009--0007--9937--6145-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0007-9937-6145)  
Is an independent researcher specializing in technical communication and English Language Teaching (ELT). As the co-author and strategic partner of the Electron Flow Model, Angelina plays a vital role in bridging the critical gap between complex theoretical physics and public understanding. Her primary contribution lies in deconstructing dense mathematical frameworks—such as hydrodynamic fluid pressure and the Unified Master Equation—and translating them into clear, highly accessible scientific communication, ensuring that profound scientific truths are democratized and available to everyone.

*We aim to bridge the gap between plasma physics, quantum mechanics, and classical astrophysics—inviting the next generation to explore the cosmos through the lens of electron dynamics.*

-----

*"Gravity is not merely curved space, but a dynamic, fluid circuit."*

-----
