```{index} Matrix methode
```

# Apply matrix methode

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://oit.tudelft.nl/CTB2210/2025/matrix/theorie.html. Deze theorie is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% Source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/matrix


```
````


De matrixmethode is een methode om aan alle soorten constructies te rekenen en lijkt heel erg op de [verplaatsingenmethode op basis van vrijheidsgraden](./displacement_method2.md). Die verplaatsingenmethode had als nadeel dat de constructie wordt gesplitst in delen die allemaal verschillende vervormingsgedrag hebben. Dat maakt een dergelijke berekening arbeidsintensief. De matrixmethode lost dit op door standaardisatie van vrijheidsgraden en gesplitste delen. Daarnaast wordt de matrixmethode vaak direct in matrixformuleringen toegepast. Met deze twee aanpassingen vormt de matrixmethode een handige methode voor computerberekeningen.

## Theorie

### Beperking tot rotaties en knoopkoppels
In dit vak beperken we ons tot de toepassing van de matrixmethode op constructies waarin de rotatie van de knopen de enige vrijheidsgraad is (knopen kunnen niet verplaatsen) en er geen krachten tussen de knopen aangrijpen. Daarnaast modelleren we enkel starre verbindingen. De matrixmethode is echter ook toe te passen op constructies met meerdere vrijheidsgraden per knoop, op constructies met krachten tussen de knopen en scharnierende / verende verbindingen.

### Aantal vrijheidsgraden

Het eerste verschil van de matrixmethode met de verplaatsingenmethode is het aantal vrijheidsgraden. Waar bij de verplaatsingenmethode slechts enkele vrijheidsgraden worden gekozen, worden bij de matrixmethode de rotaties van alle knopen als vrijheidsgraden gekozen en daarbij het evenwicht van alle knopen in acht genomen. Daarbij worden alle rotaties en momenten in dezelfde richting genomen.

```{figure} ./matrix_data/verplaats_vs_matrix_dof.svg
---
align: center
---
Verplaatsingenmethode v.s. matrixmethode: bij de verplaatsingenmethode wordt slechts één rotatie gekozen als vrijheidsgraad, bij de matrixmethode worden alle rotaties gekozen als vrijheidsgraad, wat ook gepaard gaat met meer onbekende momenten. Per nieuwe vrijheidsgraad wordt er ook een nieuwe evenwichtsvergelijking opgesteld.
```

### Matrixformulering

Het tweede verschil is dat bij de matrixmethode het momentenevenwicht wordt opgeschreven in matrixformulering. Daarbij worden de evenwichtsvergelijkingen gesplitst in een stijfheidsterm $\mathbf{K}$ (factoren voor de $\varphi$'s) en een krachtterm $\mathbf{f}$ (losse termen).

$$
\begin{array}{cc}
\text{Verplaatsingenmethode} & \text{Matrixmethode} \\
\begin{aligned}
\sum M_{\rm{B}} &= 0 \\
\downarrow \\
k \cdot \varphi  &= f
\end{aligned}
&
\begin{aligned}
\sum M_{\rm{A}} &= 0 \\
\sum M_{\rm{B}} &= 0 \\
\sum M_{\rm{C}} &= 0 \\
\downarrow \\
\mathbf{K}
\begin{bmatrix}
\varphi_{\rm{A}} \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}}
\end{bmatrix}
&= \mathbf{f}
\end{aligned} \\
\end{array}
$$

Dit leidt tot een matrixformulering $\mathbf{K} \mathbf{u} = \mathbf{f}$. De termen in de globale stijfheidsmatrix $\mathbf{K}$ kunnen geïnterpreteerd worden als de rotatiestijfheid die elk element levert aan de aanliggende knopen. De termen in de krachtvector $\mathbf{f}$ kunnen geïnterpreteerd worden als de externe koppels die op de knopen werken. $\mathbf{u}$ is de verplaatsingsvector met de onbekende rotaties van de knopen.

### Directe opstelling van de stijfheidsterm
In plaats van met de hand elke momentevenwicht op te schrijven kunnen we de $\mathbf{K} \mathbf{u} = \mathbf{f}$ direct opstellen door de stijfheden van de individuele elementen bij elkaar op te tellen bij de bijbehorende knopen. Aangezien alle elementen er exact hetzelfde uitzien (een buigende staaf van nog onbekende lengte $L$ en buigstijfheid $EI$ met koppels op het uiteinde), kunnen we voor elk element dezelfde symbolische stijfheidstermen gebruiken. Daarbij houden we voor alle rotaties en momenten dezelfde richting (tegen de klok in) aan.

```{figure} ./matrix_data/staaf.svg
---
align: center
---
Standaard element in de matrixmethode

% originele figuur: ../verplaats2/matrix_data/Tekening1.vsdx
```

Voor dit standaardelement zullen we éénmaal de stijfheidstermen moeten vinden. Net als bij de verplaatsingenmethode kunnen we met de relaties vinden tussen de koppels en de rotaties van de uiteindes van een element door de rotaties los van elkaar toe passen. Voor elke individuele element met lengte $L$ en buigstijfheid $EI$ kunnen we de zogenoemde elementstijfheidsmatrix opstellen aan de hand van een vergeet-me-nietje:

```{figure} ./matrix_data/fmn.svg
---
align: center
---
Vergeet-me-nietje waarmee we de relatie tussen koppels en de rotaties van de uiteindes van een element beschreven kunnen worden. Komt overeen met vergeet-me-nietje (7) van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

% originele figuur: ../verplaats2/matrix_data/Tekening1.vsdx
```

Voor de relaties tussen de koppels en $\varphi_2$ kunnen we onderstaande model gebruiken, waarbij $T_1$ het oplegmoment is in het vergeet-me-nietje:

```{figure} ./matrix_data/rechts.svg
---
align: center
---
Snedekrachten ten gevolge van $\varphi_2$.

% originele figuur: ../verplaats2/matrix_data/Tekening1.vsdx
```

Het vergeet-me-nietje geeft dan:

$$
\begin{aligned}
\varphi_2 &= \cfrac{L \cdot T_2}{4 \cdot EI} \\
T_1 &= \cfrac{1}{2} \cdot T_2 \\
&\downarrow \\
T_1 &= \cfrac{2 \cdot EI}{L} \cdot \varphi_2 \\
T_2 &= \cfrac{4 \cdot EI}{L} \cdot \varphi_2 \\
\end{aligned}
$$

Voor de relaties tussen de koppels en $\varphi_1$ kunnen we onderstaande model gebruiken, waarbij $T_2$ het oplegmoment is in het vergeet-me-nietje:

```{figure} ./matrix_data/links.svg
---
align: center
---
Snedekrachten ten gevolge van $\varphi_1$.
% originele figuur: ../verplaats2/matrix_data/Tekening1.vsdx
```

Dit geeft:

$$
\begin{aligned}
\varphi_1 &= \cfrac{L \cdot T_1}{4 \cdot EI} \\
T_2 &= \cfrac{1}{2} \cdot T_1 \\
&\downarrow\\
T_1 &= \cfrac{4 \cdot EI}{L} \cdot \varphi_1 \\
T_2 &= \cfrac{2 \cdot EI}{L} \cdot \varphi_1 \\
\end{aligned}
$$

Samen geeft dit twee vergelijkingen:

$$
\begin{aligned}
T_1 &= \cfrac{4 EI}{L} \cdot \varphi_1 + \cfrac{2 EI}{L} \cdot \varphi_2 \\
T_2 &= \cfrac{2 EI}{L} \cdot \varphi_1 + \cfrac{4 EI}{L} \cdot \varphi_2 \\
\end{aligned}
$$

Deze kunnen samen geschreven worden in een elementstijfheidsmatrix:

$$
\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}
$$

Welke vermenigvuldigd met de verplaatsingsvector $\mathbf{u^{\rm{(e)}}} = \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix}$ de koppels in de krachtvector $\mathbf{f^{\rm{(e)}}} = \begin{bmatrix} T_1 \\ T_2  \end{bmatrix}$ geeft.

De individuele termen van deze standaard elementstijfheidsmatrix kunnen we voortaan direct gebruiken. Dat doen we door deze op te tellen in de globale stijfheidsmatrix $\mathbf{K}$, waarbij de index van de rijen en kolommen overeen moeten komen met de uiteindes van de elementen.

$$
\begin{aligned}
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
\qquad
\rightarrow
\qquad
\begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\varphi_1 \\
\varphi_2 \\
\vdots \\
\varphi_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
\\
&\vdots \\
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
\end{aligned}
$$

### Directe opstelling van de krachtterm
Aangezien in de krachtvector alle losse koppels uitkwamen, kunnen we de externe koppels en oplegmomenten ook direct opstellen. Net als de stijfheden kunnen we dit direct doen zonder expliciet de evenwichtsvergelijkingen uit te schrijven. We hoeven enkel de externe koppels en oplegmomenten toe te voegen op de juiste plek in de krachtvector.

$$
\begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\varphi_1 \\
\varphi_2 \\
\vdots \\
\varphi_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
\leftarrow
\begin{matrix}
\text{Uitwendige koppels} \\
\text{Oplegmomenten}
\end{matrix}
$$

### Stappenplan

De stappen van de matrixmethode zijn als volgt:

::::::{prf:algorithm} Matrixmethode
:nonumber: true
:label: matrixmethode_algoritme

1. Bepaal de vrijheidsgraden (rotaties). Dit vormt de onbekende verplaatsingsvector $ \mathbf{u} =  \begin{bmatrix}  \varphi_1 \\  \varphi_2 \\ \vdots \\ \varphi_n  \end{bmatrix} $
2. Initialiseer het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{f}$ met een nulmatrix voor $\mathbf{K}$ en -vector $\mathbf{f}$.
3. Bepaal voor elk element de elementstijfheidsmatrix $\left(\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}\right)$ en voeg deze toe aan de globale stijfheidsmatrix $\mathbf{K}$ voor de bijbehorende knopen.
4. Construeer de globale krachtvector $\mathbf{f}$ door de externe krachten(koppels) toe te voegen voor de bijbehorende knopen.
5. Voeg de zowel de voorgeschreven vrijheidsgraden (rotaties) als de onbekende oplegreacties (oplegmomenten) toe aan het stelsel van vergelijkingen.
6. Los het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{f}$ op voor de onbekende vrijheidsgraden (rotaties) in $\mathbf{u}$.

::::::

## Voorbeeld

De toepassing van deze matrixmethode op een statisch onbepaalde constructie wordt in een voorbeeld getoond.

::::::{prf:example}
:nonumber: true
:label: matrix_0

```{figure} ./matrix_data/voorbeeld.svg
---
align: center
---
Voorbeeldconstructie, $EI = 4290 \ \rm{kNm}^2, EA >> EI$
```

::::::

1. Bepaal de vrijheidsgraden (rotaties). Dit vormt de onbekende verplaatsingsvector $ \mathbf{u} =  \begin{bmatrix}  \varphi_1 \\  \varphi_2 \\ \vdots \\ \varphi_n  \end{bmatrix} $

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_1

    Voor deze construtie zijn er drie knopen, dit geeft als verplaatsingsvector: $ \mathbf{u} =  \begin{bmatrix}  \varphi_A \\  \varphi_B \\  \varphi_C  \end{bmatrix} $

    Waarbij we de rotaties rechtsom / met de klok mee als positief nemen.

    ::::::

2. Initialiseer het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{f}$ met een nulmatrix voor $\mathbf{K}$ en -vector $\mathbf{f}$.


    ::::::{prf:example}
    :nonumber: true
    :label: matrix_2

    Dit geeft voor onze constructie een 3×3 matrix voor $\mathbf{K}$ en een 3×1 vector voor $\mathbf{f}$:
    
    $$
    \begin{bmatrix}
    0 & 0 & 0 \\
    0 & 0 & 0 \\
    0 & 0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}} \\
    \varphi_{\rm{C}}
    \end{bmatrix}
    = 
    \begin{bmatrix}
    0 \\
    0 \\
    0
    \end{bmatrix}
    $$

    ::::::

3. Bepaal voor elk element de elementstijfheidsmatrix $\left(\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}\right)$ en voeg deze toe aan de globale stijfheidsmatrix $\mathbf{K}$ voor de bijbehorende knopen.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_3

    Voor element $\rm{AB}$ met lengte $5 \ \rm{m}$ wordt de elementstijfheidsmatrix:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{AB}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{5} & \cfrac{2 \cdot 4290}{5} \\ \cfrac{2 \cdot 4290}{5} & \cfrac{4 \cdot 4290}{5}  \end{bmatrix} = \begin{bmatrix} 3432 & 1716 \\ 1716 & 3432  \end{bmatrix} 
    $$

    Deze kunnen we direct invullen in de globale stijfheidsmatrix $\mathbf{K}$. De knopen $\rm{A}$ en $\rm{B}$ komen overeen met de eerste en tweede rij en kolom van de globale stijfheidsmatrix. Dit geeft:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    3432 & 1716 & 0 \\
    1716 & 3432 & 0 \\
    0 & 0 & 0
    \end{bmatrix}
    $$

    Voor element $\rm{BC}$ met lengte $6.6 \ \rm{m}$ wordt de elementstijfheidsmatrix:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{BC}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{6.6} & \cfrac{2 \cdot 4290}{6.6} \\ \cfrac{2 \cdot 4290}{6.6} & \cfrac{4 \cdot 4290}{6.6}  \end{bmatrix} = \begin{bmatrix} 2600 & 1300 \\ 1300 & 2600  \end{bmatrix}
    $$

    Ook deze kunnen we direct invullen in de globale stijfheidsmatrix $\mathbf{K}$. De knopen $\rm{B}$ en $\rm{C}$ komen overeen met de tweede en derde rij en kolom van de globale stijfheidsmatrix. Dit geeft:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    3432 & 1716 & 0 \\
    1716 & 6032 & 1300 \\
    0 & 1300 & 2600
    \end{bmatrix}
    $$

    Tot slot voegen we element $\rm{AC}$ met lengte $10.4 \ \rm{m}$ toe. De elementstijfheidsmatrix is:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{AC}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{10.4} & \cfrac{2 \cdot 4290}{10.4} \\ \cfrac{2 \cdot 4290}{10.4} & \cfrac{4 \cdot 4290}{10.4}  \end{bmatrix} = \begin{bmatrix} 1650 & 825 \\ 825 & 1650  \end{bmatrix}
    $$

    Ook deze kunnen we direct invullen in de globale stijfheidsmatrix $\mathbf{K}$. De knopen $\rm{A}$ en $\rm{C}$ komen overeen met de eerste en derde rij en kolom van de globale stijfheidsmatrix. Dit geeft:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    5082 & 1716 & 825 \\
    1716 & 6032 & 1300 \\
    825 & 1300 & 4250
    \end{bmatrix}
    $$

    ::::::

4. Construeer de globale krachtvector $\mathbf{f}$ door de externe krachten (koppels) toe te voegen voor de bijbehorende knopen.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_4

    Er is één extern koppel van $209.924 \ \rm{kNm}$ dat op knoop $\rm{B}$ werkt. Deze werkt rechtsom / met de klok mee en is dus een positief koppel in onze krachtvector. Dit geeft:

    $$
    \mathbf{f} =
    \begin{bmatrix}
    0 \\
    209.924 \\
    0
    \end{bmatrix}
    $$
    ::::::

5. Voeg de zowel de voorgeschreven vrijheidsgraden (rotaties) als de onbekende oplegreacties (oplegmomenten) toe aan het stelsel van vergelijkingen.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_5

    In knoop $\rm{C}$ is de rotatie voorgeschreven als $\varphi_{\rm{C}} = 0$. Dit voegen we toe aan het stelsel van vergelijkingen door de tweede rij inclusief het onbekende oplegmoment in $\rm{C}$ die we positief aannemen:

    $$
    \begin{bmatrix}
    5082 & 1716 & 825 \\
    1716 & 6032 & 1300 \\
    825 & 1300 & 4250
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}} \\
    0
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    209.924 \\
    M_{\rm{C}}
    \end{bmatrix}
    $$

    :::::: 

6. Los het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{f}$ op voor de onbekende vrijheidsgraden (rotaties) in $\mathbf{u}$.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_6

    Alleen de eerste en tweede rij zijn relevant voor het oplossen van de onbekende rotaties. We kunnen dus de derde rij en kolom weglaten en de vergelijking herschrijven als:

    $$
    \begin{bmatrix}
    5082 & 1716 \\
    1716 & 6032
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}}
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    209.924
    \end{bmatrix}
    $$

    Dit geeft:
    - $\varphi_{\rm{A}} = -0.0013 \ \rm{rad}$
    - $\varphi_{\rm{B}} = 0.0385 \ \rm{rad}$

## Instructies in collegevorm

Dit onderwerp is [in constructiemechanica 3, 2025-2026, les 12](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/c2f0f9c684ed46848b6a754b76f1f92f1d?academicYear=2025-2026-ctb2210) gepresenteerd in collegevorm tot 0:43:10.

## Meer voorbeelden
In hoofdstuk 5 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt de matixmethode behandeld. In hoofdstuk 5.5 is de stof van voorbeeld 1 na het bepalen van de $\varphi$'s geen onderdeel van het vak. Dat geldt ook voor voorbeeld 1 in hoofdstuk 5.6.1 na het bepalen van de $\varphi$'s. Daarnaast worden hoofdstuk 5.5.2 en 5.7 niet behandeld.

## Oefeningen
Opgaves 5.1 - 5.5 in hoofdstuk 5.8 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. De opgaves e - i zijn geen onderdeel van het vak. Vervang bij opgave 5.2 - 5.5 het uitkragende gedeelte door een koppel en neem de dwarskracht niet mee. Er zijn helaas geen antwoorden beschikbaar. Je kan de constructies doorrekenen met MatrixFrame om je antwoorden te controleren.