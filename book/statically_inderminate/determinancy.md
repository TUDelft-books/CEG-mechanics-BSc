```{index} Static indeterminacy
```
```{index} Degree of static indeterminacy
```
# Static Indeterminacy

```{figure} ./determinancy_data/Example_1.svg
:align: center
:width: 300
```

A structure is statically indeterminate when it can no longer be solved using only equilibrium equations. A distinction can be made between:

- Only support reactions can be determined (externally statically determinate)
- Internal forces can be determined (internally statically determinate)

If equilibrium equations are not sufficient, a structure is statically indeterminate. The degree of static indeterminacy is expressed by the degree of static indeterminacy.

It is necessary to determine the degree of static indeterminacy in order to solve these structures using the force method.

These two categories are discussed together in sections 4.5.2 and 4.5.3 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006`. For trusses, the analysis is simplified as described in section 9.2.2 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006`. Although the equations shown with $r$, $v$, and $e$ can be effective for simple structures, they can lead to incorrect results for complex structures. An approach that always works is shown below for separately determining external and internal static indeterminacy.

```{index} Degree of external static indeterminacy
```

## Determining the degree of external static indeterminacy
For calculating external static indeterminacy, follow these steps:

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

1. Split the structure into rigid parts that can rotate relative to each other when detached from the supports. Draw the free body diagram of these hinged parts. The support reactions and any external forces act on these parts. At the hinged connection, there are two unknown forces: horizontal and vertical. These forces have equal and opposite reaction forces on the adjoining part.

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

2. Count the number of unknown forces: the support reactions and connection forces in the hinges (do not count the reaction forces separately).

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_2.svg
   ---
   name: example_sd_2
   align: center
   ---
   Number of unknown forces
   ```

   There are a total of 6 support reactions and 2 connection forces. Please be aware that the connection forces are shown twice, but these forces are the same at both ends of the connection so they can be counted as one.

   ::::::

3. Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_3.svg
   ---
   name: example_sd_3
   align: center
   ---
   Number of equilibrium equations
   ```

   There are two rigid parts, so 6 equilibrium equations.

   ::::::

4. The degree of static indeterminacy is the number of support reactions + connection forces - number of equilibrium equations.

   ::::::{prf:example}
   :nonumber: true

   The degree of external static indeterminacy for this example is $6 + 2 - 6 = 2$.

   ::::::

```{index} Degree of internal static indeterminacy
```
## Determining the degree of internal static indeterminacy
For calculating internal static indeterminacy, follow these steps:

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

1. Split the structure into all separate nodes and members, and draw the free body diagram for all nodes, taking into account which members and supports are connected to the nodes:
   - At a hinged connection and free/hinged ends, there are no bending moments.
   - On a member connected to a roller support, only a force perpendicular to the roller direction acts.
   - From a pendulum member, only a normal force acts.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_4.svg
   ---
   name: example_sd_4
   align: center
   ---
   Free body diagrams of nodes
   ```

   The structure consists of 4 nodes. Unknown support reactions act on nodes A and B. Node A is a hinged end, so there are no bending moments. At node B, bending moments in the members BC and BD could be present and be in equilibrium, although the support is hinged. At node C, no bending moment acts from member DB due to the hinged connection. Node D is hinged, so no bending moments act there.

   ::::::

2. Draw the free body diagram for the members: draw the reaction forces on the members resulting from the forces on the nodes.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_5.svg
   ---
   name: example_sd_5
   align: center
   ---
   Free body diagrams of members
   ```

   From {numref}`example_sd_4`, the reaction forces on the members can be drawn.

   ::::::

3. Count the number of unknown forces: support reactions and member forces (do not count the reaction forces separately).

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_6.svg
   ---
   name: example_sd_6
   align: center
   ---
   Number of unknown forces
   ```

   From {numref}`example_sd_4`, the number of unknown forces can be counted. There are 4 support reactions and 20 member forces.

   These member forces can also be counted in the free body diagrams of the members from {numref}`example_sd_5`:

   ```{figure} ./determinancy_data/Example_7.svg
   ---
   name: example_sd_7
   align: center
   ---
   Number of unknown member forces
   ```

   ::::::

4. Count the equilibrium equations: 1 equilibrium equation per pendulum member, 3 equilibrium equations per general member, 1 equilibrium equation for a roller hinge, 2 equilibrium equations per hinged node, and 3 equilibrium equations per general node.

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

   Of the nodes, two are fully hinged; for the rest, the moment equilibrium is also relevant. That gives 10 equilibrium equations.

   In total, there are 22 equilibrium equations.

   ::::::

5. The degree of static indeterminacy is the number of support reactions + member forces - number of equilibrium equations.

   ::::::{prf:example}
   :nonumber: true

   The degree of internal static indeterminacy for this example is $4 + 20 - 22 = 2$.

   ::::::

## Exercises
- Exercises 4.11 - 4.22, from chapter 4 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Exercise 9.6, from chapter 9 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).
