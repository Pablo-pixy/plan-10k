import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import json
t=open(os.path.join(ROOT,'src','plantilla.html'),encoding='utf-8').read()
headextra='''<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#f3f5f4">
<link rel="apple-touch-icon" href="icon-v3-180.png">
<link rel="icon" href="icon-v3-180.png">
<link rel="manifest" href="manifest-%s.webmanifest">
<script>window.__OCR_LOCAL=true;</script>
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
'''
for pid,name,f,title in [('chico','Chico','tanaka','Plan 10K Chico'),('chica','Chica','gulati','Plan 10K Chica')]:
    s=t.replace('__PROFILE_ID__',pid).replace('__DEFAULT_NAME__',name).replace('__DEFAULT_FORMULA__',f)
    s=s.replace('<title>Plan 10K · 31 dic</title>','<title>'+title+'</title>\n'+headextra%pid,1)
    open(ROOT+'/'+pid+'.html','w',encoding='utf-8').write(s)
    man={"name":title,"short_name":"10K "+name,"start_url":"./"+pid+".html","scope":"./","display":"standalone","background_color":"#f3f5f4","theme_color":"#0b8a7e","lang":"es","icons":[{"src":"icon-v3-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"icon-v3-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"icon-v3-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]}
    open(ROOT+'/manifest-'+pid+'.webmanifest','w').write(json.dumps(man,ensure_ascii=False,indent=1))
index='''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Plan 10K</title><link rel="icon" href="icon-v3-180.png"><link rel="apple-touch-icon" href="icon-v3-180.png"><meta name="theme-color" content="#f3f5f4">
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f3f5f4;--card:#fff;--ink:#1c2220;--mut:#66716d;--teal:#0b8a7e;--teal2:#d3eeea;--violet:#7a5fc8;color-scheme:light}
*{box-sizing:border-box}body{margin:0;min-height:100vh;background:var(--bg);color:var(--ink);font:16px/1.5 'Figtree',-apple-system,system-ui,sans-serif}
main{max-width:480px;margin:0 auto;padding:max(40px,env(safe-area-inset-top)) max(16px,env(safe-area-inset-right)) 40px max(16px,env(safe-area-inset-left))}
h1{font-size:34px;line-height:1.1;margin:0 0 6px;letter-spacing:-.02em}p{color:var(--mut);margin:0 0 20px}
a.r{display:flex;align-items:center;gap:14px;margin:10px 0;padding:18px;border-radius:22px;background:var(--card);color:var(--ink);text-decoration:none;font-weight:700;font-size:18px}
a.r i{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;color:#fff;font-style:normal;font-size:18px;background:var(--teal)}
a.r:nth-of-type(2) i{background:var(--violet)}a.r span{margin-left:auto;color:var(--mut);font-weight:400}
.card{background:var(--card);border-radius:22px;padding:18px;margin-top:24px}.card b{display:block;margin-bottom:6px}
ol{margin:0;padding-left:20px;color:var(--mut)}li{margin:4px 0}
</style></head><body><main>
<h1>Plan 10K</h1><p>31 de diciembre de 2026 · elige tu plan</p>
<a class="r" href="chico.html"><i>C</i>Plan chico<span>›</span></a>
<a class="r" href="chica.html"><i>C</i>Plan chica<span>›</span></a>
<div class="card"><b>Tenlo como una app en el iPhone</b><ol><li>Abre tu plan en Safari.</li><li>Toca Compartir.</li><li>Elige «Añadir a pantalla de inicio».</li></ol><p style="margin:10px 0 0">Ábrelo siempre desde ese icono: así los datos quedan guardados en el móvil.</p></div>
</main></body></html>'''
open(ROOT+'/index.html','w',encoding='utf-8').write(index)
open(ROOT+'/.nojekyll','w').write('')
open(ROOT+'/README.md','w',encoding='utf-8').write('# Plan 10K\n\nPlan de entrenamiento adaptativo hasta un 10K el 31 de diciembre de 2026. Página estática: los datos de cada persona se guardan solo en su navegador.\n\nIncluye [Tesseract.js](https://github.com/naptha/tesseract.js) (Apache-2.0) y datos de idioma de tessdata para leer capturas en el propio dispositivo.\n')
print('ok')
