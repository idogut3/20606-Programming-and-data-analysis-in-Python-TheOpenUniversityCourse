class Date:
    """
     Represents a date with year, month, and day components.

     Attributes:
         year (int): The year of the date.
         month (int): The month of the date.
         day (int): The day of the date.
     """

    def __init__(self, date_string):
        year, month, day = date_string.split('-')
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    def __str__(self):
        day_string = str(self.day)
        month_string = str(self.month)
        year_string = str(self.year)
        if self.day < 10:
            day_string = '0' + day_string
        if self.month < 10:
            month_string = '0' + month_string
        if self.year < 1000:
            year_string = '0' + year_string
        if self.year < 100:
            year_string = '0' + year_string
        if self.year < 10:
            year_string = '0' + year_string
        return f"{year_string}-{month_string}-{day_string}"

    '''
        @function year_difference
        @:returns int value:
            - 0 if the dates are in the same year
            - A positive number if self.year > other_date.year 
            - A negative number if other_date < other_date.year 
    '''

    def year_difference(self, other_date) -> int:
        return self.year - other_date.year
