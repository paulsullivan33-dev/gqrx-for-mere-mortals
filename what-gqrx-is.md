# What GQRX Is

**Scope:** the mental model — a graphical
software-defined radio receiver built from
GNU Radio blocks, where it sits among the
other SDR applications — plus the one legal
line that governs the whole hobby, and the
lab this guide is verified on.

## A receiver with a screen

The sibling guide, *RTL-SDR for Mere
Mortals*, works a cheap TV dongle through
command-line tools: `rtl_fm` for listening,
`dump1090` for aircraft, `rtl_433` for
sensors. Those tools are deliberately bare
— numbers in, audio or data out, no
picture. **GQRX** is the same hobby with
the radio put back on the screen: a live
**waterfall** of the slice of spectrum the
receiver is hearing, a frequency display
you can click and type in, demodulators
switched from a list, and the recovered
audio played through the machine's sound.

GQRX is written by Alexandru Csete and
built from three layers worth knowing by
name, because everything in this guide —
including every error message — belongs to
one of them:

- **gr-osmosdr** talks to the hardware. It
  is the layer that knows what an RTL-SDR,
  an Airspy, a HackRF, or a USRP is, and
  the layer that reports when none of them
  can be found.
- **GNU Radio** does the signal processing:
  filtering, demodulating, resampling. It
  is a construction kit of blocks, and
  GQRX is one particular arrangement of
  them, fixed in advance.
- **Qt** draws the window — the panels,
  dialogs, and the spectrum plot itself.

Check: the layers, in the program's own
words, from its startup output on the
build machine:

```
gr-osmosdr 0.2.0.0 (0.2.0) gnuradio 3.10.9.2
built-in source types: file fcd rtl rtl_tcp uhd miri hackrf bladerf rfspace airspy airspyhf soapy redpitaya freesrp xtrx
```

That second line is the census of what
this build of GQRX can drive: a file, a
Funcube Dongle, RTL-SDR hardware directly
or over the network (`rtl_tcp`), Ettus
USRP gear (`uhd`), HackRF, BladeRF,
Airspy and Airspy HF+, anything SoapySDR
can reach, and more. The manual page adds
the summary: GQRX "can operate as an
AM/FM/SSB receiver with audio output or as
an FFT-only instrument" — a spectrum
display with the demodulator switched
off, for when you only want to look.

## Where it sits

Among the graphical receivers (chapter 8
places them all), GQRX is the plain one:
one receiver, one slice of spectrum, the
standard demodulators, and a handful of
well-chosen extras — recordings, bookmarks,
and a remote-control socket. It does not
bundle decoders for the dozens of data
modes SDRangel carries, and it does not
have SDR++'s module system. What it has
instead is a shallower learning curve and
a scriptable back door, and for a first
graphical receiver those are the right
trades.

## What it cannot do

**GQRX only receives.** It has no
transmit path at all, and the receivers it
usually drives — the RTL-SDR above all —
cannot transmit either. It also cannot
want a signal into existence: with no
device attached it will faithfully display
nothing, and with no sound device
available it refuses to start at all
(chapter 2 shows the refusal, captured).
And it is a listener, not a decoder farm:
past the AFSK1200 decoder and the RDS
readout that ride along in its menus, the
structured decoding of what you hear
belongs to other tools.

## The legal line, once and plainly

Listening rules differ by country, and
this guide is not a lawyer, but the shape
of them is consistent enough to state, as
the sibling guide states it:

- **Broadcast and openly transmitted
  data** — FM radio, airband, weather
  broadcasts, amateur radio, sensor
  beacons — is the normal territory of
  this hobby and is lawful to receive in
  most places.
- **Private communications are not.** In
  many jurisdictions it is illegal to
  listen to, record, or disclose
  communications not intended for you —
  phone calls and encrypted traffic above
  all. Encryption is also a practical
  wall: the receiver hears noise and no
  more.
- **Transmitting** is a separate,
  licensed business that this software
  cannot do anyway.

When in doubt about a frequency, look it
up before you settle there. The chapters
of this guide stay inside the openly
transmitted territory, and the lab
recording contains no one's communication
at all — it is two synthesised tones.

## The lab, and its honest ceiling

This guide was built and verified on a
machine with **no receiver and no sound
card**. As with the sibling guide, that is
less of a disqualification than it sounds,
because in SDR the signal can be a file.
GQRX itself ships the proof: one of the
device types in its own list is a file of
recorded samples, chosen in the same
dialog where you would choose a dongle.

The lab recording is four seconds of
synthetic sky: two steady tones (at
+120 kHz and −200 kHz from the centre, of
amplitudes 0.5 and 0.15) over light noise,
at a million samples per second, made by
`examples/make-lab-file.py`. Everything
predictable about it was predicted:
chapter 5 finds the tones where the
arithmetic puts them, and chapter 6 finds
them again inside GQRX's own I/Q
recording of them, at the relative level
the arithmetic predicts.

Check: the tools, installed from the
Ubuntu 24.04 archive on the build machine:

```
$ dpkg-query -W gqrx-sdr gnuradio
gnuradio   3.10.9.2-1.1ubuntu2
gqrx-sdr   2.17.4-2build3
$ gqrx --help
Gqrx software defined radio receiver 2.17.4
  -l, --list           List existing configurations
  -c, --conf <file>    Start with this config file
  -e, --edit           Edit the config file before using it
  -r, --reset          Reset configuration file
```

What no capture here can show you is a
signal the build machine received over
the air, because it received none, nor
audio anyone heard: the machine's "sound
card" for the later runs was a null sink,
a place for audio to go and be counted,
not heard. Chapters 5's workflows are
exercised on the lab tones and written
from the controls' captured behaviour;
`criteria.md` keeps the ledger of exactly
which claims are documented-only.
