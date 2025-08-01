```{index} Temperature influences; for statically indeterminate structures
```
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

In hoofdstuk 4.12 van het boek Mechanica: spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt de afleiding van temperatuursinvloeden behandeld. In hoofdstuk 6.2.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` is deze versimpeld herhaald voor statisch bepaalde constucties. De aanpak met de momentenvlakstelling wordt niet behandeld in dit vak. Daarnaast worden de standaardgevallen voor een ligger op twee steunpunten en een ingeklemde ligger niet gebruikt. In hoofdstuk 6.2.2 worden statisch onbepaalde constructies behandeld. Ook hier geldt dat de momentenvlakstelling geen onderdeel is van dit vak

## Oefeningen
- Opgaves 6.25 - 6.30, 3.32 - 6.39, 6.41 - 6.43 in hoofdstuk 6.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Er zijn helaas geen antwoorden beschikbaar.