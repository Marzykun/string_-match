def get_fastest(results):
    min_time = min(res["time"] for res in results.values())

    return [
        algo for algo, res in results.items()
        if res["time"] == min_time
    ]


def get_least_comparisons(results):
    min_comp = min(res["comparisons"] for res in results.values())

    return [
        algo for algo, res in results.items()
        if res["comparisons"] == min_comp
    ]


def get_summary(results):
    return {
        "fastest": get_fastest(results),
        "least_comparisons": get_least_comparisons(results)
    }