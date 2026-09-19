import zipfile, os
from xml.etree import ElementTree as ET

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def q(t): return '{%s}%s' % (W, t)

BASE = 'D:/HuaweiMoveData/Users/Mindy/Desktop/AI study/E-portfolio'
INP = os.path.join(BASE, 'Module inputs', 'Module 1 inputs')
MOD = os.path.join(BASE, 'module1')

def para_runs(p):
    """Extract paragraph text, wrapping bold runs in **."""
    text = ''
    for r in p.iter(q('r')):
        t = ''.join(n.text or '' for n in r.iter(q('t')))
        rpr = r.find(q('rPr'))
        bold = False
        if rpr is not None:
            b = rpr.find(q('b'))
            if b is not None and b.get(q('val')) != '0':
                bold = True
        if bold and t.strip():
            text += '**' + t.strip() + '**'
        else:
            text += t
    return text

def docx_body(path):
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(q('body'))
    blocks = []
    for el in body:
        if el.tag == q('p'):
            txt = para_runs(el)
            if not txt.strip():
                blocks.append('')
                continue
            ppr = el.find(q('pPr'))
            style = ''
            if ppr is not None:
                ps = ppr.find(q('pStyle'))
                if ps is not None:
                    style = ps.get(q('val')) or ''
            if 'Heading1' in style:
                blocks.append('# ' + txt)
            elif 'Heading2' in style:
                blocks.append('## ' + txt)
            elif 'Heading3' in style:
                blocks.append('### ' + txt)
            else:
                blocks.append(txt)
        elif el.tag == q('tbl'):
            rows = []
            for tr in el.findall(q('tr')):
                cells = []
                for tc in tr.findall(q('tc')):
                    c = ''
                    for p in tc.findall(q('p')):
                        c += para_runs(p) + ' '
                    cells.append(c.strip())
                rows.append(cells)
            if rows:
                h = rows[0]
                blocks.append('| ' + ' | '.join(h) + ' |')
                blocks.append('| ' + ' | '.join(['---'] * len(h)) + ' |')
                for r in rows[1:]:
                    # pad short rows
                    r = (r + [''] * len(h))[:len(h)]
                    blocks.append('| ' + ' | '.join(r) + ' |')
                blocks.append('')
    return '\n'.join(blocks)

def file_to_md(typ, p):
    if typ == 'docx':
        return docx_body(p)
    if typ == 'md':
        return open(p, encoding='utf-8').read().strip('\n')
    if typ == 'txt':
        return open(p, encoding='utf-8', errors='ignore').read().strip('\n')
    if typ == 'py':
        s = open(p, encoding='utf-8', errors='ignore').read().strip('\n')
        return '```python\n' + s + '\n```'
    return ''

# Each unit -> ordered list of (type, path) from the ORIGINAL input files
sources = {
    2: [('docx', 'Unit2 task .docx'), ('docx', 'unit2 case study.docx')],
    3: [('docx', 'Unit3 algorithm analysis.docx')],
    4: [('docx', 'Unit4 software development methodologies.docx')],
    5: [('docx', 'Unit5 case study.docx'),
        ('md', 'Unit5 data_analysis_reflection.md'),
        ('py', 'Unit5 data_analysis_reflection.py')],
    6: [('txt', 'Unit6 AI model Analysis.txt'), ('py', 'Unit6 AI model.py')],
    7: [('docx', 'Unit7 Security Risk Assessment Report.docx')],
    8: [('docx', 'Unit8 Cybersecurity Threat Assessment and Mitigation Plan.docx')],
}

for u, srcs in sources.items():
    md_path = os.path.join(MOD, f'unit{u}.md')
    h1 = ''
    if os.path.exists(md_path):
        first = open(md_path, encoding='utf-8').readline()
        if first.startswith('# '):
            h1 = first.rstrip('\n')
    parts = [h1] if h1 else [f'# Unit {u}']
    parts.append('')
    for typ, name in srcs:
        p = os.path.join(INP, name)
        if not os.path.exists(p):
            print('MISSING', p)
            continue
        parts.append(file_to_md(typ, p))
        parts.append('')
    out = '\n'.join(parts).strip('\n') + '\n'
    open(md_path, 'w', encoding='utf-8').write(out)
    print(f'unit{u}.md  chars={len(out)}  paras~={out.count(chr(10))+1}')
print('DONE')
