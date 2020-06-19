import sys
from config import DB_DETAILS

def main():
    print("Docker Test")
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

    for arg in sys.argv:
        print(arg)
if __name__ == '__main__':
    main()
