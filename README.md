# CYBERDELIA

```
  >>> ACCESSING ... GIBSON MAINFRAME
  >>> REF. NO. 1995/CD-06        PAL 625/50
  >>> USER: ZERO COOL            STATUS: *** UNAUTHORISED ***
  >>> LOADING THEME ..........  [ OK ]
```

*Hack the planet.* This is an [Omarchy](https://omarchy.org) theme for people
who think the 3D file browser in *Hackers* (1995) was a reasonable idea and the
world just wasn't ready. Picture a Massive Attack sleeve left face-down on a
Designers Republic light table in a club called Cyberdelia: out-of-focus neon
colour fields, block Helvetica headlines, hazard stripes, chevrons, numerals the
size of a bus, katakana nobody asked for, and "REF. NO." meta text on
everything. Deliberately garish. Pre-pre-Frutiger Aero. It's in the place where
I put that thing that time.

![Cyberdelia preview](preview.png)

## JACK IN

```bash
omarchy theme install https://github.com/WeaselBiggs/omarchy-cyberdelia.git
```

One line. No modem noises, but you're welcome to make them yourself. This clones
the repo into `~/.config/omarchy/themes/cyberdelia` and switches to it; from
then on it's in the theme menu like any other theme, except louder.

## THE PALETTE (RISC IS GOOD)

| Role | Hex | Codename |
| --- | --- | --- |
| background | `#0b0c1c` | CRT off, room dark, 3 a.m. |
| foreground | `#e6ecff` | phosphor |
| accent / magenta | `#ff3ec9` | Acid Burn |
| cyan | `#00f0ff` | cathode |
| acid green | `#7dff3a` | the good kind of virus |
| hazard yellow | `#ffe600` | DO NOT CROSS |
| orange | `#ff7a1a` | Protection-era sodium glow |
| blue | `#4d7dff` | Blue Lines |
| red | `#ff3860` | Crash and Burn |

The focused window gets the full Cyberdelia lightshow: a magenta into cyan into
acid green border gradient. It's one line in `colors.toml`, and Omarchy carries
it through to Hyprland, the bar and the notifications, so you always know which
window you're about to type the wrong password into.

## THE WALLPAPERS

Six of them in `backgrounds/`, rendered at 3840x2560 (3:2), one per line you
still quote when nobody's listening:

1. **Hack the Planet** — out-of-focus neon, block-justified Helvetica
2. **Gibson** — the mainframe, the towers, the scanlines
3. **Crash and Burn** — hazard stripes, chevrons, things going wrong on purpose
4. **Zero Cool / 1507** — one number, very large. 1,507 systems in one day.
5. **Acid Burn** — magenta field, orbital roundel, hazard sash
6. **Mess With the Best** — smeared test-card bars under scanlines. Die like the rest.

The four most common passwords are love, sex, secret and god. Please don't use
any of them on this machine.

## THE GENERATOR (or: it's a UNIX system, I know this)

The wallpapers aren't painted, they're *compiled*. `gen-wallpapers.py` writes
each one as an SVG and hands it to `rsvg-convert`:

```bash
python3 gen-wallpapers.py backgrounds/            # scratch SVGs go to a temp dir
python3 gen-wallpapers.py backgrounds/ /tmp/svg/  # or keep the SVGs to hand-edit
```

Needs `python3` and `librsvg` (`rsvg-convert`). The SVGs ask for these fonts by
name and fall back to whatever fontconfig hands them: Nimbus Sans, Nimbus Sans
Narrow, URW Gothic (all in `gsfonts`), Noto Sans Mono, and Noto Sans CJK JP for
the katakana. Each wallpaper is a function, `w1()` through `w6()`. Change the
colour constants at the top and you can re-tint the whole club. Type quickly and
look worried while you do it; it helps.

`preview.png` is the theme-menu card. Its source lives in `preview-src/`, a
`preview.svg` laid over `bg-preview.png`. Rebuild it with:

```bash
cd preview-src && rsvg-convert -w 1800 -h 1012 -o ../preview.png preview.svg
```

## FILE MANIFEST

- `colors.toml` — the palette Omarchy templates every app config from
- `icons.theme` — icon theme name (Yaru-magenta-dark)
- `backgrounds/` — the six wallpapers
- `preview.png`, `unlock.png` — theme-menu card and lock-screen logo
- `gen-wallpapers.py` — the wallpaper compiler
- `preview-src/` — preview card source
- `garbage file` — deleted. You didn't see it.

## LICENCE

MIT. Fonts and the icon theme are not included and carry their own licences.
There is no Secret Service involvement at this time.

```
  >>> CONNECTION TERMINATED.        MESS WITH THE BEST.
```
