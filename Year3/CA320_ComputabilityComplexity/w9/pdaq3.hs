-- PDA accepting languages which have:
-- numbers of c's == number of a's + number of b's
-- (i.e: E = { ai bj ck| i,j,k ≥ 0 and i + j = k } )
-- Guide (slide 4/10): https://web.njit.edu/~marvin/cs341/hw/hwsoln06.pdf

abc = (1, [4], [
                ((1, "", ""), (2, "#")),
                ((2, "c", ""), (2, "c")),
                ((2, "", ""), (3, "")),
                ((3, "a", "c"),(3, "")),
                ((3, "b", "c"), (3, "")),
                ((3, "c", "a"), (3, "")),
                ((3, "c", "b"), (3, "")),
                ((3, "a", ""), (3, "a")),
                ((3, "b", ""), (3, "b")),
                ((3, "c", ""), (3, "c")),

                ((3, "", "#"), (4, "")) 
                ]
    )
    