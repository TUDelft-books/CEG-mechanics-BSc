```{index} Displacement method with degrees of freedom
```

# Apply displacement method with degrees of freedom

There are two displacement methods: the displacement method which solves for statically unknown displacements, and the displacement method which solves for degrees of freedom. This page treats the second method

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://oit.tudelft.nl/CTB2210/2025/verplaats2/theorie.html. Deze theorie is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% Source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

```
````

Een groot nadeel van de krachten- en verplaatsingenmethode met statisch onbepaalde krachten en verplaatsingen van de vorige les is namelijk dat je de statisch onbepaalde constructie moet aanpassen tot een statisch bepaalde constructie. Dat kan soms lastig zijn. Bij de verplaatsingenmethode met vrijheidsgraden. In plaats van de constructie op te lossen voor een statisch onbepaalde kracht of verplaatsingen, lossen we de constructie op voor één of meerdere vrijheidsgraden die de vervorming van de constructie bepalen. 

::::::{prf:algorithm} Verplaatsingenmethode met vrijheidsgraden
:nonumber: true
:label: verplaatsingenmethode_algoritme_2

1. Kies één of meerdere vrijheidsgraden die de vervorming van de constructie bepalen en splits de constructie in of rondom die plek(ken).
2. Bereken de krachten in de splitsing in termen van de onbekende vrijheidsgraden. Als je meerdere vrijheidsgraden hebt gedefinieerd, bereken dan de invloed van elke vrijheidsgraad los waarbij de andere vrijheidsgraden aan nul worden gesteld. Maak daarbij gebruik van de uitgebreide vergeet-me-nietjes in het geval van buiging.
3. Gebruik evenwichtsvoorwaarden om de vrijheidsgraden op te lossen.

::::::

De toepassing van deze verplaatsingenmethode op een statisch onbepaalde constructie wordt in een voorbeeld getoond.

::::::{prf:example}
:nonumber: true
:label: verplaats_2_0

```{figure} ./displacement_method2_data/structure.svg
---
align: center
---
Voorbeeldconstructie, $EI_{\rm{AB}} = 1.5 \ \rm{MNm}^2, EI_{\rm{BC}} = 3 \ \rm{MNm}^2$
```

::::::

1. Kies één of meerdere vrijheidsgraden die de vervorming van de constructie bepalen en splits de constructie in of rondom die plek(ken).

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_1

    ```{figure} ./displacement_method2_data/DOF.svg
    ---
    align: center
    ---
    De verplaatsing en rotatie van B wordt gekozen als vrijheidsgraad.
    ```

    Met de verplaatsing en rotatie van B kan de verplaatsing van de hele constructie worden bepaald. 

    ::::::

2. Bereken de krachten in de splitsing in termen van de onbekende vrijheidsgraden. Als je meerdere vrijheidsgraden hebt gedefinieerd, bereken dan de invloed van elke vrijheidsgraad los waarbij de andere vrijheidsgraden aan nul worden gesteld. Maak daarbij gebruik van de uitgebreide vergeet-me-nietjes in het geval van buiging.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_2

    De constructie wordt gesplitst in $\rm{B}$. Daarvoor kunnen we het vrijlichaamsschema van beide delen en knoop $\rm{B}$ tekenen.

    ```{figure} ./displacement_method2_data/splits.svg
    ---
    align: center
    ---
    Gesplitste constructie, $EI_{\rm{AB}} = 1.5 \ \rm{MNm^2}, EI_{\rm{BC}} = 3 \ \rm{MNm^2}$
    ```

    Voor beide delen kunnen we nu met behulp van vergeet-me-nietjes de snedekrachten in $\rm{B}$ bepalen als functie van $w_{\rm{B}}$ en $\varphi_{\rm{B}}$. in het stukje $\rm{BC}$ heeft de puntlast van $44.8 \ \rm{kN}$ ook nog invloed.

    Allereerst wordt de invloed van de rotatie $\varphi_{\rm{B}}$ op gedeelte $\rm{AB}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

    ```{figure} ./displacement_method2_data/AB_1.svg
    ---
    align: center
    ---
    Boven het vergeet-me-nietje waarmee we de snedekrachten ten gevolge van $\varphi_{\rm{B}}$ op gedeelte $\rm{AB}$ kunnen berekenen. Komt overeen met vergeet-me-nietje (7) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Daaronder het gesplitste gedeelte $\rm{AB}$ met de snedekrachten in de optredende richting
    ```

    Hieruit volgt:

    - $M_{\rm{B,1}} = \varphi_{\rm{B}} \cdot \cfrac{4EI}{L_{\rm{AB}}} = \varphi_{\rm{B}} \cdot \cfrac{4 \cdot 1500}{3} = 2000 \varphi_{\rm{B}}$
    - $V_{\rm{B,1}} = \varphi_{\rm{B}} \cdot \cfrac{6EI}{L_{\rm{AB}}^2} = \varphi_{\rm{B}} \cdot \cfrac{6 \cdot 1500}{3^2} = 1000 \varphi_{\rm{B}}$


    Vervolgens wordt de invloed van de verplaatsing $w_{\rm{B}}$ op gedeelte $\rm{AB}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

    ```{figure} ./displacement_method2_data/AB_2.svg
    ---
    align: center
    ---
    Boven het vergeet-me-nietje waarmee we de snedekrachten ten gevolge van $w_{\rm{B}}$ op gedeelte $\rm{AB}$ kunnen berekenen. Komt overeen met vergeet-me-nietje (g) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Daaronder het gesplitste gedeelte $\rm{AB}$ met de snedekrachten in de optredende richting
    ```

    Hieruit volgt:

    - $M_{\rm{B,2}} = w_{\rm{B}} \cdot \cfrac{6EI}{L_{\rm{AB}}^2} = w_{\rm{B}} \cdot \cfrac{6 \cdot 1500}{3^2} = 1000 w_{\rm{B}}$
    - $V_{\rm{B,2}} = w_{\rm{B}} \cdot \cfrac{12EI}{L_{\rm{AB}}^3} = w_{\rm{B}} \cdot \cfrac{12 \cdot 1500}{3^3} = \cfrac{2000}{3} w_{\rm{B}}$

    Nu kan ook het rechtergedeelte worden bekeken. Te beginnen met de invloed van de rotatie $\varphi_{\rm{B}}$ op gedeelte $\rm{BC}$. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

    ```{figure} ./displacement_method2_data/BC_1.svg
    ---
    align: center
    ---
    Boven het vergeet-me-nietje waarmee we de snedekrachten ten gevolge van $\varphi_{\rm{B}}$ op gedeelte $\rm{BC}$ kunnen berekenen. Komt overeen met het horizontaal gespiegelde vergeet-me-nietje (4) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Daaronder het gesplitste gedeelte $\rm{BC}$ met de snedekrachten in de optredende richting. Daarvoor is het vergeet-me-nietje in zowel horizontale als verticale richting gespiegeld.
    ```

    Hieruit volgt:
    - $M_{\rm{B,3}} = \varphi_{\rm{B}} \cdot \cfrac{3EI}{L_{\rm{BC}}} = \varphi_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3} = 3000 \varphi_{\rm{B}}$
    - $V_{\rm{B,3}} = \varphi_{\rm{B}} \cdot \cfrac{3 EI}{L_{\rm{BC}}^2} = \varphi_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3^2} = 1000 \varphi_{\rm{B}}$

    Vervolgens wordt de invloed van de verplaatsing $w_{\rm{B}}$ op gedeelte $\rm{BC}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

    ```{figure} ./displacement_method2_data/BC_2.svg
    ---
    align: center
    ---
    Boven het vergeet-me-nietje waarmee we de snedekrachten ten gevolge van $w_{\rm{B}}$ op gedeelte $\rm{BC}$ kunnen berekenen. Komt overeen met het horizontaal gespiegelde vergeet-me-nietje (f) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Daaronder het gesplitste gedeelte $\rm{BC}$ met de snedekrachten in de optredende richting. Daarvoor is het vergeet-me-nietje in verticale richting gespiegeld en is de inklemming aan de linkerkant verplaatst in plaats van de roloplegging aan de rechterkant.
    ```

    Hieruit volgt:
    - $M_{\rm{B,4}} = w_{\rm{B}} \cdot \cfrac{3EI}{L_{\rm{BC}}^2} = w_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3^2} = 1000 w_{\rm{B}}$
    - $V_{\rm{B,4}} = w_{\rm{B}} \cdot \cfrac{6EI}{L_{\rm{BC}}^3} = w_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3^3} = \cfrac{1000}{3} w_{\rm{B}}$

    Tot slot moet ook nog de invloed van de puntlast van $44.8 \ \rm{kN}$ op gedeelte $\rm{BC}$ worden meegenomen. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

    ```{figure} ./displacement_method2_data/BC_3.svg
    ---
    align: center
    ---
    Boven het vergeet-me-nietje waarmee we de snedekrachten ten gevolge van de puntlast van $44.8 \ \rm{kN}$ op gedeelte $\rm{BC}$ kunnen berekenen. Komt overeen met het horizontaal gespiegelde vergeet-me-nietje (8) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Daaronder het gesplitste gedeelte $\rm{BC}$ met de snedekrachten in de optredende richting.
    ```

    Hieruit volgt:
    - $M_{\rm{B,5}} = \cfrac{3}{16} {F} L_{\rm{BC}} = \cfrac{3}{16} \cdot 44.8 \cdot 3 = 25.2 \ \rm{kNm}$
    - $V_{\rm{B,5}} = \cfrac{11}{16} {F} = \cfrac{11}{16} \cdot 44.8 = 30.8 \ \rm{kN}$
    ::::::

3. Gebruik evenwichtsvoorwaarden om de vrijheidsgraden op te lossen.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_3

    Nu alle snedekrachten in $\rm{B}$ bekend zijn, kunnen we de evenwichtsvoorwaarden voor knoop $\rm{B}$ opstellen:

     ```{figure} ./displacement_method2_data/evenwicht_B.svg
    ---
    align: center
    ---
    Vrijlichaamsschema van knoop $\rm{B}$ met alle snedekrachten.
    ```

    Dit geeft:
    
    $$
    \begin{aligned}
    \Sigma M &= 0 \\
    -M_{\rm{B,1}} - M_{\rm{B,2}} - M_{\rm{B,3}} + M_{\rm{B,4}} - M_{\rm{B,5}} &= 0 \\
    5000 \varphi_{\rm{B}} + 25.2 &= 0 \\
    \varphi_{\rm{B}} &= -0.00504 \ \rm{rad}
    \end{aligned}
    $$

    en:

    $$
    \begin{aligned}
    \Sigma F_{\rm{v}} &= 0 \\
    -V_{\rm{B,1}} - V_{\rm{B,2}} + V_{\rm{B,3}} + V_{\rm{B,4}} - V_{\rm{B,5}} &= 0 \\
    1000 w_{\rm{B}} - 30.8 &= 0 \\
    w_{\rm{B}} &= 0.0308 \ \rm{m} = 30.8 \ \rm{mm}
    \end{aligned}
    $$

    ::::::

## Instructies in collegevorm

Dit onderwerp is [in constructiemechanica 3, 2025-2026, les 11](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/5af52bfa489c4f579dcf83847e8329c71d?sortBy=most-recent) gepresenteerd in collegevorm tot 0:47:56.

## Meer voorbeelden
In hoofdstuk 4.1 en 4.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt deze verplaatsingenmethode behandeld.

## Oefeningen
Opgaves 4.4 - 4.33, 4.35, 4.36 in hoofdstuk 4.5 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Dit zijn dezelfde opgaves als voor [](./displacement_method.md), maar de aanpak is nu anders. Er zijn helaas geen antwoorden beschikbaar. Je kan de constructies doorrekenen met MatrixFrame om je antwoorden te controleren.
