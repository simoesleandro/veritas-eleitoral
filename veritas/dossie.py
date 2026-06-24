"""Dossie rendering helpers."""
from typing import Optional

import markdown

_CSS = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; line-height: 1.6; margin: 2cm; color: #1a2138; }
h1 { color: #4285F4; border-bottom: 2px solid #4285F4; padding-bottom: 8px; }
h2 { color: #1a2138; margin-top: 1.8em; border-bottom: 1px solid #e5e7eb; padding-bottom: 4px; }
h3 { color: #1a2138; margin-top: 1.5em; }
strong { color: #0f172a; }
em { color: #475569; }
code { background: #f1f5f9; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
blockquote { border-left: 3px solid #4285F4; padding: 0.5em 1em; background: #f8fafc; margin: 1em 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #e5e7eb; padding: 8px 12px; text-align: left; }
th { background: #f1f5f9; }
ul, ol { margin: 0.5em 0; padding-left: 1.5em; }
li { margin: 0.25em 0; }
hr { border: none; border-top: 1px solid #e5e7eb; margin: 2em 0; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 99px; font-size: 0.85em; font-weight: 600; }
.badge.falso { background: #fee; color: #c33; }
.badge.verdadeiro { background: #efe; color: #3a3; }
.balse.enganoso { background: #ffe; color: #a83; }
"""


def _md_to_html(md: str) -> str:
    return markdown.markdown(md, extensions=["tables", "fenced_code"])


def gerar_dossie_pdf(dossie_md: str, output_path: Optional[str] = None) -> bytes:
    raise NotImplementedError("PDF export is outside the Veritas Eleitoral MVP v1.")
