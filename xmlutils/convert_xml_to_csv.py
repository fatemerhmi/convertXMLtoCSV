import xml.etree.ElementTree as ET
import re 
import os
import pandas as pd
import click
import collections

# Enable click
os.environ['LC_ALL'] = 'C.UTF-8'
os.environ['LANG'] = 'C.UTF-8'

def getfilename(xml_file):
    # print(xml_file)
    x = re.search("[ \w-]+?(?=\.)", xml_file)
    # print(x.group())
    return x.group()

@click.command()
@click.argument('xml_file')
@click.option('-o','--output-dir', type=click.Path(exists=True, resolve_path=True), default ="./" , 
            help='Path to the output directory.')
@click.option('-c', "--column-based", type=str, default = "attrib" ,
            help="'attrib' for setting attributes as columns, 'tag' for setting tags as columns." )
# sample 1: -c attrib
@click.option('-a', '--attrib', type = str, default = "" ,
            help = "The attribute name that its value is going to be the column names." )
# sample 1: -a name
def main(xml_file,output_dir, column_based, attrib):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except FileNotFoundError as fnf_error:
        raise RuntimeError(fnf_error)

    ########## Finding column names ############
    columns = []
    if column_based == "attrib":
        for child in root:
            for item in child:
                columns.append(item.attrib[attrib])
            break
    elif column_based == "tag":
            print(child.tag)
    else:
        raise Exception("Only attrib and tag are valid values for --column-based option.")
    
    print("column names are:", columns)

    ########### Create csv file #########
    xml_df = pd.DataFrame(columns = columns)
    for child in root:
        row = collections.OrderedDict()
        for item in child:
            row[item.attrib[attrib]: item.text]
        xml_df = xml_df.append(row,ignore_index=True)

    topic_df.to_csv(getfilename(xml_file) + ".csv", index=False) 

if __name__ == "__main__":
    main()
