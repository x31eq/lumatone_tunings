# encoding: utf-8

TUNINGS = [
    ('11-limit TE', 'te', 1200.7635, 116.7070),
    ('11-limit POTE', 'pote', 1200.0000, 116.6327),
    ('31-equal', '31', 1200.0, 12e2 * 3 / 31),
    ('41-equal', '41', 1200.0, 12e2 * 4 / 41),
    ('72-equal', '72', 1200.0, 12e2 * 7 / 72),
    ]
OCTAVE, GENERATOR = 72, 7

def get_scale(bottom, top, octave_cents, generator_cents):
    pitches = []
    for generator in range(bottom, top+1):
        octave = (generator * GENERATOR) // OCTAVE
        pitch = generator * generator_cents - octave * octave_cents
        ordinal = generator * GENERATOR - octave * OCTAVE
        if ordinal:
            pitches.append((ordinal, pitch))
    return [p for _o, p in sorted(pitches)] + [octave_cents]

def write_tuning(prefix, comment, low, high, tuning, label, octave, generator):
    pitches = get_scale(low, high, octave, generator)
    if str(len(pitches)) == label:
        # Trivial equal temperament: skip
        return
    filename = '{}_{}.scl'.format(prefix, label)
    with open(filename, 'w') as out:
        out.write("! " + filename + "\n")
        out.write("!\n")
        out.write("{} {}\n".format(comment, tuning))
        out.write("%i\n" % len(pitches))
        out.write("!\n")
        for pitch in pitches:
            out.write("%.3f\n" % pitch)

#  D-----A-----E-----B
#   \   / \   / \   / \
#    \ /   \ /   \ /   \
#     F-----C-----G-----D

# -19   -13   -7    -1
#   \   / \   / \   / \
#    \ /   \ /   \ /   \
#    -6     0     6    12

if __name__ == '__main__':
    for tuning in TUNINGS:
        comment = "Miracle on C for C major with ii triad tuned to"
        write_tuning('miracle_31_c_ii', comment, -19, 11, *tuning)

        comment = "Miracle on C for C major with V triad tuned to"
        write_tuning('miracle_31_c_V', comment, -18, 12, *tuning)

        comment = "Miracle on C around C major"
        write_tuning('miracle_41_c', comment, -23, 17, *tuning)

        comment = "Miracle on C around C major"
        write_tuning('miracle_72_c', comment, -41, 29, *tuning)
