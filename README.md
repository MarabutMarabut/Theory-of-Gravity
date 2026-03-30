# Marabūt's Theory of Gravity: The Electron Flow Model (EFM)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19264537.svg)](https://doi.org/10.5281/zenodo.19264537)
[![Live Simulation](https://img.shields.io/badge/Live_Demo-Volumetric_Profiler-success.svg)](https://marabutmarabut.github.io/Theory-of-Gravity/)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the official computational repository for **Marabūt's Theory of Gravity**. This repository hosts the mathematical engines, 3D fluid-dynamic visualization tools, and structural data validating the **Electron Flow Model (EFM)**.

Traditional astrophysics treats gravity as a static geometric property of mass, retroactively assigning mass to celestial bodies to balance orbital equations. The EFM introduces a paradigm shift: **gravity is a continuous, hydrodynamic pressure gradient driven by the consumption of vacuum flux (electrons).**

## 🌌 The Electron Flow Model (EFM)

In the EFM framework, a celestial core acts as a negative sink, initiating an **Electron Jump Cascade**. This radial inward flow of vacuum flux imparts microscopic momentum to atomic nuclei—a process defined as **Micro-Kinetic Transfer**. The macroscopic synchronization of this subatomic push-pull mechanism is what we experience as gravity.

### Key Features of this Repository:
* **The Volumetric Profiler (The Mara Scale):** A dynamic 11-point coordinate system mapping gravitational flux density from the deep-space boundary (Mara10) straight down to the core sink (Mara0).
* **The Computational Atlas:** Validation of the model against 38 celestial bodies (stars, gas giants, rocky planets, moons, dwarf planets, and interstellar anomalies) with sub-2% variances from observed NASA data.
* **`efm_engine.py`:** The core Python driver for generating 3D hydrodynamic vacuum flux vector maps based on localized impedance and ambient flux constraints.

---

## 🧮 The Unified Three-Formula System

The EFM utilizes a unified fluid-dynamic framework tailored to the structural phase state and flux-shielding capacity of the celestial body. By extracting Newton's constant ($G$) and identifying the baseline amplification as the geometric spherical integration prefactor ($\alpha = 4\pi/3$), the EFM calculates gravity forward.

**1. Primary Gas Giants (High Rotation, Fluid Surface)**
Massive bodies with isolated flux boundaries and high rotational expansion.

$$g_{surf} = \left[ (\alpha G) \cdot \rho_{eff} \cdot R \cdot \tau(T) \right] - \frac{v_{rot}^2}{R}$$

**2. Primary Rocky Planets (Self-Shielded, Solid Surface)**
Dense, rigid bodies generating isolated boundaries without extreme centrifugal offsets.

$$g_{surf} = (\alpha G) \cdot \rho_{eff} \cdot R \cdot \tau(T)$$

**3. Small Bodies & Moons (Unshielded, Ambient-Dependent)**
Bodies lacking the bulk to self-shield. Their local engines are amplified by the Ambient Flux Multiplier based on their distance to the primary reference body ($D_{ref}$).

$$g_{surf} = \left( \left[ (\alpha G) \cdot \rho_{eff} \cdot R \cdot \tau(T) \right] - \frac{v_{rot}^2}{R} \right) \cdot (D_{ref})^{0.21}$$

*Where $\rho_{eff}$ is effective density, $R$ is volumetric radius, and $\tau(T)$ is the structural/thermodynamic impedance of the planetary phase state.*

---

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

---

## 📖 The Official Manuscript & LaTeX Source

For full transparency and editorial review, the complete source code and compiled manuscript are included in this repository:
* **LaTeX Source:** `Marabuts-Theory-of-Gravity.tex`
* **Compiled PDF:** `Marabuts-Theory-of-Gravity.pdf`

These files contain the complete theoretical framework, derivations, quantum mechanical implications (including the resolution of the Energy-Thermal Paradox and Vibronic Coupling), and the full 38-body Computational Atlas.

For the officially published and archived version, our paper is hosted on CERN's Zenodo:

**Marabūt, C. B., & Marabūt, A. L. (2026).** *Marabūt's Theory of Gravity: The Push-Pull Mechanics of Vacuum Flux* (v39).
[Read the full paper on Zenodo](https://doi.org/10.5281/zenodo.19264537)

---

## 👥 About the Authors

**Christopher Berry Marabūt** [![ORCID](https://img.shields.io/badge/ORCID-0009--0001--9759--9587-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0001-9759-9587)  
Is an Associate Director of Infrastructure/Cloud Architecture and an independent researcher specializing in computational physics and complex systems. A Certified Azure Solution Architect Expert and Agentic AI Business Solutions Architect, he applies advanced programming and simulation techniques to model the universe as a dynamic system of fluid energy flows.

**Angelina Lopez Marabūt** [![ORCID](https://img.shields.io/badge/ORCID-0009--0007--9937--6145-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0007-9937-6145)  
Is a co-author, strategic partner, and vital collaborator on the theoretical development and structural refinement of the Electron Flow Model. 

*We aim to bridge the gap between plasma physics, superfluid vacuum theory, and classical mechanics—inviting the next generation to explore the "cosmic dance" of electrons.*

---
*“Gravity is not merely curved space, but a dynamic, fluid circuit.”*
```
