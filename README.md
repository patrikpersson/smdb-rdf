# smdb-rdf

Detta är ett program för att samla ihop RDF-filer (XML) från
[Svensk mediedatabas (SMDB)](https://smdb.kb.se/)
och skapa en .csv-fil. Denna .csv-fil funkar bra att importera i
exempelvis Excel eller Google Docs.

Resultatet är alltså en TV-tablå (eller radiotablå) i Excel-format.

Programmet är skrivet i Python. Jag har använt Python 2.7.10 (Mac). Jag har använt det för åren 1981-1985; om RDF-filernas information är strukturerad annorlunda kan programmet ge oväntade resultat.

---

**OBSERVERA:**
Detta program laddar endast ner _mediebeskrivningar_, inte TV- eller radioprogram.
Själva TV- och radioprogrammen skyddas av upphovsrätt och kan inte laddas ner från nätet.

---

Programmet körs i tre steg. Nedladdningen görs för ett år i taget. Här används
TV-program för år 1982 som exempel. Hur man istället laddar ner information om radioprogram beskrivs på slutet av sidan.

### 1. Ladda ner RDF-filerna för alla SMBD:s TV-inspelningar det året

```python
python stage1.py 1982
```

Det skapas en katalog som heter `rdf-1982` med filer. Det tar en stund att göra detta (ungefär en halvtimme med en bra nätförbindelse).

### 2. Ladda ner RDF-filer för de individuella programmen

```python
python stage2.py rdf-1982/*.rdf
```

Det skapas nu underkataloger i `rdf-1982` för var och en av inspelningarna,
och i dessa kataloger placeras RDF-filer för respektive TV-program. Exempel:

* rdf-1982/
  * ...
  * 001697919.rdf
  * 001697919/
    * 1.rdf
    * 2.rdf
    * 3.rdf
    * ...
  * ...

Även detta steg tar en stund (omkring en timme).

### 3. Skapa en .csv-fil utifrån de nedladdade RDF-filerna

```python
python stage3.py rdf-1982/  > 1982.csv
```

Denna konvertering tar mindre än en minut. Därefter ska det finnas en fil som
heter `1982.csv` och kan importeras i Excel eller Google Docs.  

## Ladda ner information om radioprogram

Instruktionerna ovan används för att skapa en TV-tablå. Om man istället vill ladda ner information om radioprogram kan man (i det första steget) skriva

```python
python stage1.py -radio 1982
```

Då heter den skapade katalogen istället `rdf-radio-1982`. I de följande stegen är det den katalogen man hänvisar till, istället för `rdf-1982`.
