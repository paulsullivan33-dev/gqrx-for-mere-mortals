# Configuring a Receiver

**Scope:** telling GQRX what to listen
*with* — the I/O devices dialog and the
device strings it writes, sample rates
and decimation, and the Input Controls
panel where a receiver's manners are set.
What the controls *mean* at the signal
level (gain, ppm, sample rate as a
budget) is the sibling guide's chapters
3 and 4; here they are placed, named,
and read back.

## The I/O devices dialog

**File → I/O Devices** reopens the
first-run dialog at any time. Its I/Q
input half, as captured:

| Field | What it holds |
| --- | --- |
| Device | the input, chosen from what gr-osmosdr can see |
| Device string | the same choice as text: comma-separated `key=value` pairs |
| Input rate | the device's own sample rate, when it offers a choice |
| Decimation | a whole-number divide-down of the rate, or None |
| Sample rate | the resulting rate, computed and shown (0 Msps until set) |
| Bandwidth | the analogue filter width, where the hardware has one |
| LNB LO | a local-oscillator offset that shifts only the display (satellite LNBs, upconverters) |

The **Device** list is a census, not a
catalogue: it shows the devices
gr-osmosdr found on *this* machine, plus
the file. On the build machine that was
the file alone. On a machine with a
dongle, the dongle appears — and if it
doesn't, the **Device scan** button asks
again, and chapter 9 works the problem.
Behind every friendly entry stands the
**device string**, and the string is the
real configuration: it is what the
config file stores (chapter 2), and
editing it directly is how the less
common inputs are reached at all.

## Device strings, taken apart

Check: the lab's string, written by the
dialog and stored in the configuration:

```
file=/tmp/tone.cf32,freq=100e6,rate=1e6,repeat=true,throttle=true
```

Read it as the file source's orders:

- `file=<path>` — the recording to play,
  a raw file of complex samples.
- `freq=100e6` — the centre frequency the
  file claims to be from, in Hz. (The
  Receiver Options panel went on to show
  the configuration's own 14.236 MHz and
  used that; the I/Q recorder later named
  its output using this 100 MHz figure —
  chapter 6. The string's claim and the
  display's are not the same bookkeeping.)
- `rate=1e6` — the sample rate the file
  was recorded at.
- `repeat=true` — loop the file instead
  of ending. For a 4-second lab file,
  the difference between a receiver and
  a moment.
- `throttle=true` — play at the stated
  rate, not as fast as the disk allows.
  Without it, a file source floods the
  flowgraph; with it, the lab file behaves
  like a slow, honest receiver.

Hardware strings are terser — an RTL-SDR
is typically chosen from the list and its
string accepted as written — but the
shape is the same across the source
types in chapter 1's census, including
`rtl_tcp`, which points GQRX at a dongle
served over the network by another
machine (documented-only here; the lab
had no dongle to serve).

## Sample rate and decimation

The input rate is the width of your
slice of spectrum and the size of every
bill that follows (the sibling guide's
chapter 4 does that arithmetic; it is
not repeated). GQRX adds one convenience
of its own: **decimation**, dividing the
device's rate down by a whole number
before processing — a way to run a
wideband device narrow, at a fraction of
the CPU and waterfall width. The FFT
Settings' RBW readout keeps the
consequence visible: it is always the
*effective* rate divided by the FFT
size, and on the lab's numbers it read
122.1 Hz, which is 1,000,000 ÷ 8192 —
check it against your own setup and the
panel is telling the truth.

## Input Controls: the receiver's manners

The **Input controls** tab is where the
selected input is adjusted. With the
file as the device, it was captured
showing:

| Control | What it does |
| --- | --- |
| LNB LO | the same display offset as the dialog's field |
| Hardware AGC | let the device run its own automatic gain |
| Swap I/Q | exchange the I and Q channels (repairs recordings made with them swapped, at the price of a mirrored spectrum) |
| No limits | let frequency entries roam beyond the device's stated range |
| DC remove | subtract the centre spike every direct-conversion receiver draws |
| IQ balance | correct the small gain/phase mismatch between the channels |
| Freq. correction | the receiver's error, in ppm, applied as a standing correction |
| Antenna | which of the device's antenna ports to use, when it has several |
| Reset frequency controller digits | a display preference for the big digits |
| Invert scroll wheel direction | exactly that |

Two honest observations. First, what is
**absent** for a file: gain. A recording
has no amplifier to adjust, so the panel
shows no gain sliders — and the
remote-control census agreed (chapter 6:
`l ?` on this device answered `SQL
STRENGTH AF`, three readable settings and
no `*_GAIN` entries). Second, what
appears with real hardware is therefore
documented-only in this guide: the
device's gain stages as sliders — on an
RTL-SDR, its RF gain — in this panel,
above these same checkboxes. The sibling
guide's gain chapter is the one to read
before touching them; GQRX's part is
only to put them here.

**Freq. correction** deserves its
sentence: it is the ppm error of *your*
receiver, measured the sibling guide's
way (against a signal of known
frequency), entered once, and applied to
everything. TCXO dongles sit near zero;
plain crystals can want tens of ppm, and
the correction matters exactly in
proportion to how narrow your signals
are.

## Configurations as files

Chapter 2 showed the storage:
`~/.config/gqrx/<name>.conf`, chosen at
startup with `-c`, listed with `-l`,
reset with `-r`. The working rule the
lab suggests: one configuration per
device or per job, named for it (the
file menu's Save settings writes them),
so that the first-run dialog is
something you see once per setup, not
once per session. The configuration is
plain text; the `[input]` device line is
its heart, and a configuration copied to
another machine carries its device
string with it — path and all, which
for a file device means the recording
must exist at the same address, or the
dialog will have words for you at
startup (chapter 9).
