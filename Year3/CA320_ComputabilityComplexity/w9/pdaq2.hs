-- PDA accepting languages which have:
-- same number of a's and b's, or
-- same number of a's and c's
-- Guide (slide 6/10): https://people.eecs.berkeley.edu/~sseshia/172/lectures/Lecture8.pdf

ijk = (0, [3, 7], [
                    ((0, "", ""), (1, "#")),
                    ((1, "a", ""), (1, "a")),
                    ((1, "", ""), (2, "")),
                    ((2, "b", "a"), (2, "")),
                    ((2, "", "#"), (3, "")),
                    ((3, "c", ""), (3, "")),
     
                    ((0, "", ""), (4, "#")),
                    ((4, "a", ""), (4, "a")),
                    ((4, "b", ""), (5, "")),
                    ((5, "b", ""), (5, "")),
                    ((5, "", ""), (6, "")),
                    ((6, "c", "a"), (6, "")),
                    ((6, "", "#"), (7, ""))
                   ]
    )
