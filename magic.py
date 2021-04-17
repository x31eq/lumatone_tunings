# encoding: utf-8

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

#  D-----A-----E-----B-----F♯
#   \   / \   / \   / \   / \
#    \ /   \ /   \ /   \ /   \
#     F-----C-----G-----D-----A

# -9    -4     1     6    11
#   \   / \   / \   / \   / \
#    \ /   \ /   \ /   \ /   \
#    -5     0     5    10    15

if __name__ == '__main__':
    for tuning in TUNINGS:
        comment = "Magic on C from Ab to E#"
        write_tuning('pengcheng_countdown', comment, -1, 17, *tuning)

        comment = "Magic on C from F to Cx"
        write_tuning('pengcheng_giant_steps', comment, -5 ,13, *tuning)

        comment = "Magic on C for C major with ii triad"
        write_tuning('pengcheng_c_ii', comment, -9, 9, *tuning)

        comment = "Magic on C for C major with V triad (ma grama)"
        write_tuning('pengcheng_c_V', comment, -8, 10, *tuning)

        comment = "Magic on C for G major with ii triad",
        write_tuning('pengcheng_g_ii', comment, -4, 14, *tuning)

        comment = "Magic on C for G major with V triad (ma grama)"
        write_tuning('pengcheng_g_V', comment, -3, 15, *tuning)

        comment = "Magic on C for C major"
        write_tuning('haizhou_c', comment, -10, 11, *tuning)

        comment = "Magic on C for G major"
        write_tuning('haizhou_g', comment, -5, 16, *tuning)
