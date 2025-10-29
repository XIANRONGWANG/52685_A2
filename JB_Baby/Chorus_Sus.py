# CHORUS: "Baby" – Emotional Piano Remix

# Description:
#  A slower rendition of the chorus of Justin Bieber’s “Baby”
#  with long sustains, and breathing rests.
#
# MIDI reference:
#   67 = G
#   65 = F
#   63 = D#
#   70 = A# (Bb)
#   72 = C
#
# Tempo :130 BPM

def n(p,b): playNote(p,beats=b)
def r(b):   rest(b)


# Phrase 1: “Baby, baby, baby oh…”
# Emotion: hopeful, gentle lift

n(67,1.2); r(0.1)    # "ba-" (G)
n(65,0.6); r(0.2)    # "-by" (F)
n(67,1.2); r(0.1)    # "ba-"
n(65,0.6); r(0.2)    # "-by"
n(67,1.7); r(0.1)    # "ba----"
n(70,2.4); r(0.3)    # "ohhhh" (A# long and full)


# Phrase 2: “Like baby, baby, baby no…”
# Emotion: more yearning, brighter top note (C)

n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.4); r(0.1)
n(72,2.3); r(0.5)     # “noooo” (C) – strong and open


# Phrase 3: “Like baby, baby, baby oh…”

n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.0); r(0.1)
n(65,0.6); r(0.2)
n(67,1.2); r(0.1)
n(70,1.8); r(0.4)     # “oh” shorter than first time


# Phrase 4: “Thought you’d always be mine, mine…”
# Emotion: falling sadness → gentle release

n(67,1.0); r(0.1)     # "thought you'd"
n(65,0.8); r(0.1)     # "al-"
n(67,1.2); r(0.2)     # "ways be"

# first "mine" (emotional peak)
n(65,0.3); r(0.05)    # grace note F→G
n(67,1.6); r(0.3)     # strong, soulful hold

# second "mine" (echo, falling)
n(65,0.8); r(0.2)     # soft F

# emotional descent – let the melody “fall apart”
n(65,0.4); r(0.05)
n(63,0.6); r(0.05)
n(62,0.4); r(0.05)
n(63,1.8); r(0.5)     # settle low, fading away
