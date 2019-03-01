import csv
import os

TEXT = """Dear {},
Your child, {}, was assigned to the {} team.
See you on March 15 for the first practice.
Coach Nicolas
"""

if __name__ == "__main__" : 
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')
  with open("soccer_players.csv", newline="") as csvfile:
    playerreader = csv.reader(csvfile, delimiter=",")
    players_list = list(playerreader)
  league = {}
  print("Welcome to the league builder")
  print("There are ",(len(players_list)-1), "players in the league")
  name = input("What is the name of the first team? ")
  players = []
  league[name] = players
  while True:
    cls()
    count = 1 
    print("The ", (len(players_list)-1), "players in the League would be split between", len(league),"team(s):")
    for team in league.keys():
      print(count,": ",team)
      count +=1
    if count < (len(players_list)):
      if input("Would you like to create another team? (Y/N) ").upper() == "Y": 
        name = input("What is the name of the team? ")
        players = []
        league[name] = players
    else:
      cls()
      print("OK! The ", (len(players_list)-1), "players in the League will be split between the", len(league),"following team(s):")
      count = 1
      for team in league.keys():
        print(count,": ",team)
        count +=1
      print("")
      print("See file text.txt for a detail of the",len(league),"teams.")
      print("")
      print("See",(len(players_list)-1),"individual text files for welcome letters.")
      print("") 
      break
  for player in players_list:
    player.pop(1)
  experienced_players = []
  unexperienced_players = []
  for player in players_list[1:]:
    if player[1] == "YES":
      experienced_players.append(player[0:])
    else:
      unexperienced_players.append(player[0:])
  count = 0
  for value in league.values():
    value.extend(experienced_players[count::len(league)])
    count +=1
  count = len(league)-1
  for value in league.values():
    value.extend(unexperienced_players[count::len(league)])
    count -=1
  with open("text.txt", "w") as file:
    for key, values in league.items(): 
      file.write(key.title()+"\n")
      file.write("-"*len(key)+"\n")
      for value in values:
        file.write(", ".join(value)+"\n")
      file.write("\n")
  print("")
  for keys,values in league.items():
    for value in values:
      name = value[0]
      file_name = name.replace(" ", "_").lower()+".txt"
      guardian = value[2]
      with open(file_name, "w") as file:
        file.write(TEXT.format(guardian, name, keys))
      