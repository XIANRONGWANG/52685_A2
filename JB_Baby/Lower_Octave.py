
# # Justin Bieber - Baby Chorus - LowLayer
# Octave-down layer for weight/body
#
# This uses tl() which transposes DOWN an octave.

def tl(p, b): playNote(p - 12, beats=b)  # transpose -12
def rr(b):    rest(b)

def groovy_intro_lo():
    for _ in range(2):
        tl(60,0.4); rr(0.1)
        tl(63,0.4); rr(0.1)
        tl(67,0.5); rr(0.1)
        tl(65,0.4); rr(0.1)
        tl(68,0.4); rr(0.2)
        tl(72,0.6); rr(0.2)
        tl(70,0.3); tl(72,0.3); tl(74,0.4); rr(0.3)

        tl(63,0.25); tl(64,0.25); tl(65,0.25); tl(67,0.4); rr(0.1)
        tl(70,0.4); tl(72,0.4); rr(0.2)
        tl(67,0.6); rr(0.4)

    tl(67,1.0); rr(0.4)

def phrase_baby_lo(end_note, end_hold):
    tl(67,1.0); rr(0.1)
    tl(65,0.5); rr(0.1)

    tl(67,0.9); rr(0.1)
    tl(65,0.5); rr(0.15)

    tl(67,1.2); rr(0.1)

    tl(end_note, end_hold); rr(0.4)

def phrase_mine_lo():
    tl(67,0.9); rr(0.1)
    tl(65,0.7); rr(0.1)
    tl(67,1.0); rr(0.2)

    tl(65,0.25); rr(0.05)
    tl(67,1.4); rr(0.2)

    tl(65,0.6); rr(0.15)
    tl(63,0.5); rr(0.1)
    tl(62,0.4); rr(0.1)
    tl(63,1.4); rr(0.5)

def main_chorus_lo():
    # Two options:
    # 1) Keep this ON for huge cinematic weight
    # 2) Comment this whole call out during recording of  “clean chorus”
    phrase_baby_lo(end_note=70-12, end_hold=1.6)
    phrase_baby_lo(end_note=72-12, end_hold=1.8)
    phrase_baby_lo(end_note=70-12, end_hold=1.2)
    phrase_mine_lo()

def groovy_outro_lo():
    tl(65,0.4); tl(68,0.4); tl(72,0.4); rr(0.1)
    tl(67,0.4); tl(70,0.4); tl(74,0.4); rr(0.2)

    tl(72,0.3); tl(70,0.3); tl(67,0.6); rr(0.2)
    tl(65,0.4); tl(63,0.4); tl(62,0.6); rr(0.2)

    for _ in range(2):
        tl(65,0.4); tl(67,0.4); tl(70,0.4); rr(0.15)
        tl(63,0.4); tl(65,0.4); tl(67,0.5); rr(0.2)

    tl(67,0.4); tl(70,0.4); tl(74,0.6); rr(0.2)
    tl(72,0.4); tl(70,0.4); tl(67,0.8); rr(0.3)
    tl(65,0.7); rr(0.2)
    tl(63,0.8); rr(0.2)
    tl(60,2.0); rr(0.5)

# Play order:
groovy_intro_lo()
main_chorus_lo()
groovy_outro_lo()
