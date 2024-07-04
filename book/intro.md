# Welcome to the TeachBook on Mechanics in the BSc of Civil Engineering

This <a href="https://teachbooks.tudelft.nl/"><img height="20px" src="./images/Logo_without_background.png"></img>TeachBook</a> combines all content for the mechanics in the bachelor of Civil Engineering at Delft University of Technology. It's broken down in to modules with separate parts of theory and skills including exercises. This TeachBook links heavily to relevant part of the other literature and only provides additional content when the other literature is insufficient.
- Engineering Mechanics: Volume 1: Equilibrium, by C. Hartsuijker and J.W. Welleman {cite}`Hartsuijker2006`. eBook available for free via TU Delft at [<img height="20px" src="./images/springer-logo.svg" alt="Springer">](https://link-springer-com.tudelft.idm.oclc.org/book/10.1007/978-1-4020-5483-9). This book is also available in Dutch (only paid version) at [<img height="12px" src="./images/logo-boom.svg" alt="Boom">](https://www.boomhogeronderwijs.nl/product/100-9055_Mechanica-Evenwicht-3e-druk).
- Engineering Mechanics: Volume 2: Stresses, strains and displacements, by C. Hartsuijker and J.W. Welleman {cite}`Hartsuijker2007`. eBook available for free via TU Delft at [<img height="20px" src="./images/springer-logo.svg" alt="Springer">](https://link.springer.com/book/10.1007/978-1-4020-5763-2). This book is also available in Dutch (only paid version) at [<img height="12px" src="./images/logo-boom.svg" alt="Boom">](https://www.boomhogeronderwijs.nl/product/100-9056_Mechanica-Spanningen-vervormingen-verplaatsingen-3e-druk).
- Mechanica: Statisch onbepaalde constructies en bezwijkanalyse, by C. Hartsuijker and J.W. Welleman {cite}`Hartsuijker2016`. Book available at [<img height="12px" src="./images/logo-boom.svg" alt="Boom">](https://www.boom.nl/hoger-onderwijs/100-9587_Mechanica-Statisch-onbepaalde-constructies-en-bezwijkanalyse-3e-druk). This book is only available as a paid version in Dutch
- Mechanica: Stabiliteit van het evenwicht, by C. Hartsuijker and J.W. Welleman {cite}`Hartsuijker2023`. Book available at [<img height="12px" src="./images/logo-boom.svg" alt="Boom">](https://www.boom.nl/hoger-onderwijs/100-10458_Mechanica-Stabiliteit-van-het-evenwicht). This book is only available as a paid version in Dutch
- Introduction to continuum mechanics, by C. Hartsuijker and J.W. Welleman. Book available [here](external/mechanics-BSc/book/Lecture_Notes_Elasticity.pdf)
- Additional exercises in [<img height="12px" src="./images/ANS.svg" alt="ANS">](https://ans.app/routing/courses/436978) (for TU Delft students only). You can login into this course by [logging in into ANS - clicking  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="M80-120v-720h400v160h400v560H80Zm80-80h80v-80h-80v80Zm0-160h80v-80h-80v80Zm0-160h80v-80h-80v80Zm0-160h80v-80h-80v80Zm160 480h80v-80h-80v80Zm0-160h80v-80h-80v80Zm0-160h80v-80h-80v80Zm0-160h80v-80h-80v80Zm160 480h320v-400H480v80h80v80h-80v80h80v80h-80v80Zm160-240v-80h80v80h-80Zm0 160v-80h80v80h-80Z"/></svg> - `Education TU Delft` - clicking `Join Course`  - clicking `Join` for `Constructiemechanica BSc Civiele Techniek`](https://ans.app/universities/1/courses/join_courses). Afterwards, you can directly go to the course by going to [your ANS overview](https://ans.app/routing/courses/436978) or by clicking the provided links in the book.

This TeachBook includes interactive features!
- Interactive quizzes: Some page include interactive 'H5p' quizzes. This allows you to check your understanding. Any interactions you have with this system are not stored, unless you login into H5p.
- Python interactivity: Click {fa}`rocket` --> {guilabel}`Live Code` on the top right corner of interactive page to start up a python-kernel in your browser! Any interactions you do here are not stored. You can also download the page as a notebook to apply the content on your own computer.

If you spot any mistakes, you can click on <svg class="svg-inline--fa fa-github" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" data-fa-i2svg=""><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg> --> {fa}`lightbulb`, login with GitHub account and report your issue. It'll be solved soon!

If you'd like to make this TeachBook more personal by adding (private or public) annotations I can recommend the [Hypothesis extension](https://web.hypothes.is/start/). This is only for your own use, I won't monitor public post on this platform.

The concept TOC below is work-in-progress

1.	Support reactions and internal forces
    1. Model
        1. Beams
        2. Cables
        3. Coordinate system
        4. Supports
        5. Hinges
        6. Loads
        7. Internal forces
        8. Free body diagrams
        9. Structures
    2. Transforming forces
        1. Resolution of forces
        2. Resultant force
    3. Equilibrium
        1. of a particle
        2. of a rigid body
        3. of a complete structure
        4. of a hinged part of a structure
        5. of a part of the structure
        6. of a part of a cable structure
        7. in 3D
    4. Mechanisms with small rotations
        1. with one body
        2. with two bodies
        3. with three bodies
    5. Virtual work
        1. Principle of virtual work
        2. Support reactions
        3. Internal forces
    6. Statical and kinematical determinacy
        1. Statical determinacy
        2. Kinematical determinancy
        3. Truss structures
        4. Bending structures
    7. Support reactions
        1. of rigid structures
        2. of hinged structures
        3. of 'hang- en springwerken'
    8. Internal forces in a truss structure
        1. at a cross section
        2. Zero force members
        3. using differential equations
    9. Internal forces in a bending structure
        1. at a cross section
        2. using differential equation
        3. Distribution
    10. Internal forces in a cable
    11. Shape of a cable
        1. using equilibrium
        2. using differential equations
        3. Point of force
        4. Force line
2.	Normal- and shear stresses, and displacements
    1. Model
        1. Fibre model
        2. Stresses
        3. Strains
        4. Core of a cross-section
        5. Displacements
        6. Rotations
        7. Curvature
        8. Shear distortion
        9. Thin- and thick-walled cross-sections
    2. Cross-sectional properties
        1. Area
        2. Static moment
        3. Center of gravity
        4. Second moment of area
        5. 'Weerstandsmoment'
        6. Cross moment of area
        7. Normal force centre
        8. Shear force centre
    3. Constitutive relations
        1. Extension
        2. Bending
        3. Torsion
    4. Kinematic relations
        1. Extension
        2. Bending
        3. Shear
        4. Torsion
    5. Stresses in an extension element
    6. Stresses in a bending element
        1. normal stresses
        3. shear stresses
    7. Stresses in a torsional element
        1. in circular cross-sections
        2. in thin-walled cross-sections
    8. Displacements of a truss structure with Williot
    9. Displacements of a bending structure
        1. using differential equations
        2. using forget-me-nots
        3. using 'momentenvlakstelling'
3.	Statically indeterminate structures
    1. Force method
        1. for extension elements
        2. for bending elements
        3. for bending elements with 'hoekveranderingsvergelijkingen'
        4. for bending elements with movable nodes
    2. Displacement method
        1. for extension elements
        2. for bending elements
    3. Stiffness discontinuities
    4. Support settlement
    5. Temperature influences
4.	Buckling
    1. Principle of buckling
    2. Buckling of rigid bodies
        1. Buckling load
        2. Post-buckling behaviour
        3. System of rigid bodies
        4. Two degrees of freedom
    3. Buckling of elastic bodies
        1. Euler buckling
        2. Rotational spring-supports with movable nodes
        3. Rotational spring-supports with fixed nodes
        4. Translation spring-supports
        5. Translation distributed spring-supports
    4. Buckling of combined rigid- and elastic-body systems
5.	Continuum mechanics
    1. Model
        1. Stresses in 3D
        2. Isotropic and deviatoric components
        3. Strains in 2D
    2. Transformations
        1. Analytical
        2. Graphical
    3. Stress-strain relations
    4. Failure
  
    
