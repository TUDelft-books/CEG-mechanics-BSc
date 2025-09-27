
```{index} Force method; for truss structures
```

# ... for truss structures

The general concept of the force method is shown in [](force_method) and discussed in section 2.1. Specifically, the force method for truss structures is covered in sections 2.2.8 - 2.2.10 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

We discuss the application to truss structures with the following example. This example includes a [Williot diagram](../../stresses_displacements/displacements_truss/williot.md) to calculate the displacements.

::::::{prf:example}
:nonumber: true
:label: sd_ext_0

```{figure} ./extension_data/Example.svg
---
align: center
---
Example structure. Although this is not a truss structure, deformation is only caused by extension, not by bending.
```

::::::

1. Determine [the degree of static determinacy](../determinancy.md).

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_1

    For our example, we are interested in the internal force distribution, so we need to evaluate the degree of internal static indeterminacy.

    ```{figure} ./extension_data/unknown_forces.svg
    ---
    align: center
    ---
    There are 17 unknown forces.
    ```

    ```{figure} ./extension_data/equations.svg
    ---
    align: center
    ---
    There are 16 equilibrium equations
    ```

    This structure is therefore first-order internally statically indeterminate.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force mmembers, or adding hinges: add unknown statically indeterminate forces and deformation conditions for each support you have removed and hinge you have added. Be careful not to transform the structure into a (partially) mechanism!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_2

    There are many options here, some of which are shown below:

    `````{tab-set}
    ````{tab-item} Split the structure at a hinge
    ```{figure} ./extension_data/option1.svg
    :align: center
    ```
    ````
    ````{tab-item} Add a hinge
    ```{figure} ./extension_data/option2.svg
    :align: center
    ```
    ````
    ````{tab-item} Release the horizontal movement direction of a support
    ```{figure} ./extension_data/option3.svg
    :align: center
    ```
    ````
    ````{tab-item} Remove the vertical support
    ```{figure} ./extension_data/option4.svg
    :align: center
    ```
    ````
    `````

    The last option is chosen.

    ::::::

3. Solve the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_4

    We have chosen the following statically determinate structure with deformation condition $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{figure} ./extension_data/SD_struc.svg
    ---
    align: center
    ---
    The statically determinate structure with deformation condition
    ```

    Because $\rm{AE}$ is infinitely stiff, all deformations will be the result of bars stretching/compressing. To calculate this, the normal forces can first be evaluated as a function of $B_{\rm{v}}$ using, for example, a moment equilibrium around $\rm{A}$ for the element $\text{ADE}$:

    - $N_{\rm{CD}}\left( B_{\rm{v}} \right) = 210 - 2.5 B_{\rm{v}}$
    - $N_{\rm{BE}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    This leads to the following elongation of the elements, using $\Delta L = \cfrac{N \ L}{EA}$:

    - $\Delta L_{\rm{CD}}\left( B_{\rm{v}} \right) = \cfrac{1400}{EA} - \cfrac{50 B_{\rm{v}}}{3 EA}$
    - $\Delta L_{\rm{BE}}\left( B_{\rm{v}} \right) = -\cfrac{5 B_{\rm{v}}}{EA}$

    This leads to the following displacement, using a [Williot diagram](../../stresses_displacements/displacements_truss/williot.md):

    ```{figure} ./extension_data/williot.svg
    ---
    align: center
    ---
    The displacement of $\rm{D}$ is $\cfrac{5}{4} \Delta L_{\rm{CD}} $
    ```

    - $w_{\rm{D}}\left( B_{\rm{v}} \right) = \cfrac{1750}{EA} - \cfrac{125 B_{\rm{v}}}{6 EA} \left( \downarrow \right) $
    - $w_{\rm{E}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{125 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $

    ::::::

4. Use your deformation conditions to solve for the statically indeterminate forces

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} &= 0 \\
    B_{\rm{v}} &= 75 \ \rm{kN}
    \end{align*}
    $$

    This leads to the following other results:

    - $N_{\rm{CD}} = 22.5 \ \rm{kN}$
    - $N_{\rm{BE}} -75 \ \rm{kN} $
    - $w_{\rm{D}} = \cfrac{375}{2EA} \left( \downarrow \right) $
    - $w_{\rm{E}} = \cfrac{375}{EA} \left( \downarrow \right) $

    ::::::

## Instructions from lecture 
This topic is presented in a lecture available to 42:50 [here](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/99cfa289d58d4986a4378be10efb40c31d?academicYear=2025-2026-ctb2210) in Dutch for TU Delft students.

## Exercises
- Exercises 2.31 - 2.41, in section 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`
Answers are [available here](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
