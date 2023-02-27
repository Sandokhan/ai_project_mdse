from Mancala_play import Mancala
from PIL import Image
import os

# Define the directory containing the PNG images
directory = 'images/'

# Loop through each PNG file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # Open the PNG file
        im = Image.open(os.path.join(directory, filename))

        # Remove the ICCP chunk from the metadata
        if 'icc_profile' in im.info:
            del im.info['icc_profile']

        # Save the modified PNG file
        im.save(os.path.join(directory, filename))

# Set up the background
board_image_path = "images/background.png"

# Set up the board images
background_image_path = "images/board.png"

# Set up the seed images
seed_image_path = "images/seed.png"

Current_game = Mancala(board_image_path, seed_image_path, background_image_path)
Current_game.play_game()