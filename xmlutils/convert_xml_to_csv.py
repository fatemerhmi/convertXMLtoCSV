import xml.etree.ElementTree as ET
import re 
import os
import pandas as pd
import click

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
            help="'attrib' for setting attributes as columns, 'tag' for setting tags as columns" )
def main(xml_file,output_dir, column_based):
    print(output_dir)
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ########## Finding column names ############
    columns = []
    if column_based == "attrib":
        for child in root:
            print(child.attrib)
    elif column_based == "tag":
            print(child.tag)
    else:
        raise RuntimeError("Only attrib and tag are valid values for --column-based option.")
    topic_df = pd.DataFrame(columns = columns)
    # for child in root:
    #     no = child.attrib['number']
    #     topic_df = topic_df.append({child.tag : child.attrib['number'], child[0].tag : child[0].text ,child[1].tag : child[1].text , child[2].tag : child[2].text},ignore_index=True)

    # topic_df.to_csv(getfilename(xml_file) + ".csv", index=False) 

if __name__ == "__main__":
    main()
