# smdb-rdf

Samlar ihop RDF-filer (XML) från [Svensk mediedatabas (SMDB)](https://smdb.kb.se/) och skapar en .csv-fil, som kan importeras till exempelvis Excel eller Google Docs.

Programmet körs i tre steg. Nedladdningen görs för ett år i taget. Här används år 1981 som exempel.

### 1. Ladda ner RDF-filerna för alla SMBD:s inspelningar det året.

```python
python stage1.py 1981
```

Det skapas en katalog som heter "rdf-1981".

### 2. Ladda ner RDF-filer för de individuella TV-programmen. 

```python
python stage2.py rdf-1981/*.rdf
```

Det skapas nu underkataloger i "rdf-1981" för var och en av inspelningarna, och i dessa kataloger placeras RDF-filer för respektive TV-program. Exempel:

* rdf-1981
  * 001697919
    * 1.rdf
    * 2.rdf
    * 3.rdf
    * ...
  * ...

### 3. Skapa en .csv-fil utifrån de nedladdade RDF-filerna. 

```python
python stage3.py rdf-1981/  > 1981.csv
```

Det ska nu finnas en fil som heter "1981.csv" och kan importeras till Excel eller Google Docs.  
