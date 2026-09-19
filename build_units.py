# -*- coding: utf-8 -*-
"""Convert module1/unitN.md -> module1/unitN.html as styled site pages.

The raw .md files are not served by the WorkBuddy preview server (they 404),
so we render them into proper HTML pages that match the portfolio look.
"""
import re
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MOD1 = os.path.join(ROOT, "module1")

# ---- navbar / footer markup reused from modules.html (paths use ../ to reach root) ----
NAVBAR = """    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="../index.html">Mingxia Qin</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu" aria-controls="navMenu" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navMenu">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                    <li class="nav-item"><a class="nav-link active" href="../modules.html">Modules</a></li>
                    <li class="nav-item"><a class="nav-link" href="../index.html#journey">Journey</a></li>
                </ul>
            </div>
        </div>
    </nav>"""

FOOTER = """    <footer class="footer-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <h3 class="footer-title">Let's Connect</h3>
                    <p class="footer-text">
                        I'm currently open to remote opportunities in AI education, EdTech content development,
                        and bilingual learning design. Let's build something meaningful together.
                    </p>
                </div>
                <div class="col-lg-6 text-lg-end">
                    <div class="footer-contacts">
                        <a href="mailto:your.name@example.com" class="footer-contact-item">
                            <i class="fas fa-envelope"></i>
                            <span>your.name@example.com</span>
                        </a>
                        <a href="#" class="footer-contact-item">
                            <i class="fab fa-linkedin-in"></i>
                            <span>linkedin.com/in/yourname</span>
                        </a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Mingxia Qin. E-Portfolio for University of Essex M.Sc. Artificial Intelligence.</p>
            </div>
        </div>
    </footer>"""

PAGE_CSS = """
        :root {
            --coral: #ff9f68; --lavender: #9b8bf4; --sunshine: #ffd166;
            --mint: #06d6a0; --blossom: #ff9fb7; --cream: #fff9f5;
            --ink: #2d3436; --soft-gray: #636e72;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: 'Poppins','Quicksand',sans-serif; background: var(--cream); color: var(--ink); line-height: 1.7; }
        .navbar { background: rgba(224,118,56,0.72) !important; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); box-shadow: 0 4px 18px rgba(224,118,56,0.25); padding: 0.5rem 0; }
        .navbar-brand { font-weight: 700; font-size: 1.5rem; color: #fff !important; letter-spacing: -0.5px; }
        .nav-link { font-weight: 500; color: rgba(255,255,255,0.82) !important; margin: 0 0.5rem; }
        .nav-link:hover, .nav-link.active { color: #fff !important; }
        .navbar-toggler { border-color: rgba(255,255,255,0.4) !important; }
        .navbar-toggler-icon { filter: invert(1); }
        .unit-hero { background: linear-gradient(135deg,#fff9f5 0%,#fff0e8 50%,#f5eeff 100%); padding: 60px 0 40px; border-bottom: 1px solid rgba(155,139,244,0.15); }
        .unit-hero .badge-mod { background: var(--lavender); color: #fff; font-weight: 600; padding: 0.35rem 0.9rem; border-radius: 999px; font-size: 0.85rem; }
        .unit-hero h1 { font-size: 2rem; font-weight: 700; margin: 0.8rem 0 0.3rem; }
        .unit-hero p.lead { color: var(--soft-gray); }
        .unit-body { max-width: 860px; margin: 0 auto; padding: 40px 0 30px; }
        .unit-body h2 { font-size: 1.35rem; font-weight: 700; margin: 2rem 0 0.8rem; color: var(--ink); border-left: 4px solid var(--coral); padding-left: 0.7rem; }
        .unit-body h3 { font-size: 1.1rem; font-weight: 700; margin: 1.4rem 0 0.6rem; color: var(--lavender); }
        .unit-body p { margin: 0.6rem 0; }
        .unit-body ul { margin: 0.6rem 0 0.6rem 1.2rem; }
        .unit-body li { margin: 0.3rem 0; }
        .unit-body blockquote { background: #fff; border-left: 4px solid var(--sunshine); padding: 1rem 1.2rem; border-radius: 10px; color: var(--soft-gray); margin: 1rem 0; font-style: italic; box-shadow: 0 4px 18px rgba(45,52,54,0.05); }
        .unit-body code { background: #f3eefc; color: #7a5fd6; padding: 0.1rem 0.4rem; border-radius: 6px; font-family: 'Consolas',monospace; font-size: 0.92em; }
        .unit-body pre { background: #2d3436; color: #f6f6f6; padding: 1.1rem 1.3rem; border-radius: 12px; overflow-x: auto; margin: 1rem 0; }
        .unit-body pre code { background: none; color: inherit; padding: 0; }
        .unit-body table { width: 100%; border-collapse: collapse; margin: 1rem 0; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 18px rgba(45,52,54,0.05); }
        .unit-body th, .unit-body td { border: 1px solid #eee; padding: 0.6rem 0.8rem; text-align: left; font-size: 0.95rem; }
        .unit-body th { background: var(--lavender); color: #fff; font-weight: 600; }
        .unit-body td code { background: #f3eefc; }
        .back-link { display: inline-block; margin: 0 0 1.5rem; color: var(--coral); text-decoration: none; font-weight: 600; }
        .back-link:hover { text-decoration: underline; }
        .footer-section { background: var(--ink); color: white; padding: 60px 0 30px; position: relative; overflow: hidden; }
        .footer-section::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg,var(--coral),var(--lavender),var(--sunshine),var(--mint)); background-size: 300% 300%; animation: gradientShift 5s ease infinite; }
        @keyframes gradientShift { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
        .footer-title { font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; }
        .footer-text { color: rgba(255,255,255,0.7); font-size: 0.95rem; }
        .footer-contacts { display: flex; flex-direction: column; gap: 0.9rem; align-items: flex-end; }
        .footer-contact-item { display: inline-flex; align-items: center; gap: 0.6rem; color: rgba(255,255,255,0.82); text-decoration: none; font-size: 0.98rem; }
        .footer-contact-item i { color: var(--coral); font-size: 1.15rem; width: 20px; text-align: center; }
        .footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); margin-top: 2rem; padding-top: 1.5rem; text-align: center; color: rgba(255,255,255,0.5); font-size: 0.85rem; }
    """

INLINE_RE_URL = re.compile(r"(https?://[^\s)]+)")
INLINE_RE_CODE = re.compile(r"`([^`]+?)`")
INLINE_RE_LINK = re.compile(r"\[([^\]]+?)\]\((https?://[^)]+?)\)")
INLINE_RE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_RE_ITAL = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")


def inline(text):
    text = INLINE_RE_URL.sub(
        lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(1), m.group(1)), text)
    text = INLINE_RE_CODE.sub(lambda m: "<code>" + m.group(1) + "</code>", text)
    text = INLINE_RE_LINK.sub(
        lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(2), m.group(1)), text)
    text = INLINE_RE_BOLD.sub(lambda m: "<strong>" + m.group(1) + "</strong>", text)
    text = INLINE_RE_ITAL.sub(lambda m: "<em>" + m.group(1) + "</em>", text)
    return text


def md_to_html(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    in_list = False
    in_code = False
    code_buf = []
    table_buf = []

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def flush_table():
        nonlocal table_buf
        if table_buf:
            out.append('<table class="table">')
            for idx, row in enumerate(table_buf):
                cells = [c.strip() for c in row.strip("|").split("|")]
                tag = "th" if idx == 0 else "td"
                out.append("<tr>" + "".join("<%s>%s</%s>" % (tag, inline(c), tag) for c in cells) + "</tr>")
            out.append("</table>")
            table_buf = []

    while i < n:
        line = lines[i]
        # code fence
        if line.strip().startswith("```"):
            if not in_code:
                flush_list(); flush_table()
                in_code = True
                code_buf = []
            else:
                out.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        # blank
        if not line.strip():
            flush_list(); flush_table()
            i += 1
            continue
        # table row
        if line.strip().startswith("|") and "|" in line[1:]:
            flush_list()
            # skip separator row
            if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
                i += 1
                continue
            table_buf.append(line)
            i += 1
            continue
        # heading
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush_list(); flush_table()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue
        # blockquote
        if line.lstrip().startswith(">"):
            flush_list(); flush_table()
            out.append("<blockquote>" + inline(line.lstrip()[1:].strip()) + "</blockquote>")
            i += 1
            continue
        # list item
        if re.match(r"^\s*-\s+", line):
            flush_table()
            if not in_list:
                out.append("<ul>")
                in_list = True
            item = re.sub(r"^\s*-\s+", "", line)
            out.append("<li>" + inline(item) + "</li>")
            i += 1
            continue
        # paragraph
        flush_list(); flush_table()
        out.append("<p>" + inline(line.strip()) + "</p>")
        i += 1
    flush_list(); flush_table()
    if in_code and code_buf:
        out.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
    return "\n".join(out)


def main():
    files = sorted(f for f in os.listdir(MOD1) if re.match(r"unit\d+\.md$", f))
    for f in files:
        path = os.path.join(MOD1, f)
        with open(path, encoding="utf-8") as fh:
            md = fh.read()
        html_body = md_to_html(md)
        # extract title + module number from first H1 "# Unit N · Title"
        title = f.replace(".md", "")
        m = re.search(r"^#\s+Unit\s+(\d+)\s*·\s*(.+)$", md, re.M)
        mod_no = m.group(1) if m else "?"
        unit_title = m.group(2) if m else title
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unit {mod_no} · {unit_title} | Mingxia Qin</title>
    <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../vendor/font-awesome/css/all.min.css">
    <link href="../vendor/fonts/google-fonts.css" rel="stylesheet">
    <style>{PAGE_CSS}</style>
</head>
<body>
{NAVBAR}
    <header class="unit-hero">
        <div class="container">
            <span class="badge-mod">Module 1 · Unit {mod_no}</span>
            <h1>{unit_title}</h1>
            <p class="lead">University of Essex — M.Sc. Artificial Intelligence</p>
        </div>
    </header>
    <main class="container">
        <div class="unit-body">
            <a class="back-link" href="../modules.html">&larr; Back to Modules Guide</a>
{html_body}
        </div>
    </main>
{FOOTER}
</body>
</html>
"""
        out_path = os.path.join(MOD1, f.replace(".md", ".html"))
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(page)
        print("generated", out_path)
    print("Done:", len(files), "pages")


if __name__ == "__main__":
    main()
