# -*- coding: utf-8 -*-
"""Functionsnoplots

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Am3EqmxuEu2Wo4JmWtKv1_qfMtezKmt
"""

# #mounting google drive
# from google.colab import drive
# drive.mount('/content/drive')
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.pyplot import figure
# import ipywidgets as widgets
# from IPython.display import display
# import seaborn as sns
# import math

# ###setting everything up with this data file.
# heads = 'drive/MyDrive/SMT_Data_Challenge/smt_data_challenge_2023'

# game = '-1903_16_TeamNI_TeamA3.csv'
# playerposthing = 'TeamA3/player_pos-1903_TeamA3'
# ginfo = 'game_info'
# csvgameinfo = f'game_info{game}'
# csvgameinfo2 = 'next csv'
# gameinfo = pd.read_csv(f'{heads}/{ginfo}/{csvgameinfo}')


# g = 'game_events'
# csvgamevents = f'game_events{game}'
# gameevents = pd.read_csv(f'{heads}/{g}/{csvgamevents}')

# p = f'player_pos/{playerposthing}'
# csvplayerpos = f'player_pos{game}'
# player_pos = pd.read_csv(f'{heads}/{p}/{csvplayerpos}')

# b = 'ball_pos'
# csvballpos = f'ball_pos{game}'
# ballpos = pd.read_csv(f'{heads}/{b}/{csvballpos}')

# centerfieldpos = player_pos[player_pos['player_position'] == 8].copy()
# leftpos = player_pos[player_pos['player_position'] == 7].copy()
# rightpos =  player_pos[player_pos['player_position'] == 9].copy()

# #Extracting the  from the Game Events Table
# centerfield = gameevents[gameevents['player_position'] == 8].copy()
# leftfield = gameevents[gameevents['player_position'] == 7].copy()
# rightfield = gameevents[gameevents['player_position'] == 9].copy()

# #extracting all outfielders
# outfielders = gameevents[(gameevents['player_position'] == 8) | (gameevents['player_position']== 7) | (gameevents['player_position']== 9)].copy()
# outfielders.sort_values(by = 'timestamp')
# # outfielders.head()
# outfieldersplays = outfielders['play_id'].unique
# outfieldersplays = np.unique(outfielders['play_id'])

###setting everything up with this data file.
heads = 'drive/MyDrive/SMT_Data_Challenge/smt_data_challenge_2023'

# game = '-1903_16_TeamNI_TeamA3.csv'
# playerposthing = 'TeamA3/player_pos-1903_TeamA3'
ginfo = 'game_info'
csvgameinfo = f'game_info{game}'
csvgameinfo2 = 'next csv'
gameinfo = pd.read_csv(f'{heads}/{ginfo}/{csvgameinfo}')


g = 'game_events'
csvgamevents = f'game_events{game}'
gameevents = pd.read_csv(f'{heads}/{g}/{csvgamevents}')

p = f'player_pos/{playerposthing}'
csvplayerpos = f'player_pos{game}'
player_pos = pd.read_csv(f'{heads}/{p}/{csvplayerpos}')

b = 'ball_pos'
csvballpos = f'ball_pos{game}'
ballpos = pd.read_csv(f'{heads}/{b}/{csvballpos}')

centerfieldpos = player_pos[player_pos['player_position'] == 8].copy()
leftpos = player_pos[player_pos['player_position'] == 7].copy()
rightpos =  player_pos[player_pos['player_position'] == 9].copy()

#Extracting the  from the Game Events Table
centerfield = gameevents[gameevents['player_position'] == 8].copy()
leftfield = gameevents[gameevents['player_position'] == 7].copy()
rightfield = gameevents[gameevents['player_position'] == 9].copy()

#extracting all outfielders
outfielders = gameevents[(gameevents['player_position'] == 8) | (gameevents['player_position']== 7) | (gameevents['player_position']== 9)].copy()
outfielders.sort_values(by = 'timestamp')
# outfielders.head()
outfieldersplays = outfielders['play_id'].unique
outfieldersplays = np.unique(outfielders['play_id'])

def playerposition(data):
  ##This is to put the game into word form

  columnnew = []
  for index, row in data.iterrows():
    if row['event'] == 1:
      columnnew.append('pitch')

    elif row['event'] == 2:
      columnnew.append('Ball Aquired')

    elif row['event'] == 3:
      columnnew.append('Throw')

    elif row['event'] == 4:
      columnnew.append('Ball Hit into Play')

    elif row['event'] == 5:
      columnnew.append('End of Play')

    elif row['event'] == 6:
      columnnew.append('Pick Off Throw')

    elif row['event'] == 7:
      columnnew.append('Ball Aquired - unknown Field Position')

    elif row['event'] == 8:
      columnnew.append('Throw - Unknown Field Position')

    elif row['event'] == 9:
      columnnew.append('Ball Deflection')

    elif row['event'] == 10:
      columnnew.append('Ball Deflection off Wall')

    elif row['event'] == 11:
      columnnew.append('Home Run')

    elif row['event'] == 16:
      columnnew.append('Ball Bounce')
    else:
      columnnew.append('Uknown')
  return columnnew

def playeridnumber(data, gameinfo):
  columnidea = []
  #the next thing I need to add to the dataframe is the player's id number. I don't have that rn
  for index, row in data.iterrows():
    playnumber = row['Play_per_game']
    indexnumber = gameinfo[gameinfo['play_per_game'] == playnumber].index[0]
    centerfield = gameinfo['center_field'][indexnumber]
    leftfield = gameinfo['left_field'][indexnumber]
    rightfield = gameinfo['right_field'][indexnumber]
    first = gameinfo['first_base'][indexnumber]
    second = gameinfo['second_base'][indexnumber]
    third = gameinfo['third_base'][indexnumber]
    short = gameinfo['shortstop'][indexnumber]
    catcher = gameinfo['catcher'][indexnumber]
    pitcher = gameinfo['pitcher'][indexnumber]
    batter = 'batter'
    runnerfirst = 'first base runner'
    runnersecond = 'second base runner'
    runnerthird = 'third base runner'
    balleventnoplayer = 'ball event no player'


    if  row['Player'] == 1:
      playeridentity = pitcher
    if  row['Player'] == 2:
      playeridentity = catcher
    if  row['Player'] == 3:
      playeridentity = first
    if  row['Player'] == 4:
      playeridentity = second
    if  row['Player'] == 5:
      playeridentity = third
    if  row['Player'] == 6:
      playeridentity = short
    if  row['Player'] == 7:
      playeridentity = leftfield
    if  row['Player'] == 8:
      playeridentity = centerfield
    if  row['Player'] == 9:
      playeridentity = rightfield
    if  row['Player'] == 10:
      playeridentity = batter
    if  row['Player'] == 11:
      playeridentity = runnerfirst
    if  row['Player'] == 12:
      playeridentity = runnersecond
    if  row['Player'] == 13:
      playeridentity = runnerthird
    if  row['Player'] == 255:
      playeridentity = balleventnoplayer
    if row['Words'] == 'End of Play':
      playeridentity = 'End of Play'

    columnidea.append(playeridentity)


  data['Player Identity'] = columnidea
  data2 = data.reset_index()
  return data2

def diffs(key, ALLOUTFIELDPLAYS):
  #create a dataframe of all of the distances.
  center = pd.DataFrame()
  centerx = ALLOUTFIELDPLAYS[f'{key}'].get('centerx')
  centery = ALLOUTFIELDPLAYS[f'{key}'].get('centery')
  centerT = ALLOUTFIELDPLAYS[f'{key}'].get('Centerstime')
  center['x'] = centerx
  center['y'] = centery
  center['T'] = centerT
  center['x_diff'] = center['x'].diff()
  center['y_diff'] = center['y'].diff()
  center.loc[0,'x_diff'] = 0
  center.loc[0,'y_diff'] = 0
  center['T_diff'] = center['T'].diff()
  center.loc[0,'T_diff'] = 0
  center['stepwise_dist'] = np.sqrt(center['x_diff']**2. + center['y_diff']**2.)
  TotalDistance = np.sum(center['stepwise_dist'])
  TotalTime = np.sum(center['T_diff'])
  # print(ALLOUTFIELDPLAYS)

    #add x diff to dictionary
  ALLOUTFIELDPLAYS[f'{key}']['Center x_diffs']= center['x_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Center y_diffs']= center['y_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Center T_diffs']= center['T_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Center Stepwise']= center['stepwise_dist'].tolist()



  right = pd.DataFrame()
  rightx = ALLOUTFIELDPLAYS[f'{key}'].get('rightfieldx')
  righty = ALLOUTFIELDPLAYS[f'{key}'].get('rightfieldy')
  rightT = ALLOUTFIELDPLAYS[f'{key}'].get('Righttime')
  right['x'] = rightx
  right['y'] = righty
  right['T'] = rightT
  right['x_diff'] = right['x'].diff()
  right['y_diff'] = right['y'].diff()
  right.loc[0,'x_diff'] = 0
  right.loc[0,'Y_diff'] = 0
  right['T_diff'] = right['T'].diff()
  right.loc[0,'T_diff'] = 0
  right['stepwise_dist'] = np.sqrt(right['x_diff']**2. + right['y_diff']**2.)
  TotalDistance = np.sum(right['stepwise_dist'])
  TotalTime = np.sum(right['T_diff'])

  ALLOUTFIELDPLAYS[f'{key}']['Right x_diffs']= right['x_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Right y_diffs']= right['y_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Right T_diffs']= right['T_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Right Stepwise']= right['stepwise_dist'].tolist()

  left = pd.DataFrame()
  leftx = ALLOUTFIELDPLAYS[f'{key}'].get('leftfieldx')
  lefty = ALLOUTFIELDPLAYS[f'{key}'].get('leftfieldy')
  leftT = ALLOUTFIELDPLAYS[f'{key}'].get('Lefttime')
  left['x'] = leftx
  left['y'] = lefty
  left['T'] = leftT
  left['x_diff'] = left['x'].diff()
  left['y_diff'] = left['y'].diff()
  left.loc[0,'x_diff'] = 0
  left.loc[0,'y_diff'] = 0
  left['T_diff'] = left['T'].diff()
  left.loc[0,'T_diff'] = 0
  left['stepwise_dist'] = np.sqrt(left['x_diff']**2. + left['y_diff']**2.)
  TotalDistance = np.sum(left['stepwise_dist'])
  TotalTime = np.sum(left['T_diff'])

  ALLOUTFIELDPLAYS[f'{key}']['Left x_diffs']= left['x_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Left y_diffs']= left['y_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Left T_diffs']= left['T_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Left Stepwise']= left['stepwise_dist'].tolist()


  ball = pd.DataFrame()
  ballx = ALLOUTFIELDPLAYS[f'{key}'].get('Ballx')
  bally = ALLOUTFIELDPLAYS[f'{key}'].get('Bally')
  ballz = ALLOUTFIELDPLAYS[f'{key}'].get('Ballz')
  ballT = ALLOUTFIELDPLAYS[f'{key}'].get('Balltime')
  ball['x'] = ballx
  ball['y'] = bally
  ball['z'] = ballz
  ball['T'] = ballT
  ball['x_diff'] = ball['x'].diff()
  ball['y_diff'] = ball['y'].diff()
  ball['z_diff'] = ball['z'].diff()
  ball.loc[0,'x_diff'] = 0
  ball.loc[0,'y_diff'] = 0
  ball.loc[0,'z_diff'] = 0
  ball['T_diff'] = ball['T'].diff()
  ball.loc[0,'T_diff'] = 0
  ball['stepwise_dist'] = np.sqrt(ball['x_diff']**2. + ball['y_diff']**2. + ball['z_diff']**2. )
  TotalDistance = np.sum(ball['stepwise_dist'])
  TotalTime = np.sum(ball['T_diff'])

  ALLOUTFIELDPLAYS[f'{key}']['Ball x_diffs']= ball['x_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Ball y_diffs']= ball['y_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Ball z_diffs']= ball['z_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Ball T_diffs']= ball['T_diff'].tolist()
  ALLOUTFIELDPLAYS[f'{key}']['Ball Stepwise']= ball['stepwise_dist'].tolist()

  return ALLOUTFIELDPLAYS

data = pd.DataFrame(columns = ['Timestamp','Play_id', 'Play_per_game', 'event', 'Player'])
data
#this is just a blank dataframe I'm using rn

p = 0
for value in outfieldersplays:

  ##subset of the data corresponding to this play_id### idval is play_id
  idval = value

  playpergame2 = outfielders[outfielders['play_id'] == idval]['play_per_game'].tolist()
  playpergame= playpergame2[0]

  event_codes = gameevents[gameevents['play_id'] == idval]

  #timestamp
  times = gameevents[gameevents['play_id'] == idval]
  timestamps = times["timestamp"]

  #creating the play_id column
  playidnumber = len(event_codes['play_id'])

  play_idcolumn = [idval]*playidnumber


  play_pergamecolumn = [playpergame]*playidnumber
  #Creating the event_codes that correspond to this
  event_codes = gameevents[gameevents['play_id'] == idval]
  event = event_codes["event_code"]

  #creating the player list
  playersinvolved = event_codes['player_position']

  #create dataframe
  playids = np.array(play_idcolumn)
  playpergame = np.array(play_pergamecolumn)

  event2 = np.array(event)
  playersinvolved2 = np.array(playersinvolved)
  timestamps2 = np.array(timestamps)

  for n in play_idcolumn:
    new_row = pd.DataFrame({'Timestamp': timestamps2[p],'Play_id': playids[p]},
                            index=[0]).copy()
    new_row = pd.DataFrame({'Timestamp': timestamps2[p],
                            'Play_id': playids[p],
                            'Play_per_game': playpergame[p],
                            'event':event2[p],
                            'Player': playersinvolved2[p]},
                           index=[0]).copy()
    data = pd.concat([data,new_row])

    p = p +1

  p = 0



##player position
columnnew = playerposition(data)
data["Words"] = columnnew

##Checking for missing gameinfo plays
data = data.reset_index()
rowstodrop = []
for index, row in data.iterrows():

  playnumber = row['Play_per_game']
  a = gameinfo[gameinfo['play_per_game'] == playnumber]
  a = len(a['play_per_game'].tolist())

  if a == 0:
    rowstodrop.append(index)

for n in rowstodrop:
  data = data.drop(n, axis = 0)


data2 = playeridnumber(data, gameinfo)

CFCatches = data.loc[(data['event'] == 2) & (data['Player'] == 8) & (data.event.shift(1) == 4)].copy()
CFallplays = data.loc[(data['Player'] == 8)].copy()
LeftCatch = data.loc[(data['event'] == 2) & (data['Player'] == 7) & (data.event.shift(1) == 4)].copy()
Leftallplays = data.loc[(data['Player'] == 7)].copy()
Rightcatch = data.loc[(data['event'] == 2) & (data['Player'] == 9) & (data.event.shift(1) == 4)].copy()
rightallplays = data.loc[(data['Player'] == 9)].copy()

onlyoutfielders = pd.concat([CFallplays,Leftallplays,rightallplays])
##only flyballs
alltooutfield = onlyoutfielders[onlyoutfielders['event'] == 2].copy()

#next step is to find the player's location when the ball is caught.
#another step would be to have the other fielder's location when the ball is caught (so at the same timestamp)
fieldxposition = []
fieldyposition = []
for index, row in alltooutfield.iterrows():
  playid = row['Play_id']
  Playerposition = row['Player']
  time = row['Timestamp']
  positionxtable = player_pos[(player_pos['play_id']== playid) & (player_pos['player_position'] == Playerposition) & (player_pos['timestamp'] == time)]
  positionx = np.array(positionxtable['field_x'])
  positiony = np.array(positionxtable['field_y'])

  fieldyposition.append(positiony[0])
  fieldxposition.append(positionx[0])

alltooutfield['x_pos (aquired)'] = fieldxposition
alltooutfield['y_pos (aquired)'] = fieldyposition
# alltooutfield.head()

#now I can iterate over each
# unique value to find the information I need

fieldxpositionleft = []
fieldypositionleft = []

fieldypositionright = []
fieldxpositionright = []

fieldxpositioncenter = []
fieldypositioncenter = []


for index, row in alltooutfield.iterrows():
  playid = row['Play_id']
  playpergame = row['Play_per_game']
  timestamp2 = row['Timestamp']
  #for this play I want to know the position when the ball was aquired...this means when the event ==2
  #extract centerfielderposition when event ==2
  row2 = player_pos[(player_pos['play_id'] == playid) & (player_pos['timestamp'] == timestamp2)].copy()
  centerfield = row2[row2['player_position'] == 8].copy()
  centerfieldx = centerfield['field_x'].item()
  centerfieldy = centerfield['field_y'].item()

  fieldxpositioncenter.append(centerfieldx)
  fieldypositioncenter.append(centerfieldy)

  rightfield = row2[row2['player_position'] == 9].copy()
  rightfieldx = rightfield['field_x'].item()
  rightfieldy = rightfield['field_y'].item()

  fieldxpositionright.append(rightfieldx)
  fieldypositionright.append(rightfieldy)


  leftfield = row2[row2['player_position'] == 7].copy()
  leftfieldx = leftfield['field_x'].item()
  leftfieldy = leftfield['field_y'].item()

  fieldxpositionleft.append(leftfieldx)
  fieldypositionleft.append(leftfieldy)

alltooutfield['x_pos (Center)'] = fieldxpositioncenter
alltooutfield['y_pos (Center)'] = fieldypositioncenter

alltooutfield['x_pos (Left)'] = fieldxpositionleft
alltooutfield['y_pos (Left)'] = fieldypositionleft

alltooutfield['x_pos (Right)'] = fieldxpositionright
alltooutfield['y_pos (Right)'] = fieldypositionright
# alltooutfield.head()

"""##Hit Catch Outfield"""

hitcatchoutfield = pd.concat([CFCatches,LeftCatch,Rightcatch])
#next step is to find the player's location when the ball is caught.
#another step would be to have the other fielder's location when the ball is caught (so at the same timestamp)
fieldxposition = []
fieldyposition = []

#Finding Location of the the players in the outfield.
fieldxpositionleft = []
fieldypositionleft = []
fieldypositionright = []
fieldxpositionright = []
rightfield = 9
leftfield = 7
centerfield = 8
fieldxpositioncenter = []
fieldypositioncenter = []

##now adding the id values for the other outfielders...
playerrightid = []
playerleftid = []
playercenter = []


for index, row in hitcatchoutfield.iterrows():
  playid = row['Play_id']
  Playerposition = row['Player']
  time = row['Timestamp']
  playpergame = row['Play_per_game']

  ##Ball position when caught
  positionxtable = player_pos[(player_pos['play_id']== playid) & (player_pos['player_position'] == Playerposition) & (player_pos['timestamp'] == time)]
  positionx = np.array(positionxtable['field_x'])
  positiony = np.array(positionxtable['field_y'])

  fieldyposition.append(positiony[0])
  fieldxposition.append(positionx[0])

  #position of the left fielder
  positionxtableleft = player_pos[(player_pos['play_id']== playid) & (player_pos['player_position'] == leftfield) & (player_pos['timestamp'] == time)].copy()

  positionxleft = np.array(positionxtableleft['field_x'])
  positionyleft = np.array(positionxtableleft['field_y'])

  fieldypositionleft.append(positionyleft[0])
  fieldxpositionleft.append(positionxleft[0])

  #position of right fielder
  positionxtableright = player_pos[(player_pos['play_id']== playid) & (player_pos['player_position'] == rightfield) & (player_pos['timestamp'] == time)].copy()
  positionxright = np.array(positionxtableright['field_x'])
  positionyright = np.array(positionxtableright['field_y'])

  fieldypositionright.append(positionyright[0])
  fieldxpositionright.append(positionxright[0])

  #position of the Center Fielder
  positionxtablecenter = player_pos[(player_pos['play_id']== playid) & (player_pos['player_position'] == centerfield) & (player_pos['timestamp'] == time)].copy()
  positionxcenter = np.array(positionxtablecenter['field_x'])
  positionycenter = np.array(positionxtablecenter['field_y'])

  fieldypositioncenter.append(positionycenter[0])
  fieldxpositioncenter.append(positionxcenter[0])

  ##player identity
  playerIdentitytable = gameinfo[(gameinfo['play_per_game'] == playpergame)].copy()

  playerIdentidyleft = playerIdentitytable['left_field'].values
  playerleftid.append(playerIdentidyleft[0])

  playerIdentidyright = playerIdentitytable['right_field'].values
  playerrightid.append(playerIdentidyright[0])

  playerIdentidycenter = playerIdentitytable['center_field'].values
  playercenter.append(playerIdentidycenter[0])



#add to data frame
hitcatchoutfield['x_pos (caught)'] = fieldxposition
hitcatchoutfield['y_pos (caught)'] = fieldyposition

hitcatchoutfield['x_pos (Left)'] = fieldxpositionleft
hitcatchoutfield['y_pos (Left)'] = fieldypositionleft
# onlyoutfielders['Left field']= playerleftid

hitcatchoutfield['x_pos (Right)'] = fieldxpositionright
hitcatchoutfield['y_pos (Right)'] = fieldypositionright
# onlyoutfielders['Right field']= playerrightid

hitcatchoutfield['x_pos (Center)'] = fieldxpositioncenter
hitcatchoutfield['y_pos (Center)'] = fieldypositioncenter
# onlyoutfielders['Center field']= playercenter

#add player ids
hitcatchoutfield['Left field']= playerleftid
hitcatchoutfield['Right field']= playerrightid
hitcatchoutfield['Center field']= playercenter

# hitcatchoutfield.head()

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
from scipy.spatial import ConvexHull


def encircle(x,y, ax=None, **kw):
    if not ax: ax=plt.gca()
    p = np.c_[x,y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices,:], **kw)
    ax.add_patch(poly)

# encircle(x1, y1, ec="k", fc="gold", alpha=0.2)
# encircle(x2, y2, ec="orange", fc="none")

# plt.show()

##For every play in the hitcatch outfield table, I want to make a
##table that describes how the players and the ball is moving.
listLL = []
dictionarys ={}
for index, row in hitcatchoutfield.iterrows():

  playid = row['Play_id']
  playerpositions = player_pos[player_pos['play_id']== playid].copy()
  ballpositions = ballpos[ballpos['play_id']== playid].copy()

  centerfielderposition = playerpositions[playerpositions['player_position'] == 8].copy()
  rightfield = playerpositions[playerpositions['player_position'] == 9].copy()
  leftfield = playerpositions[playerpositions['player_position'] == 7].copy()

  centerfielderpositionx = np.array(centerfielderposition['field_x']).tolist()
  rightfieldx = np.array(rightfield['field_x']).tolist()
  leftfieldx = np.array(leftfield['field_x']).tolist()
  centery = np.array(centerfielderposition['field_y']).tolist()
  rightfieldy = np.array(rightfield['field_y']).tolist()
  leftfieldy = np.array(leftfield['field_y']).tolist()

  ##Ball postion now :)
  ballx = ballpositions['ball_position_x'].tolist()
  bally = ballpositions['ball_position_y'].tolist()
  ballz = ballpositions['ball_position_z'].tolist()

  dictionarys.update({f'{playid}': {'centerx': centerfielderpositionx}})
  dictionarys[f'{playid}']['rightfieldx']= rightfieldx
  dictionarys[f'{playid}']['leftfieldx']= leftfieldx
  dictionarys[f'{playid}']['rightfieldy']= rightfieldy
  dictionarys[f'{playid}']['leftfieldy']= leftfieldy
  dictionarys[f'{playid}']['centery']= centery
  dictionarys[f'{playid}']['Ballx']= ballx
  dictionarys[f'{playid}']['Bally']= bally
  dictionarys[f'{playid}']['Ballz']= ballz
  # input()

# dictionarys.keys()

##from this dictionary we can start inputing values and lists for velocity and acceleration or just make DFs
##extracting velocity
for key, value in dictionarys.items():
  keynum = int(key)

  timestampstable = player_pos[player_pos['play_id'] == keynum].copy()
  centertimetable = timestampstable[timestampstable['player_position'] == 8]
  centertime = centertimetable['timestamp'].tolist()

  righttimetable = timestampstable[timestampstable['player_position'] == 9]
  righttime = righttimetable['timestamp'].tolist()

  lefttimetable = timestampstable[timestampstable['player_position'] == 7]
  lefttime = lefttimetable['timestamp'].tolist()


  ballpositiontable = ballpos[ballpos['play_id'] == keynum].copy()
  balltime = ballpositiontable['timestamp'].tolist()

  timestamps = np.array(timestampstable['timestamp']).tolist()
  dictionarys[f'{keynum}']['Centerstime']= centertime
  dictionarys[f'{keynum}']['Righttime']= righttime
  dictionarys[f'{keynum}']['Lefttime']= lefttime
  dictionarys[f'{keynum}']['Balltime']= balltime

##realized I needed to take the vector of the x and y positions :(
for key, value in dictionarys.items():
  #create a dataframe of all of the distances.
  center = pd.DataFrame()
  centerx = dictionarys[f'{key}'].get('centerx')
  centery = dictionarys[f'{key}'].get('centery')
  centerT = dictionarys[f'{key}'].get('Centerstime')
  center['x'] = centerx
  center['y'] = centery
  center['T'] = centerT
  centerx = center['x'].tolist()
  centery = center['y'].tolist()
  center['x_diff'] = centerx
  center['y_diff'] = centery

  center.loc[0,'x_diff'] = 0
  center.loc[0,'y_diff'] = 0
  center['T_diff'] = center['T'].diff()
  center.loc[0,'T_diff'] = 0
  center['stepwise_dist'] = np.sqrt(center['x_diff']**2. + center['y_diff']**2.)
  TotalDistance = np.sum(center['stepwise_dist'])
  TotalTime = np.sum(center['T_diff'])

  #add x diff to dictionary
  dictionarys[f'{key}']['Center x_diffs']= center['x_diff'].tolist()
  dictionarys[f'{key}']['Center y_diffs']= center['y_diff'].tolist()
  dictionarys[f'{key}']['Center T_diffs']= center['T_diff'].tolist()
  dictionarys[f'{key}']['Center Stepwise']= center['stepwise_dist'].tolist()



  right = pd.DataFrame()
  rightx = dictionarys[f'{key}'].get('rightfieldx')
  righty = dictionarys[f'{key}'].get('rightfieldy')
  rightT = dictionarys[f'{key}'].get('Righttime')
  right['x'] = rightx
  right['y'] = righty
  right['T'] = rightT
  right['x_diff'] = right['x'].diff()
  right['y_diff'] = right['y'].diff()
  right.loc[0,'x_diff'] = 0
  right.loc[0,'y_diff'] = 0
  right['T_diff'] = right['T'].diff()
  right.loc[0,'T_diff'] = 0
  right['stepwise_dist'] = np.sqrt(right['x_diff']**2. + right['y_diff']**2.)
  TotalDistance = np.sum(right['stepwise_dist'])
  TotalTime = np.sum(right['T_diff'])

  dictionarys[f'{key}']['Right x_diffs']= right['x_diff'].tolist()
  dictionarys[f'{key}']['Right y_diffs']= right['y_diff'].tolist()
  dictionarys[f'{key}']['Right T_diffs']= right['T_diff'].tolist()
  dictionarys[f'{key}']['Right Stepwise']= right['stepwise_dist'].tolist()

  left = pd.DataFrame()
  leftx = dictionarys[f'{key}'].get('leftfieldx')
  lefty = dictionarys[f'{key}'].get('leftfieldy')
  leftT = dictionarys[f'{key}'].get('Lefttime')
  left['x'] = leftx
  left['y'] = lefty
  left['T'] = leftT
  left['x_diff'] = left['x'].diff()
  left['y_diff'] = left['y'].diff()
  left.loc[0,'x_diff'] = 0
  left.loc[0,'y_diff'] = 0
  left['T_diff'] = left['T'].diff()
  left.loc[0,'T_diff'] = 0
  left['stepwise_dist'] = np.sqrt(left['x_diff']**2. + left['y_diff']**2.)
  TotalDistance = np.sum(left['stepwise_dist'])
  TotalTime = np.sum(left['T_diff'])

  dictionarys[f'{key}']['Left x_diffs']= left['x_diff'].tolist()
  dictionarys[f'{key}']['Left y_diffs']= left['y_diff'].tolist()
  dictionarys[f'{key}']['Left T_diffs']= left['T_diff'].tolist()
  dictionarys[f'{key}']['Left Stepwise']= left['stepwise_dist'].tolist()


  ball = pd.DataFrame()
  ballx = dictionarys[f'{key}'].get('Ballx')
  bally = dictionarys[f'{key}'].get('Bally')
  ballz = dictionarys[f'{key}'].get('Ballz')
  ballT = dictionarys[f'{key}'].get('Balltime')
  ball['x'] = ballx
  ball['y'] = bally
  ball['z'] = ballz
  ball['T'] = ballT
  ball['x_diff'] = ball['x'].diff()
  ball['y_diff'] = ball['y'].diff()
  ball['z_diff'] = ball['z'].diff()
  ball.loc[0,'x_diff'] = 0
  ball.loc[0,'y_diff'] = 0
  ball.loc[0,'z_diff'] = 0
  ball['T_diff'] = ball['T'].diff()
  ball.loc[0,'T_diff'] = 0
  ball['stepwise_dist'] = np.sqrt(ball['x_diff']**2. + ball['y_diff']**2. + ball['z_diff']**2. )
  TotalDistance = np.sum(ball['stepwise_dist'])
  TotalTime = np.sum(ball['T_diff'])

  dictionarys[f'{key}']['Ball x_diffs']= ball['x_diff'].tolist()
  dictionarys[f'{key}']['Ball y_diffs']= ball['y_diff'].tolist()
  dictionarys[f'{key}']['Ball z_diffs']= ball['z_diff'].tolist()
  dictionarys[f'{key}']['Ball T_diffs']= ball['T_diff'].tolist()
  dictionarys[f'{key}']['Ball Stepwise']= ball['stepwise_dist'].tolist()

for key, value in dictionarys.items():

  centerstepdist = dictionarys[f'{key}'].get('Center Stepwise')
  centertimestep = dictionarys[f'{key}'].get('Center T_diffs')
  centerT = dictionarys[f'{key}'].get('Centerstime')
  centervelocity = [i / j for i, j in zip(centerstepdist[1:], centertimestep[1:])]
  dictionarys[f'{key}']['Center velocity']= centervelocity

  rightstepdist = dictionarys[f'{key}'].get('Right Stepwise')
  righttimestep = dictionarys[f'{key}'].get('Right T_diffs')
  RightT = dictionarys[f'{key}'].get('Righttime')
  rightvelocity = [i / j for i, j in zip(rightstepdist[1:], righttimestep[1:])]
  dictionarys[f'{key}']['Right velocity']= rightvelocity

  leftstepdist = dictionarys[f'{key}'].get('Left Stepwise')
  lefttimestep = dictionarys[f'{key}'].get('Left T_diffs')
  LeftT = dictionarys[f'{key}'].get('Lefttime')
  leftvelocity = [i / j for i, j in zip(leftstepdist[1:], lefttimestep[1:])]
  dictionarys[f'{key}']['Left velocity']= leftvelocity

  ballstepdist = dictionarys[f'{key}'].get('Ball Stepwise')
  balltimestep = dictionarys[f'{key}'].get('Ball T_diffs')
  BallT = dictionarys[f'{key}'].get('Balltime')
  ballvelocity = [i / j for i, j in zip(ballstepdist[1:], balltimestep[1:])]
  dictionarys[f'{key}']['Ball velocity']= ballvelocity


##Velocity differences
#create a dataframe of all of the distances.
  center = pd.DataFrame()
  centerV = dictionarys[f'{key}'].get('Center velocity')
  centerT = dictionarys[f'{key}'].get('Center T_diffs')[1:]
  center['V'] = centerV
  center['T'] = centerT
  center['V_diff'] = center['V'].diff()

  centerA = [i / j for i, j in zip(centerV, centerT)]
  dictionarys[f'{key}']['Center Acceleration']= centerA

  ##rightfield
  right = pd.DataFrame()
  rightV = dictionarys[f'{key}'].get('Right velocity')
  rightT = dictionarys[f'{key}'].get('Right T_diffs')[1:]
  right['V'] = rightV
  right['T'] = rightT
  right['V_diff'] = right['V'].diff()

  RightA = [i / j for i, j in zip(rightV, rightT)]
  dictionarys[f'{key}']['Right Acceleration']= RightA



  ###leftfield
  left = pd.DataFrame()
  leftV = dictionarys[f'{key}'].get('Left velocity')
  leftT = dictionarys[f'{key}'].get('Left T_diffs')[1:]
  left['V'] = leftV
  left['T'] = leftT
  left['V_diff'] = left['V'].diff()

  LeftA = [i / j for i, j in zip(leftV, leftT)]
  dictionarys[f'{key}']['Left Acceleration']= LeftA

  ####ball :)
  Ball = pd.DataFrame()
  BallV = dictionarys[f'{key}'].get('Ball velocity')
  BallT = dictionarys[f'{key}'].get('Ball T_diffs')[1:]
  Ball['V'] = BallV
  Ball['T'] = BallT
  Ball['V_diff'] = Ball['V'].diff()

  BallA = [i / j for i, j in zip(BallV, BallT)]
  dictionarys[f'{key}']['Ball Acceleration']= BallA

"""##non-hitcatches"""

##dataframe of all non-hitcatches.
listofvals = hitcatchoutfield['Play_id'].unique().tolist()
a = 0
for n in listofvals:

  alltooutfielddropped = alltooutfield.loc[alltooutfield['Play_id'] != listofvals[a]]
  a = a+ 1
  alltooutfield = alltooutfielddropped

"""##non-hitcatch dictionary."""

###Now I run all the code from the other dataframe on this one--> getting velocity, acceleration, etc.
listAA = []
ALLOUTFIELDPLAYS ={}
for index, row in alltooutfielddropped.iterrows():

  playid = row['Play_id']
  playerpositions = player_pos[player_pos['play_id']== playid].copy()
  ballpositions = ballpos[ballpos['play_id']== playid].copy()

  centerfielderposition = playerpositions[playerpositions['player_position'] == 8].copy()
  rightfield = playerpositions[playerpositions['player_position'] == 9].copy()
  leftfield = playerpositions[playerpositions['player_position'] == 7].copy()

  centerfielderpositionx = np.array(centerfielderposition['field_x']).tolist()
  rightfieldx = np.array(rightfield['field_x']).tolist()
  leftfieldx = np.array(leftfield['field_x']).tolist()
  centery = np.array(centerfielderposition['field_y']).tolist()
  rightfieldy = np.array(rightfield['field_y']).tolist()
  leftfieldy = np.array(leftfield['field_y']).tolist()

  ##Ball postion now :)
  ballx = ballpositions['ball_position_x'].tolist()
  bally = ballpositions['ball_position_y'].tolist()
  ballz = ballpositions['ball_position_z'].tolist()

  ALLOUTFIELDPLAYS.update({f'{playid}': {'centerx': centerfielderpositionx}})
  ALLOUTFIELDPLAYS[f'{playid}']['rightfieldx']= rightfieldx
  ALLOUTFIELDPLAYS[f'{playid}']['leftfieldx']= leftfieldx
  ALLOUTFIELDPLAYS[f'{playid}']['rightfieldy']= rightfieldy
  ALLOUTFIELDPLAYS[f'{playid}']['leftfieldy']= leftfieldy
  ALLOUTFIELDPLAYS[f'{playid}']['centery']= centery
  ALLOUTFIELDPLAYS[f'{playid}']['Ballx']= ballx
  ALLOUTFIELDPLAYS[f'{playid}']['Bally']= bally
  ALLOUTFIELDPLAYS[f'{playid}']['Ballz']= ballz

##from this dictionary we can start inputing values and lists for velocity and acceleration or just make DFs
##extracting velocity
for key, value in ALLOUTFIELDPLAYS.items():
  keynum = int(key)
  # print(value)
  timestampstable = player_pos[player_pos['play_id'] == keynum].copy()
  centertimetable = timestampstable[timestampstable['player_position'] == 8].copy()
  centertime = centertimetable['timestamp'].tolist()

  righttimetable = timestampstable[timestampstable['player_position'] == 9].copy()
  righttime = righttimetable['timestamp'].tolist()

  lefttimetable = timestampstable[timestampstable['player_position'] == 7].copy()
  lefttime = lefttimetable['timestamp'].tolist()


  ballpositiontable = ballpos[ballpos['play_id'] == keynum].copy()
  balltime = ballpositiontable['timestamp'].tolist()
  # display(timestampstable)
  timestamps = np.array(timestampstable['timestamp']).tolist()
  ALLOUTFIELDPLAYS[f'{keynum}']['Centerstime']= centertime
  ALLOUTFIELDPLAYS[f'{keynum}']['Righttime']= righttime
  ALLOUTFIELDPLAYS[f'{keynum}']['Lefttime']= lefttime
  ALLOUTFIELDPLAYS[f'{keynum}']['Balltime']= balltime

  ALLOUTFIELDPLAYS = diffs(key, ALLOUTFIELDPLAYS)

"""Breaking into adding Acceleration"""

##had to break up the code because it was a huge chunk
for key, value in ALLOUTFIELDPLAYS.items():

  centerstepdist = ALLOUTFIELDPLAYS[f'{key}'].get('Center Stepwise')
  centertimestep = ALLOUTFIELDPLAYS[f'{key}'].get('Center T_diffs')
  centerT = ALLOUTFIELDPLAYS[f'{key}'].get('Centerstime')
  centervelocity = [i / j for i, j in zip(centerstepdist[1:], centertimestep[1:])]
  ALLOUTFIELDPLAYS[f'{key}']['Center velocity']= centervelocity


  rightstepdist = ALLOUTFIELDPLAYS[f'{key}'].get('Right Stepwise')
  righttimestep = ALLOUTFIELDPLAYS[f'{key}'].get('Right T_diffs')
  RightT = ALLOUTFIELDPLAYS[f'{key}'].get('Righttime')
  rightvelocity = [i / j for i, j in zip(rightstepdist[1:], righttimestep[1:])]
  ALLOUTFIELDPLAYS[f'{key}']['Right velocity']= rightvelocity

  leftstepdist = ALLOUTFIELDPLAYS[f'{key}'].get('Left Stepwise')
  lefttimestep = ALLOUTFIELDPLAYS[f'{key}'].get('Left T_diffs')
  LeftT = ALLOUTFIELDPLAYS[f'{key}'].get('Lefttime')
  leftvelocity = [i / j for i, j in zip(leftstepdist[1:], lefttimestep[1:])]
  ALLOUTFIELDPLAYS[f'{key}']['Left velocity']= leftvelocity

  ballstepdist = ALLOUTFIELDPLAYS[f'{key}'].get('Ball Stepwise')
  balltimestep = ALLOUTFIELDPLAYS[f'{key}'].get('Ball T_diffs')
  BallT = ALLOUTFIELDPLAYS[f'{key}'].get('Balltime')
  ballvelocity = [i / j for i, j in zip(ballstepdist[1:], balltimestep[1:])]
  ALLOUTFIELDPLAYS[f'{key}']['Ball velocity']= ballvelocity

  ##Velocity Differences
  #create a dataframe of all of the distances.
  center = pd.DataFrame()
  centerV = ALLOUTFIELDPLAYS[f'{key}'].get('Center velocity')
  centerT = ALLOUTFIELDPLAYS[f'{key}'].get('Center T_diffs')[1:]
  center['V'] = centerV
  center['T'] = centerT
  center['V_diff'] = center['V'].diff()
  centerA = [i / j for i, j in zip(centerV, centerT)]
  ALLOUTFIELDPLAYS[f'{key}']['Center Acceleration']= centerA


  ##rightfield
  right = pd.DataFrame()
  rightV = ALLOUTFIELDPLAYS[f'{key}'].get('Right velocity')
  rightT = ALLOUTFIELDPLAYS[f'{key}'].get('Right T_diffs')[1:]
  right['V'] = rightV
  right['T'] = rightT
  right['V_diff'] = right['V'].diff()
  RightA = [i / j for i, j in zip(rightV, rightT)]
  ALLOUTFIELDPLAYS[f'{key}']['Right Acceleration']= RightA


  ###leftfield
  left = pd.DataFrame()
  leftV = ALLOUTFIELDPLAYS[f'{key}'].get('Left velocity')
  leftT = ALLOUTFIELDPLAYS[f'{key}'].get('Left T_diffs')[1:]
  left['V'] = leftV
  left['T'] = leftT
  left['V_diff'] = left['V'].diff()
  LeftA = [i / j for i, j in zip(leftV, leftT)]
  ALLOUTFIELDPLAYS[f'{key}']['Left Acceleration']= LeftA



  ####ball :)
  Ball = pd.DataFrame()
  BallV = ALLOUTFIELDPLAYS[f'{key}'].get('Ball velocity')
  BallT = ALLOUTFIELDPLAYS[f'{key}'].get('Ball T_diffs')[1:]
  Ball['V'] = BallV
  Ball['T'] = BallT
  Ball['V_diff'] = Ball['V'].diff()
  BallA = [i / j for i, j in zip(BallV, BallT)]
  ALLOUTFIELDPLAYS[f'{key}']['Ball Acceleration']= BallA

##now that I have both dictionaries done, I can compare the values with t-tests.
#caught plays
CCV = []
CCA = []
RCV = []
RCA = []
LCV = []
LCA = []
BCV = []
BCA = []

#non-caught plays
CV = []
CA = []
RV = []
RA = []
LV = []
LA = []
BV = []
BA = []

for key, value in ALLOUTFIELDPLAYS.items():

  #non-caught plays
  CV.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Center velocity'))
  CA.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Center Acceleration'))
  RV.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Right velocity'))
  RA.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Right Acceleration'))
  LV.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Left velocity'))
  LA.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Left Acceleration'))
  BV.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Ball velocity'))
  BA.extend(ALLOUTFIELDPLAYS[f'{key}'].get('Ball Acceleration'))

for key, value in dictionarys.items():
  CCV.extend(dictionarys[f'{key}'].get('Center velocity'))
  CCA.extend(dictionarys[f'{key}'].get('Center Acceleration'))
  RCV.extend(dictionarys[f'{key}'].get('Right velocity'))
  RCA.extend(dictionarys[f'{key}'].get('Right Acceleration'))
  LCV.extend(dictionarys[f'{key}'].get('Left velocity'))
  LCA.extend(dictionarys[f'{key}'].get('Left Acceleration'))
  BCV.extend(dictionarys[f'{key}'].get('Ball velocity'))
  BCA.extend(dictionarys[f'{key}'].get('Ball Acceleration'))

"""##caught in the outfield"""

##onlyrightfield
droppedrightorcenter = alltooutfielddropped[(alltooutfielddropped['Player'] == 8 ) | (alltooutfielddropped['Player'] == 9 )]
caughtrightorcenter = hitcatchoutfield[(hitcatchoutfield['Player'] == 8 ) | (hitcatchoutfield['Player'] == 9 )]

##We can look at how close the players are when a ball is caught vs not.
#take the distance b
distancecenterright = []
for index, row in caughtrightorcenter.iterrows():
  playid = row['Play_id']
  forthisplay = caughtrightorcenter[caughtrightorcenter['Play_id'] == playid ].copy()
  forthisplay['x_pos (Left)'].values[0]
  # left = [forthisplay['x_pos (Left)'].values[0],forthisplay['y_pos (Left)'].values[0]]
  center = [forthisplay['x_pos (Center)'].values[0],forthisplay['y_pos (Center)'].values[0]]
  right = [forthisplay['x_pos (Right)'].values[0],forthisplay['y_pos (Right)'].values[0]]
  caught = [forthisplay['x_pos (caught)'].values[0],forthisplay['y_pos (caught)'].values[0]]

  ###right now I'm only looking at right field

  distance = math.dist(center,right)
  distancecenterright.append(distance)

caughtrightorcenter['Center and Right Distance'] = distancecenterright

"""##Dropped in the outfield"""

##We can look at how close the players are when a ball is caught vs not.
#take the distance b
distancecenterright = []
for index, row in droppedrightorcenter.iterrows():
  playid = row['Play_id']

  forthisplay = droppedrightorcenter[droppedrightorcenter['Play_id'] == playid ].copy()
  forthisplay['x_pos (Left)'].values[0]
  # left = [forthisplay['x_pos (Left)'].values[0],forthisplay['y_pos (Left)'].values[0]]
  center = [forthisplay['x_pos (Center)'].values[0],forthisplay['y_pos (Center)'].values[0]]
  right = [forthisplay['x_pos (Right)'].values[0],forthisplay['y_pos (Right)'].values[0]]
  caught = [forthisplay['x_pos (aquired)'].values[0],forthisplay['y_pos (aquired)'].values[0]]

  ###right now I'm only looking at right field

  distance = math.dist(center,right)
  distancecenterright.append(distance)

droppedrightorcenter['Center and Right Distance'] = distancecenterright

dropped = droppedrightorcenter['Center and Right Distance'].tolist()
caught = caughtrightorcenter['Center and Right Distance'].tolist()

dropped