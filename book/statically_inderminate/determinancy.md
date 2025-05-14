```{index} Statisch onbepaaldheid
```
```{index} Graad van statisch onbepaaldheid
```
# Statisch onbepaaldheid

```{figure} ./determinancy_data/Example_1.svg
:align: center
:width: 300
```

Een constructie is statisch onbepaald wanneer deze niet meer enkel met evenwichtsvergelijkingen kan worden opgelost. Er kan hierbij onderscheid worden gemaakt tussen:
- Enkel oplegreacties kunnen worden bepaald (uitwendig statisch bepaald)
- Inwendige krachten kunnnen worden bepaald (inwendig statisch bepaald)

Als evenwichtsvergelijkingen niet genoeg zijn is een constructie statisch onbepaald. De mate van statisch onbepaaldheid wordt uitgedrukt in de graad van statisch onbepaaldheid

Het is nodig de graad van statisch onbepaaldheid te bepalen om deze constructies met behulp van de krachtenmethode op te kunnen lossen.

Deze twee categorieën worden samen behandeld in hoofdstuk 4.5.2 en 4.5.3 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Voor [vakwerken](truss_structures) is de analyse versimpeld zoals beschreven in hoofdstuk 9.2.2 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Alhoewel de getoonde vergelijkingen met $r$, $v$ en $e$ effectief kunnen zijn bij simpele constucties, leiden deze in het algemeen tot verkeerde resultaten. Een aanpak die altijd werkt is hieronder getoond voor afzonderlijk uitwendig en inwendig statisch onbepaaldheid.

```{index} Graag van uitwendig statisch onbepaaldheid
```
## Bepalen graad van uitwendig statisch onbepaaldheid
Voor de berekening van uitwendig statisch onbepaaldheid gelden de volgende stappen:

::::::{prf:example}

```{figure} ./determinancy_data/Example.svg
---
name: example_sd
align: center
---
Voorbeeldconstructie
```

Als voorbeeld bepalen we de uitwendige statisch onbepaaldheid van deze constructie.

::::::

1. Splits de constructie in zo groot mogelijke, vormvaste, scharnierend verbonden delen en teken het vrijlichaamsschema van de scharnierende delen. Naast de oplegreacties werken in de scharnierende verbinding werken twee onbekende krachten: horizontaal en verticaal. Deze krachten in de verbinding hebben een even grote tegengestelde reactiekracht op het aansluitende deel.

::::::{prf:example}

```{figure} ./determinancy_data/Example_1.svg
---
name: example_sd_1
align: center
---
Gesplitste constructie
```

De constructie is onder te verdelen in twee vormvaste, scharnierend verbonden delen. De opleggingen zijn vervangen door oplegreacties en de scharnierende verbinding door een horizontale en verticale kracht (en reactiekrachten)

::::::

2. Tel het aantal onbekende krachten: de oplegreacties en verbindingskrachten in de scharnieren (de reactiekrachten tellen niet apart mee)

::::::{prf:example}

```{figure} ./determinancy_data/Example_2.svg
---
name: example_sd_2
align: center
---
Aantal onbekende krachten
```

Er zijn in totaal 6 oplegreacties en 2 verbindingskrachten

::::::


3. Tel het evenwichtsvergelijkingen: 3 evenwichtsvergelijkingen per vormvaste deel van de constructie

::::::{prf:example}

```{figure} ./determinancy_data/Example_3.svg
---
name: example_sd_3
align: center
---
Aantal onbekende evenwichtsvergelijkingen
```

Er zijn twee vormvaste delen, dus 6 evenwichtsvergelijkingen

::::::

4. De graad van statisch onbepaaldheid is het aantal oplegreacties + verbindingskrachten - aantal evenwichtsvergelijkingen

::::::{prf:example}

De graad van uitwendig statisch onbepaalheid voor dit voorbeeld $6 + 2 - 6 = 2 $.

::::::

```{index} Graag van inwendig statisch onbepaaldheid
```
## Bepalen graad van inwendig statisch onbepaaldheid
Voor de berekening van inwendig statisch onbepaaldheid gelden de volgende stappen:

::::::{prf:example}

```{figure} ./determinancy_data/Example_abc.svg
---
name: example_sd_abc
align: center
---
Voorbeeldconstructie
```

Als voorbeeld bepalen we de inwendige statisch onbepaaldheid van deze constructie.

::::::

1. Splits constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor alle knopen, rekening houdend met wat voor staven en opleggingen er aan de knopen verbonden zijn:
   - Op een scharnierende verbinding en vrije- / scharnierende uiteindes werken geen buigende momenten
   - Vanuit een pendelstaaf werkt alleen een normaalkracht

::::::{prf:example}

```{figure} ./determinancy_data/Example_4.svg
---
name: example_sd_4
align: center
---
Vrijlichaamsschema's knopen
```

De consturctie bestaat uit 6 knopen. Op knoop A, B and C werken onbekende oplegreacties. Knoop A is een scharnierend uiteinde dus daar werken geen buigende momenten. Op knoop D werkt vanuit staaf DB geen buigend moment vanwege de scharnierende verbinding. Knoop E is scharnierend, dus hier werken geen buigende momenten op. Daarnaast is staaf EG een pendelstaaf dus werkt er vanuit die staaf alleen een normaalkracht op de knoop. Datzelfde geldt voor knoop G.

::::::

2. Teken het vrijlichaamsschema voor de staven: teken de reactiekrachten op de staven ten gevolge van de krachten op de knopen.

::::::{prf:example}

```{figure} ./determinancy_data/Example_5.svg
---
name: example_sd_5
align: center
---
Vrijlichaamsschema's staven
```

Vanuit {numref}`example_sd_4` kunnen de reactiekrachten op de staven getekend worden.

::::::

3. Tel het aantal onbekende krachten: oplegreacties en staafkrachten (de reactiekrachten tellen niet apart mee)

::::::{prf:example}

```{figure} ./determinancy_data/Example_6.svg
---
name: example_sd_6
align: center
---
Aantal onbekende krachten
```

Vanuit {numref}`example_sd_4` kunnen het aantal onbekende krachten geteld worden. Er zijn 6 oplegreacties en 32 staafkrachten.

Deze straafkrachten kunnen ook geteld worden in de vrijlichaamsschema's van de staven uit {numref}`example_sd_5`:

```{figure} ./determinancy_data/Example_7.svg
---
name: example_sd_7
align: center
---
Aantal onbekende staafkrachten
```

::::::

4. Tel het evenwichtsvergelijkingen: 1 evenwichtsvergelijking per pendelstaaf, 3 evenwichtsvergelijkingen per algemene staaf, 2 evenwichtsvergelijkingen per scharnierende knoop en 3 evenwichtsvergelijkingen per algemene knoop.

::::::{prf:example}

```{figure} ./determinancy_data/Example_9.svg
---
name: example_sd_9
align: center
---
Aantal evenwichtsvergelijkingen per staaf
```

Er is een pendelstaaf, de rest zijn algemene staven. Dat geeft 19 evenwichtsvergelijkingen voor de staven.

```{figure} ./determinancy_data/Example_8.svg
---
name: example_sd_8
align: center
---
Aantal evenwichtsvergelijkingen per knoop
```

Van de knopen zijn er twee volledig scharnierend, bij de rest is ook de momentensom van belang. Dat geeft 16 evenwichtsvergelijkingen.

In totaal zijn er dus 35 evenwichtsvergelijkingen

::::::

5. De graad van statisch onbepaaldheid is het aantal oplegreacties + staafkrachten - aantal evenwichtsvergelijkingen

::::::{prf:example}

De graad van inwendig statisch onbepaalheid voor dit voorbeeld $ 6 + 32 - 35 = 3 $.

::::::

## Opgaves
- Opgaves 4.11 - 4.22, van hoofdstuk 4 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Opgave  9.6, van hoofdstuk 9 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).
