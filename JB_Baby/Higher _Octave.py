
# Justin Bieber - Baby Chorus - HighLayer
# Octave-up layer to add brightness / air

#
# Trick:
#  Reuse the same structure (groovy_intro -> main_chorus -> groovy_outro),
#  but transpose every note up +12 semitones inside tn().


def tn(p, b): playNote(p + 12, beats=b)  # transpose +12
def rr(b):    rest(b)

def groovy_intro_hi():
    for _ in range(2):
        # Bar A
        tn(60,0.4); rr(0.1)
        tn(63,0.4); rr(0.1)
        tn(67,0.5); rr(0.1)
        tn(65,0.4); rr(0.1)
        tn(68,0.4); rr(0.2)
        tn(72,0.6); rr(0.2)
        tn(70,0.3); tn(72,0.3); tn(74,0.4); rr(0.3)

        # Bar B
        tn(63,0.25); tn(64,0.25); tn(65,0.25); tn(67,0.4); rr(0.1)
        tn(70,0.4); tn(72,0.4); rr(0.2)
        tn(67,0.6); rr(0.4)

    tn(67,1.0); rr(0.4)

def phrase_baby_hi(end_note, end_hold):
    tn(67,1.0); rr(0.1)
    tn(65,0.5); rr(0.1)

    tn(67,0.9); rr(0.1)
    tn(65,0.5); rr(0.15)

    tn(67,1.2); rr(0.1)

    tn(end_note, end_hold); rr(0.4)

def phrase_mine_hi():
    tn(67,0.9); rr(0.1)
    tn(65,0.7); rr(0.1)
    tn(67,1.0); rr(0.2)

    tn(65,0.25); rr(0.05)
    tn(67,1.4); rr(0.2)

    tn(65,0.6); rr(0.15)
    tn(63,0.5); rr(0.1)
    tn(62,0.4); rr(0.1)
    tn(63,1.4); rr(0.5)

def main_chorus_hi():
    phrase_baby_hi(end_note=70+12, end_hold=1.6)  # OH (A#/Bb up an octave)
    phrase_baby_hi(end_note=72+12, end_hold=1.8)  # NO (C up an octave)
    phrase_baby_hi(end_note=70+12, end_hold=1.2)  # OH again
    phrase_mine_hi()

def groovy_outro_hi():
    tn(65,0.4); tn(68,0.4); tn(72,0.4); rr(0.1)
    tn(67,0.4); tn(70,0.4); tn(74,0.4); rr(0.2)

    tn(72,0.3); tn(70,0.3); tn(67,0.6); rr(0.2)
    tn(65,0.4); tn(63,0.4); tn(62,0.6); rr(0.2)

    for _ in range(2):
        tn(65,0.4); tn(67,0.4); tn(70,0.4); rr(0.15)
        tn(63,0.4); tn(65,0.4); tn(67,0.5); rr(0.2)

    tn(67,0.4); tn(70,0.4); tn(74,0.6); rr(0.2)
    tn(72,0.4); tn(70,0.4); tn(67,0.8); rr(0.3)
    tn(65,0.7); rr(0.2)
    tn(63,0.8); rr(0.2)
    tn(60,2.0); rr(0.5)

# Play order:
groovy_intro_hi()
main_chorus_hi()
groovy_outro_hi()
