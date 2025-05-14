```{index} Statisch onbepaaldheid
```
# Statisch onbepaaldheid

```{figure} ./determinancy_data/image.png
:align: center
:width: 300

Figure 4.50 {cite:ts}`Hartsuijker1999`
```

Een constructie is statisch onbepaald wanneer deze niet meer enkel met evenwichtsvergelijkingen kan worden opgelost. Er kan hierbij onderscheid worden gemaakt tussen:
- Enkel oplegreacties kunnen worden bepaald (uitwendig statisch bepaald)
- Inwendige krachten kunnnen worden bepaald (inwendig statisch bepaald)

Deze twee categorieën worden samen behandeld in hoofdstuk 4.5.2 en 4.5.3 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Voor [vakwerken](truss_structures) is de analyse versimpeld zoals beschreven in hoofdstuk 9.2.2 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Alhoewel de getoonde vergelijkingen met $r$, $v$ en $e$ effectief kunnen zijn bij simpele constucties, leiden deze in het algemeen tot verkeerde resultaten. De aanpak zoals beschreven in hoofdstuk 4.5.4 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999` is effectief voor alle constructies:

Voor de berekening van uitwendig statisch onbepaaldheid:
1. Teken het vrijlichaamsschema van zo groot mogelijke, vormvast, scharnierend verbonden delen van de constructie. In de scharnierende verbinden werken twee onbekende krachten: horizontaal en verticaal.
1. Tel het aantal onbekende krachten $r$ + $v$: de oplegreacties en verbindingskrachten in de scharnieren
1. Tel het evenwichtsvergelijkingen $e$: 3 evenwichtsvergelijkingen per vormvaste deel van de constructie
1. De graad van statisch onbepaladheid is $r$ + $v$ - $e$.

Voor de berekening van inwendig statisch onbepaaldheid:
1. Splits constructie in alle losse knopen en en elementen
1. Teken het vrijlichaamsschema voor elementen
   - Op een algemene staaf werken op de uiteindes een normaalkracht, dwarskracht en moment
   - Op een pendelstaaf werken op de uiteindes enkel een normaalkracht
1. Teken het vrijlichaamsschema voor de knopen: teken de reactiekrachten op de knopen ten gevolge van de krachten op de uiteindes van de staven en de oplegreacties
1. Tel het aantal onbekende krachten: oplegreacties en koppeltjes van staafkrachten
1. Tel het aantal 

## Opgaves
- Als je een student bent uit Delft, kan je oefenen met de volgende [<img height="12px" src="../images/ANS.svg" alt="ANS"> opgaves](https://ans.app/digital_test/assignments/1091576/results/new).
- Opgaves 4.11 - 4.22, van hoofdstuk 4 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Opgave  9.6, van hoofdstuk 9 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).
