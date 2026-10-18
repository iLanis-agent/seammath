#!/usr/bin/env python3
# Seam Math oracle - mirrors engine.js.
import json, math

def _h(x, msg, allow_zero):
    if not math.isfinite(x) or x < 0 or x > 1000 or (not allow_zero and x == 0):
        raise ValueError(msg)
    return math.floor(x * 100 + 0.5)

def _fmt(h):
    whole, frac = divmod(h, 100)
    if frac == 0:
        return str(whole)
    f = f"{frac:02d}"
    if f[1] == "0":
        f = f[0]
    return f"{whole}.{f}"

def _tenths(x):
    t = math.floor(x * 10 + 0.5)
    return f"{t // 10}.{t % 10}"

def cut_truth(width, height, seam):
    w = _h(width, "width must be between 0 and 1000, over 0", False)
    ht = _h(height, "height must be between 0 and 1000, over 0", False)
    s = _h(seam, "seam allowance must be between 0 and 1000", True)
    return (f"Finished {_fmt(w)} x {_fmt(ht)} with a {_fmt(s)} seam allowance on every edge: cut "
            f"{_fmt(w + 2 * s)} x {_fmt(ht + 2 * s)}.")

def hem_truth(length, hem, turns):
    l = _h(length, "length must be between 0 and 1000, over 0", False)
    d = _h(hem, "hem depth must be between 0 and 1000", True)
    if turns not in (1, 2):
        raise ValueError("turns must be 1 or 2")
    return (f"Finished length {_fmt(l)}, hem depth {_fmt(d)}, turned {'once' if turns == 1 else 'twice'}: "
            f"cut {_fmt(l + d * turns)}.")

def scale_truth(expected, measured):
    e = _h(expected, "expected size must be between 0 and 1000, over 0", False)
    m = _h(measured, "measured size must be between 0 and 1000, over 0", False)
    return (f"Test square should measure {_fmt(e)}, measured {_fmt(m)}: set the print scale to "
            f"{_tenths(e * 100 / m)}%.")

FNS = {"cutTruth": cut_truth, "hemTruth": hem_truth, "scaleTruth": scale_truth}

CASES = [
    ("cutTruth", [10, 8, 0.5]), ("cutTruth", [10, 8, 0]), ("cutTruth", [12.25, 6.5, 0.625]),
    ("cutTruth", [1.5, 1.5, 0.25]), ("cutTruth", [0, 8, 0.5]), ("cutTruth", [10, 8, -1]),
    ("cutTruth", [10, 1001, 0.5]),
    ("hemTruth", [30, 1.5, 2]), ("hemTruth", [30, 1.5, 1]), ("hemTruth", [45.75, 0, 2]),
    ("hemTruth", [30, 1.5, 3]), ("hemTruth", [0, 1.5, 2]), ("hemTruth", [30, -1, 2]),
    ("scaleTruth", [4, 3.8]), ("scaleTruth", [4, 4]), ("scaleTruth", [10, 10.4]),
    ("scaleTruth", [4, 0]), ("scaleTruth", [0, 3.8]), ("scaleTruth", [100, 97.5]),
]

out = []
for fn, args in CASES:
    try:
        exp = FNS[fn](*args)
    except ValueError as e:
        exp = "ERR:" + str(e)
    out.append({"fn": fn, "args": args, "expected": exp})
with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(len(out), "cases")
