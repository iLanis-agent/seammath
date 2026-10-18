# Seam Math

Sewing cut-size arithmetic. The pattern piece is the finished size; the fabric needs the rest.

## What it computes

- **The cut truth** - finished width and height plus a seam allowance on every edge: finished 10 x 8 with 0.5 allowance is cut 11 x 9.
- **The hem truth** - finished length plus the fabric a hem takes, turned once or twice: 30 with a 1.5 hem turned twice is cut 33.
- **The scale truth** - a test square that should measure 4 but measures 3.8 needs the print scale set to 105.3%.

## Boundary

Arithmetic only. Seam Math adds and scales the numbers you type, in your own unit, rounded to hundredths. It does not say what seam allowance or hem a pattern should use, how a garment will fit, or how fabric will behave. Your pattern and your fabric decide that.

## Files

- `index.html` - landing page.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (19 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/seammath/
Repo: https://github.com/iLanis-agent/seammath
