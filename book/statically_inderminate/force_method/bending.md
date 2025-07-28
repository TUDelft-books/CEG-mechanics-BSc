```{index} Force method; for frame structures
```

# ... for frame structures

The general concept of the force method is covered in chapter 2.1 while the force method for truss structures is treated in in chapter 2.2.1 - 2.2.7 and the more specific 'hoekveranderingsvergelijkingen' in chapter 3.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

The method of 'hoekveranderingsvergelijkingen' has the advantage that it's very easy to calculate the required rotations using forget-me-nots. However, not for all structures forget-me-nots might be available.

Whenever the book mentions the 'momentenvlakstelling' in example 2.2.6 and 2.2.7, you can also find the displacements using forget-me-nots. The method with moveable nodes ('hoekveranderingsvergelijkingen met verplaatsbare knopen') which was taught is the past is not treated anymore.

We'll cover the application to bending structures with the following example.

::::::{prf:example}
:nonumber: true
:label: sd_ben_0

```{figure} ./bending_data/Example.svg
---
align: center
---
Example structure
```

::::::

1. Determine [the degree of statical determinacy](../determinancy.md).

::::::{prf:example}
:nonumber: true
:label: sd_ben_1

For our example, we might be interested in the internal force distribution, so we need to evaluate the degree of internal statical determinacy.

```{figure} ./bending_data/onbekenden.svg
---
align: center
---
There are 14 unknown forces.
```

```{figure} ./bending_data/vergelijkingen.svg
---
align: center
---
There are 13 equilibrium equations
```

So this structure is 1st order internally statically indeterminant.

::::::

2. Transform the structure in a statical determinant system by releasing releasing a support, splitting the structure at a two-force member or adding hinges: add unknown statically indeterminate forces and displacement constraints for each of the support you released and hinges you added. Be aware that you don't transform the structure in a (partial) mechanism!

::::::{prf:example}
:nonumber: true
:label: sd_ben_2

There are many options here, of which the most obvious ones a few are shown below:

`````{tab-set}
````{tab-item} Release vertical support at $\rm{A}$
```{figure} ./bending_data/optie2.svg
:align: center
```
````
````{tab-item} Release vertical support at $\rm{B}$
```{figure} ./bending_data/optie3.svg
:align: center
```
This option is not very convenient as there are no forget-me-nots to get the displacement at $\rm{B}$ for these loads
````
````{tab-item} Release vertical support at $\rm{C}$
```{figure} ./bending_data/optie4.svg
:align: center
```
````
````{tab-item} Add hinge at $\rm{B}$
```{figure} ./bending_data/optie1.svg
:align: center
```
If only hinges are added, we call this approach 'hoekveranderingsvergelijkingen' or 'gaapvergelijkingen'
````
`````

The last option is chosen.

::::::

3. Solve for the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.

::::::{prf:example}
:nonumber: true
:label: sd_ben_4

We've chosen the following statically determinate structure with displacement constraint $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) $:

```{figure} ./bending_data/SB-systeem.svg
---
align: center
---
The statically determinate structure with displacement constraint
```

Using the forget-me-nots, the rotations can be directly be evaluated without evaluating internal forces:

- $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI}$
- $\varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) = -\cfrac{2M_{\rm{B}}}{3EI}$

::::::

4. Use your displacement constraints to solve for the statically indeterminate forces

::::::{prf:example}
:nonumber: true
:label: sd_ben_5

$$
\begin{align*}
\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) &= \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) \\
\cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI} &= -\cfrac{2M_{\rm{B}}}{3EI} \\
M_{\rm{B}} &= -20 \ \rm{kNm}
\end{align*}
$$
::::::

## Exercises
- Exercises 2.1 - 2.14, 2.23 and 2.25 in chapter 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.
- Exercises 3.1 - 3.10, 3.16 - 3.21 in chapter 3.4 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

Answers are available on [this website for chapter 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) and [here for chapter 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).