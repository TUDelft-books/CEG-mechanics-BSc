```{index} Section forces in torsion structures; diagrams
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://oit.tudelft.nl/CTB1310/2025/torsie_krachten/instructie.html en https://oit.tudelft.nl/CTB1310/2025/torsie_krachten/instructie2.html. Deze theorie is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie

```
```` 

# Diagrams

Net als bij de andere snedekrachtenlijnen (momentenlijn, dwarskrachtenlijn, normaalkrachtenlijn) kunnen we ook een wringende momentenlijn tekenen. Daarvoor introduceren we een vervormingsteken, geïnspireerd op het vrijlichaamsschema met de pijlen met dubbele pijlpunt. Deze kunnen we in een wringende momentenlijn gebruiken om de richting van de wringende momenten aan te geven. Het maakt niet uit of dit teken boven of onder de as wordt gezet.

```{figure} ./instructie_data/vervormingstekens.svg
---
align: center
---
Vervormingstekens voor wringende momenten
```

Net als bij de buigende momentenlijn kunnen we een aantal eigenschappen van de wringende momentenlijn vinden:

- De wringende momentenlijn is constant als er geen verdeelde wringende momenten op de constructie werken. Dit verband volgt uit de differentiaalvergelijking zoals hieronder wordt afgeleid.
- De wringende momentenlijn springt bij een uitwendig wringend moment. Dit volgt uit het evenwicht rondom een uitwendige wringend moment.

::::::{prf:algorithm} Bepalen wringende momentenlijn
:nonumber: true

1. Teken het vrijlichaamsschema van de constructie of maak een snede en teken het vrijlichaamschema van een deel van de constructie. Neem wringende momenten aan bij een inklemming of starre verbinding.
2. Stel de evenwichtsvergelijkingen op voor de wringende momenten rondom een as in dezelfde richting als de staaf: $\sum T_{\rm{as}} = 0$. Alle krachten, buigende en wringende momenten die een draaiing rondom deze as veroorzaken komen in deze evenwichtsvergelijking terecht.
3. Los de evenwichtsvergelijking op om de onbekende wringende momenten of oplegreacties te bepalen.
4. Herhaal dit op alle karakteristieke punten om de wringende momentenlijn te bepalen.

::::::

Het bepalen van de wringende momentenlijn wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie2_data/torsielijn.svg
---
align: center
---
Voorbeeldconstructie
```

Voor deze constructie wordt gevraagd naar de wringende momentenlijn.

Daarvoor maken we op alle karakteristieke punten een snede. Beginnend bij $\rm{G}$ aan de kant van $\rm{GH}$:

```{figure} ./instructie2_data/FBD_GH.svg
---
align: center
---
Het buigend moment $M_z$ is aangegeven met een kromme pijl en het wringend moment $M_{\rm{t}}$ met een pijl met dubbele pijlpunt. De snedekrachten in de andere vlakken en de normaalkracht zijn weggelaten.
```

Hiervoor kan een evenwichtsvergelijking worden opgesteld rondom de as:

$$
\begin{align*}
\sum T_{\rm{GH}} &= 0 \\
M_{\rm{t}}^{\rm{GH}} &= 0
\end{align*}
$$

Het wringend moment in $\rm{GH}$ is de enige bijdrage aan de evenwichtsvergelijking en is dus gelijk aan nul.

Daarmee kan een beginnetje worden gemaakt met de wringende momentenlijn:

```{figure} ./instructie2_data/Mt-lijn-GH.svg
---
align: center
---
Wringende momentenlijn met enkel deel $\rm{GH}$ bekend
```

Vervolgens maken we een snede in $\rm{E}$:

```{figure} ./instructie2_data/FBD_EH.svg
---
align: center
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{EG}} &= 0 \\
-M_{\rm{t}}^{\rm{EH}} - 10 \cdot 1 &= 0 \\
M_{\rm{t}}^{\rm{EH}} &= -10 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

```{tip}
In deze evenwichtsvergelijking kunnen de richtingen van het assenstelsel als positief worden aangenomen, maar dat is niet vereist. In dit geval wijst $M_{\rm{t}}^{\rm{EH}}$ in de negatieve $x$-richting en is daarom negatief in de evenwichtsvergelijking. Ook de kracht van $10 \ \rm{kN}$ veroorzaakt een wringend moment in de negatieve $x$-richting, als je de rechterhandregel toepast met je vingers krullend in de richting van de kracht wijst je duim in de negatieve $x$-richting.

Daarnaast zou de evenwichtsvergelijking ook kunnen worden opgesteld rondom een andere as. Echter is de as $\rm{EG}$ hier het makkelijkste omdat het onbekende buigende moment $M_{\rm{E}}$ en dwarskracht $V_{\rm{E}}$ door deze as gaan en dus een arm hebben van $0$.
```

Daarmee kan de wringende momentenlijn verder worden ingevuld:

```{figure} ./instructie2_data/Mt-lijn-EG.svg
---
align: center
---
Wringende momentenlijn met deel $\rm{GH}$ en $\rm{EH}$ bekend
```

Op dezelfde manier kunnen we doorgaan met snedes. Bijvoorbeeld met een snede bij $\rm{E}$ aan de kant van $\rm{DE}$:

```{figure} ./instructie2_data/FBD_DE.svg
---
align: center
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{DE}} &= 0 \\
M_{\rm{t}}^{\rm{DE}} - 10 \cdot 1 &= 0 \\
M_{\rm{t}}^{\rm{DE}} &= 10 \ \rm{kNm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Vervolgens het wringend moment in deel $\rm{CD}$:

```{figure} ./instructie2_data/FBD_CD.svg
---
align: center
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{CD}} &= 0 \\
M_{\rm{t}}^{\rm{CD}} + 10 \cdot 2 &= 0 \\
M_{\rm{t}}^{\rm{CD}} &= -20 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

Vervolgens het wringend moment in deel $\rm{BC}$:

```{figure} ./instructie2_data/FBD_BC.svg
---
align: center
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{BC}} &= 0 \\
M_{\rm{t}}^{\rm{BC}} + 10 \cdot 3 + 3 \cdot 2 \cdot 1 + \frac{1}{2} \cdot 6 \cdot 2 \cdot \frac{2}{3}&= 0 \\
M_{\rm{t}}^{\rm{BC}} &= -40 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

Tot slot het wringend moment in deel $\rm{AB}$:

```{figure} ./instructie2_data/FBD_AB.svg
---
align: center
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{AB}} &= 0 \\
M_{\rm{t}}^{\rm{AB}} + 10 \cdot 1 - 3 \cdot 2 \cdot 1 - \frac{1}{2} \cdot 6 \cdot 2 \cdot 1&= 0 \\
M_{\rm{t}}^{\rm{AB}} &= 2 \ \rm{kNm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Dit alles samen geeft de volgende wringende momentenlijn:

```{figure} ./instructie2_data/Mt-lijn.svg
---
align: center
---
```

::::::

## Meer voorbeelden
In hoofdstuk 6.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden ook wringende momenten uitgerekend in voorbeeld 1 - 5. Negeer de berekeningen van stijfheden, spanningen en verplaatsingen.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 6.7, 6.8, 6.11, 6.13, 6.30 in hoofdstuk 4.5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Bepaal enkel de wringend momentenlijn en negeer de vragen over stijfheden, spanningen en verplaatsingen. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter6/) beschikbaar.