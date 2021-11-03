# UPA - projekt 01: Školství v ČR
## Repo
https://github.com/xligoc03/UPA/tree/master

## Autori
Alexadra Ligocká (xligoc03)\
Filip Pleško (xplesk02)

## Spustenie

### Požiadavky pred spustením
- `Docker`
- `Python 3` 

Projekt je písaný v programovacom jazyky `Python 3` spustitelný z `__main__.py`. Potrebné knižnice sú uvedené v súbore `requirements.txt` aj s príslušnými verziami.

Pred spustením projektu je potrebné Docker kontajner, v ktorom beží databáza.

```shell 
docker-compose up -d --build
```

Po spustení projektu, skripty skontrolujú, či sú dostupné datové sady. V prípade že nie, dáta si získaju z online zdrojov. Ďalej sú dátove sady spracované, pripravené na ďalšie použitie a uložené do databázy.

Príklad spustenia z koreňového adresára: 
```shell
export PYTHONPATH=$(pwd)
python3 src/__main__.py 
```

## Databáza
Pre riešenie projektu sme sa v zhľadom na štruktúru datových sad rozhodli použiť **MongoDB** databázu.

## Spracovanie datasetov

### Obyvateľstvo ČR

V tomto datasete sa nachádzali dáta v rôznich úrovňach agregácie. Z tohoto dôvodu sme pred uložením údajov do DB najskôr odstránili agregácie a ponechali iba najnižšu úroveň agregácie so zámerom zachovať čo najväčšie množstvo informácií a možnosť vytvárať vlastné agregácie neskôr. Taktiež sa v datasete nachádzali nepotrebné dáta ako napríklad *stapro_kod*, ktorý bol pre všetky údaje rovnaký a tak sme ho odstránili. Niektoré údaje boli popísané aj textom aj kódom, ktorý reprezentoval to isté ako text. Takéto duplicitné stĺpce sme zjednotili a ponechali iba jedno označenie.

### Školy v ČR

Dataset obshahujúci informácie o školách v Českej republike bol spracovaný pomocou [The ElementTree XML API](https://docs.python.org/3.9/library/xml.etree.elementtree.html). Z tohto datasetu boli získané informácie z rôznych úrovní podľa [štruktúry](https://rejstriky.msmt.cz/opendata/metadata/PopisVetyVrejskol.txt) dát. Dáta boli uložené do kolekcie `all_schools` a obsahujú informácie o názve školy, jej adrese, riaditeľovi a jeho adrese, ďalších objektoch prislúchajúcich k danej škole (napríklad školská jedáleň) a informácie o zriaďovateľovi. 

## Prepojenie dát

Použité dáta majú spoločnú oblasť v ČR pre ktorú boli zaznamenané a však každá datová sada obsahovala iný spôsob označenia tejto oblasti. Bolo potrebné preskúmať, ktoré označenie z jednej datovej sady odpovedá označeniu z druhej datovej sady a pred uložením do DB toto označenie zjednotiť.
