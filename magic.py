TUNINGS = [
    ('11-limit TE', 'te', 1200.1435, 380.7419),
    ('11-limit POTE', 'pote', 1200.0000, 380.6964),
    ('19-equal', '19', 1200.0, 12e2 * 6 / 19),
    ('22-equal', '22', 1200.0, 12e2 * 7 / 22),
    ('41-equal', '41', 1200.0, 12e2 * 13 / 41),
    ('60-equal', '60', 1200.0, 12e2 * 19 / 60),
    ]
OCTAVE, THIRD = 19, 6

def get_scale(bottom, top, octave_cents, third_cents):
    pitches = []
    for third in range(bottom, top+1):
        octave = (third * THIRD) // OCTAVE
        pitch = third * third_cents - octave * octave_cents
        ordinal = third * THIRD - octave * OCTAVE
        if ordinal:
            pitches.append((ordinal, pitch))
    return [p for _o, p in sorted(pitches)] + [octave_cents]

if __name__ == '__main__':
    for tuning, label, octave, third in TUNINGS:
        filename = 'pengcheng_countdown_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-1, 17, octave, third)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "magic on C from Ab to E# tuned to "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = 'pengcheng_giant_steps_' + label + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-5, 13, octave, third)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "magic on C from F to Cx tuned to 11-limit "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)
