TE = 1200.1435, 380.7419
POTE = 1200.0000, 380.6964
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
    for tuning, (octave, third) in ('TE', TE), ('POTE', POTE):
        filename = 'pengcheng_countdown_' + tuning.lower() + '.scl'
        with open(filename, 'w') as out:
            pitches = get_scale(-1, 17, octave, third)
            out.write("! " + filename + "\n")
            out.write("!\n")
            out.write(
                    "magic on C from Ab to E# tuned to 11-limit "
                    + tuning + "\n")
            out.write("%i\n" % len(pitches))
            out.write("!\n")
            for pitch in pitches:
                out.write("%.3f\n" % pitch)

        filename = 'pengcheng_giant_steps_' + tuning.lower() + '.scl'
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
