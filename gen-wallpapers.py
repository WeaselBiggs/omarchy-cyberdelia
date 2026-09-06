#!/usr/bin/env python3
"""Cyberdelia wallpapers: Hackers (1995) x Massive Attack sleeves x The Designers Republic."""
import pathlib, random, subprocess, sys, math, tempfile

W, H = 3840, 2560
if len(sys.argv) < 2:
    sys.exit("usage: gen-wallpapers.py <out-dir> [svg-scratch-dir]")
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
SVG = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(tempfile.mkdtemp(prefix="cyberdelia-"))
SVG.mkdir(parents=True, exist_ok=True)
BG="#0b0c1c"; BLK="#04040f"; MAG="#ff3ec9"; CYA="#00f0ff"; ACID="#7dff3a"
ORA="#ff7a1a"; YEL="#ffe600"; BLU="#4d7dff"; RED="#ff3860"; WHITE="#f4f7ff"
HEL="Nimbus Sans"; HELN="Nimbus Sans Narrow"; GOT="URW Gothic"; MONO="Noto Sans Mono"; JP="Noto Sans CJK JP"

DEFS = f"""
<defs>
 <pattern id="scan" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="2" fill="#000" opacity="0.30"/></pattern>
 <pattern id="scanlite" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="2" fill="#000" opacity="0.16"/></pattern>
 <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="14" cy="14" r="6" fill="#000"/></pattern>
 <pattern id="dotsw" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="14" cy="14" r="6" fill="{WHITE}"/></pattern>
 <pattern id="hazard" width="160" height="160" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="80" height="160" fill="{YEL}"/><rect x="80" width="80" height="160" fill="{BLK}"/></pattern>
 <pattern id="hazardm" width="160" height="160" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="80" height="160" fill="{MAG}"/><rect x="80" width="80" height="160" fill="{BLK}"/></pattern>
 <filter id="blurXL" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="230"/></filter>
 <filter id="blurL" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="120"/></filter>
 <filter id="blurM" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="40"/></filter>
 <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>
</defs>"""

def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{body}</svg>'
def t(x,y,s,size,fill,fam=HEL,weight="bold",extra=""):
    s=s.replace("&","&amp;")
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{weight}" font-size="{size}" fill="{fill}" {extra}>{s}</text>'
def mono(x,y,lines,size=44,fill=WHITE,lh=1.35,extra=""):
    return "".join(t(x, y+i*size*lh, l, size, fill, MONO, "bold", extra) for i,l in enumerate(lines))
def scan(id="scan"): return f'<rect width="{W}" height="{H}" fill="url(#{id})"/>'

# ---------- 1  HACK THE PLANET  (Protection-era out-of-focus neon + block-justified Helvetica)
def w1():
    b = f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    b += f'<g filter="url(#blurXL)" opacity="0.95">'
    b += f'<ellipse cx="2950" cy="520" rx="950" ry="720" fill="{ORA}"/>'
    b += f'<ellipse cx="800" cy="2000" rx="1150" ry="820" fill="{MAG}"/>'
    b += f'<ellipse cx="2500" cy="1950" rx="850" ry="620" fill="{CYA}"/>'
    b += f'<ellipse cx="350" cy="250" rx="650" ry="520" fill="{BLU}"/>'
    b += f'<ellipse cx="1900" cy="1150" rx="500" ry="380" fill="{ACID}" opacity="0.7"/>'
    b += '</g>'
    b += scan()
    b += f'<rect x="0" y="0" width="64" height="{H}" fill="url(#hazard)"/>'
    tl = 'textLength="1900" lengthAdjust="spacingAndGlyphs" letter-spacing="-28"'
    b += t(200,1510,"HACK",560,WHITE,extra=tl)
    b += t(200,1965,"THE",560,WHITE,extra=tl)
    b += t(200,2420,"PLANET",560,WHITE,extra=tl)
    b += f'<rect x="200" y="1050" width="1900" height="14" fill="{WHITE}"/>'
    b += mono(2400,180,["CYBERDELIA (TM)","NEW YORK CITY / 1995","SYSTEM ▶ ONLINE","REF. NO. HTP-001","MESS WITH THE BEST"],48,WHITE)
    b += f'<rect x="2400" y="560" width="1240" height="10" fill="{ACID}"/>'
    b += t(3560,640,"ハック・ザ・プラネット",150,ACID,JP,"900",'transform="rotate(90 3560 640)"')
    b += f'<polygon points="2400,2350 2560,2440 2400,2530" fill="{YEL}"/><polygon points="2600,2350 2760,2440 2600,2530" fill="{YEL}"/><polygon points="2800,2350 2960,2440 2800,2530" fill="{YEL}"/>'
    b += mono(3060,2455,["01/06"],56,YEL)
    return svg(b)

# ---------- 2  THE GIBSON  (neon towers, perspective floor, Futura-ish label)
def w2():
    rnd = random.Random(1995)
    b = f'<rect width="{W}" height="{H}" fill="{BLK}"/>'
    b += f'<defs><radialGradient id="hz" cx="0.5" cy="1" r="0.9"><stop offset="0" stop-color="{MAG}" stop-opacity="0.95"/><stop offset="0.45" stop-color="{BLU}" stop-opacity="0.35"/><stop offset="1" stop-color="{BLK}" stop-opacity="0"/></radialGradient>'
    b += f'<linearGradient id="tw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYA}" stop-opacity="0.95"/><stop offset="0.6" stop-color="{BLU}" stop-opacity="0.55"/><stop offset="1" stop-color="{MAG}" stop-opacity="0.15"/></linearGradient></defs>'
    HZ = 1380
    b += f'<rect x="0" y="0" width="{W}" height="{HZ}" fill="url(#hz)"/>'
    # floor grid
    g=''
    for i in range(-30,31):
        x2 = 1920 + i*260
        g += f'<line x1="1920" y1="{HZ}" x2="{x2}" y2="{H}" />'
    for k in range(1,22):
        y = HZ + (k*k)*2.6
        if y>H: break
        g += f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}"/>'
    b += f'<g stroke="{CYA}" stroke-width="3" opacity="0.55">{g}</g>'
    b += f'<g stroke="{CYA}" stroke-width="10" opacity="0.5" filter="url(#glow)">{g}</g>'
    # towers in 3 depth rows
    towers=''
    for row,(base,scale,n) in enumerate([(HZ-10,0.45,26),(HZ+120,0.75,16),(HZ+330,1.15,9)]):
        for i in range(n):
            x = rnd.uniform(-100, W-100)
            w = rnd.uniform(90,220)*scale
            h = rnd.uniform(380,1100)*scale
            y = base-h
            towers += f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="url(#tw)" stroke="{CYA}" stroke-width="{2+row}" />'
            for j in range(int(h//(60*scale))):
                yy = y + 25*scale + j*60*scale
                if rnd.random()<0.6:
                    towers += f'<rect x="{x+12*scale:.0f}" y="{yy:.0f}" width="{(w-24*scale)*rnd.uniform(0.3,1):.0f}" height="{6*scale:.0f}" fill="{ACID}" opacity="0.9"/>'
    b += f'<g filter="url(#glow)" opacity="0.8">{towers}</g>{towers}'
    b += scan("scanlite")
    b += t(180,520,"GIBSON",440,WHITE,GOT,"bold",'letter-spacing="70"')
    b += mono(190,640,["ELLINGSON MINERAL CORPORATION","SUPERCOMPUTER · NODE 00 · 1995","DA VINCI VIRUS ▶ STATUS: ARMED"],48,CYA)
    b += f'<rect x="2960" y="160" width="700" height="400" fill="{RED}"/>'
    b += t(3010,320,"WARNING",120,BLK,HELN,"bold")
    b += t(3010,460,"ACCESS DENIED",92,BLK,HELN,"bold")
    b += t(3660,2460,"ギブソン",210,MAG,JP,"900",'text-anchor="end"')
    b += mono(180,2455,["02/06"],56,YEL)
    return svg(b)

# ---------- 3  CRASH AND BURN  (Blue Lines flame + orange field + black band)
def w3():
    b = f'<rect width="{W}" height="{H}" fill="{ORA}"/>'
    b += f'<g filter="url(#blurXL)" opacity="0.9"><ellipse cx="2800" cy="700" rx="1000" ry="800" fill="{YEL}"/><ellipse cx="600" cy="2100" rx="1000" ry="700" fill="{MAG}"/><ellipse cx="2000" cy="2300" rx="700" ry="500" fill="{RED}"/></g>'
    b += f'<rect x="0" y="1700" width="{W}" height="{H-1700}" fill="url(#dots)" opacity="0.14"/>'
    # flame roundel
    flame = "M 0,-330 C 110,-220 190,-120 190,20 C 190,180 90,300 0,330 C -90,300 -190,180 -190,20 C -190,-60 -150,-130 -110,-180 C -110,-90 -60,-40 -20,-30 C -70,-120 -60,-230 0,-330 Z"
    b += f'<circle cx="3160" cy="640" r="480" fill="{WHITE}"/><path d="{flame}" transform="translate(3160,640) scale(1.15)" fill="{BLK}"/>'
    b += f'<rect x="0" y="1000" width="{W}" height="560" fill="{BLK}"/>'
    b += t(170,1420,"CRASH AND BURN",420,WHITE,extra='textLength="3500" lengthAdjust="spacingAndGlyphs" letter-spacing="-16"')
    b += mono(170,1660,["NO. 003 / DIS-CONNECT / GARBAGE FILE","IT'S NOT A CRIME TO HAVE A LITTLE FUN"],48,BLK)
    b += t(180,760,"クラッシュ・アンド・バーン",170,BLK,JP,"900")
    b += t(180,300,"CYBERDELIA",150,BLK,HELN,"bold",'letter-spacing="40"')
    b += f'<rect x="180" y="330" width="1950" height="12" fill="{BLK}"/>'
    b += mono(3660,2455,["03/06"],56,BLK,extra='text-anchor="end"')
    return svg(b)

# ---------- 4  ZERO COOL / 1507  (Wipeout livery: acid green, huge numerals, chevrons)
def w4():
    b = f'<rect width="{W}" height="{H}" fill="{ACID}"/>'
    b += f'<polygon points="2300,0 {W},0 {W},1500" fill="{MAG}"/>'
    b += f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#dots)" opacity="0.10"/>'
    b += t(90,1640,"1507",1500,BLK,extra='letter-spacing="-90"')
    b += f'<rect x="0" y="1780" width="2700" height="360" fill="{BLK}"/>'
    b += t(120,2060,"ZERO COOL",300,WHITE,extra='textLength="2440" lengthAdjust="spacingAndGlyphs"')
    for i,x in enumerate([2800,3120,3440]):
        b += f'<polygon points="{x},1780 {x+240},1960 {x},2140 {x+90},2140 {x+330},1960 {x+90},1780" fill="{BLK}"/>'
    b += mono(120,2300,["1988 · 1,507 SYSTEMS CRASHED IN A SINGLE DAY · SEVEN-POINT DROP ON THE NYSE","BANNED FROM COMPUTERS AND TOUCH-TONE TELEPHONES UNTIL HIS 18TH BIRTHDAY"],48,BLK)
    b += t(3660,300,"ゼロ・クール",200,BLK,JP,"900",'text-anchor="end"')
    b += mono(3660,2455,["04/06"],56,BLK,extra='text-anchor="end"')
    return svg(b)

# ---------- 5  ACID BURN  (magenta field, orbital roundel, hazard sash)
def w5():
    b = f'<rect width="{W}" height="{H}" fill="{MAG}"/>'
    b += f'<g filter="url(#blurL)" opacity="0.8"><ellipse cx="600" cy="500" rx="900" ry="600" fill="{RED}"/><ellipse cx="1800" cy="2400" rx="900" ry="500" fill="{ORA}"/></g>'
    b += f'<circle cx="2760" cy="1250" r="1000" fill="{CYA}"/>'
    b += f'<circle cx="2760" cy="1250" r="820" fill="none" stroke="{BLK}" stroke-width="70"/>'
    b += f'<circle cx="2760" cy="1250" r="560" fill="{BLK}"/>'
    b += f'<circle cx="2760" cy="1250" r="330" fill="{YEL}"/>'
    b += f'<circle cx="2760" cy="1250" r="110" fill="{BLK}"/>'
    b += f'<circle cx="3330" cy="720" r="150" fill="{WHITE}"/>'
    b += f'<g transform="rotate(-18 1920 2000)"><rect x="-600" y="1900" width="5200" height="240" fill="url(#hazard)"/></g>'
    b += scan("scanlite")
    b += t(150,900,"ACID",760,WHITE,HELN,"bold",'letter-spacing="-30"')
    b += t(150,1560,"BURN",760,WHITE,HELN,"bold",'letter-spacing="-30"')
    b += mono(170,1900,["CYBERDELIA · 05 · 1995 · RISC IS GOOD","THE FOUR MOST COMMON PASSWORDS:","LOVE · SEX · SECRET · GOD"],48,WHITE)
    b += t(3660,2460,"アシッド・バーン",190,WHITE,JP,"900",'text-anchor="end"')
    b += mono(170,2455,["05/06"],56,WHITE)
    return svg(b)

# ---------- 6  MESS WITH THE BEST  (smeared test-card bars under scanlines, Mezzanine black)
def w6():
    cols=[YEL,CYA,ACID,MAG,RED,BLU,ORA,WHITE]
    b = f'<rect width="{W}" height="{H}" fill="{BLK}"/>'
    bw = W/len(cols)
    bars = "".join(f'<rect x="{i*bw:.0f}" y="0" width="{bw+2:.0f}" height="1500" fill="{c}"/>' for i,c in enumerate(cols))
    b += f'<g filter="url(#blurM)">{bars}</g>'
    b += f'<g filter="url(#blurL)" opacity="0.7">{bars}</g>'
    b += f'<rect x="0" y="1500" width="{W}" height="{H-1500}" fill="{BLK}"/>'
    b += scan()
    b += t(160,1860,"MESS WITH THE BEST",300,WHITE,extra='textLength="3520" lengthAdjust="spacingAndGlyphs" letter-spacing="-10"')
    b += t(160,2170,"DIE LIKE THE REST",300,ACID,extra='textLength="3520" lengthAdjust="spacingAndGlyphs" letter-spacing="-10"')
    b += mono(160,2330,["CYBERDELIA · PAL 625/50 · COLOUR BARS · NO SIGNAL"],48,CYA)
    b += mono(3680,2330,["06/06"],56,YEL,extra='text-anchor="end"')
    b += f'<rect x="0" y="0" width="{W}" height="120" fill="{BLK}"/>' + t(160,92,"CYBERDELIA",84,WHITE,HELN,"bold",'letter-spacing="30"') + t(3680,92,"サイバーデリア",84,WHITE,JP,"900",'text-anchor="end"')
    return svg(b)

names = ["1-hack-the-planet","2-gibson","3-crash-and-burn","4-zero-cool","5-acid-burn","6-mess-with-the-best"]
for name, fn in zip(names,[w1,w2,w3,w4,w5,w6]):
    p = SVG/f"{name}.svg"; p.write_text(fn())
    subprocess.run(["rsvg-convert","-w",str(W),"-h",str(H),"-o",str(OUT/f"{name}.png"),str(p)],check=True)
    print("rendered",name)
