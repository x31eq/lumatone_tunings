#!/usr/bin/env python3

from fractions import Fraction
from math import log2

octave = 29
diatonic = '1/1 9/8 81/64 4/3 3/2 27/16 16/9'
comma = Fraction(352, 351)

gamut = [None] * octave

def scale_steps(pitch):
    return int(round(log2(pitch) * octave))

for pitch in map(Fraction, diatonic.split()):
    pitch_steps = scale_steps(pitch)
    for tonic in map(Fraction, '1/1 15/16 7/8 13/16'.split()):
        new_pitch = pitch * tonic
        new_steps = pitch_steps + scale_steps(tonic)
        while new_steps < 0:
            new_steps += octave
            new_pitch *= 2
        while new_steps >= octave:
            new_steps -= octave
            new_pitch /= 2
        alternative_pitch = new_pitch * comma
        if (tonic.numerator == 13
                and alternative_pitch.denominator < new_pitch.denominator):
            new_pitch = alternative_pitch
        assert gamut[new_steps] is None
        gamut[new_steps] = new_pitch

b_natural = Fraction(243, 128)
assert gamut[scale_steps(b_natural)] is None
gamut[scale_steps(b_natural)] = b_natural

gamut.sort()

with open('ji29.scl', 'w') as out:
    out.write("! ji29.scl\n!\n")
    out.write("13-limit JI tuning for a 29 note Bosanquet\n")
    out.write("29\n!\n")
    for pitch in gamut[1:]:
        out.write(str(pitch) + "\n")
    out.write("2/1\n")
