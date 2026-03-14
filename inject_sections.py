with open('index.html', 'r') as f:
    html = f.read()

# ─── 1. SOLUTION — insert before "<!-- MARKET STATS -->" ──────────────────
SOLUTION_SECTION = '''
<!-- SOLUTION -->
<section id="solution" style="background:var(--black);padding:80px 60px">
<div class="section-inner">
  <div class="section-tag" style="color:#888">Решение</div>
  <h2 class="section-title" style="color:#fff">GUTU — <span style="color:var(--orange)">первый умный стол</span><br>для ресторанов Баку.</h2>
  <p class="section-sub" style="color:#aaa">Один девайс на стол — и ресторан превращается в цифровую платформу: заказы, оплата, реклама, аналитика. Рестораны зарабатывают больше. Рекламодатели достигают живой аудитории. Мы управляем всем.</p>

  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px">
    <div style="background:#1a1a1a;border-radius:16px;padding:32px;border:1px solid #333">
      <div style="font-size:40px;margin-bottom:16px">🏪</div>
      <h4 style="color:#fff;font-size:18px;font-weight:800;margin-bottom:12px">Рестораны</h4>
      <p style="color:#888;font-size:14px;line-height:1.7">Подписка от $29/мес за устройство. Цифровое меню, апселлы +15–25% к чеку, аналитика, вызов официанта — без найма лишнего персонала.</p>
    </div>
    <div style="background:var(--orange);border-radius:16px;padding:32px">
      <div style="font-size:40px;margin-bottom:16px">📱</div>
      <h4 style="color:#fff;font-size:18px;font-weight:800;margin-bottom:12px">GUTU</h4>
      <p style="color:rgba(255,255,255,0.85);font-size:14px;line-height:1.7">Двусторонняя платформа полного цикла. Мы устанавливаем, обслуживаем, обновляем. Рестораны просто просят изменения — мы делаем всё.</p>
    </div>
    <div style="background:#1a1a1a;border-radius:16px;padding:32px;border:1px solid #333">
      <div style="font-size:40px;margin-bottom:16px">📣</div>
      <h4 style="color:#fff;font-size:18px;font-weight:800;margin-bottom:12px">Рекламодатели</h4>
      <p style="color:#888;font-size:14px;line-height:1.7">Контекстная реклама на столах: банки, телеком, FMCG. Аудитория сидит 60–90 минут без возможности «пролистать». Доход для GUTU — доход для роста.</p>
    </div>
  </div>

  <div style="margin-top:40px;background:#111;border-radius:16px;padding:28px 32px;border:1.5px solid #333;display:flex;align-items:center;gap:24px">
    <div style="font-size:56px">💡</div>
    <div>
      <div style="font-size:22px;font-weight:800;color:#fff;letter-spacing:-0.5px;margin-bottom:8px">Одна строка: GUTU</div>
      <p style="color:var(--orange);font-size:18px;font-weight:700;line-height:1.5">"Мы превращаем каждый ресторанный стол в умный рекламный и сервисный экран — первая такая платформа в Азербайджане."</p>
    </div>
  </div>
</div>
</section>

'''

# ─── 2. BUSINESS MODEL — insert before gallery section ────────────────────
BIZ_MODEL_SECTION = '''
<!-- BUSINESS MODEL -->
<section id="business-model" style="background:#fff;padding:80px 60px">
<div class="section-inner">
  <div class="section-tag">Бизнес-модель</div>
  <h2 class="section-title">Два источника дохода.<br>Один продукт.</h2>
  <p class="section-sub">GUTU — двусторонняя платформа. Рестораны платят подписку. Рекламодатели платят за доступ к аудитории. Оба потока масштабируются вместе.</p>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:48px">
    <div style="border:2px solid var(--gray2);border-radius:20px;padding:36px">
      <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:var(--orange);margin-bottom:16px">Поток 1 — Рестораны</div>
      <h3 style="font-size:24px;font-weight:800;margin-bottom:20px">Подписная модель (SaaS)</h3>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Standard Ads — реклама на устройстве</span>
          <span style="font-weight:800">$29/мес</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Standard No Ads — без рекламы</span>
          <span style="font-weight:800">$34/мес</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Premium — всё включено</span>
          <span style="font-weight:800">$55/мес</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;font-size:14px">
          <span style="color:var(--text2)">Средний тариф (микс 40/40/20)</span>
          <span style="font-weight:800;color:var(--orange)">$36.20/устр.</span>
        </div>
      </div>
      <div style="margin-top:20px;padding:16px;background:var(--gray);border-radius:12px;font-size:13px;color:var(--text2)">
        12 устройств/ресторан × $36.20 = <strong style="color:var(--text)">$434/ресторан/мес</strong>
      </div>
    </div>

    <div style="border:2px solid var(--orange);border-radius:20px;padding:36px;background:rgba(232,66,26,0.03)">
      <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:var(--orange);margin-bottom:16px">Поток 2 — Рекламодатели</div>
      <h3 style="font-size:24px;font-weight:800;margin-bottom:20px">Рекламные пакеты</h3>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Банки и финтех</span>
          <span style="font-weight:800">По контракту</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Azerlotereya, телеком, FMCG</span>
          <span style="font-weight:800">По контракту</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gray2);font-size:14px">
          <span style="color:var(--text2)">Трезвый водитель, такси</span>
          <span style="font-weight:800">По контракту</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding:12px 0;font-size:14px">
          <span style="color:var(--text2)">Средний доход с ресторана</span>
          <span style="font-weight:800;color:var(--orange)">$150–200/мес</span>
        </div>
      </div>
      <div style="margin-top:20px;padding:16px;background:rgba(232,66,26,0.08);border-radius:12px;font-size:13px;color:var(--text2)">
        Таргетинг: тип ресторана, район, время суток, средний чек
      </div>
    </div>
  </div>

  <div style="margin-top:32px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
    <div style="background:var(--black);border-radius:16px;padding:24px;text-align:center">
      <div style="font-size:32px;font-weight:800;color:var(--orange);letter-spacing:-1px">$584</div>
      <div style="font-size:13px;color:#888;margin-top:6px">Выручка с 1 ресторана/мес</div>
    </div>
    <div style="background:var(--black);border-radius:16px;padding:24px;text-align:center">
      <div style="font-size:32px;font-weight:800;color:var(--orange);letter-spacing:-1px">55%</div>
      <div style="font-size:13px;color:#888;margin-top:6px">Маржа при 150 ресторанах</div>
    </div>
    <div style="background:var(--black);border-radius:16px;padding:24px;text-align:center">
      <div style="font-size:32px;font-weight:800;color:var(--orange);letter-spacing:-1px">$1.1M</div>
      <div style="font-size:13px;color:#888;margin-top:6px">ARR при 150 ресторанах</div>
    </div>
    <div style="background:var(--black);border-radius:16px;padding:24px;text-align:center">
      <div style="font-size:32px;font-weight:800;color:var(--orange);letter-spacing:-1px">64×</div>
      <div style="font-size:13px;color:#888;margin-top:6px">Соотношение LTV / CAC</div>
    </div>
  </div>
</div>
</section>

<!-- TRACTION -->
<section id="traction" style="background:var(--gray);padding:80px 60px">
<div class="section-inner">
  <div class="section-tag">Тракция</div>
  <h2 class="section-title">Что уже сделано.<br>Не слова — факты.</h2>
  <p class="section-sub">Стартап с реальным продуктом. Устройство работает. Поставщик согласован. Переговоры с ресторанами идут.</p>

  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px">
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#dcfce7;color:#16a34a;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">✅ Готово</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Устройство FYD-06 протестировано</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">Рабочий прототип от Shenzhen FYD получен и протестирован. Будет продемонстрирован на встрече вживую.</p>
    </div>
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#dcfce7;color:#16a34a;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">✅ Готово</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Приложение разработано</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">Базовая версия: заказы, вызов официанта, меню, оплата. Функционирует, в процессе улучшения.</p>
    </div>
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#dcfce7;color:#16a34a;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">✅ Готово</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Поставщик зафиксирован</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">Контракт с Jenny Wu (Shenzhen FYD). Цена $150/устр. Landed cost с таможней: $224.61.</p>
    </div>
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#dcfce7;color:#16a34a;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">✅ Готово</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Устные договорённости</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">Несколько ресторанов Баку выразили готовность к подключению после регистрации компании.</p>
    </div>
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#fef9c3;color:#ca8a04;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">⏳ В процессе</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Регистрация компании</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">ООО (MMC) Азербайджан — в процессе регистрации. Параллельно идут переговоры с клиентами.</p>
    </div>
    <div style="background:#fff;border-radius:16px;padding:28px">
      <div style="display:inline-block;background:#dcfce7;color:#16a34a;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:4px 12px;border-radius:100px;margin-bottom:16px">✅ Готово</div>
      <h4 style="font-size:16px;font-weight:800;margin-bottom:10px">Команда сформирована</h4>
      <p style="font-size:13px;color:var(--text2);line-height:1.6">Aziz Haziyev (CEO, концепция из Канады) + Ruslan Abbasov (COO, недвижимость Баку). Оба с опытом продаж.</p>
    </div>
  </div>
</div>
</section>

'''

# ─── 3. GO-TO-MARKET — insert before roadmap section ──────────────────────
GTM_SECTION = '''
<!-- GO-TO-MARKET -->
<section id="go-to-market" style="background:#fff;padding:80px 60px">
<div class="section-inner">
  <div class="section-tag">Стратегия выхода на рынок</div>
  <h2 class="section-title">Как GUTU захватывает<br>рынок Баку.</h2>
  <p class="section-sub">Прямые продажи, живые демо, ставка на ресторанные группы. Рекламодатели идут следом — когда рестораны подключены.</p>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:48px">
    <div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:20px">🏪 Привлечение ресторанов</h4>
      <div style="display:flex;flex-direction:column;gap:16px">
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🤝</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Прямые переговоры</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">Основатели лично ведут встречи. Цикл сделки 1–2 недели от контакта до подписания.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🏢</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Ресторанные группы — приоритет</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">1 сделка с сетью = 5–15 ресторанов. Максимальный ROI на одну встречу.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">📱</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Live-демо устройства</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">Показываем девайс вживую — владелец видит, как это работает прямо за столом.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🔒</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Эксклюзив на оборудование</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">200–300 устройств FYD в АЗ только у GUTU. Барьер для входа конкурентов.</p></div>
        </div>
      </div>
    </div>
    <div>
      <h4 style="font-size:18px;font-weight:800;margin-bottom:20px">📣 Привлечение рекламодателей</h4>
      <div style="display:flex;flex-direction:column;gap:16px">
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🏦</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Банки и финтех</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">Карты, кредиты, бонусные программы. Аудитория за обедом = платёжеспособный сегмент.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🎰</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Azerlotereya и развлечения</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">QR-лотерея прямо за столом — идеальный формат для этого контекста.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">🚗</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Трезвый водитель / Такси</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">Реклама в момент когда гость решает — идеальный контекст.</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:40px;min-width:40px;height:40px;background:var(--gray);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px">📡</div>
          <div><h5 style="font-size:14px;font-weight:700;margin-bottom:4px">Телеком (Azercell, Bakcell, Nar)</h5><p style="font-size:13px;color:var(--text2);line-height:1.5">Тарифы, акции, eSIM. Аудитория активных пользователей смартфонов.</p></div>
        </div>
      </div>
    </div>
  </div>

  <div style="margin-top:48px;background:var(--black);border-radius:20px;padding:40px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px">
    <div style="text-align:center">
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Фаза 1 · Мес 1–2</div>
      <div style="font-size:24px;font-weight:800;color:#fff">10–20</div>
      <div style="font-size:13px;color:#888">ресторанов</div>
      <div style="font-size:12px;color:var(--orange);margin-top:8px">Основатели продают лично</div>
    </div>
    <div style="text-align:center">
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Фаза 2 · Мес 3–5</div>
      <div style="font-size:24px;font-weight:800;color:#fff">до 50</div>
      <div style="font-size:13px;color:#888">ресторанов</div>
      <div style="font-size:12px;color:var(--orange);margin-top:8px">Нанимаем менеджера продаж</div>
    </div>
    <div style="text-align:center">
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Фаза 3 · Мес 6–12</div>
      <div style="font-size:24px;font-weight:800;color:var(--orange)">до 150</div>
      <div style="font-size:13px;color:#888">ресторанов</div>
      <div style="font-size:12px;color:var(--orange);margin-top:8px">Системный захват рынка</div>
    </div>
    <div style="text-align:center">
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Фаза 4 · Год 2+</div>
      <div style="font-size:24px;font-weight:800;color:#fff">300+</div>
      <div style="font-size:13px;color:#888">регионы</div>
      <div style="font-size:12px;color:var(--orange);margin-top:8px">Тбилиси → Стамбул → Казахстан</div>
    </div>
  </div>
</div>
</section>

'''

# ─── 4. VISION — insert before CTA section ────────────────────────────────
VISION_SECTION = '''
<!-- VISION -->
<section id="vision" style="background:var(--black);padding:100px 60px;text-align:center">
<div style="max-width:900px;margin:0 auto">
  <div class="section-tag" style="color:#888;display:inline-block;margin-bottom:16px">Видение</div>
  <h2 style="font-size:56px;font-weight:800;color:#fff;letter-spacing:-2px;line-height:1.1;margin-bottom:24px">
    Сегодня — Баку.<br>
    <span style="color:var(--orange)">Завтра — весь Кавказ.</span>
  </h2>
  <p style="font-size:20px;color:#888;line-height:1.7;margin-bottom:60px;max-width:700px;margin-left:auto;margin-right:auto">
    Умные столы меняют то, как рестораны работают и как бренды достигают людей. В Северной Америке и Европе это уже норма. В Азербайджане и СНГ — ниша пустая. GUTU будет первым.
  </p>

  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:60px">
    <div style="background:#111;border-radius:16px;padding:28px;border:1px solid #222">
      <div style="font-size:36px;margin-bottom:12px">🇦🇿</div>
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">2026 — Сейчас</div>
      <div style="font-size:24px;font-weight:800;color:var(--orange)">Баку</div>
      <div style="font-size:13px;color:#888;margin-top:6px">11 000 ресторанов, 0 конкурентов</div>
    </div>
    <div style="background:#111;border-radius:16px;padding:28px;border:1px solid #222">
      <div style="font-size:36px;margin-bottom:12px">🇬🇪</div>
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">2027</div>
      <div style="font-size:24px;font-weight:800;color:#fff">Тбилиси</div>
      <div style="font-size:13px;color:#888;margin-top:6px">Быстрорастущий туристический рынок</div>
    </div>
    <div style="background:#111;border-radius:16px;padding:28px;border:1px solid #222">
      <div style="font-size:36px;margin-bottom:12px">🇹🇷</div>
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">2027–2028</div>
      <div style="font-size:24px;font-weight:800;color:#fff">Стамбул</div>
      <div style="font-size:13px;color:#888;margin-top:6px">80 000+ ресторанов, огромный масштаб</div>
    </div>
    <div style="background:#111;border-radius:16px;padding:28px;border:1px solid #222">
      <div style="font-size:36px;margin-bottom:12px">🇰🇿</div>
      <div style="font-size:13px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">2028+</div>
      <div style="font-size:24px;font-weight:800;color:#fff">Казахстан</div>
      <div style="font-size:13px;color:#888;margin-top:6px">Алматы + Астана, высокий ARPU</div>
    </div>
  </div>

  <div style="background:linear-gradient(135deg,#1a1a1a 0%,#111 100%);border-radius:20px;padding:48px;border:1.5px solid #333">
    <div style="font-size:48px;font-weight:800;color:#fff;letter-spacing:-2px;margin-bottom:16px">ARR: <span style="color:var(--orange)">$1.1M → $15M+</span></div>
    <p style="color:#888;font-size:16px;line-height:1.7">Баку (2026) → Тбилиси (2027) → Стамбул (2028) → Казахстан (2028+)<br>На горизонте 3–5 лет: 2 000+ ресторанов, ARR $15M+, стоимость компании $75–150M</p>
    <div style="margin-top:24px;display:inline-block;background:var(--orange);color:#fff;padding:12px 28px;border-radius:100px;font-size:14px;font-weight:700">
      Окно возможностей открыто прямо сейчас
    </div>
  </div>
</div>
</section>

'''

# ─── APPLY INSERTIONS ─────────────────────────────────────────────────────
assert '<!-- MARKET STATS -->' in html, "Marker 1 not found"
assert '<section class="gallery-section"' in html, "Marker 2 not found"
assert '<section class="roadmap-section">' in html, "Marker 3 not found"
assert '<section class="cta-section">' in html, "Marker 4 not found"

# 1. Solution → before MARKET STATS
html = html.replace('<!-- MARKET STATS -->', SOLUTION_SECTION + '<!-- MARKET STATS -->', 1)

# 2. Business Model + Traction → before gallery
html = html.replace('<section class="gallery-section"', BIZ_MODEL_SECTION + '<section class="gallery-section"', 1)

# 3. Go-to-market → before roadmap
html = html.replace('<section class="roadmap-section">', GTM_SECTION + '<section class="roadmap-section">', 1)

# 4. Vision → before CTA
html = html.replace('<section class="cta-section">', VISION_SECTION + '<section class="cta-section">', 1)

# ─── UPDATE NAV LINKS ────────────────────────────────────────────────────
old_nav_links = '''    <a href="#features">Продукт</a>
    <a href="#market">Рынок</a>
    <a href="#market-analysis">Анализ рынка</a>
    <a href="#financials">Финансы</a>
    <a href="#team">Команда</a>
    <a href="#invest">Инвестиции</a>
    <a href="/financials.html" style="color:var(--orange);font-weight:700">📊 Финмодель</a>
    <a href="/business-plan.html" style="color:var(--orange);font-weight:700">📋 Бизнес-план</a>'''

new_nav_links = '''    <a href="#solution">Решение</a>
    <a href="#features">Продукт</a>
    <a href="#market">Рынок</a>
    <a href="#business-model">Бизнес-модель</a>
    <a href="#traction">Тракция</a>
    <a href="#financials">Финансы</a>
    <a href="#team">Команда</a>
    <a href="#invest">Инвестиции</a>
    <a href="/financials.html" style="color:var(--orange);font-weight:700">📊 Финмодель</a>
    <a href="/business-plan.html" style="color:var(--orange);font-weight:700">📋 Бизнес-план</a>'''

html = html.replace(old_nav_links, new_nav_links, 1)

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Sections injected:")
print("  ✅ Solution (after Problem)")
print("  ✅ Business Model + Traction (before Gallery)")
print("  ✅ Go-to-market (before Roadmap)")
print("  ✅ Vision (before CTA)")
print("  ✅ Nav updated")
print(f"  File size: {len(html):,} chars")
