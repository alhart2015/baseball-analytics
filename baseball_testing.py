'''
Testing out and exploring the datasets
'''

import constants.table_fieldnames as T
import constants.general_constants as G

def awards_for_year(awards_list, year):
    '''Prints out all the awards won in a given year.'''
    for row in awards_list:
        if int(row[T.YEAR]) == year:
            print row

def mvp_awards_shares_for_year(awards_shares, year):
    '''Prints all players who had a share of either mvp for that year'''
    for row in awards_shares:
        if int(row[T.YEAR]) == year:
            if row[T.AWARD] == G.MVP:
                print row
