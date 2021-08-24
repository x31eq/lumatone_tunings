import re, sys

bases = 'C C# D D# E F F# G G# A A# B'.split()

cents = [0.0] + re.findall(r'\d+\.\d+', open(sys.argv[1]).read())
_octave = cents.pop()

for index in range(-60, 68):
    keyboard_register = index // 12 + 3
    pitch_register = index // len(cents) + 3
    pitch = cents[index % len(cents)]
    semitones = float(pitch) / 100
    base = int(round(semitones))
    fraction = semitones - base
    yamahas = round(fraction * 64)
    key = bases[index % len(bases)]
    print("%-2s%i  %-2s%i %+3i" %
        (key, keyboard_register, bases[base % 12], pitch_register, yamahas))
