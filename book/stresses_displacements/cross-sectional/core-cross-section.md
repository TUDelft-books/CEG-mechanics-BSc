---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: base
  language: python
  name: python3
---

```{index} Neutral axis
```

# Core of a cross-section

```{figure} ./core-cross-section_data/image.png
:align: center
:width: 300

Figure 9.80 {cite:ts}`Hartsuijker2007`
```

```{glossary}
Core of cross-section
  A centre of force within the core corresponds with a stress distribution in the cross-section that does not exhibit a change in sign.

```

This is treated in chapter 4.9 and 9.15.1 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`. Chapter 9 is not part of the Dutch version but can be found chapter 1.5 of Niet-symmetrische en inhomogene doorsnedes {cite}`Hartsuijker2009`.

To find the complete core of a cross-section the method is treated for nonsymmetrical cross-sections in chapter 9.15.2 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`. For symmetrical cross-sections the following relations simplify:

- Equation 9.40 transforms into two independent equations: $M_y = EI_{yy} \cdot \kappa_y$ and $M_z = EI_{zz} \cdot \kappa_z$
- Equation 9.75 transforms into two independent equations: $e_y = -\cfrac{I_{yy}}{A \cdot y_1}$ and $e_z = -\cfrac{I_{zz}}{A \cdot z_1}$

## Example complete core of a symmetrical cross-section

Give is the following cross-section:

```{figure} ./core-cross-section_data/cross-section.svg
:align: center
```

with:
- $A = 180000 \text{ mm}^2$
- $I_{zz} = 4.134375 \cdot 10^9 \text{ mm}^4$
- $I_{yy} = 2.3625 \cdot 10^9 \text{ mm}^4$

The core is defined by the neutral axes along the sides of the cross-section: side $\text{AI}$, $\text{IH}$, $\text{EH}$, $\text{DE}$ and symmetrical $\text{BD}$ and $\text{AB}$.

### Side $\text{AI}$

For $\text{AI}$, $y_1 = \infty$ and $z_1 = -225 \text{ mm}$:

```{figure} ./core-cross-section_data/z1.svg
:align: center
```

This results in:

- $e_y = -\cfrac{2.3625  \cdot 10^9 }{180000 \cdot \infty} = 0 \text{ mm}$
- $e_z = -\cfrac{4.134375 \cdot 10^9}{180000 \cdot -225} \approx 102 \text{ mm} $

This gives the first core point:

```{figure} ./core-cross-section_data/e1.svg
:align: center
```

### Side $\text{IH}$

For $\text{IH}$, $y_1 = -225 \text{ mm}$ and $z_1 = \infty$. This results in:

- $e_y = -\cfrac{2.3625  \cdot 10^9 }{180000 \cdot -225} \approx 58 \text{ mm}$
- $e_z = -\cfrac{4.134375 \cdot 10^9}{180000 \cdot \infty} = 0 \text{ mm}$

### Side $\text{EH}$

For $\text{EH}$, $y_1$ and $z_1$ can not directly be found from the figure, but need to be calculated. The points $\text{E } \left(-75,375\right)$ and $\text{H }\left(-225,75\right)$ are known, giving the equation for the neutral axis: $z = 2 \cdot y + 525$. This gives $y_1 = -262.5 \text{ mm}$ and $z_1 = 525 \text{ mm}$.

```{figure} ./core-cross-section_data/z2.svg
:align: center
```

This results in:

- $e_y = -\cfrac{2.3625  \cdot 10^9 }{180000 \cdot -262.5} = 50\text{ mm}$
- $e_z = -\cfrac{4.134375 \cdot 10^9}{180000 \cdot 525} = -43.75 \text{ mm} $

### Side $\text{DE}$
For $\text{IH}$, $y_1 = \infty$ and $z_1 = 375 \text{ mm}$. This results in:

- $e_y = -\cfrac{2.3625  \cdot 10^9 }{180000 \cdot \infty} = 0 \text{ mm}$
- $e_z = -\cfrac{4.134375 \cdot 10^9}{180000 \cdot 375} = -61.25 \text{ mm}$

### Side $\text{DB}$

Side $\text{DB}$ is the mirror neutral axis and core point from $\text{EH}$ giving: 

- $e_y = -50 \text{ mm}$
- $e_z = -43.75 \text{ mm} $

### Side $\text{AB}$
Side $\text{AB}$ is the mirror neutral axis and core point from $\text{HI}$ giving: 

- $e_y \approx -58 \text{ mm}$
- $e_z = 0 \text{ mm} $

### Core
All these points result in the core:

```{figure} ./core-cross-section_data/core.svg
:align: center
```

## Exercises
- Exercises 4.65-4.72, in chapter 4.14 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol2/Chapter4/).
- Exercise 9.31:1-2, 9.32:1, 9.33:2 in chapter 9.18 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`.
- Vraagstuk 5 in chapter 2.6 of the book Niet-symmetrische en inhomogene doorsnedes {cite:p}`Hartsuijker2009`. Answers available [here](../../antwoorden_Niet-symmetrische_en_inhomogene_doorsnedes.pdf)

```{code-cell} ipython3
:tags: [remove-cell]

z_C = (300*450*150+300*150*450)/(300*450+150*300)
Izz = 1/12*450*300**3+300*450*(z_C-150)**2 + 1/12*300*150**3+300*150*(z_C-450)**2
Iyy = 1/12*450**3*300+1/12*150**3*300
A = 450*300+150*300
display(z_C, Izz, Iyy, A)

e_z_1 = -Izz / (A * -225)
print(e_z_1)
e_y_2 = -Iyy / (A * -225)
print(e_y_2)
e_y_3 = -Iyy / (A * -262.5)
e_z_3 = -Izz / (A * 525)
print(e_y_3, e_z_3)

e_z_4 = -Izz / (A * 375)
print(e_z_4)
```

```{code-cell} ipython3
:tags: [remove-cell]

import sympy as sym

a, b = sym.symbols('a b')

eq1 = sym.Eq(375, a * -75 + b)
eq2 = sym.Eq(75, -225* a + b)

sol = sym.solve((eq1, eq2), (a, b))
display(sol)
```
