# Free body diagrams

## Theory

```{index} Free body diagram ; of an entire model
```
```{index} Support reaction
```
### Free body diagram of entire model
In the free body diagram of an entire model, all forces are shown which are applied on a structure, including support reactions.

An example model is shown in {numref}`model`.

```{figure} ./FBD_data/model.png
:name: model
:width: 400px
:align: center

Example model
```

In the free body diagram of an entire model, all support are replaced by (potential) reaction forces. The direction and size of reaction forces might not be known on beforehand. Therefore, the reactions force are indicated symbolically and the direction is assumed in the free body diagram.

The free body diagram of the entire example model is shown in {numref}`FBD`.

```{figure} ./FBD_data/FBD_full_structure.png
:name: FBD
:width: 400px
:align: center

Free body diagram of the entire example model
```

```{index} Free body diagram ; of a hinged part of a model
```
```{index} Interaction forces
```
### Free body diagram of a hinged part of a model
In the free body diagram of a hinged part of a model, a cut is made at the hinge, showing the (potential) interaction forces at the hinge. Read chapter 4.2.1 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006` for which interaction forces are exerted on the model. These forces are the same as the normal and shear forces at that point in the structure. As with the reaction forces, the direction and size of the interaction forces might not be known on beforehand. Therefore, the interaction force are indicated symbolically and the direction is assumed in the free body diagram.

The free body diagram of the right hinged part of the example model is shown in {numref}`FBD_hinged`.

```{figure} ./FBD_data/FBD_hinged_part_of_structure_NV.png
:name: FBD_hinged
:width: 400px
:align: center

Free body diagram of the right hinged part of the example model
```

```{index} Free body diagram ; of a part of a model
```
```{index} Free body diagram ; of a points in the model
```
### Free body diagram of a part of a model
In the free body diagram of a part of a model, a cut is made at the any arbitrary point, showing the (potential) forces and couples in the elements. Read chapter 4.2.2 of the book Engineering Mechanics Volume 1 {cite:p}`Hartsuijker2006` for which interaction forces are exerted on the model. These interaction forces are the same as the normal- and shear forces, and the bending moments at that point in the structure. Again, the direction and size of the interaction forces might not be known on beforehand. Therefore, the interaction force are indicated symbolically and the direction is assumed in the free body diagram.

The free body diagram to the right of a cut just left of point $\text{C}$ of the example model is shown in {numref}`FBD_part`.

```{figure} ./FBD_data/FBD_part_of_structure.png
:name: FBD_part
:width: 400px
:align: center

Free body diagram to the right of a cut just left of point $\text{C}$ of the example model
```
A cut can also be made such that only a single point is left. In that case you can draw the free body diagram of this single point.

The free body diagram of point $\text{B}$ of the example model is shown in {numref}`FBD_point`

```{figure} ./FBD_data/FBD_point_in_structure.png
:name: FBD_point
:width: 400px
:align: center

Free body diagram of point $\text{B}$ of the example model
```

```{index} Free body diagram ; of a part of a cable
```
### Free body diagram of a part of a cable
"Cables are line elements in which the resistance to bending is so small that
it can be ignored. A fully flexible cable cannot transfer bending moments
nor transverse forces. The force flow occurs entirely via normal forces,
namely tensile forces.
...
Cables do not have their own shape – they adapt to the load. Here, we
assume that the axial stiffness of the cable is infinite. Therefore the cable
has the same length before and after loading. The shape of the cable and the
cable forces can then be deduced directly from the equilibrium equations.
" {cite:p}`Hartsuijker2006`

An example cable model is shown in {numref}`model-cable`.

```{figure} ./FBD_data/model_cable.png
:name: model-cable
:width: 400px
:align: center

Example cable model
```

As only normal forces are present, the free body diagram of a part of cable, only shows the (potential) normal force at a (potentially unknown) location.

The free body diagram to the left of a cut just right of point $\text{C}$ of the example cable model is shown in {numref}`FBD_cable`.

```{figure} ./FBD_data/FBD_cable.png
:name: FBD_cable
:width: 400px
:align: center

Free body diagram to the left of a cut just right of point $\text{C}$ of the example cable model
```

## Practice material
...

## Relation with other subjects
<iframe allow="fullscreen" style="width: 100%!important; height: 500px;" src="https://prime-applets.ewi.tudelft.nl/graph/CTB1110-17/show2?lecture=4&view=lecture" allowfullscreen></iframe>