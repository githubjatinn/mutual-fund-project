from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

title_slide_layout = prs.slide_layouts[0]
bullet_slide_layout = prs.slide_layouts[1]

slides_content = [
    ("Bluestock Mutual Fund Analytics",
     "Capstone Presentation\nJatin\nSPPU, Pune"),

    ("Project Overview", [
        "End-to-end mutual fund analytics platform",
        "6 Bluechip schemes, 19,798 records",
        "Python, SQLite, Power BI, Jupyter"
    ]),

    ("Data Pipeline", [
        "Live NAV fetched from mfapi.in",
        "6 schemes: HDFC, SBI, ICICI, Kotak, Nippon, Axis",
        "Cleaned, validated, loaded to SQLite"
    ]),

    ("EDA Findings", [
        "Axis Bluechip grew from Rs.10 to Rs.6,156 (2012-2026)",
        "High correlation (0.98-0.99) between HDFC, ICICI, Kotak, Nippon",
        "COVID 2020 crash visible in all schemes"
    ]),

    ("Performance Rankings", [
        "1. HDFC Top100 Direct - Score 100/100",
        "2. Kotak Bluechip - Score 86.7/100",
        "3. Nippon LargeCap - Score 81.1/100"
    ]),

    ("Risk Analysis", [
        "Highest VaR: Nippon LargeCap (-1.59%)",
        "Lowest VaR: Axis Bluechip (~0%)",
        "Best Sharpe: HDFC Top100 Direct (1.091)"
    ]),

    ("Recommendations", [
        "Conservative investors: Axis Bluechip",
        "Moderate investors: HDFC Top100, Kotak, Nippon",
        "Aggressive investors: HDFC Top100, Kotak, Nippon"
    ]),

    ("Thank You", [
        "GitHub: github.com/githubjatinn/mutual-fund-project",
        "Tag: v1.0",
        "Questions?"
    ]),
]

# Title slide
slide = prs.slides.add_slide(title_slide_layout)
slide.shapes.title.text = slides_content[0][0]
slide.placeholders[1].text = slides_content[0][1]

# Content slides
for title, bullets in slides_content[1:]:
    slide = prs.slides.add_slide(bullet_slide_layout)
    slide.shapes.title.text = title
    body = slide.placeholders[1].text_frame
    body.clear()
    for i, point in enumerate(bullets):
        if i == 0:
            p = body.paragraphs[0]
        else:
            p = body.add_paragraph()
        p.text = point
        p.font.size = Pt(24)

prs.save("dashboard/Bluestock_MF_Presentation.pptx")
print("PPTX created successfully!")