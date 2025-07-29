(krachtenmethode_balk)=
# Theorie


De krachtenmethode hebben we eerder al behandeld voor onder andere [constructies belast op rek](krachtenmethode_simpel) We behandelen de toepassing op balkconstructies met het volgende voorbeeld.

Bij de methode van 'hoekveranderingsvergelijkingen' wordt er altijd gekozen voor het toevoegen van scharnieren om de constructie statisch bepaald te maken. Dat heeft als voordeel dat het zeer eenvoudig is om de benodigde rotaties te berekenen met behulp van vergeet-mij-nietjes. Echter, voor niet alle constructies zijn vergeet-mij-nietjes beschikbaar.

We tonen de stappen van de krachtenmethode voor een balk.

::::::{prf:example}
:nonumber: true
:label: sd_ben_0

```{figure} ./bending_data/Example.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_1

    Voor ons voorbeeld zijn we geïnteresseerd in de verdeling van inwendige krachten, dus moeten we de graad van inwendige statische onbepaaldheid evalueren.

    ```{figure} ./bending_data/onbekenden.svg
    ---
    align: center
    ---
    Er zijn 14 onbekende krachten.
    ```

    ```{figure} ./bending_data/vergelijkingen.svg
    ---
    align: center
    ---
    Er zijn 13 evenwichtsvergelijkingen
    ```

    Deze constructie is dus 1e orde inwendig statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_2

    Er zijn veel opties, waarvan de meest voor de hand liggende hieronder worden getoond:

    `````{tab-set}
    ````{tab-item} Verticale oplegging bij $\rm{A}$ loslaten
    ```{figure} ./bending_data/optie2.svg
    :align: center
    ```
    ````
    ````{tab-item} Verticale oplegging bij $\rm{B}$ loslaten
    ```{figure} ./bending_data/optie3.svg
    :align: center
    ```
    Deze optie is niet erg handig omdat er geen vergeet-mij-nietjes zijn om de verplaatsing bij $\rm{B}$ te verkrijgen voor deze belastingen
    ````
    ````{tab-item} Verticale oplegging bij $\rm{C}$ loslaten
    ```{figure} ./bending_data/optie4.svg
    :align: center
    ```
    ````
    ````{tab-item} Scharnier toevoegen bij $\rm{B}$
    ```{figure} ./bending_data/optie1.svg
    :align: center
    ```
    Als alleen scharnieren worden toegevoegd, noemen we deze benadering 'hoekveranderingsvergelijkingen' of 'gaapvergelijkingen'
    ````
    `````

    De laatste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_4

    We hebben de volgende statisch bepaalde constructie gekozen met vormveranderingsvoorwaarde $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) $:

    ```{figure} ./bending_data/SB-systeem.svg
    ---
    align: center
    ---
    De statisch bepaalde constructie met vormveranderingsvoorwaarde
    ```

    Met behulp van de vergeet-mij-nietjes kunnen de rotaties direct worden geëvalueerd zonder het evalueren van inwendige krachten:

    - $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI}$
    - $\varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) = -\cfrac{2M_{\rm{B}}}{3EI}$

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_5

    $$
    \begin{align*}
    \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) &= \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) \\
    \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI} &= -\cfrac{2M_{\rm{B}}}{3EI} \\
    M_{\rm{B}} &= -20 \ \rm{kNm}
    \end{align*}
    $$
    ::::::

## Meer voorbeelden
Het algemene concept van de krachtenmethode wordt behandeld in hoofdstuk 2.1 terwijl de krachtenmethode voor vakwerkconstructies wordt behandeld in hoofdstuk 2.2.1 - 2.2.4 en de meer specifieke 'hoekveranderingsvergelijkingen' in hoofdstuk 3.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. De voorbeelden van hoofdstuk 3.1 worden behandeld in [de volgende les](krachtenmethode_raamwerk).

## Opdrachten

- Opgaves 2.1 - 2.14, 2.23, 2.25 en 2.30 in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
- Opgaves 3.1 - 3.10, 3.16 - 3.21 in hoofdstuk 3.4 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website voor hoofdstuk 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) en [hier voor hoofdstuk 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).
