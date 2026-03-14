with open('index.html', 'r') as f:
    html = f.read()

original_len = len(html)

# ─── Extract sections to move to business-plan ────────────────────────────
def extract_between(html, start_marker, end_marker):
    """Extract html between start_marker and end_marker (not including end_marker)."""
    s = html.index(start_marker)
    e = html.index(end_marker)
    return html[s:e]

solution_html    = extract_between(html, '<!-- SOLUTION -->', '<!-- MARKET STATS -->')
market_ana_html  = extract_between(html, '<!-- MARKET ANALYSIS DEEP DIVE -->', '<!-- BUSINESS MODEL -->')
biz_model_html   = extract_between(html, '<!-- BUSINESS MODEL -->', '<section class="gallery-section"')
gtm_html         = extract_between(html, '<!-- GO-TO-MARKET -->', '<section class="roadmap-section">')
vision_html      = extract_between(html, '<!-- VISION -->', '<section class="cta-section">')

# Save extracted sections for reference
with open('/tmp/extracted_sections.html', 'w') as f:
    f.write(solution_html + market_ana_html + biz_model_html + gtm_html + vision_html)

# ─── Remove them from index.html ──────────────────────────────────────────
html = html.replace(solution_html, '', 1)
html = html.replace(market_ana_html, '', 1)
html = html.replace(biz_model_html, '', 1)
html = html.replace(gtm_html, '', 1)
html = html.replace(vision_html, '', 1)

# ─── Fix nav ──────────────────────────────────────────────────────────────
old_nav = '''    <a href="#solution">Решение</a>
    <a href="#features">Продукт</a>
    <a href="#market">Рынок</a>
    <a href="#business-model">Бизнес-модель</a>
    <a href="#traction">Тракция</a>
    <a href="#financials">Финансы</a>
    <a href="#team">Команда</a>
    <a href="#invest">Инвестиции</a>
    <a href="/financials.html" style="color:var(--orange);font-weight:700">📊 Финмодель</a>
    <a href="/business-plan.html" style="color:var(--orange);font-weight:700">📋 Бизнес-план</a>'''

new_nav = '''    <a href="#features">Продукт</a>
    <a href="#market">Рынок</a>
    <a href="#pricing">Тарифы</a>
    <a href="#team">Команда</a>
    <a href="#invest">Инвестиции</a>
    <a href="/financials.html" style="color:var(--orange);font-weight:700">📊 Финмодель</a>
    <a href="/business-plan.html" style="color:var(--orange);font-weight:700">📋 Бизнес-план</a>'''

assert old_nav in html, "Nav not found — check whitespace"
html = html.replace(old_nav, new_nav, 1)

with open('index.html', 'w') as f:
    f.write(html)

new_len = len(html)
print(f"Done! Removed {(original_len - new_len):,} chars from index.html")
print(f"  Before: {original_len:,} | After: {new_len:,}")
print()
print("Removed sections (saved to /tmp/extracted_sections.html):")
print(f"  - Solution: {len(solution_html):,} chars")
print(f"  - Market Analysis: {len(market_ana_html):,} chars")
print(f"  - Business Model + Traction: {len(biz_model_html):,} chars")
print(f"  - Go-to-market: {len(gtm_html):,} chars")
print(f"  - Vision: {len(vision_html):,} chars")
