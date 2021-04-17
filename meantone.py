# encoding: utf-8

TUNINGS = [
    ('7-limit TE', 'te', 1201.2422, 504.0263),
    ('7-limit POTE', 'pote', 1200.0000, 503.5051),
    ('43-equal', '43', 1200.0000, 1200.0 * 18 / 43),
    ]
OCTAVE, FOURTH = 19, 8

def get_scale(bottom, top, octave_cents, fourth_cents):
    pitches = []
    for fourth in range(bottom, top+1):
        octave = (fourth * FOURTH) // OCTAVE
        pitch = fourth * fourth_cents - octave * octave_cents
        ordinal = fourth * FOURTH - octave * OCTAVE
        if ordinal:
            pitches.append((ordinal, pitch))
    return [p for _o, p in sorted(pitches)] + [octave_cents]

#  Bx Ex Ax Dx Gx Cx Fx B♯ E♯ A♯ D♯ G♯ C♯ F♯ B  E  A  D  G  C  F
# -19-18-17-16-15-14-13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1  0  1

#  B  E  A  D  G  C  F  B♭ E♭ A♭ D♭ G♭ C♭ F♭ B♭♭E♭♭A♭♭D♭♭G♭♭
# -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9  10 11 12 13

if __name__ == '__main__':
    for tuning, label, octave, fourth in TUNINGS:
        filename = 'meantone_19_d_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-11, 7, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "meantone on C from Cb to E# tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = 'meantone_19_a_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-12, 6, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "meantone on C from Gb to B# tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = 'meantone_19_g_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-10, 8, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "meantone on C from Fb to A# tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = 'meantone_31_d_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-17, 13, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "meantone on C from Gbb to Ax tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)
