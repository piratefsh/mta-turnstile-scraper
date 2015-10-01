# MTA Turnstile Data Scraper
Scrapes data from [MTA Turnstile data](http://web.mta.info/developers/turnstile.html) and dumps it into a SQLite database with matching column headers.

Supports older 2014 formats and converts them to the newer formats.

## Usage

```
python mta_main.py <db name> <start date: DD-MM-YYYY> <end date: DD-MM-YYYY>
```
Where <db name> is an empty database. Data will be added to a table `entries`.

### Example:

```
python mta_main.py mta_sept.db 01-09-2015 30-09-2015
```

## Output

```
id|CA|UNIT|SCP|STATION|LINENAME|DIVISION|DATE|TIME|DESC|ENTRIES|EXITS
1|A002|R051|02-00-00||||01-22-12|11:00:00|REGULAR|3483225|1203166
2|A002|R051|02-00-00||||01-22-12|15:00:00|REGULAR|3483361|1203211
3|A002|R051|02-00-00||||01-22-12|19:00:00|REGULAR|3483557|1203265
4|A002|R051|02-00-00||||01-22-12|23:00:00|REGULAR|3483662|1203286
5|A002|R051|02-00-00||||01-23-12|03:00:00|REGULAR|3483688|1203294
6|A002|R051|02-00-00||||01-23-12|07:00:00|REGULAR|3483699|1203328
7|A002|R051|02-00-00||||01-23-12|11:00:00|REGULAR|3483843|1203659
8|A002|R051|02-00-00||||01-23-12|15:00:00|REGULAR|3484060|1203733
9|A002|R051|02-00-00||||01-23-12|19:00:00|REGULAR|3484866|1203815
10|A002|R051|02-00-00||||01-23-12|23:00:00|REGULAR|3485128|1203846
```

