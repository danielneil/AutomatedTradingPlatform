#!/usr/bin/python3

import argparse
import sys
import os

from pydrill.client import PyDrill

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin runs sql code against Apache Drill - only used for testing, and only expects a single row to be returned."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-s", "--sql", help="SQL code to execute")

    args = parser.parse_args()

    if not args.sql:
        print ("UNKNOWN - You were supposed to give me some SQL")
        sys.exit(UNKNOWN)

    drill = PyDrill(host='localhost', port=8047) 

    if not drill.is_active():
        print("Drill doesn't seem to be active")
        sys.exit(CRITICAL)

    drill_result = drill.query(args.sql)
    
    df = drill_result.to_dataframe()
    
    # Get a count of the number of rows.
    index = df.index
    number_of_rows = len(index)
        
    if number_of_rows == 1:
        print("Connected to Drill and a single row was returned")
        sys.exit(OK)          
    else:
        print("Connected to Drill, but we only expected a single row, this is bad...")
        sys.exit(CRITICAL)      
