N=48
L=[]; a=L.append
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def cap(lo,hi,txt,preset=None): 
    p=f' Preset="{preset}"' if preset else ''
    a(f'  <Capability Min="{lo}" Max="{hi}"{p}>{esc(txt)}</Capability>')
a('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE FixtureDefinition>\n<FixtureDefinition xmlns="http://www.qlcplus.org/FixtureDefinition">')
a(' <Creator>\n  <Name>Q Light Controller Plus</Name>\n  <Version>4.14.4</Version>\n  <Author>Heath</Author>\n </Creator>')
a(' <Manufacturer>Xfalights</Manufacturer>\n <Model>LED RGB 3in1 192 Pixels Partition Bar Strobe Light</Model>\n <Type>LED Bar (Pixels)</Type>')
for c in ("Red","Green","Blue"): a(f' <Channel Name="{c}" Preset="Intensity{c}"/>')
a(' <Channel Name="Master dimmer" Preset="IntensityMasterDimmer"/>')
a(' <Channel Name="Strobe">\n  <Group Byte="0">Shutter</Group>')
cap(0,4,"Strobe off","ShutterOpen"); cap(5,255,"Strobe slow to fast","StrobeSlowToFast")
a(' </Channel>')
# 11 ch: CH3 function select
a(' <Channel Name="Function">\n  <Group Byte="0">Effect</Group>')
cap(0,5,"Manual: static RGB from ch 9-11")
cap(6,8,"Static colour, ch 4 selects colour")
cap(9,11,"Breathing, ch 5 selects colour")
cap(12,14,"Jump change")
cap(15,17,"Gradient change")
cap(18,20,"Pulse change, ch 5 selects colour")
for k in range(57):
    cap(21+3*k,23+3*k,f"Autorun effect {k+1}"+(" (full colour)" if k>=55 else ", ch 5 selects colour"))
cap(192,229,"Autorun effect 58 (full colour)")
for k in range(8):
    cap(230+3*k,255 if k==7 else 232+3*k,f"Sound mode {k+1}, ch 5 selects colour")
a(' </Channel>')
a(' <Channel Name="Colour / Speed / Sensitivity">\n  <Group Byte="0">Speed</Group>')
cap(0,255,"Static colour: red, green, blue, yellow, purple, cyan, white; autorun: speed slow to fast; sound: sensitivity low to high")
a(' </Channel>')
a(' <Channel Name="Effect Colour">\n  <Group Byte="0">Colour</Group>')
for lo,hi,t in [(0,28,"Default colour"),(29,56,"Red"),(57,85,"Green"),(86,113,"Blue"),(114,142,"Yellow"),
                (143,170,"Purple"),(171,199,"Cyan"),(200,227,"White"),(228,255,"User-defined colour (ch 6-8)")]: cap(lo,hi,t)
a(' </Channel>')
for grp in ("Autorun Effect Colour","Background Colour"):
    for c in ("Red","Green","Blue"):
        a(f' <Channel Name="{grp} {c}">\n  <Group Byte="0">Intensity</Group>\n  <Colour>{c}</Colour>')
        cap(0,255,f"{c} dark to bright"); a(' </Channel>')
for p in range(1,N+1):
    for c in ("Red","Green","Blue"): a(f' <Channel Name="{c} {p}" Preset="Intensity{c}"/>')
def mode(name,chs,head0=None):
    a(f' <Mode Name="{name}">')
    for i,c in enumerate(chs): a(f'  <Channel Number="{i}">{c}</Channel>')
    if head0 is not None:
        for p in range(N):
            a('  <Head>'); [a(f'   <Channel>{head0+3*p+k}</Channel>') for k in range(3)]; a('  </Head>')
    a(' </Mode>')
pix=[f"{c} {p}" for p in range(1,N+1) for c in ("Red","Green","Blue")]
mode("3 Channel",["Red","Green","Blue"])
mode("5 Channel",["Master dimmer","Strobe","Red","Green","Blue"])
mode("11 Channel",["Master dimmer","Strobe","Function","Colour / Speed / Sensitivity","Effect Colour"]
     +[f"Autorun Effect Colour {c}" for c in ("Red","Green","Blue")]+[f"Background Colour {c}" for c in ("Red","Green","Blue")])
mode("144 Channel",pix,0)
mode("146 Channel",["Master dimmer","Strobe"]+pix,2)
a(' <Physical>\n  <Bulb Type="LED" Lumens="0" ColourTemperature="0"/>\n  <Dimensions Weight="0" Width="1016" Height="120" Depth="150"/>\n  <Lens Name="Other" DegreesMin="0" DegreesMax="0"/>\n  <Focus Type="Fixed" PanMax="0" TiltMax="0"/>')
a(f'  <Layout Width="{N}" Height="1"/>\n  <Technical PowerConsumption="200" DmxConnector="3-pin"/>\n </Physical>\n</FixtureDefinition>')
import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Xfalights','Xfalights-192-Pixel-Partition-Bar-Strobe-Light.qxf'),'w').write("\n".join(L)+"\n")
