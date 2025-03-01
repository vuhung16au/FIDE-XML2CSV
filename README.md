# What is this

This tool convert FIDE's rating in XML format to CSV format with an option of choosing a country (Federation) when converting.

# How to run

## Prepare FIDE XML files
- Download FIDE rating files (FOA, Standard, Rapid, Blitz) and put in this folder and extract the zip files. (ref. https://ratings.fide.com/download_lists.phtml)
- Adjust/Change the federation if you wish 
- Run `FIDE-XML2CSV.py` 

## Input filenames
```
blitz_rating_list.xml
players_list_xml_foa.xml
rapid_rating_list.xml
standard_rating_list.xml
```

## Output filenames 

(All countries)
```
standard_rating_list.csv
rapid_rating_list.csv
players_list_xml_foa.csv
blitz_rating_list.csv
```

(Country specific if you set)
```
standard_rating_list_aus.csv
rapid_rating_list_aus.csv
players_list_xml_foa_aus.csv
blitz_rating_list_aus.csv
```

# Legends
(ref. https://ratings.fide.com/download_lists.phtml)
```
Legend:

STD/SRTNG - Standard rating
RPD/RRTNG - Rapid rating
BLZ/BRTNG - Blitz rating
SGM - number of STANDARD rated games in given period
RGM - number of RAPID rated games in given period
BGM - number of BLITZ rating games in given period
SK - STANDARD rating K factor
RK - RAPID rating K factor
BK - BLITZ rating K factor
B-day/BORN - year of birth of a player
ID NUMBER - identification number of a player within FIDE database
NAME - name of a player
TIT/TITL - title of a player (g - Grand Master, wg - Woman Grand Master, m - Interntional Master, wm - Woman International Master, f - FIDE Master, wf - Woman FIDE Master, c - Candidate Master, wc - Woman Candidate Master)
FED - Federation of a player
OTIT - Other titles of a player which may include (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)
FLAG - flag of inactivity (I - inactive, WI - woman inactive, w - woman)
SEX - sex of a player (M - male, F - female)
```

# CSV File Fields

- fideid: FIDE ID
- name: Player name
- country: Country/Federation
- sex: Male/Female
- title: FIDE title (GM, IM, FM)
- w_title: FIDE woman title
- o_title: Other titles, non-playing roles. Example: IA, FT, IO (Arbiter, Trainer, Organizer)
- foa_title: FIDE Online Arena title, online chess achievements. AGM, AIM, AFM, ACM...
- rating: Rating standard
- rapid_rating:
- blitz_rating: 
- games: Number of standard games playged
- rapid_games: 
- blitz_games:
- k: Standard rating k-factor 
- rapid_k: 
- blitz_k:
- birthday: Year of birth (FIDE may store players' full DoB internally)
- flag: See `FLAG` above

# Converted Data (2025/03)

https://drive.google.com/drive/folders/1X-D1Z9BhMRndCcNyX4FyorOv8MYv94th

## Aus standard
https://docs.google.com/spreadsheets/d/1JQ7qY7K7A17QOQtARM-b6opf3LZAljA35xVi31VCJGE/edit?gid=339730930#gid=339730930

## Aus rapid
https://docs.google.com/spreadsheets/d/1T9lf1stS16-W8jawHegBjsO3xBHIpMtFnb81-RCMNgs/edit?gid=1965181498#gid=1965181498

## Aus blitz
https://docs.google.com/spreadsheets/d/1tn0TOONOoy7oCzM-q1Z0CLsz8Uk4ITFrqVIakUrSVEQ/edit?gid=2139845551#gid=2139845551

## Aus all data
https://docs.google.com/spreadsheets/d/1r3JmkDkXvV1mfJb2_r-kDysrVX0JU9E_VYrtmzKTnNY/edit?gid=605640874#gid=605640874