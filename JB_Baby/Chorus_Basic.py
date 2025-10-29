# CHORUS: "Baby" – Basic

# Description:
#  A rendition of the Chorus of Justin Bieber’s “Baby”
#  
#
# MIDI reference:
#   67 = G
#   65 = F
#   63 = D#
#   70 = A# (Bb)
#   72 = C
#
# Tempo suggestion: ~130 BPM

def n(p,b): playNote(p,beats=b)
def r(b):   rest(b)


# CHORUS
# “Baby, baby, baby oh…”
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,1.0); r(0.25)
n(70,0.8); r(0.2)
# “Like baby, baby, baby no…”
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,1.0); r(0.25)
n(72,0.8); r(0.25)
# “Like baby, baby, baby oh…”
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,0.7); r(0.1)
n(65,0.6); r(0.1)
n(67,1.0); r(0.25)
n(70,0.8); r(0.2)
# “Thought you’d always be mine, mine…”
n(67,0.8); r(0.05)
n(65,0.6); r(0.05)
n(67,1.2); r(0.3)
n(67,0.8); r(0.05)
n(65,0.6); r(0.05)
n(67,1.5); r(0.4)
n(65,1.0); r(0.3)
n(63,1.5); r(0.5)
