# Builds index.html from src/template.html + the reviewed answer key JSON, wired to claude-shim.js.
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.load(open(root/'src'/'customer-service-robot.json', encoding='utf-8'))
js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
html = (root/'src'/'template.html').read_text(encoding='utf-8')
html = html.replace('/*__EXAMPLE_JSON__*/null', js, 1)
html = html.replace('<script>', '<script src="claude-shim.js"></script>\n<script>', 1)
html = html.replace('로그인한 claude.ai 계정으로 Claude 초안을 바로 만들 수 있습니다.', 'Claude로 초안을 바로 만들 수 있습니다.')
html = html.replace('Draft with Claude right away from your claude.ai account.', 'Draft with Claude right away.')
# The template is an artifact body; a standalone page needs its own document skeleton.
if not html.lstrip().lower().startswith('<!doctype'):
    html = '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="robots" content="noindex">\n' + html
(root/'index.html').write_text(html, encoding='utf-8')
print('wrote index.html')
