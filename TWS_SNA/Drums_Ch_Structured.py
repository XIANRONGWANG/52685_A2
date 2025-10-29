
# Song: Seven Nation Army (Drums on hook)
#
# Idea:
# - Wait 8 beats before coming in
# - Then repeat the same beat pattern (snare + hat stab, rest)


def d(p, b):
    playNote(p, beats=b)

def r(b):
    rest(b)

def beat_hit():
    # playNote(2) then playNote(6) for 0.25 beats total,
    # then rest 0.75 beats -> one beat of groove
    d(2, 0.00)      # hit sound 1 (snare)
    d(6, 0.25)      # hit sound 2 (TOM)
    r(0.75)

def one_bar():
    # 4 beats = four beat_hit() calls
    for _ in range(4):
        beat_hit()


# PERFORMANCE ORDER


r(8)        # wait before drums enter (your original rest(8))

for _ in range(6):
    one_bar()
