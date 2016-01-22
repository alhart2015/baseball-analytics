'''For referencing table field names'''

# Master.csv
PLAYER_ID = 'playerID'  # A unique code asssigned to each player.  The playerID links the data in this file with records in the other files.
BIRTH_YEAR = 'birthYear'    # Year player was born
BIRTH_MONTH = 'birthMonth' # Month player was born
BIRTH_DAY = 'birthDay'  # Day player was born
BIRTH_COUNTRY = 'birthCountry' # Country where player was born
BIRTH_STATE = 'birthState' # State where player was born
BIRTH_CITY = 'birthCity' # City where player was born
DEATH_YEAR = 'deathYear' # Year player died
DEATH_MONTH = 'deathMonth' # Month player died
DEATH_DAY = 'deathDay'  # Day player died
DEATH_COUNTRY = 'deathCountry' # Country where player died
DEATH_STATE = 'deathState' # State where player died
DEATH_CITY = 'deathCity' # City where player died
FIRST_NAME = 'nameFirst' # Player's first name
LAST_NAME = 'nameLast'  # Player's last name
GIVEN_NAME = 'nameGiven' # Player's given name (typically first and middle)
WEIGHT = 'weight'   # Player's weight in pounds
HEIGHT = 'height'   # Player's height in inches
BATS = 'bats'   # Player's batting hand (left, right, or both) # 
THROWS = 'throws' # Player's throwing hand (left or right)
DEBUT = 'debut' # Date that player made first major league appearance
FINAL_GAME = 'finalGame' # Date that player made first major league appearance (blank if still active)
RETRO_ID = 'retroID' # ID used by retrosheet
BBREF_ID = 'bbrefID' # ID used by Baseball Reference website

# Pitching.csv
PLAYER_ID = 'playerID'   # Player ID code
YEARID = 'yearID'       # Year
STINT = 'stint' # player's stint (order of appearances within a season)
TEAMID = 'teamID' # Team
LEAGUE = 'lgID'     # League
WINS = 'W'  # Wins
LOSSES = 'L'    # Losses
GAMES = 'G'     # Games
GS = 'GS' # Games Started
CG = 'CG' # Complete Games 
SHO = 'SHO' # Shutouts
SV = 'SV' # Saves
IP_OUTS = 'IPOuts' # Outs Pitched (innings pitched x 3)
H = 'H'     # Hits
ER = 'ER' # Earned Runs
HR = 'HR' # Homeruns
BB = 'BB' # Walks
SO = 'SO' # Strikeouts
BA_OPP = 'BAOpp' # Opponent's Batting Average
ERA = 'ERA' # Earned Run Average
IBB = 'IBB' # Intentional Walks
WP = 'WP' # Wild Pitches
HBP = 'HBP' # Batters Hit By Pitch
BALK = 'BK' # Balks
BFP = 'BFP' # Batters faced by Pitcher
GF = 'GF' # Games Finished
R = 'R'     # Runs Allowed
SH = 'SH' # Sacrifices by opposing batters
SF = 'SF' # Sacrifice flies by opposing batters
GIDP = 'GIDP' # Grounded into double plays by opposing batter

# Batting.csv
PLAYER_ID = 'playerID' # Player ID code
YEAR_ID = 'yearID' # Year
STINT = 'stint' # player's stint (order of appearances within a season)
TEAM_ID = 'teamID' # Team
LEAGUE = 'lgID' # League
GAME = 'G' # Games
GAME_BATTING = 'G_batting' # Game as batter
AB = 'AB' # At Bats
R = 'R' # Runs
H = 'H' # Hits
DOUBLE = '2B' #Doubles
TRIPLE = '3B' #Triples
HR = 'HR' #Homeruns
RBI = 'RBI' # Runs Batted In
SB = 'SB' #Stolen Bases
CS = 'CS' #Caught Stealing
BB = 'BB' # Base on Balls
SO = 'SO' # Strikeouts
IBB = 'IBB' # Intentional walks
HBP = 'HBP' # Hit by pitch
SH = 'SH' # Sacrifice hits
SF = 'SF' # Sacrifice flies
GIDP = 'GIDP' # Grounded into double plays
G_OLD = 'G_Old' # Old version of games (deprecated)

# AwardsPlayers table
PLAYER_ID = 'playerID' # Player ID code
AWARD = 'awardID' # Name of award won
YEAR = 'yearID' # Year
LEAGUE = 'lgID' # League
TIE = 'tie' # Award was a tie (Y or N)
NOTES = 'notes' # Notes about the award

# AwardsSharePlayers.csv
AWARD = 'awardID' # name of award votes were received for
YEAR = 'yearID' # Year
LEAGUE = 'lgID' # League
PLAYER_ID = 'playerID' # Player ID code
POINTS_WON = 'pointsWon' # Number of points received
POINTS_MAX = 'pointsMax' # Maximum numner of points possible
VOTES_FIRST = 'votesFirst' # Number of first place votes



