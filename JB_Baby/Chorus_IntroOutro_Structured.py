# CHORUS: "Baby" – Emotional Piano Remix

# Description:
#  A slower rendition of the chorus of Justin Bieber’s “Baby”
#  with long sustains, and breathing rests, with a jammy
#  intro and outro.

#  Code structued with functions and loops 
#  to make more efficient
#
# MIDI reference:
#   67 = G
#   65 = F
#   63 = D#
#   70 = A# (Bb)
#   72 = C
#
# Tempo : 130 BPM

def n(p, b): playNote(p, beats=b)
def r(b):    rest(b)


# 1) INTRO: "groovy_intro"
# more groove, more bounce


def groovy_intro():
    # Loop a 2-bar groove twice.
    # Like the band warming up.
    for _ in range(2):
        # Bar A: punchy chord tones climbing
        n(60,0.4); r(0.1)   # C stab
        n(63,0.4); r(0.1)   # D# stab
        n(67,0.5); r(0.1)   # G stab
        n(65,0.4); r(0.1)   # F answer
        n(68,0.4); r(0.2)   # G#/A♭ color
        n(72,0.6); r(0.2)   # C5 pop
        # lil reply lick
        n(70,0.3); n(72,0.3); n(74,0.4); r(0.3)

        # Bar B: chromatic walk
        n(63,0.25); n(64,0.25); n(65,0.25); n(67,0.4); r(0.1)
        n(70,0.4); n(72,0.4); r(0.2)
        # drop
        n(67,0.6); r(0.4)

    # tension chord hold before chorus
    n(67,1.0); r(0.4)  # land on G and let it ring


# 2) CHORUS: "main_chorus"
# Break the chorus into:
#    - phrase_baby(): "baby, baby, baby [oh/no]"
#    - phrase_mine(): "thought you'd always be mine"
#
# Trick: phrase_baby() takes arguments so we can reuse it
# with different emotional endings.


def phrase_baby(end_note, end_hold):
    """
    Plays one 'baby, baby, baby ...' phrase.
    end_note = MIDI pitch for the last held syllable
               (70 = A#/Bb 'oh', 72 = C 'no')
    end_hold = how long to hold that last syllable
    """
    # "ba-by" 1
    n(67,1.0); r(0.1)   # G - "ba-"
    n(65,0.5); r(0.1)   # F - "-by"

    # "ba-by" 2
    n(67,0.9); r(0.1)   # G
    n(65,0.5); r(0.15)  # F

    # lead-up "ba----"
    n(67,1.2); r(0.1)   # stretch G a bit to build tension

    # final syllable "ohhhh" / "noooo"
    n(end_note, end_hold); r(0.4)

def phrase_mine():
    """
    The resolving line:
    'Thought you'd always be mine, mine...'
    We keep it emotional but tighten spacing
    so it grooves with 96 BPM.
    """
    # "thought you'd / al- / ways be"
    n(67,0.9); r(0.1)   # G
    n(65,0.7); r(0.1)   # F
    n(67,1.0); r(0.2)   # G

    # first "mine" = big, dramatic
    n(65,0.25); r(0.05) # tiny pickup F before G
    n(67,1.4); r(0.2)   # long G hold (main 'mine')

    # second "mine" = softer echo, falling
    n(65,0.6); r(0.15)  # F
    n(63,0.5); r(0.1)   # D#
    n(62,0.4); r(0.1)   # D
    n(63,1.4); r(0.5)   # D# sigh out

def main_chorus():
    # Call phrase_baby 3 times with different endings to
    # match "oh", "no", "oh" from the original hook,
    # then finish with phrase_mine().
    phrase_baby(end_note=70, end_hold=1.6)  # "...baby, baby, baby OH"
    phrase_baby(end_note=72, end_hold=1.8)  # "...baby, baby, baby NO"
    phrase_baby(end_note=70, end_hold=1.2)  # "...baby, baby, baby OH" (shorter)
    phrase_mine()


# 3) OUTRO: "groovy_outro"
# more groove than before.


def groovy_outro():
    # Call line
    n(65,0.4); n(68,0.4); n(72,0.4); r(0.1)
    n(67,0.4); n(70,0.4); n(74,0.4); r(0.2)

    # Response line
    n(72,0.3); n(70,0.3); n(67,0.6); r(0.2)
    n(65,0.4); n(63,0.4); n(62,0.6); r(0.2)

    # A lick we repeat twice (loop shows code reuse)
    for _ in range(2):
        n(65,0.4); n(67,0.4); n(70,0.4); r(0.15)
        n(63,0.4); n(65,0.4); n(67,0.5); r(0.2)

    # Closing descent
    n(67,0.4); n(70,0.4); n(74,0.6); r(0.2)
    n(72,0.4); n(70,0.4); n(67,0.8); r(0.3)
    n(65,0.7); r(0.2)
    n(63,0.8); r(0.2)
    n(60,2.0); r(0.5)   # final low C sustain


# EXECUTION ORDER

groovy_intro()
main_chorus()
groovy_outro()
