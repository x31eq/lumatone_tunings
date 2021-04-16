# encoding: utf-8

# These really use the 2.3.10.14... limits
TUNINGS = [
    ('11-limit TE', 'te_11', 1200.3191, 497.6227),
    ('11-limit POTE', 'pote_11', 1200.0000, 497.4904),
    ('13-limit TE', 'te_13', 1200.4603, 497.4976),
    ('13-limit POTE', 'pote_13', 1200.0000, 497.3069),
    ]
OCTAVE, FOURTH = 53, 22

def get_scale(bottom, top, octave_cents, fourth_cents):
    pitches = []
    for fourth in range(bottom, top+1):
        octave = (fourth * FOURTH) // OCTAVE
        pitch = fourth * fourth_cents - octave * octave_cents
        ordinal = fourth * FOURTH - octave * OCTAVE
        if ordinal:
            pitches.append((ordinal, pitch))
    return [p for _o, p in sorted(pitches)] + [octave_cents]

#   B/  E/  A/  D/  G/  C/  F/
#  -17 -16 -15 -14 -13 -12 -11

#   A♯  D♯  G♯  C♯  F♯
#  -10  -9  -8  -7  -6

#   B   E   A   D   G   C   F   B♭  E♭  A♭  D♭  G♭
#  -5  -4  -3  -2  -1   0   1   2   3   4   5   6

#   B\  E\  A\  D\  G\  C\  F\  B♭\ E♭\ A♭\ D♭\ G♭\
#   7   8   9   10  11  12  13  14  15  16  17  18

#   B♭^ E♭^ A♭^ D♭^ G♭^
#   19  20  21  22  23

if __name__ == '__main__':
    for (tuning, label, octave, fourth) in TUNINGS:
        filename = 'andromeda_29_f_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-5, 23, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "andromeda on C with fourths from Pythagorean F tuned to biased "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

    for (tuning, label, octave, fourth) in TUNINGS:
        filename = 'andromeda_41_d_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-22, 18, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "andromeda on C with fourths symmetrically from D tuned to biased "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

    for (tuning, label, octave, fourth) in TUNINGS:
        filename = 'andromeda_53_d_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-28, 24, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "andromeda on C with fourths symmetrically from D tuned to biased "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)
