from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUT = ROOT / "README.pdf"


def make_styles():
    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        spaceAfter=6,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=10,
        spaceBefore=8,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        spaceAfter=8,
        spaceBefore=10,
    )
    h3 = ParagraphStyle(
        "H3",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=16,
        spaceAfter=6,
        spaceBefore=8,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=base,
        leftIndent=14,
        firstLineIndent=-8,
        spaceAfter=4,
    )
    num = ParagraphStyle(
        "Num",
        parent=base,
        leftIndent=14,
        firstLineIndent=-8,
        spaceAfter=4,
    )
    return base, h1, h2, h3, bullet, num


def add_svg(path: Path, story, max_width: float):
    if not path.exists():
        story.append(Paragraph(f"[Missing image: {path.as_posix()}]", styles[0]))
        story.append(Spacer(1, 0.2 * cm))
        return

    drawing = svg2rlg(str(path))
    if drawing is None:
        return
    scale = min(1.0, max_width / drawing.width)
    drawing.width *= scale
    drawing.height *= scale
    drawing.scale(scale, scale)
    story.append(drawing)
    story.append(Spacer(1, 0.25 * cm))


def to_html_inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


base, h1, h2, h3, bullet, num = make_styles()
styles = [base]

md = README.read_text(encoding="utf-8").splitlines()
doc = SimpleDocTemplate(
    str(OUT),
    pagesize=A4,
    leftMargin=1.8 * cm,
    rightMargin=1.8 * cm,
    topMargin=1.5 * cm,
    bottomMargin=1.5 * cm,
    title="Varroc Hackathon Team Playbook",
)
max_width = A4[0] - doc.leftMargin - doc.rightMargin
story = []

img_re = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
num_re = re.compile(r"^(\d+)\.\s+(.*)$")

for raw in md:
    line = raw.rstrip()

    if not line.strip():
        story.append(Spacer(1, 0.14 * cm))
        continue

    m = img_re.match(line.strip())
    if m:
        img_path = (ROOT / m.group(1)).resolve()
        add_svg(img_path, story, max_width)
        continue

    if line.startswith("### "):
        story.append(Paragraph(to_html_inline(line[4:]), h3))
        continue
    if line.startswith("## "):
        story.append(Paragraph(to_html_inline(line[3:]), h2))
        continue
    if line.startswith("# "):
        story.append(Paragraph(to_html_inline(line[2:]), h1))
        continue

    stripped = line.strip()
    if stripped.startswith("- "):
        story.append(Paragraph(f"- {to_html_inline(stripped[2:])}", bullet))
        continue

    n = num_re.match(stripped)
    if n:
        story.append(Paragraph(f"{n.group(1)}. {to_html_inline(n.group(2))}", num))
        continue

    story.append(Paragraph(to_html_inline(stripped), base))

doc.build(story)
print(f"Generated: {OUT}")
