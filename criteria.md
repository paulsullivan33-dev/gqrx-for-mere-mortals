# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Standard 3 and 4 applied to this guide,
specifically: **the build machine had no
receiver, no antenna, and no sound card.**
Ubuntu 24.04 under a virtual display
(Xvfb); GQRX 2.17.4 was installed from the
Ubuntu archive, launched, and driven
through its own menus and dialogs with
synthetic input events, with screenshots
as the working captures. It was fed a
synthetic recording as its input device
and driven over its own remote-control
port. What that honestly produces —
captured first-run behaviour, captured
panels and menus, a captured protocol
session, and two recordings whose
contents were measured afterwards — is
what the guide is built from. The
screenshots themselves are not shipped;
the load-bearing outputs are quoted in
the chapters, and the remote-control
session is kept whole in
`examples/remote-session.txt`.

**The lab.** Two halves. (1) *The
recording:* a four-second file of complex
float32 samples at 1,000,000 samples per
second, synthesised, not received: a
tone of amplitude 0.5 at +120,000 Hz and
a tone of amplitude 0.15 at −200,000 Hz
over Gaussian noise, 32,000,000 bytes.
`examples/make-lab-file.py` regenerates
it (fixed seed, so byte-identical;
the build's own copy used the same
parameters unseeded — the noise differs,
the tones, which are all any measurement
here rests on, do not). (2) *The
absences:* no dongle existed, so the
file is the only input ever used; and no
audio device existed, so the session ran
against PulseAudio with a null sink —
audio was routed and recorded, never
heard. A second application shared the
virtual display during the build and
twice took keyboard focus; two stray
clicks on the spectrum retuned the
receiver (to 14.2885 MHz and later
14.3382 MHz). Both are reported where
they happened — one of them is chapter
7's cautionary bookmark — rather than
tidied away.

**Tools as installed** (Ubuntu 24.04
archive): gqrx-sdr 2.17.4-2build3,
gnuradio 3.10.9.2-1.1ubuntu2, and
gr-osmosdr 0.2.0 as the program itself
reports it. The package's own
documentation shipped in
`/usr/share/doc/gqrx-sdr/` — the manual
page and `remote-control.txt` — is the
source for the protocol's full command
list and the macOS/Windows notes, and
its `news.txt` changelog for the 2.17.x
feature history quoted.

**Verified by running, per chapter:**

- *Ch. 1:* `dpkg-query` versions;
  `gqrx --help` in full; the startup
  banner and the gr-osmosdr source-types
  line, captured from the program's own
  output.
- *Ch. 2:* the apt install itself; the
  first-run Configure I/O devices dialog
  and every field in it, screenshotted;
  the audio refusal ("Pulseaudio error:
  Connection refused", an Abort button,
  the same line on the terminal, the
  program ending on Abort); recovery by
  null sink (pactl output quoted); the
  `default.conf` the dialog wrote, byte
  for byte; `gqrx --list` output; the
  second launch opening the main window
  directly, DSP stopped.
- *Ch. 3:* the File, Tools, and View
  menus in full (screenshots); the
  status-bar hint text verbatim; the
  Receiver Options panel and its values
  as shipped; the Mode dropdown opened
  and its twelve entries read off; the
  Filter width dropdown (Wide / Normal
  / Narrow / User — opened by a stray
  click during the build and read, not
  assumed); the FFT Settings tab in
  full, including the RBW readout of
  122.1 Hz, which is 1,000,000 ÷ 8192 as
  the chapter states; the Audio dock
  and its tabbed settings popup (FFT /
  Recording / Network tabs seen).
- *Ch. 4:* the device string the dialog
  wrote for the file input; the Input
  controls panel in full for a file
  device; the absence of gain controls
  for that device, corroborated
  independently by the remote census
  (`l ?` → `SQL STRENGTH AF`, no
  `*_GAIN` entries).
- *Ch. 5:* the tune–mode–filter loop's
  mechanics end to end on the lab file:
  click-to-tune (twice, both captured),
  mode set and read back over the
  protocol (`AM` answering a 10,000 Hz
  passband; `M USB 2400` accepted), and
  the strength pair −51.2 dBFS (noise)
  → −6.0 dBFS (on the 0.5-amplitude
  tone), against the predicted
  20 × log₁₀(0.5) = −6.02 dBFS, with the
  on-screen meter agreeing (−51.0/−51.1).
  A bookmark saved afterwards stored the
  USB Normal preset as 2700 Hz, also
  quoted.
- *Ch. 6:* an audio recording started
  and stopped over the protocol
  (`U RECORD 1/0`, `u RECORD` → 1), the
  file it produced (name, and its WAV
  header read back with Python's wave
  module: 48000 Hz, 2 channels, 16-bit,
  114,462 frames), and the program's
  log lines for it; an I/Q recording
  made with the I/Q tool (Raw format):
  its filename, its size (24,770,112
  bytes = 3,096,264 samples = 3.10 s),
  and an FFT of its contents peaking at
  +120,000 Hz and −200,000 Hz at
  −10.5 dB relative, against the
  predicted −10.46 dB; the I/Q tool's
  own window (formats Raw and SigMF
  read off its dropdown); the remote
  server enabled through its settings
  dialog (port 7356, allowed hosts
  127.0.0.1, both read off the dialog),
  the listener visible in `ss` output,
  and the full session of
  `examples/remote-session.txt`
  including `_`, `M ?`'s thirteen mode
  codes, `L SQL -60` read back as
  −60.0, and `u DSP` → 1; the burst
  behaviour of chapter 6 and 9 (fourteen
  commands pipelined at once drew only
  the version reply; the same commands
  paced one at a time were answered in
  full).
- *Ch. 7:* the Add bookmark dialog; the
  resulting `bookmarks.csv` quoted byte
  for byte (including its storing the
  stray-click frequency 14,288,500 Hz);
  the bookmark's marker visible on the
  spectrum in later screenshots,
  including one taken before DSP start;
  the startup log's BandPlanFile and
  BookmarksFile lines; and the bandplan
  file itself — with a correction owed
  to the record: no `bandplan.csv`
  existed during or at the end of that
  first session, and an early draft of
  chapter 7 accordingly called
  bandplans bring-your-own. When the
  lab files were re-examined after a
  later start of the program, the file
  was there, fully populated (106
  entries; comma-separated
  `minFrequency, maxFrequency, mode,
  step, color, name`; USA-amateur,
  radionavigation, broadcast, and
  "Other" sections), timestamped with
  that run's final configuration save.
  Chapter 7 now reports exactly that
  timing and makes no claim about the
  mechanism.

**Capture hygiene (declared trims):**
menu and panel contents are quoted from
screenshots; no screenshot is reproduced
as an image in the guide. The startup
log's UHD network-discovery errors (the
sandbox forbids the broadcasts) are not
quoted in the chapters; they are this
environment's weather, not the program's
behaviour on a normal network. Sandbox
timestamps in filenames are the build
machine's clock (November 2026 in its
reckoning) and are weather, not claims.
One measured oddity is reported, not
explained: the WAV's 114,462 frames
(≈2.38 s) came from a recording left
running roughly twice that wall-clock
time; the chapters warn the reader to
treat the recorder's first moments as
startup rather than building a cause on
a single sandbox observation.

**Documented-only (not run), and why:**

- *Everything requiring a live receiver
  or antenna:* real reception of any
  service in chapter 5 (the workflows'
  band facts are standard practice,
  labelled in the chapter), the gain
  sliders real hardware adds to Input
  controls and their per-device names,
  hardware AGC behaviour, `rtl_tcp`
  serving, and all sound — the null
  sink means no human heard any of it.
- *RDS decoding, the AFSK1200 decoder,
  and the DX Cluster:* their menus,
  panels, and protocol commands were
  seen; no signal existed to decode,
  and the cluster is a network service.
- *The UDP audio stream:* the button
  and the Network settings tab were
  seen; a listener stood on port 7355
  (the port most often quoted for it)
  for a 14-second trial with default
  settings and heard nothing. The
  guide therefore describes the stream's
  purpose and tells the reader to set
  and verify the destination, and
  asserts no default.
- *The I/Q tool's Play, and a SigMF
  recording:* the controls were seen;
  neither was exercised. (Replay by the
  `file=` device string *was* exercised
  — it is how the whole lab ran.)
- *The mode and AGC `...` settings
  dialogs, and the squelch row's A and
  R buttons:* seen, not opened or
  exercised; the chapters accordingly
  do not describe their contents.
- *Installation beyond apt:* the Linux
  AppImage, the macOS disk image, and
  the experimental Windows binary are
  stated from the project's changelog
  and manual, not run.
- *The neighbours (chapter 8):* placed
  from their projects' material, none
  installed or run.
- *Upconversion end to end:* the LNB
  LO fields are captured; no converter
  or HF signal was available.

Specimen discipline, for the record:
the lab recording is synthetic — two
tones and noise made by a script in
this repo — so no broadcast, private or
otherwise, was received, recorded, or
quoted at any point in this build; the
sandbox received no RF at all.
