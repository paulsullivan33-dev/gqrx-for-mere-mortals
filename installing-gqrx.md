# Installing GQRX

**Scope:** getting GQRX onto a machine —
the verified Linux route, the first-run
device dialog, and the audio refusal that
greets a machine with no sound — plus the
configuration system, and the other
platforms, which are documented-only.

## Linux, from your distribution

On Debian and Ubuntu, GQRX is one package:

```
$ sudo apt install gqrx-sdr
```

That is the whole of the verified route:
the package (2.17.4 in the Ubuntu 24.04
archive) brings GNU Radio and gr-osmosdr
with it as dependencies. Other
distributions package it under the same
name. Before the first long session, the
manual page recommends running
`volk_profile` once: it benchmarks the
signal-processing kernels on your
processor and records the fastest
variants, which "will in many cases give
a significant performance boost." That is
the project's own advice, quoted; the
build machine did not need it to keep up
with a 1 Msps file.

Two honest footnotes. First, an
**AppImage** build exists for Linux
(documented-only; not run here). Second,
what your distribution ships may lag the
project: 2.17.4 is the version this guide
is written against, and chapter text
names it where behaviour could differ.

## First run: the device dialog

Start GQRX with no configuration in place
and, before any window, it opens
**Configure I/O devices** — the dialog
that decides what the receiver *is*. On
the build machine, which has no receiver
of any kind, it came up offering exactly
one device, and that device is the reason
this guide could be verified at all:

- **I/Q input — Device:** "Complex
  Sampled (IQ) File". With no hardware
  found, the file is the default.
- **Device string:**
  `file=/path/to/your/file,freq=100e6,...`
  ending `...rate=1e6,repeat=true,throttle=true`
  — a placeholder path, waiting for you to
  name a real recording. Chapter 4 takes
  this string apart piece by piece.
- **Input rate, Decimation, Sample rate,
  Bandwidth, LNB LO:** the input's terms,
  mostly to be set once a real device or
  file is chosen (chapter 4).
- **Audio output — Device:** "Default";
  **Sample rate:** 48 kHz.
- Buttons: **OK**, **Device scan** (ask
  gr-osmosdr to look again), **Cancel**.

Choose a device, click OK, and the main
window (chapter 3) opens with the DSP
stopped. On every later start, GQRX skips
the dialog and opens the window directly
with the configuration it saved — the
build machine's second launch did exactly
that, verified.

## The refusal: no audio, no GQRX

First, though, the build machine produced
a more instructive first run. It has no
sound card and no audio server, and
GQRX's first act — before the device
dialog — was a small error window:

```
Pulseaudio error: Connection refused
[ Abort ]
```

The same line went to the terminal:
`"Pulseaudio error: Connection refused"`.
Clicking Abort ended the program. This is
GQRX's own built-in PulseAudio output
complaining, and the lesson is worth the
chapter space: **GQRX needs a working
audio output before it needs anything
else** — even with no intention of
listening (the FFT-only mode exists, but
the audio device is still opened at
startup). A machine with a sound card and
a running PulseAudio or PipeWire service
never sees this. A headless or virtual
machine very well might.

Check: the lab's fix, for readers in the
same boat — give the machine a null sink,
a place for audio to go:

```
$ pactl load-module module-null-sink sink_name=dummy
$ pactl set-default-sink dummy
$ pactl info | grep "Default Sink"
Default Sink: dummy
```

With PulseAudio running and that sink in
place, the same GQRX proceeded to the
device dialog. Nothing was heard — there
is nothing to hear it with — but every
control, recording, and measurement in
this guide works the same, because GQRX
neither knows nor cares that its "sound
card" is a bucket.

## Configurations: several receivers in one program

GQRX keeps a named configuration per
setup — one per device, say, or one per
purpose — as plain files in
`~/.config/gqrx/`. The one the lab built
says almost everything about the model:

Check: the lab's configuration after the
first-run dialog, and the list command:

```
$ cat ~/.config/gqrx/default.conf
[General]
crashed=false

[input]
device="file=/tmp/tone.cf32,freq=100e6,rate=1e6,repeat=true,throttle=true"

$ gqrx --list
 Existing configuration files in /home/<you>/.config/gqrx/
     default.conf
```

(The build machine's home was a scratch
directory; yours will be your real one.)
The command line picks and manages them:
`-c <file>` starts with a chosen
configuration, `-e` opens it in the
device dialog first, `-r` resets it, and
inside the program **File → Load
settings / Save settings** (Ctrl+L,
Ctrl+S) and **Recent settings** do the
same work. Bookmarks live beside the
configurations, in `~/.config/gqrx/`
(chapter 7).

## macOS and Windows (documented-only)

Neither was run for this guide; stated
from the project's own material so the
reader is not surprised. On **macOS**,
GQRX is distributed as a disk image (the
project's changelog notes the current
builds require macOS 12.7 or later) and
through the usual package managers; the
device dialog and everything after it are
the same program. On **Windows** there is
no long-standing native build — the
2.17.4 changelog announces an
*experimental* Windows binary, RTL-SDR
devices only. Windows readers who want a
graphical receiver today are usually
served by SDR++ or SDR# (chapter 8), or
run GQRX inside a Linux environment —
with the caveat that passing a USB radio
through to a virtual machine is its own
project (the sibling guide's
troubleshooting has the general shape of
that problem).
