prob_w_f = 0.8
prob_w_c = 0.6

prob_l_f = 1 - prob_w_f
prob_l_c = 1 - prob_w_c

sets = 3

# Probability of winning 2 (two) sets in a row in a three sets game.
# Possible outcomes:
#	W-W-W
#	W-W-L
#	L-W-W

# Starter function
def main():
	prob_w_fcf = 0 # Probability of Winning in the F-C-F order
	prob_w_cfc = 0 # Probability of Winning in the C-F-C order
	possible_predictions  = ['W-W-W', 'W-W-L', 'L-W-W']

	for i in range(len(possible_predictions)):
		prob_w_fcf += calc_game_win_prediction(possible_predictions[i], 'F-C-F')
		prob_w_cfc += calc_game_win_prediction(possible_predictions[i], 'C-F-C')

	print("Probability of winning F-C-F:", round(prob_w_fcf, 4))
	print("Probability of winning C-F-C:", round(prob_w_cfc, 4))
		
# Get the Game winning prediction
def calc_game_win_prediction(set_predictions, set_play_order_s):
	set_outcomes_arr = set_predictions.split('-')
	set_play_order_arr = set_play_order_s.split('-') 

	game_win_prediction = 1 

	# Sum each set prediction
	for i in range(len(set_outcomes_arr)):
		game_win_prediction *= get_probability(set_outcomes_arr[i], set_play_order_arr[i])

	return game_win_prediction

# Converts W or L to the actual individual probability for the given player
# Params:
#    prediction:
#	- w: Win
#	- l: Lose
#    player:
#	- f: Father
#	- c: Champion
def get_probability(outcome = 'w', player = 'f'):
	if (outcome.lower() == 'w' and player.lower() == 'f'):
		return prob_w_f
	elif (outcome.lower() == 'l' and player.lower() == 'f'):
		return prob_l_f
	elif (outcome.lower() == 'w' and player.lower() == 'c'):
		return prob_w_c
	elif (outcome.lower() == 'l' and player.lower() == 'c'):
		return prob_l_c
	else:
		return 0

# Execute the main function
main()
