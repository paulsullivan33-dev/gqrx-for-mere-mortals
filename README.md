# GQRX for Mere Mortals

The command-line SDR tools hand you numbers
in a terminal and expect you to imagine the
radio. **GQRX** puts the radio back on the
screen: a waterfall of the slice of spectrum
your receiver is hearing, a tuning dial, a
demodulator you switch with a click, and the
audio in your speakers. It is the graphical
receiver most new dongle owners meet first,
and it is more than a picture — it records
what it hears two different ways, keeps its
bookmarks in a plain-text file you can edit
by hand, and speaks a remote-control
protocol that lets other programs (or your
own scripts) drive it.

Underneath, GQRX is an arrangement of other
people's work: **GNU Radio** does the signal
processing, **gr-osmosdr** talks to the
hardware, and the Qt toolkit draws the
window. That layering explains both its
reach — the long list of receivers it can
drive, from a TV dongle to a USRP — and its
failure modes, which are usually one of the
layers complaining, in its own accent, about
a missing device or a missing sound card.
This guide teaches you to read those
complaints.

The lab is one synthetic recording and two
absences. The recording is a four-second
file of I/Q samples containing two steady
tones and some noise, made by a script
(`examples/make-lab-file.py`) rather than an
antenna — a small, fully known sky whose
every feature can be predicted with
arithmetic and then found, on screen and in
the recordings, exactly where the arithmetic
put it. The absences are a receiver and a
sound card: the build machine has no dongle
and no audio device, and GQRX was run
anyway, so its honest no-hardware behaviour
is captured and quoted — including the
dialog with which it refuses to start when
it can find no audio at all. What needs
real radio is marked as needing real radio.

A note on how this guide was verified.
GQRX 2.17.4 (with GNU Radio 3.10.9 and
gr-osmosdr 0.2.0) ran on Ubuntu 24.04 under
a virtual display, was driven through its
own menus and dialogs, was fed the lab
recording as its input device, and was
retuned, re-moded, and recorded through its
own remote-control port. The captures —
menus, panels, protocol replies, the files
its recorders wrote — are quoted in the
chapters, and `criteria.md` keeps the full
ledger of what is documented-only.

## What this guide covers

- [**What GQRX is**](what-gqrx-is.md) —
  the graphical receiver and its layers,
  where it sits among the SDR applications,
  receive-only stated plainly, the legal
  line, and the lab
- [**Installing GQRX**](installing-gqrx.md) —
  the Linux install, the first-run device
  dialog, the audio error that stops a
  soundless machine, multiple
  configurations, and the other platforms
- [**The main window**](the-main-window.md) —
  the frequency displays, the FFT plot and
  waterfall, the Receiver Options panel
  control by control, the three settings
  tabs, and the Audio dock
- [**Configuring a receiver**](configuring-a-receiver.md) —
  the I/O devices dialog, device strings,
  sample rates, the Input Controls panel,
  frequency correction, the LNB LO field,
  and the configuration files on disk
- [**Listening workflows**](listening-workflows.md) —
  the tune–mode–filter–squelch loop, then
  broadcast FM, airband AM, narrowband FM,
  and SSB/CW including HF through an
  upconverter, with the lab tones as the
  worked example
- [**Recording and remote control**](recording-and-remote-control.md) —
  audio recordings as WAV, I/Q recordings
  as raw sample files, the replay routes,
  and the rigctl-style remote-control
  protocol, exercised end to end
- [**Bookmarks and the bandplan**](bookmarks-and-bandplan.md) —
  the bookmarks file and its exact format,
  tags and colours, markers on the
  spectrum, and the bandplan file GQRX
  writes from its built-in default
- [**The neighbours**](the-neighbours.md) —
  SDR++, CubicSDR, SDRangel and the other
  receivers, the command-line shelf, other
  people's receivers on the web, and the
  GNU Radio engine room underneath
- [**Troubleshooting**](troubleshooting.md) —
  the audio refusal, the file-only device
  list, the yellow waterfall, silence with
  a picture, remote-control refusals, and
  recordings that eat the disk
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Receiving itself, from the antenna up: the
dongle, the tuner, sample rates and ppm as
subjects belong to the sibling guide,
*RTL-SDR for Mere Mortals*, and this guide
points there rather than re-teaching them.
Transmitting — GQRX only receives, and the
hardware it usually drives cannot transmit
either; the licensed half of radio lives in
*Ham Radio for Mere Mortals*. Building GNU
Radio flowgraphs of your own is pointed to
in chapter 8, not taught. And no chapter
here will tell you a "best" gain or a
"best" anything: the guide's job is to make
GQRX's dials legible so your own sky can be
measured with them.

## How to use this guide

Read chapter 1, install with chapter 2, and
generate the lab recording with
`examples/make-lab-file.py`. Configure
GQRX to use that file as its input (chapter
4 gives the exact device string) and every
capture in chapters 3, 5, 6, and 7 can be
reproduced on your machine, dongle or not.
When a real receiver joins the desk, the
same chapters apply unchanged — only the
device string is different, and the sky is
live.
