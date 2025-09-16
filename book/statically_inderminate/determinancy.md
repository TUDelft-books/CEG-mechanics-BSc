
```{index} Static indeterminacy
```
```{index} Degree of static indeterminacy
```
# Static Indeterminacy

```{figure} ./determinancy_data/Example_1.svg
:align: center
:width: 300
```

A structure is statically indeterminate when it can no longer be solved using only equilibrium equations. There is a distinction between:
- Only support reactions can be determined (externally statically determinate)
- Internal forces can be determined (internally statically determinate)

If equilibrium equations are not sufficient, a structure is statically indeterminate. The degree of static indeterminacy is expressed as the degree of static indeterminacy.

It is necessary to determine the degree of static indeterminacy to solve these structures using the force method.

These two categories are discussed together in sections 4.5.2 and 4.5.3 of the book *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. For trusses, the analysis is simplified as described in section 9.2.2 of the book *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Although the equations shown with $r$, $v$, and $e$ can be effective for simple structures, they lead to incorrect results for complex structures. An approach that always works is shown below for separately determining external and internal static indeterminacy.

```{index} Degree of external static indeterminacy
```
## Determining the Degree of External Static Indeterminacy
For the calculation of external static indeterminacy, follow these steps:

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example.svg
---
name: example_sd
align: center
---
Example structure
```

As an example, we determine the external static indeterminacy of this structure.

::::::

1. Split the structure into rigid parts that can rotate independently of each other when separated from the supports. Draw the free-body diagram of these hinged parts. The support reactions and any external forces act on these parts. At the hinged connection, two unknown forces act: horizontal and vertical. These forces at the connection have an equal and opposite reaction force on the adjoining part.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_1.svg
   ---
   name: example_sd_1
   align: center
   ---
   Split structure
   ```

   The structure can be divided into two rigid, hinge-connected parts. The supports are replaced by support reactions, and the hinged connection by a horizontal and vertical force (and reaction forces). The external force acts only on one of the two parts.

   ::::::

2. Count the number of unknown forces: the support reactions and connection forces in the hinges (do not count the reaction forces separately)

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_2.svg
   ---
   name: example_sd_2
   align: center
   ---
   Number of unknown forces
   ```

   There are a total of 6 support reactions and 2 connection forces. Note: the connection forces are shown twice, but these forces are equal at both ends of the connection, so they can be counted as one.
   ::::::

3. Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_3.svg
   ---
   name: example_sd_3
   align: center
   ---
   Number of equilibrium equations
   ```

   There are two rigid parts, so 6 equilibrium equations

   ::::::

4. The degree of static indeterminacy is the number of support reactions + connection forces - number of equilibrium equations

::::::{prf:example}
:nonumber: true

The degree of external static indeterminacy for this example is $6 + 2 - 6 = 2$.

::::::

```{index} Degree of internal static indeterminacy
```
## Determining the Degree of Internal Static Indeterminacy
For the calculation of internal static indeterminacy, follow these steps:

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example_abc.svg
---
name: example_sd_abc
align: center
---
Example structure
```

As an example, we determine the internal static indeterminacy of this structure.

::::::

1. Split the structure into all separate nodes and members, and draw the free-body diagram for all nodes, considering which members and supports are connected to the nodes:
   - At a hinged connection and free/hinged ends, no bending moments act
   - On a member connected to a roller support, only a force perpendicular to the roller direction acts.
   - From a two-force member, only a normal force acts

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_4.svg
   ---
   name: example_sd_4
   align: center
   ---
   Free-body diagrams of nodes
   ```

   The structure consists of 4 nodes. Unknown support reactions act on nodes A and B. Node A is a hinged end, so no bending moments act there. In node B, bending moments can occur from BC and BD and be in equilibrium, although the support is a hinge. On node C, no bending moment acts from bar DB due to the hinged connection. Node D is hinged, so no bending moments act there.

   ::::::

2. Draw the free-body diagram for the members: draw the reaction forces on the members resulting from the forces on the nodes.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_5.svg
   ---
   name: example_sd_5
   align: center
   ---
   Free-body diagrams of members
   ```

   From {numref}`example_sd_4`, the reaction forces on the members can be drawn.

   ::::::

3. Count the number of unknown forces: support reactions and section forces (do not count the reaction forces separately)

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_6.svg
   ---
   name: example_sd_6
   align: center
   ---
   Number of unknown forces
   ```

   From {numref}`example_sd_4`, the number of unknown forces can be counted. There are 4 support reactions and 20 section forces.

   These section forces can also be counted in the free-body diagrams of the members from {numref}`example_sd_5`:

   ```{figure} ./determinancy_data/Example_7.svg
   ---
   name: example_sd_7
   align: center
   ---
   Number of unknown section forces
   ```

   ::::::

4. Count the equilibrium equations: 1 equilibrium equation per two-force member, 3 equilibrium equations per general member, 1 equilibrium equation for a roller hinge, 2 equilibrium equations per hinged node, and 3 equilibrium equations per general node.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_9.svg
   ---
   name: example_sd_9
   align: center
   ---
   Number of equilibrium equations per member
   ```

   All members are general members. That gives 12 equilibrium equations for the members.

   ```{figure} ./determinancy_data/Example_8.svg
   ---
   name: example_sd_8
   align: center
   ---
   Number of equilibrium equations per node
   ```

   Of the nodes, two are fully hinged; for the rest, the moment sum is also important. That gives 10 equilibrium equations.

   In total, there are 22 equilibrium equations

   ::::::

5. The degree of static indeterminacy is the number of support reactions + section forces - number of equilibrium equations

   ::::::{prf:example}
   :nonumber: true

   The degree of internal static indeterminacy for this example is $4 + 20 - 22 = 2$.

   ::::::

## Instructions from lecture
This topic is presented in a lecture available from 0:34:40 - 1:00:40 [here in Dutch](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/757766716fcb45718fca678dadaa396d1d?academicYear=2025-2026-ctb2210) for TU Delft students.

## Exercises
- Exercises 4.11 - 4.22, from chapter 4 of the book *Mechanics: Evenwicht* {cite:p}`Hartsuijker1999`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Exercise 9.6, from chapter 9 of the book *Mechanics: Evenwicht* {cite:p}`Hartsuijker1999`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).
