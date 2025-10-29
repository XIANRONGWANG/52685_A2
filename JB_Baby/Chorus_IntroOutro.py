# CHORUS: "Baby" – Emotional Piano Remix

# Description:
#  A slower rendition of the chorus of Justin Bieber’s “Baby”
#  with long sustains, and breathing rests, with a jammy
#  intro and outro.
#
# MIDI reference:
#   67 = G
#   65 = F
#   63 = D#
#   70 = A# (Bb)
#   72 = C
#
# Tempo: 130 BPM

def n(p,b): playNote(p, beats=b)
def r(b):   rest(b)


# INTRO – Freestyle jam into groove

n(60,0.4); n(63,0.4); n(67,0.6); r(0.2)
n(65,0.4); n(68,0.4); n(72,0.6); r(0.2)
n(67,0.6); n(70,0.5); n(74,0.5); r(0.2)
n(65,0.4); n(68,0.4); n(72,0.6); r(0.3)

# quick chromatic climb
n(63,0.3); n(64,0.3); n(65,0.3); n(67,0.3); n(70,0.6); r(0.3)
n(67,0.3); n(70,0.3); n(74,0.3); r(0.2)
n(65,0.3); n(68,0.3); n(72,0.4); r(0.3)
n(67,1.0); r(0.4)   # hold G before the main melody enters


# CHORUS – “Baby, baby, baby oh…”
# Tempo: Slower phrasing (1.5–3.0 beat sustains)
# Idea: Heavy emotional rhythm + held “oh/no” tones


# Phrase 1: “Baby, baby, baby oh…”
n(67,1.4); r(0.1)   # "ba-" (G, confident)
n(65,0.7); r(0.2)   # "-by" (F)
n(67,1.3); r(0.15)  # "ba-" (slight delay)
n(65,0.6); r(0.2)   # "-by"
n(67,1.8); r(0.1)   # "ba----"
n(70,2.6); r(0.4)   # "ohhhh" (long soulful sustain)

# Phrase 2: “Like baby, baby, baby no…”
n(67,1.1); r(0.15)
n(65,0.7); r(0.2)
n(67,1.1); r(0.15)
n(65,0.7); r(0.2)
n(67,1.4); r(0.1)
n(72,2.6); r(0.5)   # “noooo” (C high, full voice)

# Phrase 3: “Like baby, baby, baby oh…”
n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.3); r(0.15)
n(70,1.9); r(0.4)   # “oh” more mellow

# Phrase 4: “Thought you’d always be mine, mine…”
n(67,1.1); r(0.1)   # "thought you'd"
n(65,0.9); r(0.1)   # "al-"
n(67,1.3); r(0.2)   # "ways be"

# first “mine” (big hold)
n(65,0.3); r(0.05)  # quick pickup F→G
n(67,1.8); r(0.25)  # emotional main "mine"

# second “mine” (softer, descending)
n(65,0.8); r(0.15)
n(63,0.6); r(0.1)
n(62,0.5); r(0.1)
n(63,1.9); r(0.6)   # fade-out like echo


# SOLO / OUTRO – expressive, loose improv finish

# blues-style climb (grace notes, attitude)
n(63,0.3); n(65,0.3); n(67,0.4); r(0.1)
n(70,0.4); n(72,0.4); n(74,0.4); r(0.2)
n(72,0.3); n(70,0.3); n(67,0.4); r(0.2)
n(65,0.4); n(63,0.4); n(62,0.6); r(0.2)

# repeat echo riff
for _ in range(2):
    n(65,0.4); n(67,0.4); n(70,0.4); r(0.2)
    n(63,0.4); n(65,0.4); n(67,0.5); r(0.2)

# final expressive climb + release
n(67,0.4); n(70,0.4); n(74,0.6); r(0.2)
n(72,0.4); n(70,0.4); n(67,0.8); r(0.3)
n(65,0.7); r(0.2)
n(63,0.8); r(0.2)
n(60,2.5); r(1.0)   # long held C to close piece
