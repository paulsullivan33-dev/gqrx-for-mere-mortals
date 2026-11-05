# The Neighbours

**Scope:** everything around GQRX — the
other graphical receivers, the
command-line shelf, other people's
receivers on the web, and the
construction kit underneath them all.
None of these were run on the build
machine; this chapter places them, and
says so, exactly as the sibling guide's
neighbours chapter placed GQRX itself.

## The other receivers with dials

**SDR++** is the modern cross-platform
entry — Windows, macOS, and Linux — with
a module system that lets decoders and
sources plug into the receiver instead
of living in separate programs. For a
Windows reader (chapter 2's gap), it is
usually the first recommendation. **CubicSDR**
is the older, simpler cross-platform
receiver: fewer features, a gentler
surface, the same gr-osmosdr family of
devices underneath. **SDRangel** goes
furthest in the other direction: a large
application bundling demodulators and
decoders for dozens of modes — ADS-B,
packet radio, digital voice, satellite
telemetry — where GQRX deliberately
stops at listening. **SDR#** (SDRSharp)
is the Windows veteran, Airspy's own,
with a deep plugin bench; it does not
come to Linux.

What they trade, in one view: every one
of them draws the same waterfall over
the same samples. They differ in what
rides along (decoders, modules,
recording tools), in platform reach,
and in how much they ask you to learn
before the first station. GQRX's corner
of that space is the plain receiver
with the scriptable back door (chapter
6) and the plain-text bookmarks
(chapter 7) — a combination none of
the neighbours quite repeats.

## The command-line shelf

Nothing about choosing GQRX retires the
sibling guide's tools. `rtl_fm` still
listens without a screen and scripts
beautifully; `dump1090` and `rtl_433`
still decode what GQRX only lets you
hear; `rtl_power` still surveys a whole
band while GQRX shows a slice of it.
The honest division of labour: the
graphical receiver is for *exploring* —
finding what is there, learning its
shape — and the command line is for
*repeating* — the decode you want every
day, unattended. Most desks end up with
both, and chapter 5's workflows translate
between them without friction, because
the concepts (mode, filter, squelch,
gain) are the same concepts wearing
different clothes.

## Other people's receivers

**WebSDR** and **KiwiSDR** stations are
real receivers run by volunteers, whose
waterfalls stream to any browser: tune
them, pick a demodulator, listen — no
hardware, no install, and (relevant here)
a working picture of exactly the
interface this guide describes, drawn by
someone else's antenna. They are how
you check whether a silence is your
setup or the band, and how the HF bands
sound on the far side of the night. The
etiquette is that of any shared
instrument; the lesson for this guide's
reader is that the controls transfer.

## The engine room: GNU Radio

Every tool named in this chapter is,
underneath, a chain of blocks — source,
filter, demodulate, decode — plumbed in
some order. GQRX is one fixed chain,
drawn as a radio. **GNU Radio** is the
workshop the chain was built in: a
graphical companion (and a Python API)
for assembling your own from the live
stream. It is a subject the size of
this whole guide, and this guide's
honest place for it is the same pointer
the sibling guide gave: when the
decoder you want doesn't exist, or a
demodulator's *insides* are what you
actually want to know, that is the
door. Knowing it is under GQRX already
explains GQRX — the startup banner,
the layer-cake errors, the fact that a
missing sound card is a GNU Radio
complaint wearing a GQRX dialog.
