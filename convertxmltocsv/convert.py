import xml.etree.ElementTree as ET
import re 
import os
import pandas as pd
import click
import collections

# import convertxmltocsv

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
@click.option('-c', "--column-based", type=str, default = "attr" ,
            help="'attr' for setting attributes as columns, \
            'tag' for setting tags as columns." )
@click.option('-v', "--value", type = str, default = "text",
            help="'tag' for settting tag as a column value,  \
            'text' for setting text as the column value, \
            'attr' for settting attrib for a column value")
@click.option('-a', '--attr', type = str , default = "",
            help = "The attribute name that its value is going to be the column names or values." )
def main(xml_file,output_dir, column_based, value, attr):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except FileNotFoundError as fnf_error:
        raise RuntimeError(fnf_error)

    ########## Finding column names ############
    columns = []
    if column_based == "attr":
        for child in root:
            for item in child:
                columns.append(item.attrib[attr])
            break
    elif column_based == "tag":
        for child in root:
            for item in child:
                columns.append(item.tag)
            break
            # print(child.tag)
    else:
        raise Exception("Only 'attr' and 'tag' are valid values for --column-based option.")
    
    print("column names are:", columns)

    ########## Create csv file #########
    xml_df = pd.DataFrame(columns = columns)
    if value == "text" and column_based == "attr":
        for child in root:
            row = collections.OrderedDict()
            for item in child:
                row[item.attrib[attr]]= item.text
            xml_df = xml_df.append(row,ignore_index=True)
    elif value == "text" and column_based == "tag":
        for child in root:
            row = collections.OrderedDict()
            for item in child:
                row[item.tag]= item.text
            xml_df = xml_df.append(row,ignore_index=True)

    xml_df.to_csv(output_dir + '/'+ getfilename(xml_file) + ".csv", index=False) 

if __name__ == "__main__":
    main()
