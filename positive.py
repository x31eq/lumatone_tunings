# encoding: utf-8

TUNINGS = [
    ('Andromeda', 'biased 11-limit TE', 'te_11', 1200.3191, 497.6227),
    ('Andromeda', 'biased 11-limit POTE', 'pote_11', 1200.0000, 497.4904),
    ('Andromeda', 'biased 13-limit TE', 'te_13', 1200.4603, 497.4976),
    ('Andromeda', 'biased 13-limit POTE', 'pote_13', 1200.0000, 497.3069),
    ('Cassandra', '13-limit TE', 'te_13', 1200.1727, 497.9591),
    ('Cassandra', '13-limit POTE', 'pote_13', 1200.0000, 497.8874),
    ('Garibaldi', '7-limit TE', 'te', 1200.1250, 497.9667),
    ('Garibaldi', '7-limit POTE', 'pote', 1200.0000, 497.9148),
    ('Helmholtz', '5-limit TE', 'te', 1200.0749, 498.2952),
    ('Helmholtz', '5-limit POTE', 'pote', 1200.0000, 498.2641),
    ('Pontiac', '7-limit TE', 'te', 1200.0989, 498.2844),
    ('Pontiac', '7-limit POTE', 'pote', 1200.0000, 498.2433),
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

def augment_scale(pitches):
    """
    Make the scale transposable by 2 octaves all within 63 steps
    """
    octave_steps = len(pitches)
    octave_pitch = pitches[-1]
    extra_notes = 62 - octave_steps
    extra_treble = extra_notes // 2
    extra_bass = extra_notes - extra_treble
    new_pitches = [octave_pitch + pitch for pitch in pitches[:extra_treble]]
    new_pitches += [octave_pitch + pitch for pitch in pitches[-extra_bass-1:-1]]
    assert len(new_pitches) == extra_notes
    return pitches + new_pitches + [octave_pitch * 2]

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
    for tclass, tuning, label, octave, fourth in TUNINGS:
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

        filename = '{}_29_a_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-15, 13, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from A tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = '{}_41_a_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-21, 19, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from A tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = '{}_53_a_{}.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = get_scale(-27, 25, octave, fourth)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from A tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = '{}_53_a_{}_zyn_hack.scl'.format(
                tclass.lower(), label)
        with open(filename, 'w') as out:
            pitches = augment_scale(get_scale(-27, 25, octave, fourth))
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    tclass
                    + " on C with fourths symmetrically from A tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)
