#!E:\Skripsi\SPlantStructure\flask\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rdflib==4.2.0','console_scripts','rdf2dot'
__requires__ = 'rdflib==4.2.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rdflib==4.2.0', 'console_scripts', 'rdf2dot')()
    )
