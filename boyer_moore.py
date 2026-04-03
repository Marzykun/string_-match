import time

def bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore_search(text, pattern):
    start_time = time.time()

    n = len(text)
    m = len(pattern)

    table = bad_char_table(pattern)

    matches = []
    comparisons = 0

    s = 0  # shift

    while s <= n - m:
        j = m - 1

        while j >= 0:
            comparisons += 1
            if pattern[j] != text[s + j]:
                break
            j -= 1

        if j < 0:
            matches.append(s)
            s += (m - table.get(text[s + m], -1)) if s + m < n else 1
        else:
            shift = max(1, j - table.get(text[s + j], -1))
            s += shift

    end_time = time.time()

    return {
        "matches": matches,
        "comparisons": comparisons,
        "time": end_time - start_time
    }
