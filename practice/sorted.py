def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'Bad', 'bada', 'baDa', 'Backstreetboys'])
print sorted(['bob', 'Bad', 'bada', 'baDa', 'Backstreetboys'],cmp_ignore_case)
