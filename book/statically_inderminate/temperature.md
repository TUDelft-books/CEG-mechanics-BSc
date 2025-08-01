```{index} Temperature influences; for statically indeterminate structures
```
# Solve structures subjected to temperature influences

Elements elongate under uniform loading with an additional strain of $\epsilon^{\rm{T}} = \alpha \ \Delta T$ with $\alpha$ the linear expansion coefficient. When loaded by a temperature change over the height of an element, fibres elongate individually, leading to bending of elements with an additional curvature of $\kappa^{\rm{T}} = \alpha \ \cfrac{\Delta T}{h}$, with $h$ the height of an element. So, in statically determinate structures, this leads to additional stressless strains (leading to displacements) without influencing the force distribution as the force distribution is independent of the displacements. 

Displacement can be found by integrating the stressless strains using the differential equations. Alternatively, using an equivalent load which leads to the same curvature allows the use of forget-me-nots. This requires a kinematic equivalent load which doesn't influence reactions forces and internal forces:

```{figure} ./temperature_data/kin_eq_load_SB.svg
:align: center

Kinematic equivalent load leading to the same strain and curvature as strain due to linear expansion
```

In statically indeterminate structures the displacement and force distribution is coupled, leading to reaction forces and internal stresses due to the (intended) displacement due to the temperature change. These forces can, again, be found by integrating the strains (both the stress-causing strains and stressless temperature strains) using the differential equations. Alternatively, a kinematic equivalent load, as in statically determinate structures, can be applied in combination with the force method: the displacement due to the temperature are included into the displacement constraints.

```{figure} ./temperature_data/kin_eq_load_SO.svg
:align: center

Kinematic equivalent load leading to the same strain and curvature as strain due to linear expansion, while statically indeterminate reaction forces cause stresses and reaction forces
```

This topic is treated in chapter 6.2.2 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

## Exercises
Exercises 6.25 - 6.44 in chapter 6.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`. Unfortunately there are no answers available.