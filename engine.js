// Seam Math engine - sewing cut-size arithmetic in hundredths of a unit.
// Mirrored by oracle.py; keep the op order identical.
// The unit (inches or centimeters) is the owner's; it is never converted.

function _h(x, msg, allowZero) {
  if (!isFinite(x) || x < 0 || x > 1000 || (!allowZero && x === 0)) throw new Error(msg);
  return Math.floor(x * 100 + 0.5);
}

function _fmt(h) {
  var whole = Math.floor(h / 100), frac = h % 100;
  if (frac === 0) return String(whole);
  var f = (frac < 10 ? "0" : "") + frac;
  if (f.charAt(1) === "0") f = f.charAt(0);
  return whole + "." + f;
}

function _tenths(x) {
  var t = Math.floor(x * 10 + 0.5);
  return Math.floor(t / 10) + "." + (t % 10);
}

// The cut truth: finished size plus seam allowance on every edge.
function cutTruth(width, height, seam) {
  var w = _h(width, "width must be between 0 and 1000, over 0", false);
  var ht = _h(height, "height must be between 0 and 1000, over 0", false);
  var s = _h(seam, "seam allowance must be between 0 and 1000", true);
  return "Finished " + _fmt(w) + " x " + _fmt(ht) + " with a " + _fmt(s) + " seam allowance on every edge: cut " +
    _fmt(w + 2 * s) + " x " + _fmt(ht + 2 * s) + ".";
}

// The hem truth: finished length plus the fabric a turned hem takes.
function hemTruth(length, hem, turns) {
  var l = _h(length, "length must be between 0 and 1000, over 0", false);
  var d = _h(hem, "hem depth must be between 0 and 1000", true);
  if (turns !== 1 && turns !== 2) throw new Error("turns must be 1 or 2");
  return "Finished length " + _fmt(l) + ", hem depth " + _fmt(d) + ", turned " + (turns === 1 ? "once" : "twice") +
    ": cut " + _fmt(l + d * turns) + ".";
}

// The scale truth: print scale that corrects a test square.
function scaleTruth(expected, measured) {
  var e = _h(expected, "expected size must be between 0 and 1000, over 0", false);
  var m = _h(measured, "measured size must be between 0 and 1000, over 0", false);
  return "Test square should measure " + _fmt(e) + ", measured " + _fmt(m) + ": set the print scale to " +
    _tenths(e * 100 / m) + "%.";
}
