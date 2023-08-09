from pygame import mixer
import time

# Initialize the pygame mixer
mixer.init()

# Load a sound file

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
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()

    # Sleep for a few seconds while the sound plays
    time.sleep(sound.get_length())

def kill():
    # Clean up resource
    mixer.quit()
