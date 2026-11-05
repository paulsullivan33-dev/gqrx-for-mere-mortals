# Recording and Remote Control

**Scope:** the three ways GQRX hands its
signal to the future or to other
programs — audio recordings, I/Q
recordings, and the remote-control
protocol — all three exercised in the
lab, plus the UDP audio stream, which
was not.

## Audio recording: the WAV in your home directory

The Audio dock's **Rec** button (and the
remote command below) records the
demodulated audio to a WAV file in your
home directory. The name is the whole
metadata:

Check: a recording made in the lab,
started and stopped over the remote
control, and read back afterwards:

```
(recording runs a few seconds)
$ ls gqrx_*.wav
gqrx_20261105_084908_14356000.wav
$ python3 -c "import wave; w=wave.open('gqrx_20261105_084908_14356000.wav'); print(w.getframerate(), w.getnchannels(), w.getsampwidth(), w.getnframes())"
48000 2 2 114462
```

Program, date, time, and the demodulator
frequency in Hz — `..._14356000.wav` was
made sitting on the lab tone at
14.356 MHz. The format is fixed: 48 kHz,
16-bit, stereo (the two channels carry
the same mono audio for the modes the
lab used), which prices storage at
192,000 bytes a second — about 11.5 MB
a minute, 691 MB an hour. The frames
counted (114,462, about 2.4 s) came from
a recording the lab ran for roughly
twice that wall-clock time; treat the
recorder's first moments as startup,
not as signal, when timing matters. The
log confirms each take by name
("Recording audio to ...", "Audio
recorder stopped"), the **Play** button
beside Rec plays the last recording
back through the receiver's own audio
path, and the project's changelog notes
the WAVs are written 6 dB down to leave
headroom against clipping.

## I/Q recording: the sky itself, to replay

**Tools → I/Q recorder** (Ctrl+I) opens
the I/Q recording and replay tool: a
format choice (**Raw** or **SigMF**), a
location (your home directory as
shipped), the list of recordings already
there, **Rec** and **Play** buttons, an
elapsed/total readout, and a seek
slider. Where the WAV keeps only the
demodulated audio of one channel, an I/Q
recording keeps the input samples
themselves — the whole slice, every
signal in it, re-runnable through any
demodulator later.

Check: the lab's I/Q recording of the
lab file, measured after the fact:

```
gqrx_20261105_084953_100000000_1000000_fc.raw
24,770,112 bytes = 3,096,264 samples
3.10 s at the stated 1,000,000 samples/s
strongest component: +120,000 Hz (0 dB)
second component:    -200,000 Hz (-10.5 dB)
```

Name, decoded: date, time, the input's
centre frequency in Hz (100,000,000 —
the file device's claimed centre from
its device string, chapter 4's note),
the sample rate, and `_fc` for the
format, complex float. The contents
check is the point: an FFT of the
recording finds the two lab tones at
exactly their synthesised offsets, at
−10.5 dB relative — and the recipe
predicts 20 × log₁₀(0.15 ÷ 0.5) =
−10.46 dB. The recorder neither adds nor
loses; it transcribes.

Storage is the discipline: complex
float is 8 bytes a sample, so the bill
is `rate × 8` bytes a second — 8 MB/s
at the lab's 1 Msps, 28.8 GB an hour;
at a dongle's 2.4 Msps, 19.2 MB/s and
69 GB an hour. **SigMF**, the other
format, wraps the same samples with a
JSON sidecar describing them (rate,
frequency, time) so other tools can
make sense of the file without being
told — the format's existence and place
in the tool are captured; the lab's
recording was made in Raw. Replay is
the tool's **Play**, which feeds a
recording back as the input — and,
equivalently and verifiably, a raw
recording is exactly what the `file=`
device string of chapter 4 consumes:
this whole guide is that replay, run
for four chapters.

## The UDP audio stream (documented-only)

The Audio dock's **UDP** button streams
the demodulated audio over the network
as raw samples — the standard trick for
feeding a decoder on the same machine
(a packet decoder, a weather-satellite
demodulator, another program entirely)
without analogue cables. Its destination
is set in the audio settings' Network
tab (chapter 3). The lab configured
nothing and captured nothing: a
listener stood on the port most often
quoted for this stream for the length
of a trial and heard silence, which
verifies only that the default path
needs its settings read before it is
believed. Set the destination
deliberately, then check for the stream
with your listener before building on
it.

## Remote control: the rigctl door

**Tools → Remote control** switches on a
TCP server; **Tools → Remote control
settings** sets its terms, captured as
shipped: listen on port **7356**, allowed
hosts **127.0.0.1**. That allow-list is
the whole security model — there is no
password — so the default, this machine
only, is the right default, and widening
it is a decision to make on purpose.

The protocol is a subset of the hamlib
**rigctl** language, one command per
line, which is what lets existing
amateur software (satellite trackers
above all, which retune for Doppler as a
pass crosses) drive GQRX as if it were a
radio. The package ships the full list
as `remote-control.txt` in its
documentation; the working set:

| Command | Does |
| --- | --- |
| `f` / `F <Hz>` | get / set the demodulator frequency |
| `m` / `M <mode> [Hz]` | get / set mode and passband; `M ?` lists the modes |
| `l STRENGTH` | the channel's strength, dBFS |
| `l SQL` / `L SQL <dB>` | get / set the squelch |
| `l AF` / `L AF <dB>` | get / set the audio gain |
| `l <name>_GAIN` / `L ...` | per-device gain stages, when the device has them |
| `u DSP` / `U DSP <0/1>` | is the receiver running / start or stop it |
| `u RECORD` / `U RECORD <0/1>` | the audio recorder's state / start or stop it |
| `AOS` / `LOS` | signal acquired / lost — start and stop recording, for satellite passes |
| `LNB_LO [Hz]` | the display offset of chapter 4 |
| `_` | the version string |
| `q` | close the connection |

Replies are the value, or `RPRT 0` for
success and `RPRT 1` for failure. The
session in chapter 5 was run this way;
`examples/remote-session.txt` keeps it
whole. Two behaviours the lab learned
and the guide passes on: the server
rewards patience — commands sent one at
a time, each awaited, were answered in
full, while one burst of fourteen
commands down a fresh connection drew
only the first reply before the pipe
closed; and its frequency is the
*demodulator's*, so a client that wants
the hardware recentred must ask for a
frequency outside the current slice and
let chapter 5's rule do it. Check,
with the server on:

```
$ ss -ltn | grep 7356
LISTEN 0  0  *:7356  *:*
$ printf 'f\n' | nc -q 2 127.0.0.1 7356
14236000
```
