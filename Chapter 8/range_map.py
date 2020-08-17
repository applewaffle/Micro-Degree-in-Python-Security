from collections_extended import RangeMap
from datetime import date

us_presidents = RangeMap()
us_presidents[date(1993, 1, 20):date(2001, 1, 20)] = "Bill Clinton"
us_presidents[date(2001, 1, 20):date(2009, 1, 20)] = "George W. Bush"
us_presidents[date(2009, 1, 20):date(2017, 1, 20)] = "Barack Obama"


if __name__ == "__main__":
    print(us_presidents[date(2001, 1, 19)])
    print(us_presidents[date(2001, 1, 20)])
    us_presidents[date(2017, 1, 20):] = "Donald Trump"
    print(us_presidents[date(2019, 1, 20)])

