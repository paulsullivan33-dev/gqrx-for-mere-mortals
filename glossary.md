# Glossary

**AFSK1200** — audio frequency-shift
keying at 1200 baud, the sound of
packet radio and APRS. GQRX carries a
decoder for it in the Tools menu.
Chapters 3, 8.

**AGC** — automatic gain control: the
receiver adjusting its own amplification
(or the demodulator's audio level, which
is the AGC in Receiver Options).
Chapters 3, 4.

**Bandplan** — the chart of what lives
where in the spectrum, drawn as shading
behind GQRX's plot. Written to
`bandplan.csv` from the program's
built-in default, and yours to edit
thereafter. Chapter 7.

**Bookmark** — a saved station:
frequency, name, mode, bandwidth, tags,
held in the plain-text `bookmarks.csv`
and drawn as a marker on the spectrum.
Chapter 7.

**cf32** — complex float32, the sample
format of GQRX's raw I/Q recordings:
8 bytes per I/Q pair. Chapter 6.

**dBFS** — decibels relative to full
scale: 0 is the top of the converter's
range and everything real is negative.
The plot's, the meter's, and the remote
protocol's unit. Chapters 3, 5, 6.

**Decimation** — dividing the sample
rate by a whole number before
processing: a narrower slice for less
work. Chapter 4.

**Demodulator** — the stage that turns
samples into audio: AM, FM, SSB and
their kin, chosen from the Mode list.
The thing GQRX's Receiver Options panel
controls. Chapters 3, 5.

**Device string** — the text form of an
input choice, comma-separated
`key=value` pairs handed to gr-osmosdr,
and the heart of every configuration
file. Chapter 4.

**DSP** — digital signal processing;
in GQRX, the running of the whole
receive chain, started and stopped from
the toolbar or File menu (Ctrl+D).
Chapters 3, 6.

**FFT** — fast Fourier transform, the
computation that turns a block of
samples into a spectrum. Its size
against the sample rate sets the RBW.
Chapters 3, 4.

**gr-osmosdr** — the library that talks
to SDR hardware on GNU Radio's behalf;
the layer that finds, or fails to
find, your receiver. Chapters 1, 2, 9.

**LNB LO** — a local-oscillator offset
(GQRX's field of that name) that shifts
only the displayed frequency; for
satellite LNBs and upconverters.
Chapters 2, 4, 5.

**NBFM** — narrowband FM: voice FM with
small deviation, the mode of repeaters
and utility radios. GQRX's "Narrow FM".
Chapter 5.

**OIRT** — the former Eastern European
FM broadcast band and its stereo
system; GQRX's WFM (oirt) mode serves
it. Chapter 3.

**Pandapter** — the spectrum plot
itself, in the older radio word the
settings popup uses ("panoramic
adapter"). Chapters 3, 9.

**Passband** — the width of signal the
demodulator accepts, set by the filter.
In Hz, in the panel and the protocol.
Chapters 3, 5, 6.

**ppm** — parts per million, the unit
of a crystal's frequency error and of
GQRX's Freq. correction field. The
measurement itself is the sibling
guide's chapter 4. Chapters 4, 9.

**RBW** — resolution bandwidth: how
fine a frequency detail the FFT can
separate; sample rate ÷ FFT size.
Chapter 4.

**RDS** — Radio Data System, the data
a broadcast FM station sends beside
its audio: name, programme type, text.
GQRX's RDS panel decodes it. Chapters
3, 5.

**Remote control** — GQRX's TCP server
(port 7356 as shipped) speaking a
rigctl-style language, so other
programs can tune and record.
Chapter 6.

**Rigctl** — hamlib's radio-control
protocol, the dialect of the remote
control above; satellite trackers
speak it to retune for Doppler.
Chapter 6.

**SigMF** — the Signal Metadata Format:
an I/Q recording plus a JSON sidecar
describing it, so other tools can read
it unaided. The I/Q tool's second
format. Chapter 6.

**Squelch** — the gate that mutes
audio below a set signal level, in
dB. Silence, automated. Chapters 3, 5.

**Throttle** — in a device string, the
instruction to play a file at its
stated rate instead of flat out.
Chapter 4.

**UDP stream** — GQRX's network audio:
the demodulated sound sent as raw
samples to another program. Chapter 6.

**Waterfall** — the spectrum over
time: frequency across, time downward,
strength as colour. Chapters 3, 9.

**WFM** — wideband FM, broadcast FM's
shape; in GQRX, mono, stereo, and
oirt variants. Chapters 3, 5.
