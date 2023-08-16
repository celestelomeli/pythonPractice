
#List of letters and their corresponding points 
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Create a dictionary that maps letters to their corresponding points
letter_to_points = {letters:points for letters, points in zip(letters, points)}

#Add a key-value pair for a space character equal to 0 points
letter_to_points[" "] = 0
print(letter_to_points)

#Define a function to calculate the score of a word based on letter points
def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i, 0)
  return point_total

#Calculate and print the points for the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Dictionary mapping players to their played words  
player_to_words = {
  "player1" : ["BLUE", "TENNIS", "EXIT"],
  "wordNerd" : ["EARTH", "EYES", "MACHINE"],
  "Lexi Con" : ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader" : ["ZAP", "COMA", "PERIOD"]
}

#Dictionary to store players' total points
player_to_points = {}

#Function to update the point totals for each player
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

#Function to add a word for a player and update their points
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

#Play the word "CODE" for "player1"
play_word("player1", "CODE")
print(player_to_words)

#print the total points for each player 
print(player_to_points)