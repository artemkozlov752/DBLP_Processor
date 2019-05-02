# DBLP PARSER

## Description
This module implements the DBLP downloading in gz format, parse, convert it to pandas DataFrame and save
a pdf histogram of the amount of the books per year.

Main data link:

http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/dblp/dblp.xml.gz.

## How to launch main.py
```
1. create and source venv
2. cd DBLP_Processor
3. pip3.6 install -r requirements.txt
4. python3.6 main.py
```
## How to test the module
```
1. create and source venv
2. cd DBLP_Processor
3. pip3.6 install -r requirements.txt
4. python3.6 -m pytest tests/
```
## How to check logs
See `DBLP_Processor/logs/info.log`

## Result
The downloaded gz xml will be in the `DBLP_Processor/xml_data/dblp.xml.gz`

The result histogram will be in `DBLP_Processor/pictures/amount_per_year.pdf`
