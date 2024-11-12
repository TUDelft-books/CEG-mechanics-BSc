```{index} Normal stresses bending
```
```{index} Stress formula
```

# Normal stresses

```{figure} ./normal_data/image.png
:align: center
:width: 300

Figure 4.14a {cite:ts}`Hartsuijker2007`
```

The bending moment gives a linear normal stress distribution:

$$\sigma^{(M)} = \frac{M_{z}z}{I_{zz}}$$

Combining with normal stress due to [extension](../solve_extension/normal.md) gives the stress formula:

$$\sigma(z) = \frac{N}{A} + \frac{M_{z}z}{I_{zz}}$$

This is treated in chapter 4.4 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`.

When there is bending in both the $xz$ plane and $xy$ plane, the general stress formula is obtained:

$$\sigma(y,z) = \frac{N}{A} + \frac{M_{y}y}{I_{yy}} + \frac{M_{z}z}{I_{zz}}$$

This is treated in chapter 4.8 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`.

## Exercises
Exercises 4.1-4.64, in chapter 4.14 of the book Engineering Mechanics Volume 2 {cite:p}`Hartsuijker2007`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol2/Chapter4/).