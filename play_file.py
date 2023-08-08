import pygame
import time

# Initialize the pygame mixer
pygame.mixer.init()

# Load a sound file
sound_file = "wolf-howl.mp3"  # Replace with the path to your sound file
sound = pygame.mixer.Sound(sound_file)

# Play the sound
sound.play()

# Sleep for a few seconds while the sound plays
time.sleep(sound.get_length())

# Clean up resources
pygame.mixer.quit()

