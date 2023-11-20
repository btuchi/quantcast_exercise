class CookieLogParser:
    def __init__(self, file_path):
        """
        Initializes the parser with the path to the cookie log file.
        """
        self.file_path = file_path

    def find_most_active_cookies(self, date):
        """
        Finds the most active cookies for a given date.
        """
        with open(self.file_path, 'r') as file:
            cookie_counts = {}

            for line in file:
                # separate cookie and timestamp
                cookie, timestamp = line.strip().split(',')
                # separate the date from time
                cookie_date = timestamp.split('T')[0]
                
                if cookie_date == date:
                    # count the cookie
                    if cookie in cookie_counts:
                        cookie_counts[cookie] += 1
                    else:
                        cookie_counts[cookie] = 1

            # the maximum count
            max_count = max(cookie_counts.values(), default=0)

            # return the cookies with maximum count
            return [cookie for cookie, count in cookie_counts.items() if count == max_count]

