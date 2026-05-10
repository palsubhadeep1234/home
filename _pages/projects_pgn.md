---
permalink: /projects/pgn/
title: "Polymer-Grafted Nanoparticles (PGNs)"
layout: single
author_profile: true
---

<a href="/home/projects/" class="back-link">← Back to Research Projects</a>

Polymer-grafted nanoparticles — nanoparticle cores with polymer chains tethered to their surface — exhibit a uniquely tunable combination of stiffness, toughness, and self-organization that makes them compelling for next-generation structural and protective materials. A central theme of my PhD was to understand, model, and design PGN systems across multiple length scales: from atomistic coarse-grained MD through particle-based mesoscale models, and ultimately validated against experiments. This category encompasses ballistic response, shear mechanics, binary architectures, ultra-coarse-grained modeling, and nanocomposite design.

---

### 3. Micro-Ballistic Performance of PGN Thin-Film Monolayers
*Advisor: Dr. Sinan Keten* · **2022 – 2024**

- Performed micro-ballistic **LIPIT** simulations on coarse-grained SiO₂–PMMA PGN films to study how **graft chain length** and **NP core density** affect ballistic performance.
- Identified a positive relation between **cohesive energy density** and **specific penetration energy** (E<sub>p</sub><sup>∗</sup>), and a failure-mode shift from **segment pull-out** to **fragmentation** for shorter grafts due to lower cohesion.
- Proposed a new ballistic metric, **average deceleration rate of the bullet** (A<sub>b</sub>). Found **intermediate graft lengths** (N ≈ 40–100) optimize both E<sub>p</sub><sup>∗</sup> and A<sub>b</sub>, suggesting designs for **impact-resistant** coatings where backface deformation must stay low.

**Related publication:**
- **Pal, S.**, & Keten, S., *Micro-Ballistic Response of Thin Polymer-Grafted Nanoparticle Films.* **Soft Matter**, 2024. DOI: [10.1039/D4SM00718B](https://doi.org/10.1039/D4SM00718B) [*Soft Matter Pioneering Investigators series*]

---

### 4. Characterizing the Shear Response of PGNs
*Advisors/Collaborators: Dr. Sinan Keten; Arman Moussavi; Dr. Zhenghao Wu (Xi'an Jiaotong University)* · **2022 – 2023**

- Built PGN models with **Kremer–Grest beads** and **FENE** bonds to probe shear response across NP core radius, grafting density, and chain length; observed a **linear** relation between **NP volume fraction** and **modulus**.
- Showed PGNs with **short grafts** have **higher stiffness** than linear polymer melts due to **NP reinforcement**, indicating routes to stronger polymer composites and reduced reliance on single-use plastics.

**Related publications:**
- Moussavi, A., **Pal, S.**, Wu, Z., & Keten, S., *Characterizing the Shear Response of Polymer-Grafted Nanoparticles.* **Journal of Chemical Physics**, 2024. DOI: [10.1063/5.0188494](https://doi.org/10.1063/5.0188494)
- Moussavi, A., Wu, Z., **Pal, S.**, & Keten, S., *Nanoconfinement Release Toughens Polymer-Grafted Nanoparticle Assemblies Through Better Interdigitation and Entanglements.* **Nano Letters**, 2025. DOI: [10.1021/acs.nanolett.5c00680](https://doi.org/10.1021/acs.nanolett.5c00680)

---

### 5. Binary PGN Mechanics & Active Learning
*Advisors/Collaborators: Dr. Sinan Keten; Dr. Wei Chen* · **2023 – 2025**

- Constructed molecular models of **binary PGNs** with different graft architectures, reproducing experimentally observed PGN superlattices and elucidating their mechanical responses; revealed that **NaCl-like binary PGNs** offer simultaneously higher modulus and toughness due to efficient packing.
- Implemented a **Gaussian process (GP) metamodel** and **Bayesian optimization (BO)** to complement CG-MD results and efficiently probe the complex design space — reducing uncertainty, constructing the **Pareto front**, and mapping structure-property relationships across the binary composition space.

**Related publications:**
- **Pal, S.**, Khumbhojkar, G., Chen, W., & Keten, S., *From Packing to Performance: Decoding Nanoscale Mechanics of Binary Polymer-Grafted Nanoparticles via Active Learning.* **Macromolecules** *(In press)*
- Singh, M., Lin, H., **Pal, S.**, et al., *Process-Driven Control of the Properties of Polymer Grafted Nanoparticle Composites.* **ACS Nano** *(In press)*

---

### 6. Implicit Chain Particle Model (ICPM) — Particle-Based PGN Modeling
*Advisors/Collaborators: Dr. Sinan Keten; Dr. Wei Chen; Dr. Sanat K. Kumar (Columbia); Dr. Zhenghao Wu (Xi'an Jiaotong University)* · **2022 – 2024**

- Advanced the **Implicit Chain Particle Model (ICPM)** representing each PGN as a **single bead**, achieving ~**10⁷× speed-up** over all-atom models while accurately predicting bulk modulus and toughness.
- Built **two- and three-body** interaction forms from strain-energy functions, complemented by an **ML model** trained on simulation data, enabling **micron-scale simulations** beyond traditional MD length-scale limits.

**Related publication:**
- Wu, Z., **Pal, S.**, & Keten, S., *Implicit Chain Particle Model for Polymer-Grafted Nanoparticles.* **Macromolecules**, 2023. DOI: [10.1021/acs.macromol.2c02272](https://doi.org/10.1021/acs.macromol.2c02272)

---

### 7. Engineering Nanocomposite Mechanics via Polymer-Conformation Programming
*Advisors/Collaborators: Dr. Sinan Keten; Tiffany Chen; Dr. Ting Xu (UC Berkeley)* · **2023 – 2024**

- Employed the **ICPM framework** to construct micron-scale PGN thin films with nanoparticle radii 10–100× larger than graft lengths, enabling efficient simulation of **nanoindentation** responses and quantitative modulus comparison.
- Achieved close agreement with experimental modulus trends and failure patterns, revealing that stiffness enhancement arises from **increased inter-PGN cohesion** mediated by activated polymer volume — a molecular-level mechanism inaccessible to experiments alone.

**Related publication:**
- Chen, T., Qian, Y., Laine, A., Kwon, J., Liu, L., **Pal, S.**, et al., *Engineer Reversible Nanocomposite by Programming Amorphous Polymer Conformation Under Nanoconfinement.* **Advanced Materials**, 2025. DOI: [10.1002/adma.202415352](https://doi.org/10.1002/adma.202415352)
