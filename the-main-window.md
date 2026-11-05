# The Main Window

**Scope:** the window itself — every
panel and control, what each number means,
and which of the two frequencies on screen
is which. Operations live in chapters 4
to 6; this is the map they refer to.

## The shape of it

The window divides into a menu bar and
toolbar at the top, the spectrum display
filling the left and centre, a stack of
control panels (dock widgets) on the
right, and a status bar along the bottom.
The panels can be hidden, shown, and
rearranged; **View** is the menu that
owns them:

| View entry | What it shows |
| --- | --- |
| Input controls | the input's panel (chapter 4) |
| Receiver Options | the demodulator panel, below |
| RDS | the Radio Data System readout for FM |
| Audio | the audio panel, below |
| FFT Settings | the spectrum display's settings |
| Bookmarks | the bookmarks panel (chapter 7) |
| Main toolbar | the toolbar under the menus |
| Full screen (F11) | the window, and nothing else |

The menus, captured on the build machine:
**File** holds Start/Stop DSP (Ctrl+D),
I/O Devices, Load settings (Ctrl+L), Save
settings (Ctrl+S), Recent settings, and
Quit (Ctrl+Q). **Tools** holds Remote
control and its settings, Add bookmark
(Ctrl+Shift+B), I/Q recorder (Ctrl+I),
AFSK1200 Decoder, and DX Cluster
(Ctrl+C). **Help** holds the about
information. The status bar, when the DSP
is stopped, teaches the display's whole
grammar in one line, quoted verbatim:

```
Click, drag or scroll on spectrum to tune. Drag and scroll X and Y axes for pan and zoom. Drag filter edges to adjust filter.
```

## The spectrum display

Two pictures share one frame. The **FFT
plot** (top) is the spectrum now: signal
strength in **dBFS** — decibels relative
to full scale, so 0 is the top of the
converter's range and everything real is
a negative number — against frequency.
The **waterfall** (below) is the same
measurement stacked over time, newest at
the top, strength as colour, so a signal
that comes and goes draws a stripe. A
vertical line marks the demodulator's
position, flanked by the edges of its
filter; a small meter at the plot's top
right shows the demodulated channel's
strength (the lab's noise read −51.0
dBFS there; chapter 5 puts a tone under
it and watches it climb).

Three things the display does that are
worth knowing before they surprise you:

- **Clicking tunes.** A click on the plot
  or waterfall moves the demodulator
  there (the build machine's stray clicks
  retuned it twice, both captured). Drag
  moves smoothly; the mouse wheel steps.
- **The scale is adjustable in two
  places.** The plot's dB range and the
  waterfall's dB range are separate
  sliders (FFT Settings tab, chapter 4's
  neighbour); a waterfall whose range
  sits far above your noise floor draws
  one flat colour — the lab's first
  waterfall was a wall of yellow for
  exactly this reason (chapter 9).
- **Bookmarks and the bandplan draw on
  it.** Saved stations appear as labelled
  markers above the plot (the lab's "Lab
  tone" bookmark is visible in several
  captures), and the bandplan shades the
  bands behind the spectrum (chapter
  7).

## The frequency displays: two numbers

GQRX keeps two frequencies, and keeping
them straight is half of using it:

- **Hardware freq** (Receiver Options,
  right-aligned, not editable there) is
  where the receiver itself is centred —
  the middle of the slice you are
  receiving.
- The **big digits** at the window's top
  left, and the **Frequency** field in
  Receiver Options, are the **demodulator
  frequency**: the station you are
  actually listening to, which can sit
  anywhere inside the slice.

Between them sits a third readout, the
demodulator's **offset** from the centre
in kHz (it read 0.0000 when the two
coincided, and 102.200 after a click
moved the demodulator 102.2 kHz up-band).
Tuning behaviour follows from the split:
typing a nearby frequency moves only the
demodulator; asking for a frequency
outside the slice re-centres the hardware
to contain it. The startup default in a
fresh configuration placed both at
14.236000 MHz — the program's own
starting point, not a measurement.

## Receiver Options, control by control

The demodulator panel, top to bottom as
captured:

| Control | What it does |
| --- | --- |
| Frequency | the demodulator frequency, in kHz, typed or stepped |
| Filter width | Wide / Normal / Narrow / User — presets for the passband, or yours |
| Filter shape | the filter's edge steepness (Normal, as shipped) |
| Mode | the demodulator, from the list below |
| AGC | automatic gain control for the demodulated audio: Medium as shipped, with its own settings behind the `...` button |
| Squelch | the level in dB below which audio is muted; −150.0 dB as shipped, which is to say, off |
| Noise blanker | NB1 and NB2, two blankers for pulse-type noise, with settings behind `...` |

The Mode list is the heart of the panel.
Captured open, it reads: **Demod Off,
Raw I/Q, AM, AM-Sync, LSB, USB, CW-L,
CW-U, Narrow FM, WFM (mono), WFM
(stereo), WFM (oirt)**. Demod Off and Raw
I/Q are the honest odd ones out — the
first makes GQRX the FFT-only instrument
of chapter 1, the second passes the raw
samples through untouched. AM-Sync is AM
with a synchronous detector, kinder to
fading shortwave signals. The CW pair are
SSB with a narrow filter and a beat note,
lower and upper. WFM (oirt) serves the
old Eastern European broadcast band,
whose stereo encoding differs. Chapter 6
shows the same list in its other
costume, the remote-control codes:
OFF RAW AM AMS LSB USB CWL CWR CWU CW
FM WFM WFM_ST WFM_ST_OIRT.

## The three tabs, and the Audio dock

Under the demodulator panel, three tabs
share one dock: **Input controls** and
**FFT Settings** get their own sections
in chapter 4 and below; **Receiver
Options** is the tab that shows the
panel above. The FFT Settings tab, as
captured with the lab's 1 Msps input:

| Setting | Lab value | Meaning |
| --- | --- | --- |
| FFT Size | 8192 | samples per spectrum frame |
| RBW | 122.1 Hz | resolution bandwidth: 1,000,000 ÷ 8192 |
| Rate | 25 fps | frames per second drawn |
| Window | Hann | the FFT's window function |
| Plot Mode | Max | each bin's maximum in the frame |
| Plot Scale | dBFS | the plot's units |

Below the tabs, the **Audio** dock: a
small FFT of the demodulated audio (the
quickest proof that a demodulator is
producing anything), a **Gain** slider
for the audio level (−6.0 dB as shipped),
and buttons **Mute**, **UDP** (stream the
audio over the network — chapter 6),
**Rec** (record the audio — chapter 6),
**Play** (play a recording back), and a
`...` for audio settings, whose popup is
tabbed FFT / Recording / Network. The
word **DSP** at the panel's foot is the
processing indicator; the toolbar's
triangular button — **File → Start/Stop
DSP**, Ctrl+D — is what starts and stops
the whole chain.
