#!/usr/bin/env python3

from fractions import Fraction
from math import log2

octave = 41
chord = '1/1 9/8 6/5 5/4 11/8 3/2 13/8 7/4 15/8'

gamut = [None] * octave

def scale_steps(pitch):
    return int(round(log2(pitch) * octave))

for tonic in map(Fraction, '1/1 4/3 3/2 9/8 27/16 16/9'.split()):
    for pitch in map(Fraction, chord.split()):
        new_pitch = pitch * tonic
        new_steps = scale_steps(pitch) + scale_steps(tonic)
        while new_steps < 0:
            new_steps += octave
            new_pitch *= 2
        while new_steps >= octave:
            new_steps -= octave
            new_pitch /= 2
        old_pitch = gamut[new_steps]
        if old_pitch is None:
            gamut[new_steps] = new_pitch
        elif new_pitch != old_pitch:
            print("Discrepancy: {} ≠ {}, comma {}".format(
                new_pitch, old_pitch, new_pitch / old_pitch))

assert gamut[8] is None
gamut[8] = Fraction(8, 7)

assert gamut[10] is None
gamut[10] = Fraction(243, 128) * 5/4 / 2

assert gamut[15] is None
gamut[15] = Fraction(9, 7)

# Pythagorean F♯
assert gamut[21] is None
gamut[21] = Fraction(3 ** 6, 2 ** 9)

assert gamut[25] is None
gamut[25] = Fraction(81, 80) * 3/2

assert gamut[32] is None
gamut[32] = Fraction(12, 7)

assert gamut[39] is None
gamut[39] = Fraction(27, 14)

with open('ji41.scl', 'w') as out:
    out.write("! ji41.scl\n!\n")
    out.write("13-limit JI tuning for a 41 note Bosanquet\n")
    out.write("41\n!\n")
    for pitch in gamut[1:]:
        out.write(str(pitch) + "\n")
    out.write("2/1\n")
