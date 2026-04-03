from naive import naive_search
from kmp import kmp_search
from boyer_moore import boyer_moore_search


def run_all_algorithms(text, pattern):
    results = {}

    results["Naive"] = naive_search(text, pattern)
    results["KMP"] = kmp_search(text, pattern)
    results["Boyer-Moore"] = boyer_moore_search(text, pattern)

    return results


# CLI testing (for now)
if __name__ == "__main__":
    text = input("Enter text: ")
    pattern = input("Enter pattern: ")

    results = run_all_algorithms(text, pattern)

    print("\n--- Results ---")
    for algo, res in results.items():
        print(f"\n{algo}:")
        print("Matches:", res["matches"])
        print("Comparisons:", res["comparisons"])
        print("Time:", res["time"])
