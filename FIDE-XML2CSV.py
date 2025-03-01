import csv
import xml.etree.ElementTree as ET

# 
def xml_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract headers from XML elements
    headers = [elem.tag for elem in root[0]]

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # Write headers

        for child in root:
            row = [child.find(header).text if child.find(header) is not None else '' for header in headers]
            writer.writerow(row)

# List of input and output files
files = [
    ("blitz_rating_list.xml", "blitz_rating_list.csv"),
    ("players_list_xml_foa.xml", "players_list_xml_foa.csv"),
    ("rapid_rating_list.xml", "rapid_rating_list.csv"),
    ("standard_rating_list.xml", "standard_rating_list.csv")
]

# Convert each XML file to CSV
# Comment out the following line to avoid converting the files
# for xml_file, csv_file in files:
#     xml_to_csv(xml_file, csv_file)

def xml_to_csv_country(xml_file, csv_file, country="ALL"):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract headers from XML elements
    headers = [elem.tag for elem in root[0]]

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # Write headers

        for child in root:
            player_country = child.find('country').text if child.find('country') is not None else ''
            if country == "ALL" or player_country == country:
                row = [child.find(header).text if child.find(header) is not None else '' for header in headers]
                writer.writerow(row)

# List of input files
input_files = [
    "blitz_rating_list.xml",
    "players_list_xml_foa.xml",
    "rapid_rating_list.xml",
    "standard_rating_list.xml"
]

# Convert each XML file to CSV with country filter
for xml_file in input_files:
    xml_to_csv_country(xml_file, f"{xml_file.split('.')[0]}_ALL.csv", country="ALL")
    xml_to_csv_country(xml_file, f"{xml_file.split('.')[0]}_AUS.csv", country="AUS")