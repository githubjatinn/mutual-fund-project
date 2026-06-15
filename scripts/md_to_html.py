import markdown

with open("reports/Final_Report.md", "r", encoding="utf-8") as f:
    text = f.read()

html = markdown.markdown(text, extensions=['tables'])

styled = f"""
<html>
<head>
<style>
body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; line-height: 1.6; }}
h1, h2, h3 {{ color: #2c3e50; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ddd; padding: 8px; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

with open("reports/Final_Report.html", "w", encoding="utf-8") as f:
    f.write(styled)

print("HTML created!")