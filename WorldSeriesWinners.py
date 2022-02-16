#Open File
infile = open('WorldSeriesWinners.txt')

#Create reader object
reader = infile.read().split('\n')

#Create Team Dictionary
teams = {}

for line in reader:
    if line in teams:
        teams[line] += 1
    else:
        teams[line] = 1


#Create Year Dictionary
year = 1903
team_year = {}
for team in reader:
    if year == 1903 or year == 1993:
        team_year[year] = team
        year += 2
    else:
        team_year[year] = team
        year += 1


#Prompt user for Year choice
choice = int(input('Enter a year between 1903 and 2008: '))


#Display team and number of wins
try:
    for year in team_year:
        if choice == year:
            selected_team = team_year[choice]
    for team in teams:
        if selected_team == team:
            number_wins = str(teams[team])
    print(selected_team + ': ' + number_wins + ' wins')
    
except:
    if choice > 2009 or choice < 1903:
        print('You selected a year outside of the range')
    elif choice == 1904 or choice == 1994:
        print('There was no World Series in this year')

infile.close()    
        

