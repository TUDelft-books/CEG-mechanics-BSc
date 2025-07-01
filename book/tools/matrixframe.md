```{index} Matrixframe
```
```{index} Software
```
# Matrixframe

Matrixframe is commercial software used for structural analysis. MatrixFrame uses symbols that are very similar to those used in the Delft curriculum. For students, there is a free [student license](https://www.matrix-software.com/contact/studentversion) (registration with MatrixFrame required) and [a version](https://software.tudelft.nl/371/) that only works on the TU Delft network (possibly via [VPN connection](https://www.tudelft.nl/en/student/my-study-me/study-tools/remote-services)). If you have applied for the student license but have not received it, you can submit a ticket via [this link](https://matrix-software.freshdesk.com/en/support/tickets/new).

A few points are important when using MatrixFrame:

- When using MatrixFrame, you will always need to enter the stiffnesses of the elements ('profile data in MatrixFrame'). MatrixFrame needs this to perform the structural analysis, even though it is not necessary for the internal forces in statically determinate structures. If this data is not known, you can enter any large value under 'Manual input'. As long as the value is several orders of magnitude larger than the other values, it is fine; if the value is too large, numerical issues may arise.
- Sometimes elements may overlap without it being visible.

A comprehensive manual with more options can be found [here](https://icozct.tudelft.nl/TUD_CT/CT2031/oefening/matrix/files/Introductie%20MatrixFrame.pdf). In addition, [the official documentation](https://knowledge-base.matrix-software.com/nl/help/matrix-frame) provides further explanation.

As an example, we will determine the external static indeterminacy of this structure.

::::::{prf:example}
:label: mf_example_0
:nonumber: true

```{figure} ./matrixframe_data/constructie.svg
---
align: center
class: dark-light
---
Example structure
```

::::::

1. Create a new project - '2D-Raamwerk' and click 'Ok'. The options '1D-Ligger' and '2D_vakwerk_' are simplifications of the '2D Frame' option. You can try the '3D-Raamwerk' and '3D-Vakwerk' options, but they are generally more complex.

::::::{prf:example}
:label: mf_example_1
:nonumber: true

```{figure} ./matrixframe_data/step1.png
---
align: center
class: dark-light
---
Since this is a 2D-Raamwerk, we select that option.
```

::::::

2. You will immediately enter the 'Geometrie' interface. Click on the grid to create your geometry. The coordinates are visible in the bottom bar, and the dimensions appear while clicking. Use `Esc` on your keyboard to stop or to start a new element that is not connected to the end of the previous element. Adjust dimensions if necessary using the grids on the left or the coordinates at the bottom of the screen.

::::::{prf:example}
:label: mf_example_2
:nonumber: true

```{figure} ./matrixframe_data/step3.png
---
align: center
class: dark-light
---
The first bar has been drawn, and for the second bar, the coordinate $\left(9,0 \right)$ is visible in the bar at the bottom.
```

```{figure} ./matrixframe_data/step3_2.png
---
align: center
class: dark-light
---
Once all nodes and bars are drawn, this is the result.
```

::::::

3. Continue with the 'Profielgegevens' interface. Even if this information is not known, entering it is required. Under 'Profielen' - 'Handmatige invoer', you can enter $A$, $I$, and $E$. It is not possible to enter a value of $0$ or $\infty$; instead, you must enter a small or large numerical value.
Tip: $\cdot10^6$ can be entered as `e6`. Don't forget to click 'Apply to all'! At the bottom left of the screen, you will now see a profile name behind each bar.

::::::{prf:example}
:label: mf_example_3
:nonumber: true

In this example, only $EI$ is given, while we need to enter separate $E$ and $I$. Therefore, you can choose two numbers whose product is $7.8 \cdot 10^4$, for example $E = 200 \cdot 10^6$ and $I = 3.9 \cdot 10^-2$. $EA$ is $\infty$, for which we can enter a large numerical value, for example $A = 10 \cdot 10^3$.

```{figure} ./matrixframe_data/step5.png
---
align: center
class: dark-light
---
Once everything is entered, this is the result.
```

::::::

4. The next step is to add supports. There are several standard options, but you can also manually fix translation and rotation directions. Supports can be placed on nodes or along a bar (in which case a new node is created).

::::::{prf:example}
:label: mf_example_4
:nonumber: true

```{figure} ./matrixframe_data/step6.png
---
align: center
class: dark-light
---
The fixed and roller supports of the example are visible both in the graphical display and in the lower window after adding.
```

::::::

5. Now we can proceed with hinges. In a frame, everything is rigidly connected by default. For each bar, you can specify for each end whether it should be a hinge by clicking on a part of that bar. If two connecting bars are hinged, it is not necessary to hinge both bar ends; one is sufficient.

::::::{prf:example}
:label: mf_example_5
:nonumber: true

```{figure} ./matrixframe_data/step7.png
---
align: center
class: dark-light
---
In this example, there are no hinges, so this step can be skipped.
```

::::::

6. The last configuration step is to add loads. You can add different load cases, but as long as you only need to analyze one, it is not necessary to adjust those options. For each load, you need to specify the value and direction and click the bar on which the load acts. In the window at the bottom of the screen, you can also adjust these.

::::::{prf:example}
:label: mf_example_6
:nonumber: true

```{figure} ./matrixframe_data/step8.png
---
align: center
class: dark-light
---
In this example, there are two loads. The distributed load is applied in the local z direction, and the point load in the global x direction with a negative value so that it acts to the left.
```

::::::

7. Now that everything is configured, you can click on 'L.E. berekening' (linear-elastic calculation). A dialog window will open that gives error messages if something is incorrect.

::::::{prf:example}
:label: mf_example_7
:nonumber: true

```{figure} ./matrixframe_data/step9.png
---
align: center
class: dark-light
---
In this example, everything is correctly configured and the logbook shows no error messages.
```

::::::

8. To view the results, there are several options. The support reactions can be shown separately. Note that the direction of the arrows indicates the actual direction of the forces and moments; a possible minus sign indicates that the force acts in the negative direction of the coordinate system.

::::::{prf:example}
:label: mf_example_8
:nonumber: true

```{figure} ./matrixframe_data/step10.png
---
align: center
class: dark-light
---
In this example, four support reactions are visible. The vertical support reactions act upwards; the minus sign indicates that these act in the negative z-direction.
```

::::::

9. The internal force diagrams can also be shown. These can be displayed per internal force according to the deformation symbols as we are used to. If the deformation symbols are not visible, you can zoom in or increase the scale under 'Weergave-instellingen' - 'Beeldinstellingen' - 'Eigenschappen' - 'Resultaten' - 'Normaalkracht (Nx)'/'Dwarskracht (Vz)'/'Momenten (My)' - 'Vorm' - 'Schaal' - Enter value and click 'Toepassen'. If a bar is clicked, all internal forces and displacements of that bar are visible on the left side of the screen. At the bottom of the screen, some characteristic values are shown. The values are shown according to the local coordinate system.

::::::{prf:example}
:label: mf_example_9
:nonumber: true

```{figure} ./matrixframe_data/step11.png
---
align: center
class: dark-light
---
The moments are displayed with bar AD in detail on the left. The scale has been adjusted so that the deformation symbols are visible.
```

```{figure} ./matrixframe_data/step12.png
---
align: center
class: dark-light
---
The shear forces can also be displayed. The deformation symbol of DB is not visible in this view; if you zoom in further or increase the scale, it will become visible.
```

```{figure} ./matrixframe_data/step13.png
---
align: center
class: dark-light
---
The normal forces can also be displayed.
```

::::::

10. Displacements can also be displayed. The number of decimals can be adjusted under 'Weergave-instellingen' - 'Beeldinstellingen' - 'Eigenschappen' - 'Resultaten' - 'Verplaatsingen/Doorbuigingen' - 'Label' - 'Decimalen' - Enter value and click 'Toepassen'.

::::::{prf:example}
:label: mf_example_10
:nonumber: true

```{figure} ./matrixframe_data/step14.png
---
align: center
class: dark-light
---
The displacements are displayed. The number of decimals has been adjusted so that the exact displacements can be found.
```

::::::

11. Finally, values at specific positions can be read using the spy function. To do this, click a bar and enter a location under 'Input pos:' in the local coordinate system. The table and graphical display will then show values of internal forces and displacements at that point.

::::::{prf:example}
:label: mf_example_11
:nonumber: true

```{figure} ./matrixframe_data/step15.png
---
align: center
class: dark-light
---
At $3$ meters to the right of A, the internal forces and displacements for this example are: a displacement of $0.000042 \ \rm{m}$, a moment of $39.73 \ \rm{kNm}$, a shear force of $33.38 \ \rm{kN}$, and a normal force of $-20 \ \rm{kN}$.
```

::::::

::::::{prf:example}
:label: mf_example_12
:nonumber: true

The file for this example can be downloaded [here](./matrixframe_data/example.mxe).

::::::
