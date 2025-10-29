
# Song: Seven Nation Army (main hook on piano)
# Structure:
#   main_riff_once() repeated 3x
#   riff_ending() to finish
#

def n(p, b, sus=None):
    # wrapper: allows optional sustain, matches how you played 60 with sustain
    if sus is None:
        playNote(p, beats=b)
    else:
        playNote(p, beats=b, sustain=sus)

def r(b):
    rest(b)

def main_riff_once():
    # This matches repeating riff block:
    # E  E  G  E  D  C... (in this octave: 64,64,67,64,62,60...)
    n(64,1.00); r(0.50)          # 64 = E4
    n(64,0.25); r(0.25)
    n(67,0.50); r(0.25)          # 67 = G4
    n(64,0.25); r(0.50)
    n(62,0.25); r(0.25)          # 62 = D4
    n(60,2.00, sus=2.75)         # 60 = C4 (long hold with sustain)
    n(59,1.50); r(0.50)          # 59 = B3

def riff_ending():
    # This matches  final block / variation:
    n(64,1.25); r(0.25)
    n(64,0.25); r(0.25)
    n(67,0.50); r(0.25)
    n(64,0.25); r(0.50)
    n(62,0.25); r(0.25)
    n(60,0.25); r(0.50)
    n(62,0.25); r(0.50)
    n(60,0.25); r(0.50)
    n(59,1.75)                    # long B3 fall at the end


# PERFORMANCE ORDER


# play main riff three times (first 3 chunks)
for _ in range(3):
    main_riff_once()

# then play the ending variation once
riff_ending()
