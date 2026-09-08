from pathlib import Path
from datetime import datetime

def render_html(out, title, checks, summary, metadata):
    rows=''.join(f'<tr><td>{c["name"]}</td><td class="{c["status"].lower()}">{c["status"]}</td><td>{c["detail"]}</td></tr>' for c in checks)
    html=f'''<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>body{{font-family:Arial,sans-serif;max-width:1000px;margin:40px auto;padding:0 20px;color:#222}}h1{{margin-bottom:4px}}.badge{{display:inline-block;padding:7px 12px;border-radius:6px;font-weight:bold}}.pass{{color:#18794e}}.warn{{color:#9a6700}}.fail{{color:#b42318}}table{{width:100%;border-collapse:collapse;margin-top:24px}}th,td{{padding:11px;border-bottom:1px solid #ddd;text-align:left}}th{{background:#f5f5f5}}.card{{padding:16px;border:1px solid #ddd;border-radius:8px;margin-top:18px}}</style></head>
<body><h1>{title}</h1><small>Generated {datetime.now().isoformat(timespec='seconds')}</small>
<div class="card"><span class="badge {summary['overall'].lower()}">OVERALL: {summary['overall']}</span><p>PASS: {summary['pass']} &nbsp; WARN: {summary['warn']} &nbsp; FAIL: {summary['fail']}</p></div>
<div class="card"><h2>Simulation metadata</h2><pre>{metadata}</pre></div>
<table><thead><tr><th>Check</th><th>Status</th><th>Details</th></tr></thead><tbody>{rows}</tbody></table>
</body></html>'''
    Path(out).write_text(html,encoding='utf-8')
