'''
Main point of entry for the baseball project.

Doing some exploration with a baseball dataset. The eventual goal is to apply
batting/pitching stats to a machine learning model (undecided on implementation)
to predict MVP/cy young voting.
'''

import time
import csv
import sklearn
import constants.table_fieldnames as T
import constants.general_constants as G
import baseball_testing as test

PITCHING_DATA_FILE = './data/lahman-csv_2014-02-14/Pitching.csv'
MASTER_DATA_FILE = './data/lahman-csv_2014-02-14/Master.csv'
AWARDS_PLAYERS_FILE = './data/lahman-csv_2014-02-14/AwardsPlayers.csv'
AWARDS_SHARE_PLAYERS_FILE = './data/lahman-csv_2014-02-14/AwardsSharePlayers.csv'

def get_raw_data(filename):
    '''Reads the input csv and returns a list of the raw data'''
    raw_data = []
    with open(filename, 'r') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            raw_data.append(row)
    return raw_data

def main():

    start = time.time()

    name_dict = get_raw_data(MASTER_DATA_FILE)
    print 'Read in master data:', time.time() - start
    # print name_dict[0]

    raw_pitching_data = get_raw_data(PITCHING_DATA_FILE)
    print 'Read in pitching data:', time.time() - start
    # print raw_pitching_data[0][T.PLAYER_ID]

    awards_players_data = get_raw_data(AWARDS_PLAYERS_FILE)
    print 'Read in player awards data:', time.time() - start
    # print awards_players_data[1]

    awards_share_players_data = get_raw_data(AWARDS_SHARE_PLAYERS_FILE)
    print 'Read in awards share players file:', time.time() - start
    # print awards_share_players_data[10]

    print test.mvp_awards_shares_for_year(awards_share_players_data, 2013)

    # test.awards_for_year(awards_players_data, 2013)

    # print raw_pitching_data[100]
    # print len(raw_pitching_data)
    # print name_dict[raw_pitching_data[100][0]]


if __name__ == '__main__':
    main()