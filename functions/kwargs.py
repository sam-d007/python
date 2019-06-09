
def fav_team(**kwargs):
    ''' kwargs stores all the key value pairs as a dictionary'''
    print(kwargs)
    print(type(kwargs))
    for name, team in kwargs.items():
        # print(f"{name}'s fav club is {team}")
        print(name,team)

# fav_team(Saumi="Real Madrid", Kartik ="Manchester United", Mayank="Bayern Munich")

names = {"Saumi":"Real Madrid", "Kartik":"Manchester United", "Mayank":"Bayern Munich"}

#dictionary unpacking
fav_team(**names)