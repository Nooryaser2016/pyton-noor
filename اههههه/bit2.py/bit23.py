def implement_circuit(A: int, B: int, C: int) -> int:
# Works for single bits (0/1) or bitwise on integers
    return (A & B) | (B & C)

# quick check
    for A in (0,1):
        for B in (0,1):
            for C in (0,1):
                    print(A, B, C, "->", implement_circuit(A,B,C))