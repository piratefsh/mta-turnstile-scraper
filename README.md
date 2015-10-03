# MTA Turnstile Data Scraper
Scrapes data from [MTA Turnstile data](http://web.mta.info/developers/turnstile.html) and dumps it into a SQLite database with matching column headers.

Supports older 2014 formats and converts them to the newer formats.

## Usage

```

python mta_main.py <db name> <start date: YYYY-MM-DD> <end date: YYYY-MM-DD>
```

Where `<db name>` is an empty database. Will be created if does not exists, else will just append to existing database. Data will be added to a table `entries`.

### To create an empty SQLite database

```
$ sqlite3 test.db 
sqlite > .database
sqlite > .exit
```

And `test.db` should now exist in your directory

### Example:

```
python mta_main.py mta_sept.db 2015-09-01 2015-09-30
```

## Output

_Note: I converted the DATE column into a combined DATETIME column for ease of use_

Newer format.

```
id|CA|UNIT|SCP|STATION|LINENAME|DIVISION|DATETIME|TIME|DESC|ENTRIES|EXITS
1|A002|R051|02-00-00|LEXINGTON AVE|NQR456|BMT|2015-09-19 00:00:00|00:00:00|REGULAR|5317608|1797091
2|A002|R051|02-00-00|LEXINGTON AVE|NQR456|BMT|2015-09-19 04:00:00|04:00:00|REGULAR|5317644|1797096
3|A002|R051|02-00-00|LEXINGTON AVE|NQR456|BMT|2015-09-19 08:00:00|08:00:00|REGULAR|5317675|1797116
4|A002|R051|02-00-00|LEXINGTON AVE|NQR456|BMT|2015-09-19 12:00:00|12:00:00|REGULAR|5317778|1797215
5|A002|R051|02-00-00|LEXINGTON AVE|NQR456|BMT|2015-09-19 16:00:00|16:00:00|REGULAR|5318058|1797266
```

Older 2014 format. Note that Station, Linename and Division data is missing. Date format has also been formatted to be the same as newer format: `YYYY-MM-DD`.

```
id|CA|UNIT|SCP|STATION|LINENAME|DIVISION|DATETIME|TIME|DESC|ENTRIES|EXITS
1|A002|R051|02-00-00||||2010-04-18 08:00:00|08:00:00|REGULAR|2705436|929002
2|A002|R051|02-00-00||||2010-04-18 12:00:00|12:00:00|REGULAR|2705495|929054
3|A002|R051|02-00-00||||2010-04-18 16:00:00|16:00:00|REGULAR|2705657|929101
4|A002|R051|02-00-00||||2010-04-18 20:00:00|20:00:00|REGULAR|2705884|929137
5|A002|R051|02-00-00||||2010-04-19 00:00:00|00:00:00|REGULAR|2705901|929142
```

## Tests

Simple tests available for each source code file in the files themselves. Note `mta_db.py` needs a `test.db` to run tests.
