from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# What A, B, C could be
XoRA = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
XoRB = And(Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
XoRC = And(Or(CKnight, CKnave), Not(And(CKnight, CKnave)))

# Puzzle 0
# A says "I am both a knight and a knave."

# The Statment said:
AStatement = And(AKnight, AKnave)

knowledge0 = And(
        XoRA,
        # Check A Statement
        Implication(AKnight, AStatement), 
        Implication(AKnave, Not(AStatement))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

# The Statement said:
AStatement = And(AKnave, BKnave)

knowledge1 = And(
        XoRA,
        XoRB,
        # Check A Statement
        Implication(AKnight, AStatement),
        Implication(AKnave, Not(AStatement))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# The Statement said:
AStatement = Or(And(AKnight, BKnight), And(AKnave, BKnave))
BStatement = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
        XoRA,
        XoRB,
        # Check A Statement
        Implication(AKnight, AStatement),
        Implication(AKnave, Not(AStatement)),
        # Check B Statement
        Implication(BKnight, BStatement),
        Implication(BKnave, Not(BStatement))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# The Statement said:
AStatement = And(Implication(AKnight, AKnave), Implication(AKnave, AKnight))
BStatement = And(Implication(AKnight, AKnight), Implication(AKnave, AKnave))

knowledge3 = And(
    XoRA,
    XoRB,
    XoRC,

    # Check A Statement
    # Check B Statement
    Implication(BKnight, AStatement),
    Implication(BKnave, BStatement),
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # Check C Statement
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
        
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
