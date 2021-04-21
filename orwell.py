# encoding: utf-8

TUNINGS = [
    ('11-limit TE', 'te', 1200.6045, 271.5628),
    ('11-limit POTE', 'pote', 1200.0000, 271.4261),
    ('22-equal', '22', 1200.0, 12e2 * 5 / 22),
    ('31-equal', '31', 1200.0, 12e2 * 7 / 31),
    ('53-equal', '53', 1200.0, 12e2 * 12 / 53),
    ('84-equal', '84', 1200.0, 12e2 * 19 / 84),
    ]
OCTAVE, THIRD = 84, 19

def get_scale(bottom, top, octave_cents, third_cents):
    pitches = []
    for third in range(bottom, top+1):
        octave = (third * THIRD) // OCTAVE
        pitch = third * third_cents - octave * octave_cents
        ordinal = third * THIRD - octave * OCTAVE
        if ordinal:
            pitches.append((ordinal, pitch))
    return [p for _o, p in sorted(pitches)] + [octave_cents]

def write_tuning(prefix, comment, low, high, tuning, label, octave, third):
    pitches = get_scale(low, high, octave, third)
    if str(len(pitches)) == label:
        # Trivial equal temperament: skip
        return
    filename = '{}_{}.scl'.format(prefix, label)
    with open(filename, 'w') as out:
        out.write("! " + filename + "\n")
        out.write("!\n")
        out.write("{} tuned to {}\n".format(comment, tuning))
        out.write("%i\n" % len(pitches))
        out.write("!\n")
        for pitch in pitches:
            out.write("%.3f\n" % pitch)

#  D-----A-----E-----B
#   \   / \   / \   / \
#    \ /   \ /   \ /   \
#     F-----C-----G-----D

# -17   -10   -3     4
#   \   / \   / \   / \
#    \ /   \ /   \ /   \
#    -7     0     7    14

if __name__ == '__main__':
    for tuning in TUNINGS:
        comment = "Orwell on C for C major with ii triad"
        write_tuning('orwell_31_c_ii', comment, -17, 13, *tuning)

        comment = "Orwell on C for C major with V triad"
        write_tuning('orwell_31_c_V', comment, -16, 14, *tuning)

        comment = "Orwell with equal generators up and down"
        write_tuning('orwell_31_symmetric', comment, -15, 15, *tuning)

        comment = "Orwell on C without a major key"
        write_tuning('orwell_22_c', comment, -12, 9, *tuning)

        comment = "Orwell on C around C major"
        write_tuning('orwell_53_c', comment, -27, 25, *tuning)
