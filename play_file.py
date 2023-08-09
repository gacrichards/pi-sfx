from pygame import mixer
import time
import os

# Initialize the pygame mixer
mixer.init()
script_dir = os.path.dirname(os.path.abspath(__file__))
# Load a sound file
def welcome():
    play("evil-welcom.mp3")
def ghost_breath():
    play("eerie-ghostly-breath.mp3")
def wind():
    play("spooky-wind.mp3")
def loud_laugh():
    play("evil-laugh-loud.mp3")
def scary_lady():
    play("ghostly-female.mp3")
def ghost_breath2():
    play("ghostbreath.mp3")
def laughing():
    play("laughing.mp3")
def evil_laugh():
    play("evil-laugh.mp3")
def wolf():
    play("wolf-howl.mp3")
def owl():
    play("owl.mp3")
def door_creek():
    play("door-creek.mp3")
    
def play(sound_file):
    file_path = os.path.join(script_dir, sound_file)
    sound = mixer.Sound(file_path)
    # Play the sound
    sound.play()

    # Sleep for a few seconds while the sound plays
    time.sleep(sound.get_length())

def kill():
    # Clean up resource
    mixer.quit()
