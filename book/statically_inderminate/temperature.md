```{index} Temperature influences; for statically indeterminate structures
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://oit.tudelft.nl/CTB2210/2025/temperatuur/theorie.html. Deze theorie is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
````

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/temperatuur

# Doorrekenen van constructies onder invloed van temperatuur

Elementen verlengen onder uniforme belasting met een extra rek van $\epsilon^{\rm{T}} = \alpha \ \Delta T$, waarbij $\alpha$ de lineaire uitzettingscoëfficiënt is. Wanneer een temperatuurverandering over de hoogte van een element optreedt, verlengen de vezels individueel, wat leidt tot buiging van elementen met een extra kromming van $\kappa^{\rm{T}} = \alpha \ \cfrac{\Delta T}{h}$, waarbij $h$ de hoogte van het element is. In statisch bepaalde constructies leidt dit tot extra spanningsloze rekken (en dus vervormingen) zonder invloed op de krachtverdeling, omdat de krachtverdeling onafhankelijk is van de vervormingen.

De vervorming kan worden gevonden door de spanningsloze rekken te integreren met behulp van de differentiaalvergelijkingen. Alternatief kan een equivalente belasting worden gebruikt die tot dezelfde kromming leidt, zodat de vergeet-me-nietjes toegepast kunnen worden. Dit vereist een kinematisch equivalente belasting die geen invloed heeft op reactiekrachten en interne krachten:

```{figure} ./temperature_data/kin_eq_load_SB.svg
:align: center

Kinematisch equivalente belasting die tot dezelfde rek en kromming leidt als rek door lineaire uitzetting
```

In statisch onbepaalde constructies zijn de vervorming en krachtverdeling gekoppeld, wat leidt tot reactiekrachten en interne spanningen door de (tegengehouden) vervormingen als gevolg van de temperatuurverandering. Deze krachten kunnen opnieuw worden gevonden door de rekken (zowel de spanningsveroorzakende rekken als spanningsloze temperatuurrekken) te integreren met behulp van de differentiaalvergelijkingen. Alternatief kan een kinematisch equivalente belasting, zoals bij statisch bepaalde constructies, worden toegepast in combinatie met de krachtmethode: de verplaatsingen door temperatuur worden meegenomen in de vormveranderingsvoorwaarden.

```{figure} ./temperature_data/kin_eq_load_SO.svg
:align: center

Kinematisch equivalente belasting die tot dezelfde rek en kromming leidt als rek door lineaire uitzetting, terwijl statisch onbepaalde reactiekrachten spanningen en reactiekrachten veroorzaken
```

De temperatuursinvloeden kunnen worden meegenomen in de krachtenmethode met de volgende stappen, waarbij stappen 1 en 4 zijn toegevoegd aan de standaard krachtenmethode:

::::::{prf:algorithm} Temperatuursinvloeden en krachtenmethode
:nonumber: true
:label: krachtenmethode_temperatuur

1. **Bepaal de kromming en rek als gevolg van de temperatuursinvloed los van alle opleggingen.**
2. Bepaal de graad van statische bepaaldheid.
3. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen.
4. **Stel kinematisch equivalente belastingen op die dezelfde vervorming veroorzaken als de temperatuursinvloed.**
5. Los de verplaatsing op in termen van de onbekende onbepaalde krachten.
6. Gebruik je vervormingsvoorwaarden om de statisch onbepaalde krachten op te lossen.

::::::

De toepassing van temperatuursinvloeden op een statisch onbepaalde constructie wordt in een voorbeeld getoond met de krachtenmethode.

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Dit voorbeeld is aangepast van https://oit.tudelft.nl/CT1000/2024/week_7/session_3/intro.html
```
````

::::::{prf:example}
:nonumber: true
:label: temp_0

```{figure} ./temperature_data/structure2.svg
---
align: center
---
Voorbeeldconstructie, $EI = 6 \ \rm{MNm^2}$
```

Het temperatuurverschil over de hoogte van de balk geeft de kromming $\kappa^{\rm{T}} = 10^{-3} \ \rm{m}^{-1}$ over de gehele lengte van de balk:

```{figure} ./temperature_data/curv_sun.svg
---
align: center
---
Krommingslijn ten gevolge van de temperatuur los van alle opleggingen
```

Om de kinematisch equivalente kracht te vinden moeten we de constructie eerste statisch bepaald maken. Dat kan bijvoorbeeld met het volgende statisch bepaalde systeem:

```{figure} ./temperature_data/structure_deter2.svg
---
align: center
---
Statisch bepaald systeem met vormveranderingsvoorwaarde, $EI = 6 \ \rm{MNm^2}$
```

Voor dit systeem krijgen we met een koppel (↻) op het uiteinde van de balk dezelfde vorm van de krommingslijn. De waarde van dat koppel moet $M = \kappa \cdot EI = 6 \ \rm{kNm}$ zijn voor dezelfde kromming. Dat geeft het volgende statisch bepaalde systeem:

```{figure} ./temperature_data/structure_deter3.svg
---
align: center
---
Statisch bepaald systeem met vormveranderingsvoorwaarde en kinematisch equivalente belasting door de temperatuursinvloed, $EI = 6 \ \rm{MNm^2}$
```

Nu kunnen we verder met de krachtenmethode zoals we die gewend zijn. De verplaatsing van $\rm{B}$ kan gevonden worden met vergeet-me-nietjes: $  w_{\rm{B}} = - \cfrac{6 \cdot 6 ^2}{2 \cdot 6000} + \cfrac{B_{\rm{v}} \cdot 6^3}{3 \cdot 6000}= -0.018 + \cfrac{3}{250}B_{\rm{v}}$.

Dit geeft $B_{v} = 1.5 \ \rm{kN}$

De momentenlijn en verplaatsingen kunnen nu gevonden worden. Voor de momentenlijn dient de kinematisch equivalente belasting van $6 \ \rm{kNm}$ niet te worden meegenomen, maar voor de verplaatsingen wel. Dit geeft:


```{figure} temperature_data/M-line.svg
:align: center

Momentenljin
```

```{figure} temperature_data/disp_total.svg
:align: center

Vervormde constructie
```

::::::

## Instructies in collegevorm

Dit onderwerp is [in constructiemechanica 3, 2025-2026, les 9](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/d7800c424fcc4f87a9156d9189ef91501d?academicYear=2025-2026-ctb2210) gepresenteerd in collegevorm tot 0:33:00.

## Afleiding en meer voorbeelden
In hoofdstuk 6.2.2 van Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`worden statisch onbepaalde constructies behandeld. De momentenvlakstelling geen onderdeel is van dit vak

## Oefeningen
- Opgaves 6.25 - 6.30, 3.32 - 6.39, 6.41 - 6.43 in hoofdstuk 6.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Er zijn helaas geen antwoorden beschikbaar.
