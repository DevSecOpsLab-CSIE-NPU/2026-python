from typing import List, Dict

def sequence_clean(line: str) -> Dict[str, List[int]]:
    parts = line.strip().split()
    nums = [int(x) for x in parts if x.strip() != ""]

    seen = set()
    dedupe = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            dedupe.append(n)

    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    evens = [n for n in nums if n % 2 == 0]

    return {
        "dedupe": dedupe,
        "asc": asc,
        "desc": desc,
        "evens": evens,
    }


def format_sequence_clean(output: Dict[str, List[int]]) -> str:
    return (
        "dedupe: " + " ".join(str(x) for x in output["dedupe"]) + "\n"
        + "asc: " + " ".join(str(x) for x in output["asc"]) + "\n"
        + "desc: " + " ".join(str(x) for x in output["desc"]) + "\n"
        + "evens: " + " ".join(str(x) for x in output["evens"]))
