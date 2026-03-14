import re

with open('index.html') as f:
    html = f.read()
    lines = html.splitlines(keepends=True)

print(f"Total lines: {len(lines)}")

def get_lines(start, end):
    """Extract lines [start..end] (1-indexed, inclusive)."""
    return ''.join(lines[start-1:end])

# ─── Extract shared CSS + HEAD ─────────────────────────────────────────────
# Extract <head>...</head> + CSS from index.html
head_match = re.search(r'<head>.*?</head>', html, re.DOTALL)
HEAD = head_match.group(0)

# Extract logo base64 from nav (search full file)
logo_match = re.search(r'<img src="(data:image[^"]+)"', html)
LOGO = logo_match.group(1)

# ─── Shared page template ──────────────────────────────────────────────────
def page_nav(active_label=''):
    links = [
        ('/', 'Главная'),
        ('/product.html', 'Продукт'),
        ('/solution.html', 'Решение'),
        ('/market.html', 'Рынок'),
        ('/business-model.html', 'Бизнес-модель'),
        ('/traction.html', 'Тракция'),
        ('/team.html', 'Команда'),
        ('/roadmap.html', 'Роадмап'),
        ('/invest.html', 'Инвестиции'),
        ('/financials.html', '📊 Финмодель'),
        ('/business-plan.html', '📋 Бизнес-план'),
    ]
    nav_links = ''
    for href, label in links:
        style = ' style="color:var(--orange);font-weight:700"' if label == active_label else ''
        nav_links += f'    <a href="{href}"{style}>{label}</a>\n'

    return f'''<nav>
  <div class="nav-logo">
    <a href="/"><img src="{LOGO}" alt="GUTU"></a>
  </div>
  <div class="nav-links">
{nav_links}  </div>
  <a class="nav-cta" href="/invest.html">Инвестировать</a>
</nav>'''

FOOTER = '''<footer>
  <div class="f-logo">GUTU</div>
  <div class="f-copy">© 2026 GUTU. Умные столики для ресторанов. Баку, Азербайджан.</div>
  <div class="f-links">
    <a href="/">Главная</a> &nbsp;·&nbsp;
    <a href="/product.html">Продукт</a> &nbsp;·&nbsp;
    <a href="/market.html">Рынок</a> &nbsp;·&nbsp;
    <a href="/business-model.html">Бизнес-модель</a> &nbsp;·&nbsp;
    <a href="/team.html">Команда</a> &nbsp;·&nbsp;
    <a href="/invest.html">Инвестиции</a> &nbsp;·&nbsp;
    <span>info@gutu.com</span>
  </div>
</footer>'''

def wrap_page(title, active_label, body):
    return f'''<!DOCTYPE html>
<html lang="ru">
{HEAD.replace('<title>GUTU</title>', f'<title>GUTU — {title}</title>')}
<body>
{page_nav(active_label)}
{body}
{FOOTER}
</body>
</html>'''

# ─── Extract section blocks ────────────────────────────────────────────────
# Boundaries (1-indexed line numbers from index.html):
# 69-279:   Product: Features + Attention + Problem
# 280-314:  Solution
# 315-661:  Market Stats + Market Analysis
# 664-745:  Business Model section
# 746-787:  Traction section
# 788-993:  Gallery + Advertiser Features + Tariffs
# 994-1171: Financials section (internal summary)
# 1172-1224: Why GUTU Wins
# 1225-1283: Team
# 1284-1366: Roadmap comment + Go-to-market
# 1367-1476: Roadmap section + Supplier + Risks
# 1478-1687: Investment
# 1688-1760: CTA + Vision

FEATURES_PROBLEM    = get_lines(69, 279)
SOLUTION_BLOCK      = get_lines(280, 314)
MARKET_BLOCK        = get_lines(315, 661)
BIZMODEL_BLOCK      = get_lines(664, 745)
TRACTION_BLOCK      = get_lines(746, 787)
GALLERY_ADV_TARIFFS = get_lines(788, 993)
FINANCIALS_BLOCK    = get_lines(994, 1171)
WHY_BLOCK           = get_lines(1172, 1224)
TEAM_BLOCK          = get_lines(1225, 1283)
GTM_BLOCK           = get_lines(1284, 1366)   # roadmap comment + go-to-market
ROADMAP_RISKS_BLOCK = get_lines(1367, 1476)   # roadmap + supplier + risks
INVEST_BLOCK        = get_lines(1478, 1687)
VISION_CTA_BLOCK    = get_lines(1688, 1760)

# ─── 1. SOLUTION PAGE ─────────────────────────────────────────────────────
solution_page = wrap_page('Решение', 'Решение', SOLUTION_BLOCK)
with open('solution.html', 'w') as f:
    f.write(solution_page)
print(f"✅ solution.html ({len(solution_page):,} chars)")

# ─── 2. PRODUCT PAGE ──────────────────────────────────────────────────────
product_page = wrap_page('Продукт', 'Продукт',
    FEATURES_PROBLEM + '\n' + GALLERY_ADV_TARIFFS)
with open('product.html', 'w') as f:
    f.write(product_page)
print(f"✅ product.html ({len(product_page):,} chars)")

# ─── 3. MARKET PAGE ───────────────────────────────────────────────────────
market_page = wrap_page('Рынок', 'Рынок', MARKET_BLOCK)
with open('market.html', 'w') as f:
    f.write(market_page)
print(f"✅ market.html ({len(market_page):,} chars)")

# ─── 4. BUSINESS MODEL PAGE ───────────────────────────────────────────────
bizmodel_page = wrap_page('Бизнес-модель', 'Бизнес-модель',
    BIZMODEL_BLOCK + '\n' + FINANCIALS_BLOCK + '\n' + WHY_BLOCK)
with open('business-model.html', 'w') as f:
    f.write(bizmodel_page)
print(f"✅ business-model.html ({len(bizmodel_page):,} chars)")

# ─── 5. TRACTION PAGE ─────────────────────────────────────────────────────
traction_page = wrap_page('Тракция', 'Тракция',
    TRACTION_BLOCK + '\n' + GTM_BLOCK)
with open('traction.html', 'w') as f:
    f.write(traction_page)
print(f"✅ traction.html ({len(traction_page):,} chars)")

# ─── 6. TEAM PAGE ─────────────────────────────────────────────────────────
team_page = wrap_page('Команда', 'Команда', TEAM_BLOCK)
with open('team.html', 'w') as f:
    f.write(team_page)
print(f"✅ team.html ({len(team_page):,} chars)")

# ─── 7. ROADMAP PAGE ──────────────────────────────────────────────────────
roadmap_page = wrap_page('Роадмап', 'Роадмап', ROADMAP_RISKS_BLOCK)
with open('roadmap.html', 'w') as f:
    f.write(roadmap_page)
print(f"✅ roadmap.html ({len(roadmap_page):,} chars)")

# ─── 8. INVEST PAGE ───────────────────────────────────────────────────────
invest_page = wrap_page('Инвестиции', 'Инвестиции',
    INVEST_BLOCK + '\n' + VISION_CTA_BLOCK)
with open('invest.html', 'w') as f:
    f.write(invest_page)
print(f"✅ invest.html ({len(invest_page):,} chars)")

# ─── 9. CLEAN UP INDEX.HTML ───────────────────────────────────────────────
# Keep: Nav + Hero + Stats + new landing cards
hero_stats = get_lines(31, 68)

# New landing section with cards to all pages
LANDING_CARDS = '''
<section style="background:#fff;padding:80px 60px">
<div style="max-width:1100px;margin:0 auto">
  <div class="section-tag">Презентация для инвесторов</div>
  <h2 style="font-size:44px;font-weight:800;letter-spacing:-1.5px;margin-bottom:16px;line-height:1.1">
    GUTU — первая платформа умных<br>столиков для ресторанов Баку.
  </h2>
  <p style="font-size:18px;color:var(--text2);margin-bottom:48px;max-width:640px">
    Все разделы питч-дека доступны по отдельным ссылкам.
    Нажмите на нужный раздел.
  </p>

  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
    <a href="/solution.html" style="text-decoration:none;display:block;background:var(--black);border-radius:16px;padding:28px;transition:opacity 0.2s">
      <div style="font-size:32px;margin-bottom:12px">💡</div>
      <h4 style="font-size:18px;font-weight:800;color:#fff;margin-bottom:8px">Решение</h4>
      <p style="font-size:13px;color:#888">Как GUTU решает проблему ресторанов</p>
    </a>
    <a href="/product.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">📱</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Продукт</h4>
      <p style="font-size:13px;color:var(--text2)">Устройство, функции, галерея</p>
    </a>
    <a href="/market.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">📊</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Рынок</h4>
      <p style="font-size:13px;color:var(--text2)">TAM/SAM/SOM, конкурентный анализ</p>
    </a>
    <a href="/business-model.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">💰</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Бизнес-модель</h4>
      <p style="font-size:13px;color:var(--text2)">Тарифы, метрики, доходность</p>
    </a>
    <a href="/traction.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">🚀</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Тракция</h4>
      <p style="font-size:13px;color:var(--text2)">Что уже сделано, стратегия роста</p>
    </a>
    <a href="/team.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">👥</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Команда</h4>
      <p style="font-size:13px;color:var(--text2)">Aziz Haziyev + Ruslan Abbasov</p>
    </a>
    <a href="/roadmap.html" style="text-decoration:none;display:block;background:var(--gray);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">🗺️</div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:8px">Роадмап</h4>
      <p style="font-size:13px;color:var(--text2)">Планы, риски, поставщики</p>
    </a>
    <a href="/invest.html" style="text-decoration:none;display:block;background:var(--orange);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">🤝</div>
      <h4 style="font-size:18px;font-weight:800;color:#fff;margin-bottom:8px">Инвестиции</h4>
      <p style="font-size:13px;color:rgba(255,255,255,0.8)">$80K ask, форматы участия, видение</p>
    </a>
    <a href="/financials.html" style="text-decoration:none;display:block;background:var(--black);border-radius:16px;padding:28px">
      <div style="font-size:32px;margin-bottom:12px">📈</div>
      <h4 style="font-size:18px;font-weight:800;color:#fff;margin-bottom:8px">Финмодель</h4>
      <p style="font-size:13px;color:#888">Cash flow, ARR, ROI сценарии</p>
    </a>
  </div>
</div>
</section>
'''

# Read the original index.html nav
nav_start = html.index('<nav>')
nav_end = html.index('</nav>') + len('</nav>')
nav_block = html[nav_start:nav_end]

# Build clean index.html
new_index = f'''<!DOCTYPE html>
<html lang="ru">
{HEAD}
<body>
{nav_block}
{hero_stats}
{LANDING_CARDS}
{FOOTER}
</body>
</html>'''

# Update nav links in index to go to sub-pages (not anchors)
new_index = new_index.replace(
    '    <a href="#solution">Решение</a>',
    '    <a href="/solution.html">Решение</a>'
).replace(
    '    <a href="#features">Продукт</a>',
    '    <a href="/product.html">Продукт</a>'
).replace(
    '    <a href="#market">Рынок</a>',
    '    <a href="/market.html">Рынок</a>'
).replace(
    '    <a href="#business-model">Бизнес-модель</a>',
    '    <a href="/business-model.html">Бизнес-модель</a>'
).replace(
    '    <a href="#traction">Тракция</a>',
    '    <a href="/traction.html">Тракция</a>'
).replace(
    '    <a href="#financials">Финансы</a>',
    '    <a href="/financials.html">Финмодель</a>'
).replace(
    '    <a href="#team">Команда</a>',
    '    <a href="/team.html">Команда</a>'
).replace(
    '    <a href="#invest">Инвестиции</a>',
    '    <a href="/invest.html">Инвестиции</a>'
)

with open('index.html', 'w') as f:
    f.write(new_index)
print(f"✅ index.html (clean landing, {len(new_index):,} chars)")
print()
print("All pages built!")
