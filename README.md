# smdb-rdf

Detta är ett program för att samla ihop RDF-filer (XML) från
[Svensk mediedatabas (SMDB)](https://smdb.kb.se/)
och skapa en .csv-fil. Denna .csv-fil funkar bra att importera i
exempelvis Excel eller Google Docs.

Resultatet är alltså en TV-tablå i Excel-format.

Programmet är skrivet i Python. Jag har använt Python 2.7.10 (Mac). Jag har använt det för åren 1981-1985; om RDF-filernas information är strukturerad annorlunda kan programmet ge oväntade resultat.

---

**OBSERVERA:**
Detta program laddar endast ner _mediebeskrivningar_, inte TV-program.
Själva TV-programmen skyddas av upphovsrätt och kan inte laddas ner från nätet.

---

Programmet körs i tre steg. Nedladdningen görs för ett år i taget. Här används
år 1982 som exempel.

### 1. Ladda ner RDF-filerna för alla SMBD:s inspelningar det året

```python
python stage1.py 1982
```

Det skapas en katalog som heter `rdf-1982` med filer. Det tar en stund att göra detta (ungefär en halvtimme med en bra nätförbindelse).

### 2. Ladda ner RDF-filer för de individuella TV-programmen

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
