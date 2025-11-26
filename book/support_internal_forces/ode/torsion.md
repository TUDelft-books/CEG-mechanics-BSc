```{index} Differential equations for equilibrium relations; for torsion
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is adapted from https://oit.tudelft.nl/CTB1310/2025/torsie_krachten/instructie.html.

% source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
```
````

# ... for torsion

The differential equation for equilibrium relations for bending is based on the infinitesimal small loaded torsional bar:

```{figure} ./instructie_data/deltax.svg
---
align: center
---
Free body diagram of an infinitesimal small loaded torsional bar
```

Equilibrium of moments around the longitudinal axis results in the following differential equation:

$$
\begin{align*}
\sum T_{\rm{element}} &= 0 \\
- M_{\rm{t}} + q_{\rm{M}_{\rm{t}}} \cdot \Delta x +  M_{\rm{t}} + \Delta M_{\rm{t}} &= 0 \\
q_{\rm{M}_{\rm{t}}} \cdot \Delta x + \Delta M_{\rm{t}} &= 0 \\
\mathop {\lim }\limits_{\Delta x \to 0 } \left( \cfrac{\Delta M_{\rm{t}}}{\Delta x} \right) &= \mathop {\lim }\limits_{\Delta x \to 0 } \left( - q_{\rm{M}_{\rm{t}}} \right) \\
\cfrac{dM_{\rm{t}}}{dx} &= - q_{\rm{M}_{\rm{t}}}
\end{align*} 
$$