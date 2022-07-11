# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#players 
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

#goals scored in match minutes
goal_0 = 32
goal_1 = 54

"""creating a string with the + operator 
    to display the players name and
    the minute they scored"""
    
scorers = player_0 + ' ' + str(goal_0)+ ", " + player_1 + ' ' + str(goal_1)
print(scorers)

# using a f string with line break to report the match status
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)



#Part 2

player = 'Jan Wouters'

# use slicing and find method to isolate and store the players first name
first_name = player[:player.find(" ")]
print(first_name)

# use find, slicing and len to isolate and store the length of the last name
last_name_len = len(player[player.find(" ")+1:]) 
print(last_name_len)

# use f-string, slicing and find method for short_name
name_short = f'{player[:1]}.{player[player.find(" "):]}'
print(name_short)

# use + operator and len to produce a chant
chant_2 = (first_name + "!" + " ")  * len(first_name)
print(chant_2)

# use .join and .rstrip to remove the space at the end of the string
chant = "".join(chant_2.rstrip())
print(chant)

# comparing the 2 chants to check if the space is removed
good_chant = chant_2 != chant
print(good_chant)
