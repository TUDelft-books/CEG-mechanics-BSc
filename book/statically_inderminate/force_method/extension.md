```{index} Krachtenmethode; voor vakwerkconstructies
```

# ... voor vakwerkconstructies

Het algemene concept van de krachtenmethode wordt getoond in [](./force_method.md) en behandeld in hoofdstuk 2.1. Specifiek de krachtenmethode voor vakwerkconstructies wordt behandeld in hoofdstuk 2.2.8 - 2.2.10 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

We behandelen de toepassing op vakwerkconstructies met het volgende voorbeeld. Dit voorbeeld bevat een [Williot diagram](../../stresses_displacements/displacements_truss/williot.md) om de verplaatsingen te berekenen.

::::::{prf:example}
:nonumber: true
:label: sd_ext_0

```{figure} ./extension_data/Example.svg
---
align: center
---
Voorbeeldconstructie. Hoewel dit geen vakwerkconstructie is, worden vervorming enkel veroorzaakt door extensie, niet door buiging.
```

    ::::::

    1. Bepaal [de graad van statische bepaaldheid](../determinancy.md).

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_1

    Voor ons voorbeeld zijn we geïnteresseerd in de interne krachtenverdeling, dus moeten we de graad van interne statische onbepaaldheid evalueren.

    ```{figure} ./extension_data/unknown_forces.svg
    ---
    align: center
    ---
    Er zijn 17 onbekende krachten.
    ```

    ```{figure} ./extension_data/equations.svg
    ---
    align: center
    ---
    Er zijn 16 evenwichtsvergelijkingen
    ```

    Deze constructie is dus 1e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_2

    Er zijn hier veel opties, waarvan er enkele hieronder worden getoond:

    `````{tab-set}
    ````{tab-item} Splits de constructie bij een scharnier
    ```{figure} ./extension_data/option1.svg
    :align: center
    ```
    ````
    ````{tab-item} Scharnier toevoegen
    ```{figure} ./extension_data/option2.svg
    :align: center
    ```
    ````
    ````{tab-item} De horizontale bewegingsrichting van een oplegging vrijmaken
    ```{figure} ./extension_data/option3.svg
    :align: center
    ```
    ````
    ````{tab-item} Verticale oplegging weghalen
    ```{figure} ./extension_data/option4.svg
    :align: center
    ```
    ````
    `````

    De laatste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_4

    We hebben de volgende statisch bepaalde constructie gekozen met vervormingsvoorwaarde $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{figure} ./extension_data/SD_struc.svg
    ---
    align: center
    ---
    De statisch bepaalde constructie met vervormingsvoorwaarde
    ```

    Omdat $\rm{AE}$ oneindig stijf is, zullen alle vervormingen het gevolg zijn van staven die uitrekken/samendrukken. Om dit te berekenen, kunnen eerst de normaalkrachten worden geëvalueerd als functie van $B_{\rm{v}}$ met behulp van bijvoorbeeld een momentenevenwicht rond $\rm{A}$ voor het element $\text{ADE}$:

    - $N_{\rm{CD}}\left( B_{\rm{v}} \right) = 210 - 2.5 B_{\rm{v}}$
    - $N_{\rm{BE}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    Dit leidt tot de volgende uitrekking van de elementen, met behulp van $\Delta L = \cfrac{N \ L}{EA}$:

    - $\Delta L_{\rm{CD}}\left( B_{\rm{v}} \right) = \cfrac{1400}{EA} - \cfrac{50 B_{\rm{v}}}{3 EA}$
    - $\Delta L_{\rm{BE}}\left( B_{\rm{v}} \right) = -\cfrac{5 B_{\rm{v}}}{EA}$

    Dit leidt tot de volgende verplaatsing, met behulp van een [Williot diagram](../../stresses_displacements/displacements_truss/williot.md):

    ```{figure} ./extension_data/williot.svg
    ---
    align: center
    ---
    De verplaatsing van $\rm{D}$ is $\cfrac{5}{4} \Delta L_{\rm{CD}} $
    ```

    - $w_{\rm{D}}\left( B_{\rm{v}} \right) = \cfrac{1750}{EA} - \cfrac{125 B_{\rm{v}}}{6 EA} \left( \downarrow \right) $
    - $w_{\rm{E}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{125 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} &= 0 \\
    B_{\rm{v}} &= 75 \ \rm{kN}
    \end{align*}
    $$

    Dit leidt tot de volgende andere resultaten:

    - $N_{\rm{CD}} = 22.5 \ \rm{kN}$
    - $N_{\rm{BE}} -75 \ \rm{kN} $
    - $w_{\rm{D}} = \cfrac{375}{2EA} \left( \downarrow \right) $
    - $w_{\rm{E}} = \cfrac{375}{EA} \left( \downarrow \right) $

    ::::::

## Oefeningen
- Opgaves 2.31 - 2.41, in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
Antwoorden zijn [hier beschikbaar](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
