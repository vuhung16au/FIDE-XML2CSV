# FIDE XML to CSV

Write a program to convert FIDE ratings files from XML format to CSV format 

Input files 
```
blitz_rating_list.xml
players_list_xml_foa.xml
rapid_rating_list.xml
standard_rating_list.xml
```

Output files 
```
blitz_rating_list.csv
players_list_xml_foa.csv
rapid_rating_list.csv
standard_rating_list.csv 
```

When converting from XML to CSV, 
mapping 1-to-1 from all XML elements to CSV fields. 

Include headers in CSV files. 

# FIDE XML to CSV (Aus)

Write a Python function:

- Function name: 
def xml_to_csv_country(xml_file, csv_file, country = "AUS"):

This function will extract all player with "country" param equals to <country> element in XML file. 

When the param "country" = "ALL", extract all the countries. 

Input files 
```
blitz_rating_list.xml
players_list_xml_foa.xml
rapid_rating_list.xml
standard_rating_list.xml
```

Output files 
```
blitz_rating_list_aus.csv
players_list_xml_foa_aus.csv
rapid_rating_list_aus.csv
standard_rating_list_aus.csv 
```



