#!/usr/bin/env python3
"""Insert 5 new marketing sections into index.html after stats bar."""

NEW_SECTIONS = """

<!-- ===== SECTION 1: PRODUCT FEATURES ===== -->
<section style="background:#fff;padding:80px 60px;text-align:center">
  <div style="max-width:900px;margin:0 auto">
    <!-- icon -->
    <div style="display:inline-flex;align-items:center;justify-content:center;width:72px;height:72px;background:#f2f2f2;border-radius:50%;margin-bottom:32px">
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4" y="4" width="24" height="24" rx="5" stroke="#111" stroke-width="2"/>
        <path d="M16 10v6M16 18v.5" stroke="#111" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </div>
    <!-- heading -->
    <h2 style="font-size:52px;font-weight:800;letter-spacing:-2px;line-height:1.1;margin-bottom:40px;color:#111">
      GUTU превращает каждый стол<br>в умный центр обслуживания
    </h2>
    <!-- feature pills -->
    <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center">
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Самообслуживание</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Цифровое меню</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Вызов официанта</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Запрос счёта</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Управление столом</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Сенсорный интерфейс</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Срочный сервис</span>
      <span style="padding:10px 20px;border:1.5px solid #222;border-radius:100px;font-size:15px;font-weight:500;color:#111">Умная навигация</span>
    </div>
  </div>
</section>

<!-- ===== SECTION 2: PRODUCT HERO WITH IMAGE ===== -->
<section style="background:#fff;padding:60px 60px 80px">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center">
    <!-- device image -->
    <div style="border-radius:20px;overflow:hidden;background:#f5f5f5">
      <img src="/device.jpg" alt="GUTU устройство" style="width:100%;height:auto;display:block;object-fit:contain">
    </div>
    <!-- description -->
    <div>
      <p style="font-size:28px;font-weight:600;line-height:1.45;color:#111">
        Умное настольное устройство, объединяющее заказы, оплату, взаимодействие с гостями и таргетированную рекламу в единой системе — превращает каждый стол в активный источник дохода и ярких впечатлений.
      </p>
    </div>
  </div>
</section>

<!-- ===== SECTION 3: FOR RESTAURANTS / FOR ADVERTISERS ===== -->
<section style="background:#fff;padding:40px 60px 80px">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:24px">
    <!-- card: restaurants -->
    <div style="background:#f7f7f7;border-radius:20px;padding:40px">
      <div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:#fff;border-radius:12px;margin-bottom:24px">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 3C8.69 3 6 5.69 6 9c0 2.97 2.16 5.44 5 5.92V19h-2v2h6v-2h-2v-4.08C15.84 14.44 18 11.97 18 9c0-3.31-2.69-6-6-6z" fill="#111"/>
          <circle cx="12" cy="9" r="2" fill="#fff"/>
        </svg>
      </div>
      <h3 style="font-size:24px;font-weight:700;color:#111;margin-bottom:16px">Для владельцев ресторанов</h3>
      <p style="font-size:16px;color:#555;line-height:1.6">
        Удобная навигация, мгновенные заказы, простые платежи — ваша команда сосредоточена только на качестве и раскрывает весь потенциал обслуживания.
      </p>
    </div>
    <!-- card: advertisers -->
    <div style="background:#f7f7f7;border-radius:20px;padding:40px">
      <div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:#fff;border-radius:12px;margin-bottom:24px">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3A4.5 4.5 0 0016.5 9a4.5 4.5 0 000-9" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M19.07 4.93a10 10 0 010 14.14" stroke="#111" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </div>
      <h3 style="font-size:24px;font-weight:700;color:#111;margin-bottom:16px">Для рекламодателей</h3>
      <p style="font-size:16px;color:#555;line-height:1.6">
        Ваш бренд находится прямо на столе — в момент принятия решения, в центре полного внимания гостя.
      </p>
    </div>
  </div>
</section>

<!-- ===== SECTION 4: DISCOVERY CTA ===== -->
<section style="background:#fff;padding:80px 60px;text-align:center">
  <div style="max-width:800px;margin:0 auto">
    <h2 style="font-size:52px;font-weight:800;letter-spacing:-2px;line-height:1.1;color:#111;margin-bottom:24px">
      Откройте для себя, как GUTU добавляет ценность вашему заведению.
    </h2>
    <p style="font-size:18px;color:#666;line-height:1.6">
      Умный опыт за столом — созданный для современных ресторанов и брендов, которые растут вместе с ними.
    </p>
  </div>
</section>

<!-- ===== SECTION 5: THREE COLUMN BENEFITS ===== -->
<section style="background:#fff;padding:40px 60px 100px">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:48px">
    <!-- col 1 -->
    <div>
      <div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:#f2f2f2;border-radius:12px;margin-bottom:24px">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17 5.8 21.3l2.4-7.4L2 9.4h7.6L12 2z" stroke="#111" stroke-width="1.5" stroke-linejoin="round"/>
        </svg>
      </div>
      <h3 style="font-size:26px;font-weight:700;color:#111;margin-bottom:16px;line-height:1.2">Выигрывают обе стороны</h3>
      <p style="font-size:16px;color:#555;line-height:1.65">
        Рестораны превращают опыт за столом в источник дохода. Бренды устанавливают контакт в момент принятия решения — в точке максимального внимания.
      </p>
    </div>
    <!-- col 2 -->
    <div>
      <div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:#f2f2f2;border-radius:12px;margin-bottom:24px">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10z" stroke="#111" stroke-width="1.5"/>
          <path d="M12 6v6l4 2" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h3 style="font-size:26px;font-weight:700;color:#111;margin-bottom:16px;line-height:1.2">Устойчивое и измеримое внимание</h3>
      <p style="font-size:16px;color:#555;line-height:1.65">
        До часа за одним столом — разговоры, выборы, принятие решений. Ваш бренд в самом центре этого внимания, с полной аналитикой охвата.
      </p>
    </div>
    <!-- col 3 -->
    <div>
      <div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:#f2f2f2;border-radius:12px;margin-bottom:24px">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <polyline points="16 6 12 2 8 6" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <line x1="12" y1="2" x2="12" y2="15" stroke="#111" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </div>
      <h3 style="font-size:26px;font-weight:700;color:#111;margin-bottom:16px;line-height:1.2">Естественное и плавное взаимодействие</h3>
      <p style="font-size:16px;color:#555;line-height:1.65">
        От изучения меню до оплаты — каждое взаимодействие проходит плавно. Гостям комфортнее, команде спокойнее, ресторану эффективнее.
      </p>
    </div>
  </div>
</section>

"""

content = open('/home/aziz/.openclaw/workspace/gutu-site/index.html', 'r').read()

ANCHOR = '</div>\n</div>\n\n\n\n<section style="background:#fff;padding:80px 60px">'

if ANCHOR not in content:
    # try alternative
    ANCHOR = '</div>\n</div>'
    count = content.count(ANCHOR)
    print(f'Fallback anchor count: {count}')
else:
    insert_after = content.find(ANCHOR)
    # Insert after the stats bar closing tags
    # The anchor is: closing </div></div> of stats bar followed by empty lines
    stats_end = content.find('</div>\n</div>\n\n\n\n<section')
    print(f'Stats end position: {stats_end}')
    
    # Split at the investment pitch section start
    split_point = stats_end + len('</div>\n</div>')
    new_content = content[:split_point] + NEW_SECTIONS + content[split_point:]
    
    with open('/home/aziz/.openclaw/workspace/gutu-site/index.html', 'w') as f:
        f.write(new_content)
    print('Done! Sections inserted.')
