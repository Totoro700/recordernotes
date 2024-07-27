import time, os
fingerings = {
    'E4': '0 3 2',
    'F#4': '0 3 1',
    'G4': '0 3 0',
    'A4': '0 2 0',
    'D4': '0 3 3',
    'C4': '0 3 4',
    'B4': '0 1 0',
    'C5': '0 -1/2',
    'D#4': '0 3 3.5',
    'A#4': '0 1.5 0'
}

# Function to convert a list of notes to their fingerings
def convert_notes_to_fingerings(notes):
    return [fingerings[note] for note in notes if note in fingerings]

# Example list of notes
notes = input("Notes to convert: (format like this without quotation marks: \"E4 C5 D4 A#4 D#4\", see docs for list of notes available)" ).split(" ")

# Convert the notes to fingerings
fingerings_list = convert_notes_to_fingerings(notes)

final = []

# Print the results
for note, fingering in zip(notes, fingerings_list):
    print(f'{note}: {fingering}')
    final.append(f'{note}: {fingering}')

os.system('echo ' + ''.join(final) + '| clip')
time.sleep(999)