#1.1 Create Dictionaries (2.5 points)

birthdays={"Soumith":"12/16/1993","Sivanand":"01/10/1993","Vasanth":"03/11/1990"}

print(birthdays["Sivanand"])

#1.2 Update Dictionaries (2.5 points)

birthdays["Vasanth"]="06/06/1980"

print(birthdays["Vasanth"])

#1.3 Dictionary With Lists (2.5 points)

seasons={"Fall":["September","October","November"],"Spring":["March","April","May"],"Summer":["June","July","August"]}
print(seasons["Spring"])

#1.4 Dictionary Merge (2.5 points)
seasons={"Fall":["September","October","November"],"Spring":["March","April","May"],"Summer":["June","July","August"]}
print(seasons)
winter_season={"Winter":["December","January","February"]}
seasons.update(winter_season)
print(seasons)