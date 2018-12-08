"""
 ______   __  __   ________   ___   __    ______
/_____/\ /_/\/_/\ /_______/\ /__/\ /__/\ /_____/\
\:::_ \ \\ \ \ \ \\::: _  \ \\::\_\\  \ \\:::_ \ \
 \:(_) \ \\:\_\ \ \\::(_)  \ \\:. `-\  \ \\:\ \ \ \
  \: ___\/ \::::_\/ \:: __  \ \\:. _    \ \\:\ \ \ \
   \ \ \     \::\ \  \:.\ \  \ \\. \`-\  \ \\:\_\ \ \
    \_\/      \__\/   \__\/\__\/ \__\/ \__\/ \_____\/


py-ano
Ver. 1.0
5/7/2018
haythamm

Takes txt files containing digits from given directory and creates a sythesized representation of them.
numbers 0-9 are assigned ascending notes, with the length of each note depending on whether or not the
previous number is a multiple of 2, 3.

Note: Performance can be improved by initially rendering each note and concatenating the audio files prerendered files
    in the correct order, however overlap may be required for smoothness.

"""
import pysynth_s as psb
import os

if not os.path.exists("output"):
    os.makedirs("output")
if not os.path.exists("py_files"):
    os.makedirs("py_files")

path = os.getcwd()
print(path)
# Place txt file(s) containing the digits you would like to synthesize in the py_files folder
for filename in os.listdir('py_files'):
    track = []  # Holds the notes to be synthesized
    lst = []  # Holds the raw digits of pi

    # Fill the lst with digits from the file.
    print("Now processing " + filename)
    with open('py_files/' + filename, 'r') as f:
        for line in f.readline():
            for chars in line:
                lst.append(chars)

    # Fills track with notes
    last = 0
    for num in lst:
        last = int(last)
        if num == '0':
            if last % 2 == 0:
                track.append(('g2', 4))

            elif last % 3 == 0:
                track.append(('g2', 3))

            else:
                track.append(('g2', 2))

        if num == '1':
            if last % 2 == 0:
                track.append(('b2', 4))

            elif last % 3 == 0:
                track.append(('b2', 3))

            else:
                track.append(('b2', 2))

        if num == '2':
            if last % 2 == 0:
                track.append(('d#3', 4))

            elif last % 3 == 0:
                track.append(('d#3', 3))

            else:
                track.append(('d#3', 2))

        if num == '3':
            if last % 2 == 0:
                track.append(('g3', 4))

            elif last % 3 == 0:
                track.append(('g3', 3))

            else:
                track.append(('g3', 2))

        if num == '4':
            if last % 2 == 0:
                track.append(('b3', 4))

            elif last % 3 == 0:
                track.append(('b3', 3))

            else:
                track.append(('b3', 2))

        if num == '5':
            if last % 2 == 0:
                track.append(('d#4', 4))

            elif last % 3 == 0:
                track.append(('d#4', 3))

            else:
                track.append(('d#4', 2))

        if num == '6':
            if last % 2 == 0:
                track.append(('g4', 4))

            elif last % 3 == 0:
                track.append(('g4', 3))

            else:
                track.append(('g4', 2))

        if num == '7':
            if last % 2 == 0:
                track.append(('b4', 4))

            elif last % 3 == 0:
                track.append(('b4', 3))

            else:
                track.append(('b4', 2))

        if num == '8':
            if last % 2 == 0:
                track.append(('d#5', 4))

            elif last % 3 == 0:
                track.append(('d#5', 3))

            else:
                track.append(('d#5', 2))

        if num == '9':
            if last % 2 == 0:
                track.append(('g5', 4))

            elif last % 3 == 0:
                track.append(('g5', 3))

            else:
                track.append(('g5', 2))

        last = num

    psb.make_wav(track, fn=filename[:-4] + ".wav")  # Builds track into audio file

    # Organize Things
    os.rename(filename[:-4] + ".wav", "output/" + filename[:-4] + ".wav")
    print(filename[:-4] + " is complete!")
