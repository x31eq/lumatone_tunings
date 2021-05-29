#!/usr/bin/env python3

from fractions import Fraction

diatonic = [Fraction(x) for x in
        '1/1 9/8 81/64 4/3 3/2 27/16 243/128'.split()]
comma = Fraction(352, 351)

gamut = []

for pitch in diatonic:
    for new_pitch in pitch, pitch * 15/16, pitch * 7/8, pitch * 13/16:
        while new_pitch < 1:
            new_pitch *= 2
        while new_pitch >= 2:
            new_pitch /= 2
        alternative_pitch = new_pitch * comma
        if alternative_pitch.denominator < new_pitch.denominator:
            new_pitch = alternative_pitch
        gamut.append(new_pitch)
gamut.append(Fraction(4, 3) * 13/12)  # Pythogorean F♯

gamut.sort()

with open('ji29.scl', 'w') as out:
    out.write("! ji29.scl\n!\n")
    out.write("13-limit JI tuning for a 29 note Bosanquet\n")
    out.write("29\n!\n")
    for pitch in gamut[1:]:
        out.write(str(pitch) + "\n")
    out.write("2/1\n")
