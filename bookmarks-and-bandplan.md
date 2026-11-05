# Bookmarks and the Bandplan

**Scope:** GQRX's memory — the stations
you save, the file they live in (quoted
exactly, because it is plain text and
yours), tags and colours, and the
bandplan file the program looks for but
does not provide.

## Saving a station

Tune to something worth keeping, set its
mode and filter the way you like them,
and **Tools → Add bookmark**
(Ctrl+Shift+B). The dialog asks for one
thing — a name — and offers tags:
**Create new Tag** makes one, and the
tags you already have are listed for
ticking. Everything else about the
station, GQRX already knows, and saves
for you.

Check: the file the dialog wrote, in
`~/.config/gqrx/bookmarks.csv`, after
one bookmark was saved in the lab. This
is the whole file, quoted exactly:

```
# Tag name          ;  color
Untagged            ; #c0c0c0

# Frequency ; Name                     ; Modulation          ;  Bandwidth; Tags
    14288500; Lab tone                 ; USB                 ;       2700; Untagged
```

## Reading the format

The file is semicolon-separated text in
two sections, and it is a contract you
can write by hand:

- **Tags first.** Each tag is a name and
  a colour, as a hex value. The default
  tag, Untagged, is grey (`#c0c0c0`).
  Colours are what the spectrum markers
  (below) are drawn in.
- **Then the stations.** Frequency in
  Hz, name, modulation in the remote
  protocol's spelling (chapter 6's codes:
  USB here), bandwidth in Hz, and the
  tag list.

The lab's single entry is worth reading
as a caution as well as an example. It
stored 14,288,500 Hz, USB, 2700 Hz —
because those were the receiver's
settings at the moment of saving, and
the moment of saving was a few minutes
after a stray click on the spectrum had
moved the demodulator off the tone the
operator meant to save (chapter 5's
click-to-tune, working as designed).
The 2700 is instructive too: it is the
USB Normal filter preset, current at
the time — not the 2400 the remote
session had set earlier and the click
had since reset. **A bookmark is a
photograph of the panel, not of your
intentions.** Set the station up, look
at it, then save.

`examples/bookmarks-sample.csv` is a
starter file in this exact format, with
generic entries, for readers who would
rather edit than click.

## Using them

Saved stations appear in two places.
On the spectrum, each bookmark draws a
**labelled marker** at its frequency in
its tag's colour — in the lab's captures
the "Lab tone" flag stands over
14.29 MHz in shot after shot, including
before the DSP starts, because the
markers come from the file, not the
signal. And **View → Bookmarks**
(Ctrl+B) opens the bookmarks panel: the
list, by tag, from which a double-click
(or the panel's controls) returns the
receiver to the station, mode and
bandwidth included. Deleting is the
panel's job too (the changelog records
the Delete key as the shortcut for it).
Editing the CSV in a text editor while
GQRX is closed achieves the same ends
in bulk — it is your file, in your
config directory, in a format the
program itself documents on the file's
own comment lines.

## The bandplan: the map under the markers

GQRX's startup log names a second file:

```
BandPlanFile is /home/<you>/.config/gqrx/bandplan.csv
BookmarksFile is /home/<you>/.config/gqrx/bookmarks.csv
```

The **bandplan** is the chart of what
lives where — the amateur allocations,
the broadcast bands, the airband — drawn
as shading behind the spectrum (the
**Band Plan** checkbox in FFT Settings,
chapter 3, controls its display) and
used to label regions you sweep across.
GQRX carries a built-in default and
writes it out to that path as its
configuration settles: on the build
machine the file had not appeared during
the first session — bookmarks saved, no
bandplan beside them — and by the next
start it was there in full. Check the
folder before assuming you must supply
one.

Check: the written file's own header and
shape, from the lab's copy:

```
# minFrequency, maxFrequency, mode, step, color, name

# USA Amateur Radio
135700,       137800,       CW,  10, #90009470, 2200m Ham Band
...
118000000, 137000000, AM,   5000, #900000FF, Air Band Voice
```

Comma-separated this time, note — not
the bookmarks file's semicolons. One
line per band: lowest and highest
frequency in Hz, the mode a listener
would use there, a tuning step, a colour
(an alpha value rides in front: the
`#90` of `#90009470` is translucency),
and a name. The default's 106 entries
run in four sections — USA amateur
bands, radionavigation (its header
credits an NTIA allocation chart),
broadcast, and a remainder of air band,
marine, CB, and the like. It is, by
construction, an American chart; a
reader elsewhere edits the file — it is
as plain as the bookmarks file, and
yours once written — or replaces it
with a local one in the same format.
