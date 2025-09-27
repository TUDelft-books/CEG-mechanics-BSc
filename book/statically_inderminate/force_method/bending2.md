```{index} krachenmethode; voor raamwerkconstructies
```

(krachtenmethode_raam)=
# ... voor raamwerkconstructies

Het algemene concept van de krachtenmethode wordt behandeld in hoofdstuk 2.1 terwijl de krachtenmethode voor raamwerkconstructies wordt behandeld in hoofdstuk 2.2.5-2.2.7 en de meer specifieke 'hoekveranderingsvergelijkingen' in hoofdstuk 3.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. 

De methode van 'hoekveranderingsvergelijkingen' heeft als voordeel dat het zeer eenvoudig is om de benodigde rotaties te berekenen met behulp van vergeet-mij-nietjes. Echter, voor niet alle constructies zijn vergeet-mij-nietjes beschikbaar.

We behandelen de toepassing op raamwerkconstructies met het volgende voorbeeld. 


::::::{prf:example}
:nonumber: true
:label: sd_raam_0

```{figure} ./theorie_data/example.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

1. Bepaal [de graad van statische bepaaldhei](../determinancy.md).

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_1

    Voor ons voorbeeld zijn we geïnteresseerd in de verdeling van inwendige krachten, dus moeten we de graad van inwendige statische onbepaaldheid evalueren.

    ```{figure} ./theorie_data/onbekenden.svg
    ---
    align: center
    ---
    Er zijn 21 onbekende krachten.
    ```

    ```{figure} ./theorie_data/vergelijkingen.svg
    ---
    align: center
    ---
    Er zijn 19 evenwichtsvergelijkingen
    ```

    Deze constructie is dus 2e orde inwendig statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_2

    Er zijn veel opties, waarvan een aantal mogelijke opties:

    `````{tab-set}
    ````{tab-item} Horizontale oplegging bij $\rm{B}$ loslaten en scharnier toevoegen in $\rm{B}$
    ```{figure} ./theorie_data/optie1.svg
    :align: center
    ```
    ````
    ````{tab-item} Horizontale oplegging bij $\rm{B}$ en $\rm{C}$ loslaten
    ```{figure} ./theorie_data/optie2.svg
    :align: center
    ```

    ````
    ````{tab-item} Horizontale en verticale oplegging bij $\rm{A}$ loslaten
    ```{figure} ./theorie_data/optie3.svg
    :align: center
    ```
    ````
    ````{tab-item} Horizontale oplegging bij $\rm{A}$ loslaten en scharnier toevoegen in $\rm{B}$
    ```{figure} ./theorie_data/optie4.svg
    :align: center
    ```
    ````
    `````

    De derde optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_4

    We hebben de volgende statisch bepaalde constructie gekozen met vormveranderingsvoorwaardes $w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $ en $w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $:

    ```{figure} ./theorie_data/SB-systeem.svg
    ---
    align: center
    ---
    De statisch bepaalde constructie met vormveranderingsvoorwaarde
    ```

    De krachtsverdeling kan worden gevonden met evenwicht:

    - $M_{\rm{C}} = 90 \ \rm{kNm}$ (◠/ᑐ)
    - $M_{\rm{B}} = 6A_{\rm{v}}$ (◡/ᑐ)

    Met behulp van de vergeet-mij-nietjes kunnen de rotaties nu worden geëvalueerd:

    - $\varphi_{\rm{B}} = \cfrac{90 \cdot 3}{6 \cdot 5000} + \cfrac{6A_{\rm{v}} \cdot 3}{3 \cdot 5000} = 0.0012 A_{\rm{v}} + 0.009$ (↻)
    - $w_{\rm{A}} = \varphi_{\rm{B}} \cdot 6 + \cfrac{A_{\rm{v}} \cdot 6^3}{3 \cdot 5000}= 0.0216 A_{\rm{v}} + 0.054$

    Voor de horizontale verplaatsing geldt: $w_{\rm{A,h}}  = \cfrac{6A_{\rm{h}}}{EA} $ 

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_5

    $$
    \begin{align*}
    w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    0.0216 A_{\rm{v}} + 0.054 &= 0 \\
    A_{\rm{v}} &= -2.5 \ \rm{kN} \\
    \\
    w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    \cfrac{6A_{\rm{h}}}{EA} &= 0 \\
    A_{\rm{h}} &= 0 \ \rm{kN}
    \end{align*}
    $$
    ::::::

## Instructies in collegevorm

Dit onderwerp is [in constructiemechanica 3, 2025-2026, les 7](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/2e0fc9db91574fc9adacecd1eb833ce71d?academicYear=2025-2026-ctb2210) gepresenteerd in collegevorm van 0:07:50 - 0:31:50.

## Opdrachten

- Opgaves 2.15 - 2.22, 2.24, 2.26 - 2.29, 2.42 - 2.48 in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
- Opgaves 3.11 - 3.15, 3.22, 3.23, 3.25 - 3.33/1, 3.35, 3.36, 3.45, 3.47-1, 3.47-2, 3.47-4, 3.50, 3.51 in hoofdstuk 3.4 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website voor hoofdstuk 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) en [hier voor hoofdstuk 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).