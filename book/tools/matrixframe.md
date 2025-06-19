```{index} Matrixframe
```
```{index} Software
```
# Matrixframe

Matrixframe is commerciele software waarmee constructies kunnen worden doorgerekend. MatrixFrame gebruikt symbolen die erg lijken op de symbolen gebruikt bij de opleiding in Delft. Voor studenten is er een gratis [studentenlicentie](https://www.matrix-software.com/contact/studentversion) (registratie bij MatrixFrame vereist) en [een versie](https://software.tudelft.nl/371/) die alleen op het TU Delft netwerk (eventueel via [VPN verbinding](https://www.tudelft.nl/studenten/mijn-studie-ik/studietools/remote-inloggen)) werkt. Als je de studentenlicentie hebt aangevraagt maar niet ontvangen, kun je een ticket indienen via [deze link](https://matrix-software.freshdesk.com/en/support/tickets/new).

Een aantal punten zijn van belang bij het gebruik van MatrixFrame:
- Bij het gebruik van matrixframe zal je altijd stijfheden van de elementen moeten invoeren ('profielgegevens in MatrixFrame'). Dit heeft MatrixFrame nodig om de constructie door te rekenen, ook al is dat voor de krachtsgrootheden in statisch bepaalde constructies niet nodig. In het geval dat deze gegegevens niet bekend zijn kan je een willekeurige grote waarde nemen onder 'Handmatige invoer'. Als de waarde een paar ordegroottes groter is dan de andere waardes is het al goed, bij een te grote waarde ontstaan er numerieke issues.
- Soms kunnen elementen overlappen zonder dat je het ziet.

Een uitgebreide handleiding met meer opties is [hier](https://icozct.tudelft.nl/TUD_CT/CT2031/oefening/matrix/files/Introductie%20MatrixFrame.pdf) te vinden. Daarnaast biedt [de officiële documentatie](https://knowledge-base.matrix-software.com/nl/help/matrix-frame) ook meer uitleg.


Als voorbeeld bepalen we de uitwendige statisch onbepaaldheid van deze constructie.

::::::{prf:example}
:nonumber: true

```{figure} ./matrixframe_data/constructie.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

1. Maak een nieuw project - '2D-Raamwerk' en klik 'Ok'. De optie '1D-ligger' en '2D-vakwerk' zijn versimpelingen van de '2D-Raamwerk'-optie. De optie '3D-Raamwerk' en '3D-Vakwerk' kan je proberen, maar daar krijgt men over het algemeen hoofdpijn van.

::::::{prf:example}
```{figure} ./matrixframe_data/step1.png
---
align: center
---
```
Aangezien het hier gaat om een 2D-Raamwerk selecteren we die optie.
::::::

2. Je beland direct in de 'Geometrie' interface.

::::::{prf:example}
```{figure} ./matrixframe_data/step2.png
---
align: center
---
```

::::::

3. Klik in het grid om je geometrie te vormen. De coördinaten zijn zijn zichtbaar in de onderbalk en de afmetingen verschijnen tijdens het klikken. Gebruik `Esc` op je toetsenbord om te stoppen of op een volgend element te beginnen die niet vastzit aan het uiteinde van het vorige element.

::::::{prf:example}
```{figure} ./matrixframe_data/step3.png
---
align: center
---
```

De eerste staaf is al getekend en van de tweede staaf is de coordinaat $\left(9,0 \right)$ zichtbaar in de balk onderaan.
::::::

4. Ga verder met de 'Profielgegevens' interface. Onder 'Profielen' - 'Handmatige invoer' kan je een $A$, $I$ en $E$ invullen.

::::::{prf:example}
```{figure} ./matrixframe_data/step4.png
---
align: center
---
```

In dit voorbeeld is er enkel een $EI$ gegeven, terwijl we een losse $E$ en $I$ moeten invoeren. Daarom kan je twee getallen kiezen waarvan het product $7.8 \cdot 10^4$ is, bijvoorbeeld $E = 200 \cdot 10^6$ en $I = 3.9 \cdot 10^-2$. $EA$ is $\infty$, waarvoor we een grote numerieke waarde kunnen invoeren, bijvoorbeeld $A  = 10 \cdot 10^3$. Tip, $\cdot10^6$ kan je invoeren als `e6` Vergeet niet op 'Pas toe op alles' te klikken!

```{figure} ./matrixframe_data/step5.png
---
align: center
---
```
::::::
