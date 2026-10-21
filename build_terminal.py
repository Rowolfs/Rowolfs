from pathlib import Path
from html import escape
p = Path(__file__).resolve().parent
(p/'assets').mkdir(exist_ok=True)
rows=[
(0.4,'$ ssh rowolfs@github','#dce5ef',True),
(2.0,'Connecting to github.com ...','#8796a8',False),
(2.7,'Connection established. Welcome back, Roman.','#73d9a2',False),
(4.0,'~ $ whoami','#dce5ef',True),
(5.1,'Roman Volkov / @Rowolfs','#f2f5f9',False),
(5.4,'Building AI-powered platforms, cloud infrastructure & automation.','#8796a8',False),
(6.8,'~ $ cat stack.txt','#dce5ef',True),
(8.0,'Python  /  Go  /  Docker  /  Linux','#73d9a2',False),
(9.4,'~ $ ls projects/','#dce5ef',True),
(10.6,'KolosLinux/  AITalkingAgent/  backyard-client-config-proxy-golang/','#8cbaff',False),
(10.9,'SchoolAdmin/  Task_manager/  shop-project/','#8cbaff',False),
(12.4,'~ $ help','#dce5ef',True),
(13.2,'whoami          a little about me','#8796a8',False),
(13.4,'cat stack.txt   tools I work with','#8796a8',False),
(13.6,'ls projects/    things I build','#8796a8',False),
(15.0,'~ $ ','#73d9a2',False),
]
css=['text{font-family:ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace;font-size:15px;white-space:pre}', '@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}','.cursor{animation:blink 1s step-end infinite}']
body=[]
for i,(t,s,c,typed) in enumerate(rows):
    start=t/22*100
    end=(t+(0.04*len(s) if typed else .01))/22*100
    width=len(s)*9.1+3
    css.append(f'@keyframes r{i}{{0%,{start:.3f}%{{width:0}}{end:.3f}%,97%{{width:{width:.1f}px}}100%{{width:0}}}}')
    css.append(f'#r{i}{{animation:r{i} 22s {"steps("+str(len(s))+",end)" if typed else "step-end"} infinite}}')
    body.append(f'<clipPath id="c{i}"><rect id="r{i}" x="30" y="{79+i*26}" width="{width}" height="25"/></clipPath>')
    body.append(f'<text x="30" y="{97+i*26}" fill="{c}" clip-path="url(#c{i})">{escape(s)}</text>')
css.append('@keyframes showCursor{0%,68.18%{opacity:0}68.19%,97%{opacity:1}100%{opacity:0}}.cursor-wrap{animation:showCursor 22s step-end infinite}')
css.append('@media(prefers-reduced-motion:reduce){rect[id^="r"]{animation:none!important}.cursor-wrap{animation:none}.cursor{animation:none}}')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="550" viewBox="0 0 880 550" role="img" aria-labelledby="title desc">
<title id="title">Rowolfs — terminal profile</title><desc id="desc">An animated terminal introducing Roman Volkov, his Python, Go, Docker and Linux stack, and public projects.</desc>
<style>{''.join(css)}</style>
<rect x="1" y="1" width="878" height="548" rx="14" fill="#0d1117" stroke="#303b49"/>
<path d="M15 1H865Q879 1 879 15V53H1V15Q1 1 15 1" fill="#171e28"/>
<path d="M1 53H879" stroke="#303b49"/>
<circle cx="26" cy="27" r="5.5" fill="#f07878"/><circle cx="46" cy="27" r="5.5" fill="#e9c46a"/><circle cx="66" cy="27" r="5.5" fill="#73d9a2"/>
<text x="440" y="32" text-anchor="middle" fill="#9baabd" style="font-size:12px">rowolfs@github: ~</text>
{''.join(body)}
<g class="cursor-wrap"><rect class="cursor" x="67" y="474" width="9" height="18" rx="1" fill="#73d9a2"/></g>
<circle cx="784" cy="523" r="3" fill="#73d9a2"/><text x="795" y="527" fill="#73d9a2" style="font-size:10px">CONNECTED</text>
</svg>'''
(p/'assets'/'terminal.svg').write_text(svg,encoding='utf-8')
(p/'README.md').write_text('![Animated terminal introducing Roman Volkov (@Rowolfs), his Python, Go, Docker and Linux stack, and public projects.](assets/terminal.svg)\n',encoding='utf-8')
projects = [
    ("KolosLinux", "C++ · Vulkan · Linux", "Prototype", "Linux-side AHardwareBuffer/dma-buf import and buffer lifecycle experiments on ARM64 Debian with Qualcomm Turnip."),
    ("AITalkingAgent", "Python · Whisper · Ollama · Piper", "Prototype", "Telegram voice conversations powered by local speech recognition, language-model inference and speech synthesis."),
    ("backyard-client-config-proxy-golang", "Go · HTTP · Docker", "Prototype", "Reverse proxy that transforms Remnawave subscription responses using user and host metadata."),
    ("SchoolAdmin", "TypeScript · Next.js · Prisma · PostgreSQL", "Coursework", "School administration application with separate frontend and backend services, data modeling and database migrations."),
    ("Task_manager", "Flutter · Dart", "Study project", "Construction project and defect tracking with role-specific screens and local persistence."),
    ("shop-project", "Node.js · WebSocket · Nginx · Docker", "Learning demo", "Storefront and admin interfaces, a product API and live chat, packaged as separate services."),
]
with (p/'README.md').open('a', encoding='utf-8') as f:
    f.write("\n## Selected projects\n\n")
    f.write("Systems programming, local AI, backend services and application development.\n\n")
    f.write("| Project | What it explores | Stack / status |\n| --- | --- | --- |\n")
    for name, stack, status, description in projects:
        f.write(f"| [{name}](https://github.com/Rowolfs/{name}) | {description} | {stack}<br>**{status}** |\n")
    f.write("\n[Browse all repositories →](https://github.com/Rowolfs?tab=repositories)\n")
import xml.etree.ElementTree as ET
ET.fromstring(svg)
print('SVG XML valid; generated',len(svg),'bytes')
