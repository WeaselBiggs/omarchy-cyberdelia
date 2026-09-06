# Cyberdelia

An [Omarchy](https://omarchy.org) theme. *Hackers* (1995) by way of a Massive
Attack sleeve and a Designers Republic layout: out-of-focus neon colour fields,
block Helvetica headlines, hazard stripes, chevrons, huge numerals, katakana and
"REF. NO." meta text. Deliberately garish. Pre-pre-Frutiger Aero.

![Cyberdelia preview](preview.png)

## Install

```bash
omarchy theme install https://github.com/WeaselBiggs/omarchy-cyberdelia.git
```

That clones this repo into `~/.config/omarchy/themes/cyberdelia` and switches to
it. Afterwards it shows up in the theme menu like any other theme.

## Palette

| Role | Hex |
| --- | --- |
| background | `#0b0c1c` |
| foreground | `#e6ecff` |
| accent / magenta | `#ff3ec9` |
| cyan | `#00f0ff` |
| acid green | `#7dff3a` |
| hazard yellow | `#ffe600` |
| orange | `#ff7a1a` |
| blue | `#4d7dff` |
| red | `#ff3860` |

Focused windows get a magenta into cyan into acid green border gradient. That
single `hyprland_active_border` line in `colors.toml` flows through to Hyprland,
the bar and notifications.

## Wallpapers

Six wallpapers in `backgrounds/`, rendered at 3840x2560 (3:2), one per line
from the film:

1. Hack the Planet
2. Gibson
3. Crash and Burn
4. Zero Cool / 1507
5. Acid Burn
6. Mess With the Best

They are generated, not painted. `gen-wallpapers.py` writes each one as an SVG
and renders it with `rsvg-convert`:

```bash
python3 gen-wallpapers.py backgrounds/            # scratch SVGs go to a temp dir
python3 gen-wallpapers.py backgrounds/ /tmp/svg/  # or keep the SVGs to hand-edit
```

Needs `python3` and `librsvg` (`rsvg-convert`). The SVGs reference these fonts
by name and fall back to whatever fontconfig gives you if they are missing:
Nimbus Sans, Nimbus Sans Narrow, URW Gothic (all in `gsfonts`), Noto Sans Mono
and Noto Sans CJK JP. Edit the `w1()` to `w6()` functions to change a
wallpaper, or the colour constants at the top to re-tint the lot.

`preview.png` is the theme-menu card. Its source is in `preview-src/`:
`preview.svg` laid over `bg-preview.png`. Rebuild it with:

```bash
cd preview-src && rsvg-convert -w 1800 -h 1012 -o ../preview.png preview.svg
```

## Files

- `colors.toml` — the palette Omarchy templates every app config from
- `icons.theme` — icon theme name (Yaru-magenta-dark)
- `backgrounds/` — the six wallpapers
- `preview.png`, `unlock.png` — theme-menu card and lock-screen logo
- `gen-wallpapers.py` — wallpaper generator
- `preview-src/` — preview card source

## Licence

MIT. Fonts and the icon theme are not included and carry their own licences.
