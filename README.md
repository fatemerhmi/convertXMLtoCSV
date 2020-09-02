# convertXMLtoCSV
This project is under construction :)

This is a simple tool to convert your xml file to csv file. This scripts uses [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html). The medium post cooresponding to this library is also available. 

* Fatemeh Rahimi, Sep 2020
* link to medium (coming soon)

You can either use the python command itself for running the script or use the CLI tool. 

## installation
1. clone the repo
`git clone giturl`
change your directory to the convertXMLtoCSV directory. 

**Usage:**      
Sample1:       
`python3 xmlutils/convert_xml_to_csv.py samples/sample1.xml -c attr -v text -a name -o samples/`

sample2:    
`python3 xmlutils/convert_xml_to_csv.py samples/sample2.xml -c tag -v text -o samples/`

sample3:    
`python3 xmlutils/convert_xml_to_csv.py samples/sample3.xml -c tag -v text -o samples/`

2. using pip       
after cloning the repo, install it with pip     
`pip install .`     
Now you can use this CLI tool through your command line. 

**Usage:**     
sample1:      
`convertxmltocsv samples/sample1.xml -c attr -v text -a name -o samples/`

sample2:      
`convertxmltocsv samples/sample2.xml -c tag -v text -o samples/`
     
sample3:      
`convertxmltocsv samples/sample3.xml -c tag -v text -o samples/`

3. Running the samples:
