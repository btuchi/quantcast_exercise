import sys
from cookie_log_parser import CookieLogParser

def main():
    # check if the command line offers correct amount of arguments
    if len(sys.argv) != 4 or sys.argv[2] != '-d':
        print("Usage: ./most_active_cookie <file_path> -d <date>")
        sys.exit(1)
    

    # extract file path and date from the command line
    file_path = sys.argv[1]
    date = sys.argv[3]

    parser = CookieLogParser(file_path)
    most_active = parser.find_most_active_cookies(date)

    for cookie in most_active:
        print(cookie)

if __name__ == "__main__":
    main()
