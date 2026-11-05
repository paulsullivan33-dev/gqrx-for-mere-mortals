# Listening Workflows

**Scope:** the working loop — tune, mode,
filter, squelch — and then the four
everyday services: broadcast FM, airband,
narrowband FM, and SSB/CW including HF
through an upconverter. The loop's
mechanics are verified on the lab
recording; what real signals sound like
through each step is standard practice,
stated as such, because the lab's sky
contains two tones and noise and nothing
else.

## The loop

Every listening task in GQRX is the same
four decisions, in this order:

1. **Tune.** Click the signal on the
   spectrum, drag, scroll, or type the
   frequency. You are placing the
   *demodulator* (chapter 3's two
   frequencies); if the target sits
   outside the current slice, the
   hardware recentres to contain it.
2. **Mode.** Choose the demodulator that
   matches how the signal was made
   (chapter 3's list). The wrong mode is
   the commonest cause of "visible but
   unintelligible": an FM signal in an AM
   demodulator is a loud, garbled
   presence, not a quiet one.
3. **Filter.** The passband should hug
   the signal: wide enough to hold it,
   narrow enough to exclude the
   neighbours. Wide / Normal / Narrow
   presets, the User width if you set
   one, and filter edges you can drag on
   the plot itself.
4. **Squelch.** Set the gate just above
   the noise, so silence is silent and
   signals open it. −150.0 dB (the
   shipped setting) is no gate at all.

Check: the loop's instruments, agreeing
with each other. With the lab file as the
input, the demodulator parked between
the tones, and then placed on the
stronger one — driven entirely through
the remote control (chapter 6), with the
on-screen meter reading the same numbers:

```
$ (session over TCP, one command at a time)
f                 → 14236000
l STRENGTH        → -51.2        (noise only)
F 14356000        → RPRT 0
l STRENGTH        → -6.0         (on the tone)
```

The −6.0 is checkable from the lab
file's recipe: the tone's amplitude is
0.5, and 20 × log₁₀(0.5) = −6.02 dBFS.
The meter is honest; so is the file.

## Broadcast FM: WFM, and the RDS readout

The starting point of most SDR evenings.
Mode **WFM (stereo)** (WFM (mono) for a
weak or noisy station — stereo costs
signal-to-noise), the station centred in
the filter, squelch usually unnecessary.
Stations sit on a regular grid (200 kHz
spacing in the Americas, 100 kHz in much
of Europe), which makes the waterfall
read like a ruler. **View → RDS** opens
the Radio Data System panel: the station
name, programme type, and text the
station broadcasts alongside the audio,
decoded from the signal itself. A mode
settings button (`...` beside Mode)
holds the mode-specific adjustments.
Documented-only in this guide — the lab
has no FM station to decode — but the
panel and its place in the menus are
captured facts (chapters 3 and 6; the
remote protocol even has RDS commands
that answer only in WFM mode).

## Airband: AM, patiently

Aircraft voice is AM, roughly 118–137
MHz, in channels spaced 25 kHz (8.33 kHz
in parts of Europe). Mode **AM** — in
the lab, an `m` query answered with a
10,000 Hz passband, the service's shape
in one number — and the squelch earns
its keep here, because the band is
silence punctuated by seconds of speech.
Workflow: squelch just above the noise,
then step through the local frequencies
(tower, approach, the area centre) and
wait. Nothing about the band rewards
haste; transmissions are brief and the
interesting ones are not announced. The
legality is the hobby's standard one
(chapter 1): airband is openly
transmitted and receivable in most
places; some jurisdictions restrict
*recording or relaying* it, which is a
reason to read your local rules before
chapter 6's recorder, not after.

## Narrowband FM: repeaters and utilities

**Narrow FM** is the voice of amateur
repeaters, marine and business radios,
and many utility services: deviation a
small fraction of broadcast FM's, so the
filter narrows to roughly a voice
channel (the presets' Narrow end) and
the squelch does real work. The workflow
is the airband one with the mode changed
— and one addition: repeaters listen on
one frequency and transmit on another,
offset by a standard amount for the
band, so a busy output frequency and a
silent input is the normal picture, not
a fault. CTCSS tones and offsets are
set on the *transmitting* side, which
GQRX is not (chapter 1); for listening,
mode, filter, and squelch are the whole
of your part.

## SSB and CW: the narrow end

Single sideband is half an AM signal —
one sideband, no carrier — and it asks
the most of the operator: the demodulator
must replace the missing carrier at
exactly the right frequency, or voices
slide toward ducks or toward mud. Mode
**USB** above 10 MHz and **LSB** below
it, by long amateur convention (the
receiver neither knows nor cares; the
convention is the stations'). The
passband is a voice's width: the lab's
remote session set 2400 Hz explicitly,
and a bookmark stored later showed the
mode's Normal preset at 2700 Hz. Tuning
is in small steps — GQRX tunes by
clicks, drags, and digit-by-digit entry,
and SSB is where the fine digits earn
their place. **CW-L / CW-U** are the
same demodulators with a much narrower
filter and an offset beat note, for
Morse: the workflow is to find the
stripe on the waterfall and centre it,
at which point the note's pitch is your
tuning error made audible.

## HF through an upconverter

An RTL-SDR's tuner floor is around
500 kHz at best and typically nearer
24 MHz in practice, so shortwave needs
help: an **upconverter** shifts the
0–30 MHz world up by a fixed offset
(125 MHz is a common one) into the
tuner's range. GQRX's part in the trick
is the **LNB LO** field (chapters 2 and
4): enter the offset, and the frequency
displays subtract it, so the dial reads
the true HF frequency while the hardware
listens 125 MHz higher. Everything else
is the SSB workflow above, plus HF's own
weather — the band that is busy at dusk
can be empty at noon, and no setting in
this panel changes that. Documented-only
in this guide: the fields are captured,
the converter and the ionosphere were
not available to the lab.
