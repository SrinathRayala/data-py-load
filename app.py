import sys
from utils import get_tables, load_db_details
from read import read_table
from write import load_table

def main():
    print("Docker Test")
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables=get_tables('tables_list')
    for table_name in tables['table_name']:
        data,column_names = read_table(db_details,table_name)
        load_table(db_details, data, column_names, table_name)

if __name__ == '__main__':
    main()
