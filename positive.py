# encoding: utf-8

# These really use the 2.3.10.14... limits
TUNINGS = [
    ('Andromeda', 'biased 11-limit TE', 'te_11', 1200.3191, 497.6227),
    ('Andromeda', 'biased 11-limit POTE', 'pote_11', 1200.0000, 497.4904),
    ('Andromeda', 'biased 13-limit TE', 'te_13', 1200.4603, 497.4976),
    ('Andromeda', 'biased 13-limit POTE', 'pote_13', 1200.0000, 497.3069),
    ('Pythagorean', 'high precision', '', 1200.0, 498.045),
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
    for (tclass, tuning, label, octave, fourth) in TUNINGS:
        filename = '{}_29_f_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-5, 23, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths from Pythagorean F tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

    for (tclass, tuning, label, octave, fourth) in TUNINGS:
        filename = '{}_29_d_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-16, 12, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from D tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

    for (tclass, tuning, label, octave, fourth) in TUNINGS:
        filename = '{}_41_d_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-22, 18, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from D tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

    for (tclass, tuning, label, octave, fourth) in TUNINGS:
        filename = '{}_53_d_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-28, 24, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from D tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)
