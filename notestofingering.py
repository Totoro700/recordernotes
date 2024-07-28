import time, os
fingerings = {
    'E': '0 3 2',
    'F#': '0 3 1',
    'G': '0 3 0',
    'A': '0 2 0',
    'D': '0 3 3',
    'C4': '0 3 4',
    'B': '0 1 0',
    'C5': '0 -1/2',
    'D#': '0 3 3.5',
    'A#': '0 1.5 0'
}

# Function to convert a list of notes to their fingerings
def convert_notes_to_fingerings(notes):
    return [fingerings[note] for note in notes if note in fingerings]

# Example list of notes
notes = input("Notes to convert: (format like this without quotation marks: \"E C5 D A# D#\", see docs for list of notes available)" ).split(" ")

# Convert the notes to fingerings
fingerings_list = convert_notes_to_fingerings(notes)

final = []

# Print the results
for note, fingering in zip(notes, fingerings_list):
    print(f'{note}: {fingering}')
    final.append(f'{note}: {fingering}')

os.system('echo ' + ''.join(final) + '| clip')
time.sleep(999)