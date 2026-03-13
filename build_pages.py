import re

with open('index.html', 'r') as f:
    index = f.read()

# Extract logo base64
nav_start = index.index('<nav>')
nav_end = index.index('</nav>') + len('</nav>')
nav_block = index[nav_start:nav_end]
logo_match = re.search(r'<img src="(data:image/png;base64,[^"]+)"', nav_block)
LOGO = logo_match.group(1)

# ─── NAV for index.html (update with new page links) ───────────────────────
new_index_nav = f'''<nav>
  <div class="nav-logo">
    <a href="/"><img src="{LOGO}" alt="GUTU"></a>
  </div>
  <div class="nav-links">
    <a href="#features">Продукт</a>
    <a href="#market">Рынок</a>
    <a href="#market-analysis">Анализ рынка</a>
    <a href="#financials">Финансы</a>
    <a href="#team">Команда</a>
    <a href="#invest">Инвестиции</a>
    <a href="/financials.html" style="color:var(--orange);font-weight:700">📊 Финмодель</a>
    <a href="/business-plan.html" style="color:var(--orange);font-weight:700">📋 Бизнес-план</a>
  </div>
  <button class="nav-cta" onclick="document.getElementById('invest').scrollIntoView({{behavior:'smooth'}})">Инвестировать в GUTU</button>
</nav>'''

# ─── NAV for sub-pages ────────────────────────────────────────────────────
def page_nav(active_href):
    active_style = lambda href: ' style="color:var(--orange);font-weight:700"' if href == active_href else ''
    return f'''<nav>
  <div class="nav-logo">
    <a href="/"><img src="{LOGO}" alt="GUTU"></a>
  </div>
  <div class="nav-links">
    <a href="/">← Главная</a>
    <a href="/financials.html"{active_style('/financials.html')}>📊 Финмодель</a>
    <a href="/business-plan.html"{active_style('/business-plan.html')}>📋 Бизнес-план</a>
  </div>
  <a class="nav-cta" href="mailto:info@gutu.com">Связаться</a>
</nav>'''

FOOTER = '''<footer>
  <div class="f-logo">GUTU</div>
  <div class="f-copy">© 2026 GUTU. Умные столики для ресторанов. Баку, Азербайджан.</div>
  <div class="f-links">
    <a href="/">Главная</a> &nbsp;·&nbsp;
    <a href="/financials.html">Финмодель</a> &nbsp;·&nbsp;
    <a href="/business-plan.html">Бизнес-план</a> &nbsp;·&nbsp;
    <span>info@gutu.com</span>
  </div>
</footer>'''

# ─────────────────────────────────────────────────────────────────────────────
# FINANCIALS.HTML
# ─────────────────────────────────────────────────────────────────────────────
FINANCIALS = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>GUTU — Финансовая модель</title>
  <link rel="stylesheet" href="/src/style.css"/>
  <script type="module" src="/src/main.js"></script>
  <style>
    .fin-hero{{background:var(--black);padding:100px 60px 80px;text-align:center}}
    .fin-hero h1{{font-size:56px;font-weight:800;color:#fff;letter-spacing:-2px;margin-bottom:16px}}
    .fin-hero h1 span{{color:var(--orange)}}
    .fin-hero p{{font-size:18px;color:#888;max-width:600px;margin:0 auto}}

    .cf-table-section{{padding:80px 60px;background:#fff}}
    .cf-inner{{max-width:1400px;margin:0 auto;overflow-x:auto}}
    .cf-table{{width:100%;border-collapse:collapse;font-size:13px}}
    .cf-table th{{background:var(--black);color:#fff;padding:12px 10px;text-align:center;white-space:nowrap;font-weight:700}}
    .cf-table th:first-child{{text-align:left;padding-left:16px}}
    .cf-table td{{padding:10px;text-align:center;border-bottom:1px solid var(--gray2);white-space:nowrap}}
    .cf-table td:first-child{{text-align:left;padding-left:16px;font-weight:600;color:var(--text)}}
    .cf-table tr:nth-child(even){{background:var(--gray)}}
    .cf-table .row-sep td{{background:#f0f0f0;font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#888}}
    .cf-table .row-total td{{background:#0a0a0a;color:#fff;font-weight:800;font-size:14px}}
    .cf-table .row-total td:first-child{{color:#fff}}
    .cf-table .row-cumul td{{background:var(--orange);color:#fff;font-weight:800}}
    .green{{color:#16a34a;font-weight:700}}
    .red{{color:#dc2626;font-weight:700}}
    .orange-val{{color:var(--orange);font-weight:700}}
    .cf-table tr.row-net td.pos{{color:#16a34a;font-weight:800}}
    .cf-table tr.row-net td.neg{{color:#dc2626;font-weight:800}}

    .unit-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}}
    .unit-card{{border:1.5px solid var(--gray2);border-radius:16px;padding:28px 24px}}
    .unit-card h4{{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--orange);margin-bottom:16px}}
    .unit-row{{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--gray2);font-size:14px}}
    .unit-row:last-child{{border-bottom:none}}
    .unit-row .lbl{{color:var(--text2)}}
    .unit-row .val{{font-weight:700;color:var(--text)}}
    .unit-row .val.accent{{color:var(--orange)}}

    .funds-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}}
    .fund-card{{border-radius:16px;padding:28px 24px;background:var(--gray)}}
    .fund-card .pct{{font-size:40px;font-weight:800;color:var(--orange);letter-spacing:-1px}}
    .fund-card h4{{font-size:16px;font-weight:700;margin:8px 0}}
    .fund-card p{{font-size:13px;color:var(--text2);line-height:1.6}}
    .fund-card .amt{{font-size:22px;font-weight:800;margin-top:12px;color:var(--text)}}

    .arr-table{{width:100%;border-collapse:collapse;margin-top:40px}}
    .arr-table th{{background:var(--black);color:#fff;padding:14px 20px;text-align:center;font-weight:700}}
    .arr-table td{{padding:16px 20px;text-align:center;border-bottom:1px solid var(--gray2);font-size:15px}}
    .arr-table tr.best{{background:#0a0a0a}}
    .arr-table tr.best td{{color:#fff;font-weight:700}}
    .arr-table tr.best td:first-child{{border-radius:0}}
    .arr-highlight{{color:var(--orange);font-weight:800}}

    .rev-bars{{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:40px;align-items:start}}
    .rev-bar-block h4{{font-size:16px;font-weight:700;margin-bottom:20px}}
    .bar-item{{margin-bottom:16px}}
    .bar-label{{display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;color:var(--text2)}}
    .bar-track{{background:var(--gray2);border-radius:100px;height:12px;overflow:hidden}}
    .bar-fill{{height:100%;border-radius:100px}}
  </style>
</head>
<body>
{page_nav('/financials.html')}

<!-- HERO -->
<section class="fin-hero">
  <div class="section-tag" style="color:#888;display:inline-block;margin-bottom:12px">Финансовая модель</div>
  <h1>Детальный <span>Cash Flow</span><br>и финансовые прогнозы</h1>
  <p style="margin-top:16px">12 месяцев · Три сценария · Реальные формулы · ARR и юнит-экономика</p>
</section>

<!-- STATS BAR -->
<div class="stats-bar">
  <div class="stats-bar-inner" style="grid-template-columns:repeat(5,1fr)">
    <div class="stat-item"><div class="num"><span>$</span>53K</div><div class="lbl">Чистая прибыль в мес 12</div></div>
    <div class="stat-item"><div class="num">55<span>%</span></div><div class="lbl">Маржа при 150 ресторанах</div></div>
    <div class="stat-item"><div class="num"><span>~</span>3</div><div class="lbl">Месяц выхода на прибыль</div></div>
    <div class="stat-item"><div class="num"><span>$</span>1.14M</div><div class="lbl">ARR при 150 ресторанах</div></div>
    <div class="stat-item"><div class="num">64<span>×</span></div><div class="lbl">LTV : CAC</div></div>
  </div>
</div>

<!-- 12-MONTH CASH FLOW TABLE -->
<section class="cf-table-section">
  <div class="cf-inner">
    <div class="section-tag">Cash Flow</div>
    <h2 class="section-title">12 месяцев. Помесячно.</h2>
    <p class="section-sub">Рост от 10 до 150 ресторанов. Рекламный доход начинается со 2-го месяца. Все расчёты в USD.</p>

    <div style="overflow-x:auto;margin-top:40px">
    <table class="cf-table">
      <thead>
        <tr>
          <th style="min-width:180px">Показатель</th>
          <th>Мес 1</th><th>Мес 2</th><th>Мес 3</th><th>Мес 4</th>
          <th>Мес 5</th><th>Мес 6</th><th>Мес 7</th><th>Мес 8</th>
          <th>Мес 9</th><th>Мес 10</th><th>Мес 11</th><th>Мес 12</th>
        </tr>
      </thead>
      <tbody>
        <tr class="row-sep"><td colspan="13">📈 РОСТ</td></tr>
        <tr>
          <td>Ресторанов</td>
          <td>10</td><td>20</td><td>35</td><td>55</td>
          <td>75</td><td>90</td><td>105</td><td>115</td>
          <td>125</td><td>135</td><td>142</td><td>150</td>
        </tr>
        <tr>
          <td>Устройств</td>
          <td>120</td><td>240</td><td>420</td><td>660</td>
          <td>900</td><td>1 080</td><td>1 260</td><td>1 380</td>
          <td>1 500</td><td>1 620</td><td>1 704</td><td>1 800</td>
        </tr>
        <tr class="row-sep"><td colspan="13">💰 ВЫРУЧКА</td></tr>
        <tr>
          <td>Подписки (устр. × ср. $36.20)</td>
          <td>$4 344</td><td>$8 688</td><td>$15 204</td><td>$23 892</td>
          <td>$32 580</td><td>$39 096</td><td>$45 612</td><td>$49 956</td>
          <td>$54 300</td><td>$58 644</td><td>$61 685</td><td>$65 160</td>
        </tr>
        <tr>
          <td>Реклама (локаций × ср. $150–200)</td>
          <td>$0</td><td>$1 000</td><td>$2 000</td><td>$3 500</td>
          <td>$5 500</td><td>$9 000</td><td>$13 500</td><td>$17 250</td>
          <td>$20 000</td><td>$23 000</td><td>$26 000</td><td>$30 000</td>
        </tr>
        <tr class="row-total">
          <td>Итого выручка</td>
          <td>$4 344</td><td>$9 688</td><td>$17 204</td><td>$27 392</td>
          <td>$38 080</td><td>$48 096</td><td>$59 112</td><td>$67 206</td>
          <td>$74 300</td><td>$81 644</td><td>$87 685</td><td>$95 160</td>
        </tr>
        <tr class="row-sep"><td colspan="13">📉 РАСХОДЫ</td></tr>
        <tr>
          <td>OPEX устройств ($19.58/устр.)</td>
          <td>$2 350</td><td>$4 700</td><td>$8 224</td><td>$12 923</td>
          <td>$17 622</td><td>$21 146</td><td>$24 671</td><td>$27 020</td>
          <td>$29 370</td><td>$31 720</td><td>$33 364</td><td>$35 244</td>
        </tr>
        <tr>
          <td>Фикс. расходы (зарплаты + офис)</td>
          <td>$4 388</td><td>$4 388</td><td>$4 388</td><td>$4 388</td>
          <td>$4 388</td><td>$4 388</td><td>$4 388</td><td>$4 388</td>
          <td>$4 388</td><td>$4 388</td><td>$4 388</td><td>$4 388</td>
        </tr>
        <tr>
          <td>Масштабирование команды</td>
          <td>—</td><td>—</td><td>—</td><td>—</td>
          <td>—</td><td>—</td><td>$600</td><td>$1 200</td>
          <td>$1 200</td><td>$2 000</td><td>$2 000</td><td>$2 400</td>
        </tr>
        <tr class="row-total">
          <td>Итого расходы</td>
          <td>$6 738</td><td>$9 088</td><td>$12 612</td><td>$17 311</td>
          <td>$22 010</td><td>$25 534</td><td>$29 659</td><td>$32 608</td>
          <td>$34 958</td><td>$38 108</td><td>$39 752</td><td>$42 032</td>
        </tr>
        <tr class="row-sep"><td colspan="13">📊 ПРИБЫЛЬ</td></tr>
        <tr class="row-net">
          <td>Чистая прибыль / мес</td>
          <td class="neg">-$2 394</td><td class="pos">$600</td><td class="pos">$4 592</td><td class="pos">$10 081</td>
          <td class="pos">$16 070</td><td class="pos">$22 562</td><td class="pos">$29 453</td><td class="pos">$34 598</td>
          <td class="pos">$39 342</td><td class="pos">$43 536</td><td class="pos">$47 933</td><td class="pos">$53 128</td>
        </tr>
        <tr class="row-cumul">
          <td>Накопленная прибыль</td>
          <td>-$2 394</td><td>-$1 794</td><td>$2 798</td><td>$12 879</td>
          <td>$28 949</td><td>$51 511</td><td>$80 964</td><td>$115 562</td>
          <td>$154 904</td><td>$198 440</td><td>$246 373</td><td>$299 501</td>
        </tr>
        <tr>
          <td>Маржа</td>
          <td class="red">—</td><td class="green">6.2%</td><td class="green">26.7%</td><td class="green">36.8%</td>
          <td class="green">42.2%</td><td class="green">46.9%</td><td class="green">49.8%</td><td class="green">51.5%</td>
          <td class="green">53.0%</td><td class="green">53.3%</td><td class="green">54.7%</td><td class="green">55.8%</td>
        </tr>
      </tbody>
    </table>
    </div>

    <div style="margin-top:24px;padding:20px 24px;background:var(--gray);border-radius:12px;font-size:14px;color:var(--text2)">
      <strong style="color:var(--text)">Формулы расчёта:</strong>
      Подписки = кол-во устройств × средний тариф $36.20 (микс 40% Std Ads $29 + 40% Std No Ads $34 + 20% Premium $55).
      Реклама = активных ресторанов (прошлого мес.) × ср. доход $150–200/мес. (авт. продажи).
      OPEX = устройств × $19.58/устр./мес. (амортизация оборудования + связь + SSPF).
      Фикс. расходы = зарплаты $1 988 + рекл. операции $1 900 + офис $500.
    </div>
  </div>
</section>

<!-- REVENUE STRUCTURE -->
<section style="background:var(--gray);padding:80px 60px">
  <div class="section-inner">
    <div class="section-tag">Структура выручки</div>
    <h2 class="section-title">Два источника дохода.<br>Оба растут.</h2>
    <p class="section-sub">Подписки дают предсказуемый базовый доход. Реклама — масштабируемый апсайд.</p>

    <div class="rev-bars">
      <div class="rev-bar-block">
        <h4>Структура выручки — Месяц 12 (150 ресторанов)</h4>
        <div class="bar-item">
          <div class="bar-label"><span>Подписки ресторанов</span><span style="font-weight:700;color:var(--text)">$65 160 / 68.5%</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:68.5%;background:var(--black)"></div></div>
        </div>
        <div class="bar-item">
          <div class="bar-label"><span>Рекламный доход</span><span style="font-weight:700;color:var(--orange)">$30 000 / 31.5%</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:31.5%;background:var(--orange)"></div></div>
        </div>
        <div class="bar-item" style="margin-top:24px">
          <div class="bar-label"><span><strong>Итого выручка</strong></span><span style="font-weight:800;font-size:20px;color:var(--text)">$95 160 / мес</span></div>
        </div>
      </div>
      <div class="rev-bar-block">
        <h4>Тарифный микс ресторанов</h4>
        <div class="bar-item">
          <div class="bar-label"><span>Standard Ads — $29/мес</span><span style="font-weight:700;color:var(--text)">40%</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:40%;background:#555"></div></div>
        </div>
        <div class="bar-item">
          <div class="bar-label"><span>Standard No Ads — $34/мес</span><span style="font-weight:700;color:var(--text)">40%</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:40%;background:#888"></div></div>
        </div>
        <div class="bar-item">
          <div class="bar-label"><span>Premium — $55/мес</span><span style="font-weight:700;color:var(--orange)">20%</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:20%;background:var(--orange)"></div></div>
        </div>
        <div class="bar-item" style="margin-top:24px">
          <div class="bar-label"><span><strong>Средний тариф (взвешенный)</strong></span><span style="font-weight:800;font-size:20px;color:var(--text)">$36.20 / устр.</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- UNIT ECONOMICS -->
<section style="background:#fff;padding:80px 60px">
  <div class="section-inner">
    <div class="section-tag">Юнит-экономика</div>
    <h2 class="section-title">Один ресторан.<br>Полный расчёт.</h2>
    <p class="section-sub">12 устройств на ресторан. Окупаемость аппаратуры — 5 месяцев. LTV в 64 раза превышает CAC.</p>

    <div class="unit-grid">
      <div class="unit-card">
        <h4>📦 Аппаратура (CAPEX)</h4>
        <div class="unit-row"><span class="lbl">Цена FYD-06 (с завода)</span><span class="val">$150 / устр.</span></div>
        <div class="unit-row"><span class="lbl">Логистика + таможня АЗ</span><span class="val">$74.61 / устр.</span></div>
        <div class="unit-row"><span class="lbl">Итого landed cost</span><span class="val accent">$224.61 / устр.</span></div>
        <div class="unit-row"><span class="lbl">Устройств / ресторан</span><span class="val">12</span></div>
        <div class="unit-row"><span class="lbl">CAPEX / ресторан</span><span class="val accent">$2 695</span></div>
        <div class="unit-row"><span class="lbl">Умные часы</span><span class="val">$84.35 / шт.</span></div>
        <div class="unit-row"><span class="lbl">Принтер</span><span class="val">$99 / ресторан</span></div>
      </div>
      <div class="unit-card">
        <h4>💵 Выручка / ресторан / мес</h4>
        <div class="unit-row"><span class="lbl">Подписки (12 устр. × $36.20)</span><span class="val">$434</span></div>
        <div class="unit-row"><span class="lbl">Рекламный доход (ср.)</span><span class="val">$150–200</span></div>
        <div class="unit-row"><span class="lbl">Итого / ресторан</span><span class="val accent">$584–634</span></div>
        <div class="unit-row"><span class="lbl">OPEX устройств</span><span class="val">$235 / мес</span></div>
        <div class="unit-row"><span class="lbl">Доля фикс. расходов</span><span class="val">$29 / мес</span></div>
        <div class="unit-row"><span class="lbl">Вклад в прибыль (1 рест.)</span><span class="val accent">$320–370</span></div>
      </div>
      <div class="unit-card">
        <h4>📈 LTV / CAC</h4>
        <div class="unit-row"><span class="lbl">CAC (стоимость привлечения)</span><span class="val">$50–60</span></div>
        <div class="unit-row"><span class="lbl">Средний контракт</span><span class="val">12–24 мес</span></div>
        <div class="unit-row"><span class="lbl">LTV (24 мес × $320)</span><span class="val">$7 680</span></div>
        <div class="unit-row"><span class="lbl">LTV : CAC</span><span class="val accent">64×</span></div>
        <div class="unit-row"><span class="lbl">Payback period CAPEX</span><span class="val">5 мес</span></div>
        <div class="unit-row"><span class="lbl">Churn (прогноз)</span><span class="val">&lt; 5%</span></div>
        <div class="unit-row"><span class="lbl">Gross margin</span><span class="val accent">~55%</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ARR SCENARIOS -->
<section style="background:var(--black);padding:80px 60px">
  <div class="section-inner">
    <div class="section-tag" style="color:#888">ARR — Годовой рекуррентный доход</div>
    <h2 class="section-title" style="color:#fff">Три сценария.<br>Все прибыльные.</h2>
    <table class="arr-table" style="margin-top:40px">
      <thead>
        <tr>
          <th style="text-align:left;border-radius:12px 0 0 0">Сценарий</th>
          <th>Ресторанов</th>
          <th>Устройств</th>
          <th>Ежемес. выручка</th>
          <th>Ежемес. прибыль</th>
          <th>ARR</th>
          <th>Маржа</th>
          <th style="border-radius:0 12px 0 0">Оценка компании (×5–10 ARR)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:700;text-align:left;color:#ccc">Консервативный</td>
          <td style="color:#ccc">50</td>
          <td style="color:#ccc">600</td>
          <td style="color:#ccc">$29 220</td>
          <td class="arr-highlight">$13 834</td>
          <td class="arr-highlight">$350 808</td>
          <td style="color:#ccc">47.3%</td>
          <td style="color:#aaa">$1.75M – $3.5M</td>
        </tr>
        <tr class="best">
          <td style="font-weight:800;text-align:left;color:var(--orange)">⭐ Базовый</td>
          <td>150</td>
          <td>1 800</td>
          <td style="color:#fff">$95 160</td>
          <td class="arr-highlight">$53 128</td>
          <td class="arr-highlight">$1 141 920</td>
          <td>55.8%</td>
          <td style="color:var(--orange);font-weight:800">$5.7M – $11.4M</td>
        </tr>
        <tr>
          <td style="font-weight:700;text-align:left;color:#ccc">Оптимистичный</td>
          <td style="color:#ccc">300</td>
          <td style="color:#ccc">3 600</td>
          <td style="color:#ccc">$190 320</td>
          <td class="arr-highlight">$116 344</td>
          <td class="arr-highlight">$2 283 840</td>
          <td style="color:#ccc">61.1%</td>
          <td style="color:#aaa">$11.4M – $22.8M</td>
        </tr>
      </tbody>
    </table>
    <p style="color:#666;font-size:13px;margin-top:16px">Оценка компании = ARR × 5–10× (стандартный мультипликатор SaaS-стартапов). При базовом сценарии доля 20% = $1.14M–$2.28M vs инвестиции $80K → ROI 14×–29×</p>
  </div>
</section>

<!-- USE OF FUNDS -->
<section style="background:#fff;padding:80px 60px">
  <div class="section-inner">
    <div class="section-tag">Использование инвестиций</div>
    <h2 class="section-title">$80 000. Куда идут.</h2>
    <p class="section-sub">Каждый доллар инвестиций работает на захват рынка и быстрый выход на прибыль. Детальный план трат по статьям.</p>
    <div class="funds-grid">
      <div class="fund-card">
        <div class="pct">67%</div>
        <h4>Оборудование</h4>
        <p>FYD-06 устройства для первых 20–25 ресторанов. Умные часы для персонала. Тепловые принтеры.</p>
        <div class="amt">$53 600</div>
      </div>
      <div class="fund-card">
        <div class="pct">14%</div>
        <h4>Операционный резерв</h4>
        <p>3 месяца операционных расходов до выхода на прибыль. Зарплаты, офис, связь.</p>
        <div class="amt">$11 200</div>
      </div>
      <div class="fund-card">
        <div class="pct">11%</div>
        <h4>Маркетинг и продажи</h4>
        <p>Демо-материалы, презентации, встречи с ресторанами и потенциальными рекламодателями.</p>
        <div class="amt">$8 800</div>
      </div>
      <div class="fund-card">
        <div class="pct">8%</div>
        <h4>Юридика и регистрация</h4>
        <p>Регистрация ООО (MMC), договоры с ресторанами, IP-защита, бухгалтерия.</p>
        <div class="amt">$6 400</div>
      </div>
    </div>
    <div style="margin-top:32px;padding:24px;background:var(--gray);border-radius:16px;display:flex;align-items:center;gap:20px">
      <div style="font-size:48px">💡</div>
      <div>
        <strong>Окупаемость инвестиций</strong><br>
        <span style="color:var(--text2);font-size:14px">При варианте Revenue Share (8–10%) инвестор получает $80 000 обратно за ~18–24 месяца из выручки. При варианте Equity (15–20%) инвестор владеет долей в компании стоимостью <strong>$5.7M–$11.4M</strong> при базовом сценарии — ROI <strong style="color:var(--orange)">14×–29×</strong> на горизонте 2–3 лет.</span>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="cta-inner">
    <h2>Готовы изучить<br><span>детальную модель</span>?</h2>
    <p>Запросите полный Excel с формулами, допущениями и сценарным анализом — или перейдите к бизнес-плану.</p>
    <div class="cta-btns">
      <a href="mailto:info@gutu.com" class="btn-primary" style="font-size:16px;padding:16px 36px">Связаться с нами</a>
      <a href="/business-plan.html" class="btn-outline" style="font-size:16px;padding:16px 36px">→ Бизнес-план</a>
    </div>
  </div>
</section>
{FOOTER}
</body>
</html>'''

# ─────────────────────────────────────────────────────────────────────────────
# BUSINESS-PLAN.HTML
# ─────────────────────────────────────────────────────────────────────────────
BUSINESS_PLAN = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>GUTU — Бизнес-план 2026</title>
  <link rel="stylesheet" href="/src/style.css"/>
  <script type="module" src="/src/main.js"></script>
  <style>
    .bp-hero{{background:var(--black);padding:100px 60px 80px;text-align:center}}
    .bp-hero h1{{font-size:56px;font-weight:800;color:#fff;letter-spacing:-2px;margin-bottom:16px}}
    .bp-hero h1 span{{color:var(--orange)}}
    .bp-section{{padding:80px 60px}}
    .bp-inner{{max-width:1100px;margin:0 auto}}

    .ops-grid{{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:48px}}
    .ops-card{{border-radius:16px;border:1.5px solid var(--gray2);padding:32px}}
    .ops-card h4{{font-size:16px;font-weight:800;margin-bottom:16px;letter-spacing:-0.3px}}
    .ops-card ul{{list-style:none;display:flex;flex-direction:column;gap:10px}}
    .ops-card ul li{{font-size:14px;color:var(--text2);padding-left:20px;position:relative;line-height:1.6}}
    .ops-card ul li::before{{content:"→";position:absolute;left:0;color:var(--orange);font-weight:700}}

    .phase-track{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}}
    .phase{{border-radius:16px;padding:28px 24px;border-top:4px solid var(--orange)}}
    .phase .ph-num{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:var(--orange);margin-bottom:8px}}
    .phase h4{{font-size:17px;font-weight:800;margin-bottom:12px}}
    .phase p{{font-size:13px;color:var(--text2);line-height:1.6}}
    .phase .ph-result{{margin-top:16px;font-size:14px;font-weight:700;color:var(--orange)}}

    .traction-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}}
    .tract-card{{border-radius:16px;padding:28px 24px}}
    .tract-card .t-badge{{display:inline-block;padding:4px 12px;border-radius:100px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px}}
    .done{{background:#dcfce7;color:#16a34a}}
    .inprog{{background:#fef9c3;color:#ca8a04}}
    .tract-card h4{{font-size:17px;font-weight:800;margin-bottom:12px}}
    .tract-card p{{font-size:14px;color:var(--text2);line-height:1.6}}

    .exit-grid{{display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-top:48px}}
    .exit-card{{border-radius:20px;padding:36px;border:2px solid var(--gray2)}}
    .exit-card.featured{{border-color:var(--orange);background:rgba(232,66,26,0.03)}}
    .exit-card h3{{font-size:22px;font-weight:800;margin-bottom:20px}}
    .exit-row{{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--gray2);font-size:14px}}
    .exit-row:last-child{{border-bottom:none}}
    .exit-row .el{{color:var(--text2)}}
    .exit-row .er{{font-weight:700}}

    .legal-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px}}
    .legal-card{{background:var(--gray);border-radius:16px;padding:24px}}
    .legal-card h4{{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--orange);margin-bottom:12px}}
    .legal-card p{{font-size:14px;color:var(--text);line-height:1.6}}

    .region-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}}
    .region-card{{border-radius:16px;padding:24px;border:1.5px solid var(--gray2);text-align:center}}
    .region-card .flag{{font-size:40px;margin-bottom:12px}}
    .region-card h4{{font-size:16px;font-weight:800;margin-bottom:6px}}
    .region-card p{{font-size:12px;color:var(--text2)}}
    .region-card .ryr{{font-size:11px;font-weight:700;text-transform:uppercase;color:var(--orange);margin-top:12px}}

    .mkt-grid{{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:48px}}
    .mkt-block h4{{font-size:18px;font-weight:800;margin-bottom:20px}}
    .mkt-item{{display:flex;gap:16px;margin-bottom:20px}}
    .mkt-icon{{width:40px;height:40px;min-width:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px}}
    .mkt-text h5{{font-size:14px;font-weight:700;margin-bottom:4px}}
    .mkt-text p{{font-size:13px;color:var(--text2);line-height:1.5}}
  </style>
</head>
<body>
{page_nav('/business-plan.html')}

<!-- HERO -->
<section class="bp-hero">
  <div class="section-tag" style="color:#888;display:inline-block;margin-bottom:12px">Бизнес-план 2026</div>
  <h1>GUTU — <span>Умная платформа</span><br>для ресторанов Баку</h1>
  <p style="margin-top:16px;color:#888;font-size:18px">Операционный план · Стратегия продаж · Тракция · Стратегия выхода · Юридика</p>
</section>

<!-- STATS BAR -->
<div class="stats-bar">
  <div class="stats-bar-inner">
    <div class="stat-item"><div class="num"><span>$</span>80K</div><div class="lbl">Запрашиваемые инвестиции</div></div>
    <div class="stat-item"><div class="num">15–<span>20%</span></div><div class="lbl">Equity или Revenue Share 8–10%</div></div>
    <div class="stat-item"><div class="num"><span>~</span>3</div><div class="lbl">Месяц выхода в прибыль</div></div>
    <div class="stat-item"><div class="num">64<span>×</span></div><div class="lbl">LTV : CAC</div></div>
  </div>
</div>

<!-- ОПЕРАЦИОННЫЙ ПЛАН -->
<section class="bp-section" style="background:#fff">
  <div class="bp-inner">
    <div class="section-tag">Операционный план</div>
    <h2 class="section-title">Как работает<br>GUTU изнутри.</h2>
    <p class="section-sub">GUTU — двусторонняя платформа полного цикла. Рестораны получают технологию и сервис. Рекламодатели — доступ к живой аудитории. Мы управляем всем.</p>

    <div class="ops-grid">
      <div class="ops-card">
        <h4>🏪 Работа с ресторанами</h4>
        <ul>
          <li>Прямые продажи — основатели лично ведут переговоры на старте</li>
          <li>Установка устройств FYD-06 на каждый стол (12 устройств / ресторан)</li>
          <li>Инструктаж персонала: официанты, менеджер, хозяин — после каждого подключения</li>
          <li>Ресторан просто запрашивает изменения — GUTU делает всё сам</li>
          <li>Облачная CMS: обновление меню, акций, рекламы в реальном времени</li>
          <li>Техподдержка: замена устройства в течение 24 часов</li>
        </ul>
      </div>
      <div class="ops-card">
        <h4>📣 Работа с рекламодателями</h4>
        <ul>
          <li>Целевые рекламодатели: банки, Azerlotereya, Трезвый водитель, телеком, FMCG</li>
          <li>Продажа рекламных пакетов: по локациям, районам, времени суток</li>
          <li>Рекламодатель платит за охват — мы гарантируем 60–90 мин внимания</li>
          <li>Контент загружается через наш рекламный кабинет (облако)</li>
          <li>Таргетинг: тип ресторана, средний чек, район, время</li>
          <li>Отчёт рекламодателю: охват, клики, конверсия по QR</li>
        </ul>
      </div>
      <div class="ops-card">
        <h4>⚙️ Технологическая инфраструктура</h4>
        <ul>
          <li>Устройство: FYD-06 (Shenzhen FYD) — Android-планшет со встроенной зарядкой</li>
          <li>Облачная CMS для управления контентом на всех столах</li>
          <li>Приложение: система заказов, вызов официанта, оплата, чаевые</li>
          <li>Аналитика в реальном времени: популярные блюда, часы пик, активность</li>
          <li>Поставщик: Jenny Wu, szfyd.net — контакт налажен, MOQ обсужден</li>
        </ul>
      </div>
      <div class="ops-card">
        <h4>👥 Команда и структура</h4>
        <ul>
          <li>Aziz Haziyev — CEO 60%: стратегия, продажи, продукт</li>
          <li>Ruslan Abbasov — COO 40%: операции, логистика, партнёрства в Баку</li>
          <li>Месяц 3–4: нанять менеджера по продажам (рестораны)</li>
          <li>Месяц 5–6: нанять рекламного менеджера (рекламодатели)</li>
          <li>Месяц 7+: техник по обслуживанию устройств</li>
          <li>Удалённая разработка: поддержка и улучшение приложения</li>
        </ul>
      </div>
    </div>

    <div class="section-tag" style="margin-top:64px">Фазы масштабирования</div>
    <h3 style="font-size:28px;font-weight:800;letter-spacing:-1px;margin-bottom:8px">От 10 до 300+ ресторанов.</h3>
    <div class="phase-track">
      <div class="phase" style="background:#f5f5f5">
        <div class="ph-num">Фаза 1 · Мес 1–2</div>
        <h4>Запуск</h4>
        <p>10–20 ресторанов. Основатели продают лично. Отрабатываем процесс установки, инструктажа, поддержки.</p>
        <div class="ph-result">Цель: 10 ресторанов / выручка $4K+</div>
      </div>
      <div class="phase" style="background:#f5f5f5">
        <div class="ph-num">Фаза 2 · Мес 3–5</div>
        <h4>Рост</h4>
        <p>До 50 ресторанов. Первые рекламодатели. Нанимаем менеджера продаж. Система работает автономно.</p>
        <div class="ph-result">Цель: 50 ресторанов / выход в плюс</div>
      </div>
      <div class="phase" style="background:var(--black)">
        <div class="ph-num" style="color:var(--orange)">Фаза 3 · Мес 6–12</div>
        <h4 style="color:#fff">Масштаб</h4>
        <p style="color:#888">До 150 ресторанов. Системный захват рынка. Рекламный пайплайн работает. ARR $1M+.</p>
        <div class="ph-result">Цель: 150 ресторанов / $53K/мес</div>
      </div>
      <div class="phase" style="background:#f5f5f5">
        <div class="ph-num">Фаза 4 · Год 2+</div>
        <h4>Регионы</h4>
        <p>300 ресторанов в Баку. Экспансия: Тбилиси → Стамбул → Алматы. Франшизная модель.</p>
        <div class="ph-result">Цель: 300 рест. / региональный старт</div>
      </div>
    </div>
  </div>
</section>

<!-- МАРКЕТИНГ И ПРОДАЖИ -->
<section class="bp-section" style="background:var(--gray)">
  <div class="bp-inner">
    <div class="section-tag">Маркетинг и продажи</div>
    <h2 class="section-title">Как мы привлекаем<br>рестораны и рекламодателей.</h2>
    <p class="section-sub">Прямые продажи + демонстрации в действии. Никакой случайной рекламы — только точечная работа с ЛПРами.</p>

    <div class="mkt-grid">
      <div>
        <h4>🏪 Привлечение ресторанов</h4>
        <div class="mkt-item">
          <div class="mkt-icon">🤝</div>
          <div class="mkt-text">
            <h5>Прямые переговоры</h5>
            <p>Основатели лично встречаются с владельцами. Цикл сделки 1–2 недели от первого контакта до подписания.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">🏢</div>
          <div class="mkt-text">
            <h5>Ресторанные группы — приоритет</h5>
            <p>Одна сделка с сетью = 5–15 ресторанов сразу. Максимальный ROI на один контакт.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">📱</div>
          <div class="mkt-text">
            <h5>Live-демо</h5>
            <p>Показываем устройство вживую. Владелец видит продукт в работе — не слайды, а реальный экран.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">📊</div>
          <div class="mkt-text">
            <h5>ROI-аргумент</h5>
            <p>Апселл +15–25% среднего чека + реклама = устройство окупается за 2–3 месяца для ресторана.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">🔒</div>
          <div class="mkt-text">
            <h5>Эксклюзивность оборудования</h5>
            <p>200–300 единиц FYD в АЗ только у GUTU. Создаёт барьер для входа конкурентов.</p>
          </div>
        </div>
      </div>
      <div>
        <h4>📣 Привлечение рекламодателей</h4>
        <div class="mkt-item">
          <div class="mkt-icon">🏦</div>
          <div class="mkt-text">
            <h5>Банки и финтех</h5>
            <p>Карточные продукты, кредиты, бонусные программы. Аудитория за обедом = платёжеспособный сегмент.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">🍹</div>
          <div class="mkt-text">
            <h5>FMCG и напитки</h5>
            <p>Coca-Cola, местные бренды, воды, пиво. Контекстная реклама там, где продукт потребляется.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">🎰</div>
          <div class="mkt-text">
            <h5>Azerlotereya и развлечения</h5>
            <p>QR-лотерея прямо за столом — идеальный формат. Уже есть цифровые продукты.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">🚗</div>
          <div class="mkt-text">
            <h5>Трезвый водитель / Такси</h5>
            <p>Реклама в момент когда гость решает — ехать домой или вызвать водителя. Идеальный контекст.</p>
          </div>
        </div>
        <div class="mkt-item">
          <div class="mkt-icon">📡</div>
          <div class="mkt-text">
            <h5>Телеком (Azercell, Bakcell, Nar)</h5>
            <p>Тарифы, акции, eSIM. Аудитория активных пользователей смартфонов — прямое попадание.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ТРАКЦИЯ -->
<section class="bp-section" style="background:#fff">
  <div class="bp-inner">
    <div class="section-tag">Тракция</div>
    <h2 class="section-title">Что уже сделано.<br>Не слова — факты.</h2>
    <p class="section-sub">Стартап с продуктом. Не идея на салфетке — реальное устройство, протестированная система, живые переговоры.</p>

    <div class="traction-grid">
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge done">✅ Готово</span>
        <h4>Устройство FYD-06 протестировано</h4>
        <p>Рабочий прототип получен от Shenzhen FYD. Устройство работает. Будет продемонстрировано на встрече с инвестором вживую.</p>
      </div>
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge done">✅ Готово</span>
        <h4>Приложение разработано</h4>
        <p>Базовая версия приложения существует: заказы, вызов официанта, меню, оплата. Требует улучшений, но функционирует.</p>
      </div>
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge done">✅ Готово</span>
        <h4>Поставщик зафиксирован</h4>
        <p>Контакт с Jenny Wu (Shenzhen FYD) установлен. Цена $150/устр. согласована. Логистика и таможня просчитаны: $224.61 landed.</p>
      </div>
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge done">✅ Готово</span>
        <h4>Устные договорённости с ресторанами</h4>
        <p>Несколько заведений Баку выразили интерес и готовность к подключению после завершения регистрации компании.</p>
      </div>
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge inprog">⏳ В процессе</span>
        <h4>Регистрация компании</h4>
        <p>ООО (MMC) Азербайджан — в процессе регистрации. Параллельно идут переговоры с потенциальными клиентами.</p>
      </div>
      <div class="tract-card" style="background:var(--gray)">
        <span class="t-badge inprog">⏳ На старте</span>
        <h4>Команда сформирована</h4>
        <p>Aziz Haziyev (CEO, Канада — увидел концепцию там) + Ruslan Abbasov (COO, недвижимость Баку). Оба с профессиональным опытом продаж.</p>
      </div>
    </div>
  </div>
</section>

<!-- СТРАТЕГИЯ ВЫХОДА -->
<section class="bp-section" style="background:var(--black)">
  <div class="bp-inner">
    <div class="section-tag" style="color:#888">Стратегия выхода</div>
    <h2 class="section-title" style="color:#fff">Два пути для инвестора.<br><span style="color:var(--orange)">Оба выгодны.</span></h2>
    <p class="section-sub" style="color:#888">Выбирайте формат в зависимости от стратегии: быстрый возврат или долгосрочный рост.</p>

    <div class="exit-grid">
      <div class="exit-card" style="background:#111;border-color:#333">
        <h3 style="color:#fff">💰 Revenue Share</h3>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Доля от выручки</span><span class="er" style="color:#fff">8–10% / мес</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">До возврата суммы</span><span class="er" style="color:#fff">$120 000</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Срок возврата</span><span class="er" style="color:#fff">18–24 месяца</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Риск инвестора</span><span class="er" style="color:#fff">Низкий (прямые выплаты)</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">После возврата</span><span class="er" style="color:var(--orange)">Все права у основателей</span></div>
      </div>
      <div class="exit-card featured" style="background:#111">
        <h3 style="color:#fff">🚀 Equity <span style="color:var(--orange)">(Рекомендуем)</span></h3>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Доля в компании</span><span class="er" style="color:#fff">15–20%</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Оценка компании (базовый ARR×5)</span><span class="er" style="color:var(--orange)">$5.7M–$11.4M</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Доля инвестора при оценке $5.7M</span><span class="er" style="color:var(--orange)">$855K–$1.14M</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">ROI на $80K инвестиций</span><span class="er" style="color:var(--orange)">10×–14× за 2–3 года</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">При оптимистичном сценарии (ARR×10)</span><span class="er" style="color:var(--orange)">до $4.5M (56×)</span></div>
        <div class="exit-row" style="border-color:#333"><span class="el" style="color:#888">Дивиденды</span><span class="er" style="color:#fff">Ежеквартально с прибыли</span></div>
      </div>
    </div>

    <div class="section-tag" style="margin-top:64px;color:#888">Региональная экспансия</div>
    <h3 style="font-size:28px;font-weight:800;color:#fff;letter-spacing:-1px;margin-bottom:8px">Баку — первый шаг.</h3>
    <div class="region-grid">
      <div class="region-card" style="background:#111;border-color:#333">
        <div class="flag">🇦🇿</div>
        <h4 style="color:#fff">Баку</h4>
        <p style="color:#888">Запуск. 11 000+ ресторанов. Уже идёт.</p>
        <div class="ryr" style="color:var(--orange)">2026 — СЕЙЧАС</div>
      </div>
      <div class="region-card" style="background:#111;border-color:#333">
        <div class="flag">🇬🇪</div>
        <h4 style="color:#fff">Тбилиси</h4>
        <p style="color:#888">Схожий рынок, быстрорастущий туризм.</p>
        <div class="ryr">2027</div>
      </div>
      <div class="region-card" style="background:#111;border-color:#333">
        <div class="flag">🇹🇷</div>
        <h4 style="color:#fff">Стамбул</h4>
        <p style="color:#888">80 000+ ресторанов. Огромный масштаб.</p>
        <div class="ryr">2027–2028</div>
      </div>
      <div class="region-card" style="background:#111;border-color:#333">
        <div class="flag">🇰🇿</div>
        <h4 style="color:#fff">Алматы / Астана</h4>
        <p style="color:#888">Казахстан — высокий ARPU, нет конкурентов.</p>
        <div class="ryr">2028</div>
      </div>
    </div>

    <div style="margin-top:48px;background:#111;border-radius:16px;padding:36px;border:1.5px solid #333">
      <h4 style="color:#fff;font-size:20px;font-weight:800;margin-bottom:20px">📈 ARR при региональной экспансии</h4>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">
        <div style="text-align:center"><div style="font-size:13px;color:#888;margin-bottom:6px">Баку (Год 2)</div><div style="font-size:28px;font-weight:800;color:var(--orange)">$1.14M</div><div style="font-size:12px;color:#888">150 ресторанов</div></div>
        <div style="text-align:center"><div style="font-size:13px;color:#888;margin-bottom:6px">+ Тбилиси (Год 3)</div><div style="font-size:28px;font-weight:800;color:var(--orange)">$2.5M</div><div style="font-size:12px;color:#888">~330 ресторанов</div></div>
        <div style="text-align:center"><div style="font-size:13px;color:#888;margin-bottom:6px">+ Стамбул (Год 4)</div><div style="font-size:28px;font-weight:800;color:var(--orange)">$7M+</div><div style="font-size:12px;color:#888">900+ ресторанов</div></div>
        <div style="text-align:center"><div style="font-size:13px;color:#888;margin-bottom:6px">+ Казахстан (Год 5)</div><div style="font-size:28px;font-weight:800;color:var(--orange)">$15M+</div><div style="font-size:12px;color:#888">2 000+ ресторанов</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ЮРИДИЧЕСКАЯ СТРУКТУРА -->
<section class="bp-section" style="background:#fff">
  <div class="bp-inner">
    <div class="section-tag">Юридическая структура</div>
    <h2 class="section-title">Прозрачно. Официально.<br>По закону АЗ.</h2>
    <p class="section-sub">Регистрация ООО в Азербайджане обеспечивает минимальный налог, простую структуру и полную защиту инвестора.</p>

    <div class="legal-grid">
      <div class="legal-card">
        <h4>Форма организации</h4>
        <p><strong>ООО (MMC)</strong> — Mühüdiyyətli Məsuliyyətli Cəmiyyət<br>Азербайджан, г. Баку<br>Статус: <strong>в процессе регистрации</strong></p>
      </div>
      <div class="legal-card">
        <h4>Доли основателей</h4>
        <p><strong>Aziz Haziyev — 60%</strong> (CEO)<br><strong>Ruslan Abbasov — 40%</strong> (COO)<br>Доля инвестора оформляется при подписании договора</p>
      </div>
      <div class="legal-card">
        <h4>Налогообложение</h4>
        <p><strong>5% с оборота</strong> (при 3+ сотрудниках в штате)<br>SSPF работодателя: ~12.6%<br>НДС: освобождение при выручке до порогового значения</p>
      </div>
      <div class="legal-card">
        <h4>Защита инвестора</h4>
        <p>Договор инвестирования по нормам ГК АЗ<br>Нотариально заверенные изменения в уставе<br>Ежеквартальная финансовая отчётность</p>
      </div>
      <div class="legal-card">
        <h4>IP и эксклюзивность</h4>
        <p>Эксклюзивный дилерский договор с Shenzhen FYD на Азербайджан<br>Торговая марка GUTU — регистрация в АЗ<br>Программный код: собственность компании</p>
      </div>
      <div class="legal-card">
        <h4>Договоры с ресторанами</h4>
        <p>Типовой договор аренды/обслуживания<br>Срок: 12–24 месяца с автопролонгацией<br>Уведомление о расторжении: 30 дней</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="cta-inner">
    <h2>Готовы стать<br>частью <span>GUTU</span>?</h2>
    <p>Первая умная платформа для ресторанов Баку. Ноль конкурентов. Реальный продукт. Реальные цифры. Давайте поговорим.</p>
    <div class="cta-btns">
      <a href="mailto:info@gutu.com" class="btn-primary" style="font-size:16px;padding:16px 36px">Связаться с нами</a>
      <a href="/financials.html" class="btn-outline" style="font-size:16px;padding:16px 36px">📊 Финансовая модель</a>
    </div>
  </div>
</section>
{FOOTER}
</body>
</html>'''

# ─── UPDATE INDEX.HTML NAV ─────────────────────────────────────────────────
old_nav = index[nav_start:nav_end]
new_index = index[:nav_start] + new_index_nav + index[nav_end:]

with open('index.html', 'w') as f:
    f.write(new_index)
print("index.html nav updated")

with open('financials.html', 'w') as f:
    f.write(FINANCIALS)
print(f"financials.html written: {len(FINANCIALS):,} chars")

with open('business-plan.html', 'w') as f:
    f.write(BUSINESS_PLAN)
print(f"business-plan.html written: {len(BUSINESS_PLAN):,} chars")

print("All done!")
PYEOF
