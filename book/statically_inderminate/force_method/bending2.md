```{index} Force method; for frame structures
```

# ... for frame structures

The general concept of the force method is covered in chapter 2.1 while the force method for framestructures is treated in in chapter 2.2.5 - 2.2.7 and the more specific 'hoekveranderingsvergelijkingen' in chapter 3.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

Again, the method of 'hoekveranderingsvergelijkingen' has the advantage that it's very easy to calculate the required rotations using forget-me-nots. However, not for all structures forget-me-nots might be available.

Whenever the book mentions the 'momentenvlakstelling' in example 2.2.6 and 2.2.7, you can also find the displacements using forget-me-nots. The method with moveable nodes ('hoekveranderingsvergelijkingen met verplaatsbare knopen') which was taught is the past is not treated anymore.

We'll cover the application to bending structures with the following example.

::::::{prf:example}
:nonumber: true
:label: sd_raam_0

```{figure} ./theorie_data/example.svg
---
align: center
---
Example structure
```

::::::

1. Determine [the degree of statical determinacy](../determinancy.md).

::::::{prf:example}
:nonumber: true
:label: sd_raam_1

For our example, we are interested in the distribution of internal forces, so we must evaluate the degree of internal static indeterminacy.

```{figure} ./theorie_data/onbekenden.svg
---
align: center
---
There are 21 unknown forces.
```

```{figure} ./theorie_data/vergelijkingen.svg
---
align: center
---
There are 19 equilibrium equations
```

This structure is therefore 2nd degree internally statically indeterminate.

::::::

2. Transform the structure in a statical determinant system by releasing releasing a support, splitting the structure at a two-force member or adding hinges: add unknown statically indeterminate forces and displacement constraints for each of the support you released and hinges you added. Be aware that you don't transform the structure in a (partial) mechanism!

::::::{prf:example}
:nonumber: true
:label: sd_raam_2

There are many options, some of which are possible options:

`````{tab-set}
````{tab-item} Release horizontal support at $\rm{B}$ and add hinge at $\rm{B}$
```{figure} ./theorie_data/optie1.svg
:align: center
```
````
````{tab-item} Release horizontal supports at $\rm{B}$ and $\rm{C}$
```{figure} ./theorie_data/optie2.svg
:align: center
```

````
````{tab-item} Release horizontal and vertical supports at $\rm{A}$
```{figure} ./theorie_data/optie3.svg
:align: center
```
````
````{tab-item} Release horizontal support at $\rm{A}$ and add hinge at $\rm{B}$
```{figure} ./theorie_data/optie4.svg
:align: center
```
````
`````

The third option is chosen.

::::::

3. Solve for the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.

::::::{prf:example}
:nonumber: true
:label: sd_raam_4

We have chosen the following statically determinate structure with displacement conditions $w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $ and $w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $:

```{figure} ./theorie_data/SB-systeem.svg
---
align: center
---
The statically determinate structure with displacement conditions
```

The force distribution can be found with equilibrium:

- $M_{\rm{C}} = 90 \ \rm{kNm}$ (◠/ᑐ)
- $M_{\rm{B}} = 6A_{\rm{v}}$ (◡/ᑐ)

Using the forget-me-nots method, the rotations can now be evaluated:

- $\varphi_{\rm{B}} = 0.0012 A_{\rm{v}} - 0.018$
- $w_{\rm{A}} = 0.0216 A_{\rm{v}} - 0.108$

For the horizontal displacement applies: $w_{\rm{A,h}}  = \cfrac{6A_{\rm{h}}}{EA} $

::::::

4. Use your displacement constraints to solve for the statically indeterminate forces

::::::{prf:example}
:nonumber: true
:label: sd_raam_5

$$
\begin{align*}
w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
 0.0216 A_{\rm{v}} - 0.108 &= 0 \\
A_{\rm{v}} &= 5 \ \rm{kN} \\
\\
w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
\cfrac{6A_{\rm{h}}}{EA} &= 0 \\
A_{\rm{h}} &= 0 \ \rm{kN}
\end{align*}
$$
::::::

## Exercises

- Exercises 2.15 - 2.22, 2.24, 2.26 - 2.29, 2.42 - 2.48 in chapter 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.
- Exercises 3.11 - 3.15, 3.22, 3.23, 3.25 - 3.33/1, 3.35, 3.36, 3.45, 3.47-1, 3.47-2, 3.47-4, 3.50, 3.51 in chapter 3.4 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

Answers are available on [this website for chapter 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) and [here for chapter 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).