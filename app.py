import constants

if __name__ == '__main__':
    players = constants.PLAYERS
    teams = constants.TEAMS
    panthers = []
    bandits = []
    warriors = []
    experienced = []
    inexperienced = []
    
    
    def clear_data():
        i = 0
        while i < len(players):
            if players[i]['experience'] == 'YES':
                players[i]['experience'] = True
            elif players[i]['experience'] == 'NO':
                players[i]['experience'] = False
                
            height = players[i]['height'].split()
            players[i]['height'] = int(height[0])
            
            players[i]['guardians'] = (", ".join(players[i]['guardians'].split(" and ")))
            i += 1
            
    def experience():
        i = 0
        while i < len(players):
            if players[i]['experience'] == True:
                experienced.append(players[i])
                i += 1
            elif players[i]['experience'] == False:
                inexperienced.append(players[i])
                i += 1
            
            
    def balance_teams():
        num_players_team = len(players) / len(teams)
        p = 0
        t = 0
        while p < len(experienced):
            if t == 0:
                panthers.append(experienced[p])
            elif t == 1:
                bandits.append(experienced[p])
            elif t == 2:
                warriors.append(experienced[p])
                
            p += 1
            t += 1
            
            if t == 3:
                t = 0
                
                
        p = 0
        t = 0        
        while p < len(inexperienced):
            if t == 0:
                panthers.append(inexperienced[p])
            elif t == 1:
                bandits.append(inexperienced[p])
            elif t == 2:
                warriors.append(inexperienced[p])
                
            p += 1
            t += 1
            
            if t == 3:
                t = 0
        
        
    def panthers_players():
        p = 0
        panthers_team = []
        while p < len(panthers):
            panthers_team.append(panthers[p]['name'])
            p += 1
        panthers_team = (", ".join(panthers_team))
        return panthers_team
    
    
    def bandits_players():
        p = 0
        bandits_team = []
        while p < len(bandits):
            bandits_team.append(bandits[p]['name'])
            p += 1
        bandits_team = (", ".join(bandits_team))
        return bandits_team
    
    
    def warriors_players():
        p = 0
        warriors_team = []
        while p < len(warriors):
            warriors_team.append(warriors[p]['name'])
            p += 1
        warriors_team = (", ".join(warriors_team))
        return warriors_team
        
    
    def ln_exp(team): 
        p = 0
        exp = 0
        while p < len(team):
            if team[p]['experience'] == True:
                exp += 1
            p += 1
        return exp
    
    def ln_inexp(team): 
        p = 0
        inexp = 0
        while p < len(team):
            if team[p]['experience'] == False:
                inexp += 1
            p += 1
        return inexp
    
    
    def avg_height(team):
        p = 0
        height = 0
        while p < len(team):
            height += team[p]['height']
            p += 1
        height = round(height / len(team), 1)
        return height
    
    
    def guardians(team):
        p = 0
        team_guards = []
        while p < len(team):
            team_guards.append(team[p]['guardians'])
            p += 1
        team_guards = (", ".join(team_guards))
        return team_guards
        

    clear_data()
    experience()
    balance_teams()
    
    quit = 'a'    
    while quit == 'a':    
        print("BASKETBALL TEAM STATS TOOL\n")
        print("----MENU----\n")
        print("  Here are your choices:")
        print("  A) Display Team Stats")
        print("  B) Quit")
        
        
        option1 = input("\nEnter an option:   ").lower()
        if option1 == 'a':
            print("\nA) Panthers")
            print("B) Bandits")
            print("C) Warriors")
        else:
            print("Thank you for using the Basketball Team Stats Tool")
            break
            
        option2 = input("\nEnter an option:   ").lower()
        if option2 == 'a':
            print("\nPanthers Stats")
            print("--------------")
            print(f"Total players: {len(panthers)}")
            print(f"Total experienced: {ln_exp(panthers)}")
            print(f"Total inexperienced: {ln_inexp(panthers)}")
            print(f"Average height: {avg_height(panthers)}")
            print("\nPlayers on Team:")
            print(panthers_players())
            print("\nGuardians:")
            print(guardians(panthers))
            print("\n")
        elif option2 == 'b':
            print("\nBandits Stats")
            print("--------------")
            print(f"Total players: {len(bandits)}")
            print(f"Total experienced: {ln_exp(bandits)}")
            print(f"Total inexperienced: {ln_inexp(bandits)}")
            print(f"Average height: {avg_height(panthers)}")
            print("\nPlayers on Team:")
            print(bandits_players())
            print("\nGuardians:")
            print(guardians(bandits))
            print("\n")
        elif option2 == 'c':
            print("\nWarriors Stats")
            print("--------------")
            print(f"Total players: {len(warriors)}")
            print(f"Total experienced: {ln_exp(warriors)}")
            print(f"Total inexperienced: {ln_inexp(warriors)}")
            print(f"Average height: {avg_height(panthers)}")
            print("\nPlayers on Team:")
            print(warriors_players())
            print("\nGuardians:")
            print(guardians(warriors))
            print("\n")
            
        input("Press Enter to continue...")
            
