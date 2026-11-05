#!/usr/bin/env python3
"""Make this guide's lab recording: a small, fully
known sky in a file.

Writes tone.cf32 -- four seconds of complex
float32 I/Q samples at 1,000,000 samples per
second, containing:

  * a steady tone of amplitude 0.5 at +120,000 Hz
  * a steady tone of amplitude 0.15 at -200,000 Hz
  * light Gaussian noise under both

Everything the guide measures comes off these
two tones:

  * parked between them, GQRX's STRENGTH reads
    about -51 dBFS (the noise in the channel);
    tuned onto the strong tone it reads about
    -6.0 dBFS, because 20 * log10(0.5) = -6.02
  * an FFT of any honest recording of this file
    finds the tones at +120,000 Hz (0 dB) and
    -200,000 Hz (-10.5 dB, because
    20 * log10(0.15 / 0.5) = -10.46)

The random generator is seeded, so the file is
byte-identical on every run: 32,000,000 bytes.

Usage: python3 make-lab-file.py [output-file]
Default output: ./tone.cf32

Feed it to GQRX with the device string from
chapter 4:
  file=<path>,freq=100e6,rate=1e6,repeat=true,throttle=true
"""

import sys

import numpy as np

RATE = 1_000_000
SECONDS = 4


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "tone.cf32"
    rng = np.random.default_rng(20261105)
    n = RATE * SECONDS
    t = np.arange(n) / RATE
    signal = (
        0.5 * np.exp(2j * np.pi * 120_000 * t)
        + 0.15 * np.exp(2j * np.pi * -200_000 * t)
    )
    noise = (rng.standard_normal(n) + 1j * rng.standard_normal(n)) * 0.02
    (signal + noise).astype(np.complex64).tofile(out)
    print(f"wrote {out}: {n} samples, {SECONDS} s at {RATE} samples/s")
    print("tones: +120000 Hz at amplitude 0.5, -200000 Hz at amplitude 0.15")


if __name__ == "__main__":
    main()
