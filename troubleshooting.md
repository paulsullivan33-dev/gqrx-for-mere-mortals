# Troubleshooting

**Scope:** GQRX's failures, by symptom.
The first two are the ones this guide's
build machine exhibits on purpose, and
the most instructive is the waterfall
that shows you nothing in one flat colour
while working perfectly.

## Symptom: GQRX stops at "Pulseaudio error: Connection refused"

```
"Pulseaudio error: Connection refused"
[ Abort ]
```

**Cause:** there is no audio output for
GQRX to open — no sound card, or a card
but no running PulseAudio/PipeWire
service. GQRX opens its audio at
startup, before the device dialog, so
this refusal pre-empts everything else
and is easily misread as a radio problem.
It is not one. Fixes, in order: check
the audio service is running and a
default sink exists (`pactl info`); on a
headless or virtual machine, give it a
null sink (chapter 2 gives the two
commands; the lab ran its whole session
into one). Only when the dialog gives
way to Configure I/O Devices is audio
settled and the radio the next question.

## Symptom: the device list offers only "Complex Sampled (IQ) File"

**Cause:** gr-osmosdr found nothing.
Work it as the sibling guide works its
census, because it is the same census
wearing a dialog: the device scan button
asks again; the dongle must be seated
and, on Linux, not claimed by the
kernel's TV driver (the `dvb_usb_rtl28xxu`
blacklist, sibling guide chapter 9) nor
fenced off by permissions; the driver
for exotic hardware may simply not be in
your distribution's build (chapter 1's
source-types line is the list of what
*is*). Test the device with its own
tool — `rtl_test` for a dongle — before
blaming the window: if the command line
can't see it, GQRX can't either.

## Symptom: the waterfall is one flat colour

**Cause:** the waterfall's dB range sits
far from your signals. The lab's first
live waterfall was a wall of yellow over
a noise floor of about −65 dBFS: the
range as shipped mapped that floor to
the top of the colour scale, so
everything — noise and the two clear
tones above it — rendered at full
brightness. The plot, whose range is a
*separate* pair of sliders, showed the
same sky correctly in the same window,
which is the diagnostic: **if the plot
discriminates and the waterfall doesn't,
the receiver is fine and the waterfall's
range is wrong.** Fix in FFT Settings
(or the plot's own settings popup):
bring the waterfall's dB window down
until the noise floor sits at its dark
end and signals stand out of it. There
is no universally right pair of numbers;
they are set against your floor, which
is why they are sliders.

## Symptom: a signal is visible, the meter moves, and nothing is heard

**Cause, in the order to check it:**
the **mode** (a picture cannot tell you
a signal is FM; the demodulator has to
agree with how it was made — chapter
5's table of services is the checklist);
the **squelch**, set above the signal
by a little or a lot (at −150.0 dB it
is off; the strength readout tells you
where your signal actually lives, so
set the gate below that); the **audio
gain and mute** in the Audio dock,
whose own little FFT is the arbiter —
if it dances, demodulation is happening
and the problem is downstream (the
machine's volume, the wrong output
device, chapter 2's audio again); if
it is flat while the main meter moves,
the problem is the demodulator chain
itself: mode, filter width swallowing
or excluding the signal, or the
demodulator parked a few kHz off it.

## Symptom: stations land offset by a fixed amount

**Cause:** the receiver's crystal error,
in ppm (the sibling guide's chapter 4
owns the subject). GQRX's part is one
field: **Freq. correction** in Input
controls, which applies a standing
correction to everything. Measure the
error against a signal of known
frequency, enter it, and the offset
leaves all stations at once, which is
also the test that it *was* ppm and not
one station's eccentricity. Narrow
modes accuse first: a few ppm is
inaudible on broadcast FM and a ruined
SSB contact.

## Symptom: remote control refuses, or answers strangely

**Cause:** the server, in order. It is
off until **Tools → Remote control**
switches it on (chapter 6). It listens
on 7356 as shipped — `ss -ltn | grep
7356` shows the listener — and only for
the hosts on its allow-list, 127.0.0.1
as shipped; a client on another machine
is refused by design until the list is
widened on purpose. And it is a
conversation, not a slot machine: the
lab's fourteen-command burst down one
connection drew a single reply, while
the same commands sent one at a time
were answered in full. Script it
interactively (chapter 6's session is
the shape), and treat `RPRT 1` as the
server's honest "no" — most often a
mode name misspelt or a setting the
current device doesn't have (a file
has no gains to give you; chapter 4).

## Symptom: recordings eat the disk

**Cause:** arithmetic, not malfunction.
An I/Q recording costs sample rate × 8
bytes a second in Raw — 28.8 GB an hour
at 1 Msps, 69 GB at 2.4 Msps — and an
audio recording a gentler 691 MB an
hour (chapter 6 shows both sums). The
mitigations are the same as every
recorder's: record the narrowest input
that holds the signal (decimation,
chapter 4), prefer audio when the
demodulated result is all you need,
and let the I/Q tool's list be your
early warning — it shows what is
accumulating in the recordings folder
by name.

## Symptom: GQRX opens the wrong setup, or a broken one

**Cause:** configurations are files,
and the last one used is the next one
opened. `gqrx --list` shows what exists
(chapter 2); `-c <file>` chooses one at
startup; File → Recent settings chooses
inside the program; `-r` resets the
default. The sharpest version: a
configuration whose device string names
a file or device that has moved will
fail at startup in the dialog's own
terms — repoint the string (chapter 4)
rather than reinstalling anything.
