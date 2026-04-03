import time

def naive_search(text, pattern):
    start_time = time.time()

    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    end_time = time.time()

    return {
        "matches": matches,
        "comparisons": comparisons,
        "time": end_time - start_time
    }
