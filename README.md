# QLC+ fixture profiles — Xfalights

[QLC+](https://www.qlcplus.org/) 4 fixture definitions for Xfalights lights that QLC+ doesn't ship a profile for.

| Fixture | File | Modes |
|---|---|---|
| Xfalights LED RGB 3in1 192 Pixels Partition Bar Strobe Light (200 W, 768 LEDs, 48 pixels) | [`Xfalights/Xfalights-192-Pixel-Partition-Bar-Strobe-Light.qxf`](Xfalights/Xfalights-192-Pixel-Partition-Bar-Strobe-Light.qxf) | 3, 5, 11, 144, 146 ch |

## Install

Copy the `.qxf` into your QLC+ user fixtures folder and restart QLC+:

- **macOS:** `~/Library/Application Support/QLC+/Fixtures/`
- **Windows:** `%USERPROFILE%\QLC+\Fixtures\`
- **Linux:** `~/.qlcplus/fixtures/`

It then appears under **Xfalights → LED RGB 3in1 192 Pixels Partition Bar Strobe Light**.

## 192 Pixels Partition Bar — channel modes

The "192 partitions" are 4 × 48 LED groups; DMX addresses them as 48 RGB pixels.

| Mode | Layout |
|---|---|
| 3 ch | Red, Green, Blue (whole bar) |
| 5 ch | Master dimmer, Strobe, Red, Green, Blue |
| 11 ch | Master dimmer, Strobe, Function, Colour/Speed/Sensitivity, Effect Colour, Autorun Effect Colour R/G/B, Background Colour R/G/B |
| 144 ch | 48 pixels × RGB (R1 G1 B1 … R48 G48 B48) — 48 heads for the RGB Matrix |
| 146 ch | Master dimmer, Strobe, then 48 pixels × RGB — 48 heads |

**Strobe:** 0–4 off, 5–255 slow → fast.

**Function (11 ch, CH3):**

| Value | Function |
|---|---|
| 0–5 | Manual — static RGB from CH9–11 (Background Colour) |
| 6–8 | Static colour — CH4 picks red, green, blue, yellow, purple, cyan or white |
| 9–11 / 12–14 / 15–17 / 18–20 | Breathing / Jump change / Gradient change / Pulse change |
| 21–185 | Autorun effects 1–55 (3 values each), colour from CH5 |
| 186–188 / 189–191 / 192–229 | Autorun effects 56 / 57 / 58, full colour |
| 230–255 | Sound modes 1–8 (3 values each, 8 = 251–255), colour from CH5 |

**CH4** is static colour select, autorun speed (slow → fast) or sound sensitivity (low → high),
depending on the function. QLC+ can't switch a channel's meaning, so it is one channel with all three described.

**Effect Colour (CH5):** default (0–28), red, green, blue, yellow, purple, cyan, white, then
user-defined (228–255) which takes its colour from CH6–8.

## Sources

- The printed Xfalights user manual (section 5, DMX Channels).
- Cross-checked against Lightkey's built-in "Xfalights – LED RGB 3in1 192 Pixels Partition Bar
  Strobe Light" profile, which agrees on every channel except the bottom of the strobe range
  (Lightkey starts strobe at 0; the manual at 5).

The manual elides autorun effects 4–55; they are assumed to take their colour from CH5 like
effects 1–3. Dimensions (40 × 4.7 × 5.9 in) and power come from the retail listing; weight and
lumens aren't published, so they are left at 0. They don't affect control.

## Regenerating

The `.qxf` is generated so the 144 pixel channels and 70-odd function ranges stay consistent:

```bash
python3 generate_xfalights_192_pixel_bar.py
```

Status: the XML validates and every mode resolves; not yet exercised against a bar in QLC+.

## License

[Millstone Solutions Church and Ministry Use License](LICENSE). This is source-available, not open source.
Christian churches and ministries may use it free of charge. Installers may set it up for them.
Any other use requires written permission; to ask, open an issue.
