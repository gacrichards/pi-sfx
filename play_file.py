from pygame import mixer
from mutagen.mp3 import MP3

import time
import os

# Initialize the pygame mixer
mixer.init()
script_dir = os.path.dirname(os.path.abspath(__file__))
# Load a sound file
def ghost_breath():
    play("eerie-ghostly-breath.mp3")
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
def toil_spell():
    play("witch-voice-double-double-toil-and-trouble-168410.mp3")
def come_in():
    play("shady-witch-voice-5-vol-001-159184.mp3")
def single_raven():
    play("RavenCallSingle%20PE914605.mp3")
def ravens():
    play("turk-ormannda-karga-sesi-130473.mp3")
def chanting():
    play("tibetan-monks-22297.mp3")
def demon_chant():
    play("demon-chant-latin-14489.mp3")
def music_box1():
    play("horror-music-box-147341.mp3")
def music_box2():
    play("strange-lullaby-28691.mp3")
def thunder():
    play("thunder-crack-31702.mp3")
def monster():
    play("lurking-horror-monster-143278.mp3")
def growl():
    play("demonic-halloween-horror-sound-3-vol-005-163997.mp3")
def witch_laugh():
    play("disturbing-horror-sound-2-creepy-laughter-vol-001-157464.mp3")
def beware():
    play("ominous-horror-sound-possessed-4-beware-vol-001-167398.mp3")

to_be_removed = [ 'raven-manymp3-14529.mp3', 'gate-heavy-openclose-wav-103288.mp3', 'crows-6371.mp3', 'tibetan-monks-22297.mp3', 'demon-chant-latin-14489.mp3', 'thunder-crack-31702.mp3']

all_files = ["eerie-ghostly-breath.mp3",
"spooky-wind.mp3",
"evil-laugh-loud.mp3",
"ghostly-female.mp3",
"ghostbreath.mp3",
"laughing.mp3",
"evil-laugh.mp3",
"wolf-howl.mp3",
"owl.mp3",
"door-creek.mp3",
"witch-voice-double-double-toil-and-trouble-168410.mp3",
"shady-witch-voice-5-vol-001-159184.mp3",
"magic-spell-in-weird-language-66118.mp3",
"raven-manymp3-14529.mp3",
"gate-heavy-openclose-wav-103288.mp3",
"crows-6371.mp3",
"RavenCallSingle%20PE914605.mp3",
"turk-ormannda-karga-sesi-130473.mp3",
"tibetan-monks-22297.mp3",
"demon-chant-latin-14489.mp3",
"horror-music-box-147341.mp3",
"strange-lullaby-28691.mp3",
"thunder-crack-31702.mp3",
"lurking-horror-monster-143278.mp3",
"demonic-halloween-horror-sound-3-vol-005-163997.mp3",
"disturbing-horror-sound-2-creepy-laughter-vol-001-157464.mp3",
"ominous-horror-sound-possessed-4-beware-vol-001-167398.mp3"]

def sort_working():
    works = []
    for next_file in all_files:
        if play(next_file):
            works.append(next_file)
    print(works)
            

def play(sound_file):
    try:
        print("plays sound")
        file_path = os.path.join(script_dir, sound_file)
        sound = mixer.Sound(file_path)
        # Play the sound
        sound.play()

        # Sleep for a few seconds while the sound plays
        time.sleep(sound.get_length())
        return True
    except:
        print("plays music")
        file_path = os.path.join(script_dir, sound_file)
        mixer.music.load(file_path)
        audio = MP3(file_path)
        duration_in_seconds = audio.info.length
        mixer.music.set_volume(0.1)
        mixer.music.play()
        time.sleep(duration_in_seconds)
        return False

def kill():
    # Clean up resource
    mixer.quit()
