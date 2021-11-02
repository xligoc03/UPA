# UPA - projekt 01: Školství v ČR

## Autori:
Alexadra Ligocká (xligoc03)\
Filip Pleško (xplesk02)

## Spustenie
Projekt je písaný v Python spustitelný z `__main__.py`.

Po spustení projektu, skripty skontrolujú, či sú dostupné datové sady. V prípade že nie, dáta si získaju z online zdrojov. Ďalej sú dátove sady spracované, pripravené na  ďalšie použitie a uložené do databázy.

## Databáza
Pre riešenie projektu sme sa v zhľadom na štruktúru datových sad rozhodli použiť **MongoDB** databázu.

## Spracovanie datasetov

### Obyvateľstvo ČR

V tomto datasete sa nachádzali dáta v rôznich úrovňach agregácie. Z tohoto dôvodu sme pred uložením údajov do DB najskôr odstránili agregácie a ponehali iba najnižšu úroveň agregácie so zámerom zachovať čo najväčšie množstvo informácií a možnosť vytvárať vlastné agregácie neskôr. Taktiež sa v datasete nachádzali nepotrebné dáta ako napríklad *stapro_kod*, ktorý bol pre všetky údaje rovnaký a tak sme ho odstránili. Niektoré údaje boli popísané aj textom aj kódom, ktorý reprezentoval to isté ako text. Takéto duplicitné stĺpce sme zjednotili a ponehali iba jedno označenie.

### Školy v ČR

## Prepojenie dát

Použité dáta majú spoločnú oblasť v ČR pre ktorú boli zaznamenané a však každá datová sada obsahovala iný spôsob označenia tejto oblasti. Bolo potrebné preskúmať, ktoré označenie z jednej datovej sady odpovedá označeniu z druhej datovej sady a pred uložením do DB toto označenie zjednotiť.