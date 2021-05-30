#!/usr/bin/env python3

from fractions import Fraction
from math import log2

octave = 29
chord = '1/1 9/8 5/4 11/8 3/2 13/8 7/4 15/8'
comma = Fraction(352, 351)

gamut = [None] * octave

def scale_steps(pitch):
    return int(round(log2(pitch) * octave))

for pitch in map(Fraction, chord.split()):
    pitch_steps = scale_steps(pitch)
    for tonic in map(Fraction, '1/1 9/8 4/3 3/2 27/16 16/9'.split()):
        new_pitch = pitch * tonic
        new_steps = pitch_steps + scale_steps(tonic)
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
            print("Discrepancy: {}, {}".format(new_pitch, old_pitch))
            if new_pitch.denominator < old_pitch.denominator:
                gamut[new_steps] = new_pitch


for pitch in map(Fraction, '1/1 9/8 81/64 4/3 3/2 27/16'.split()):
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
        if gamut[new_steps] is None:
            print("New pitch needed: {}".format(new_pitch))
            gamut[new_steps] = new_pitch

gamut.sort()

with open('ji29.scl', 'w') as out:
    out.write("! ji29.scl\n!\n")
    out.write("13-limit JI tuning for a 29 note Bosanquet\n")
    out.write("29\n!\n")
    for pitch in gamut[1:]:
        out.write(str(pitch) + "\n")
    out.write("2/1\n")
