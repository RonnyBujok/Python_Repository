import csv
import os
from pydub import AudioSegment, silence
from pydub.playback import play

# We have three conditions: High Frequency (HF), Low Frequency (LF), and Non-Words (NW).
# All words for each condition are stored in one .wav file.
# Your task is to:
#       split the words on the silence
#       make sure they all have the same loudness
#       save them in a folder corresponding to their condition (folder names: HF, LF, NW)

path_to_repository = "K:\\01. Ronny_PhD\\02. IMPRS\\Courses\\Python\\session2b-sound\\session2b-sound"  # add your own path here!

# This piece of code is here to help you.
# It reads a text file with information about the stimuli you are going to split (names & condition),
# and returns a dictionary named 'stimuli' with condition as key, and the word itself as value.
# Use this dictionary to name the files you have to save.
stimuli_info = open(os.path.join(path_to_repository, "lexdec_stimuli.txt"))
stimuli_reader = csv.reader(stimuli_info, delimiter=',')
headers = next(stimuli_reader, None)

# Create the dictionary
stimuli = {}
for stimulus in stimuli_reader:
    if stimulus[2] not in stimuli.keys():
        stimuli[stimulus[2]] = list()
    stimuli[stimulus[2]].append(stimulus[3])

# Put them in alphabetical order
for condition, words in stimuli.items():
    sort = sorted(words)
    stimuli[condition] = sort

# change the non-word condition name
stimuli["NW"] = stimuli.pop("none")

# Now you have the stimulus names. Let's take a look at the dictionary:
# print(stimuli)




# YOUR CODE HERE.




# where are the soundfiles?
sound_folder = "K:\\01. Ronny_PhD\\02. IMPRS\\Courses\\Python\\session2b-sound\\session2b-sound\\raw"

# create silence
silent_time = AudioSegment.silent(duration=200)

conditions = ['HF', 'LF', 'NW']

# create new folders for all three conditions

for condition in conditions:
    new_folder = "K:\\01. Ronny_PhD\\02. IMPRS\\Courses\\Python\\session2b-sound\\session2b-sound\\" + condition
    if not os.path.isdir(new_folder):
        os.mkdir(new_folder)

    sound_name = condition + "_recording.wav"
    sound_path = os.path.join(sound_folder, sound_name)
    sound = AudioSegment.from_wav(sound_path)

    list = silence.split_on_silence(sound, min_silence_len=200, silence_thresh=-50)

    list_normalized = []

    target_volume = -6

    for sound in list:
        change = target_volume - sound.dBFS
        target_sound = sound.apply_gain(change)
        list_normalized.append(target_sound)

    for i in range(len(list_normalized)):
        sound = list_normalized[i]
        filename = stimuli[condition][i] + '.wav'
        new_path = os.path.join(new_folder, filename)
        sound.export(new_path, format='wav')



# Some hints:
# 1. Where are the stimuli? check
# 2. How loud do you want your stimuli to be? Store it in a variable check
# 3. Where do you want to save your files? Make separate folders for the conditions. check
# 4. Do you normalize the volume for the whole sequence or for separate words? Why (not)? Try it if you like :)
# must be for every stimulus individually because the average for every stimulus will be different
# check
# 5. You can check whether your splitting worked by playing the sound, or by printing the length of the resulting list
# CHECK
# 6. Use the index of the word [in the list of words you get after splitting]
# to get the right text from the dictionary. check
# 7. Recall you can plot your results to see what you have done.
# Good luck!
