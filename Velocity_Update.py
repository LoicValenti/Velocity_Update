from mido import MidiFile

def print_hi(name):
    print(f'Hi, {name}')

import os

directory = "midi_files"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if filename.endswith(".mid"):
        print(os.path.join(directory, filename))
        mid = MidiFile(f)

        for track in mid.tracks:
            for i, msg in enumerate(track):
                if msg.is_cc(7):
                    print('Volume changed to', 0)

        mid.save('updated_velocity_{}'.format(filename))

if __name__ == '__main__':
    print_hi('velocity updated')

