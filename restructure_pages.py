#!/usr/bin/env python3
"""
Move from product.html → business-model.html:
  - ATTENTION SECTION  (Рестораны теряют деньги)
  - PROBLEM → SOLUTION
  - TARIFFS
Order in business-model.html:
  Attention → Problem/Solution → Business Model → Tariffs → Financials → ... → Why GUTU Wins
"""

product_path = '/home/aziz/.openclaw/workspace/gutu-site/product.html'
bizmodel_path = '/home/aziz/.openclaw/workspace/gutu-site/business-model.html'

product  = open(product_path, 'r').read()
bizmodel = open(bizmodel_path, 'r').read()

# ── 1. Extract sections from product.html ─────────────────────────────────────

def extract(content, start_marker, end_marker):
    s = content.find(start_marker)
    e = content.find(end_marker)
    assert s != -1, f"start marker not found: {start_marker}"
    assert e != -1, f"end marker not found: {end_marker}"
    assert s < e,   f"markers out of order: {start_marker} / {end_marker}"
    return content[s:e]

attention = extract(product, '<!-- ATTENTION SECTION -->', '<!-- PROBLEM → SOLUTION -->')
problem   = extract(product, '<!-- PROBLEM → SOLUTION -->', '<!-- ADVERTISER FEATURES -->')
tariffs   = extract(product, '<!-- TARIFFS -->', '<!-- EXTRA SERVICES -->')

print(f"attention: {len(attention):,} chars")
print(f"problem:   {len(problem):,} chars")
print(f"tariffs:   {len(tariffs):,} chars")

# ── 2. Remove sections from product.html ─────────────────────────────────────

# Remove attention + problem block (they're contiguous)
attention_problem_block = extract(product, '<!-- ATTENTION SECTION -->', '<!-- ADVERTISER FEATURES -->')
product_new = product.replace(attention_problem_block, '', 1)

# Remove tariffs block
tariffs_block = extract(product, '<!-- TARIFFS -->', '<!-- EXTRA SERVICES -->')
product_new = product_new.replace(tariffs_block, '', 1)

assert attention_problem_block not in product_new, "attention/problem block not removed"
assert tariffs_block not in product_new, "tariffs block not removed"
print(f"\nproduct.html: {len(product):,} → {len(product_new):,} chars")

# ── 3. Insert into business-model.html ───────────────────────────────────────
# Target order: Attention → Problem/Solution → Business Model → Tariffs → Financials → ...

biz_start_marker = '<!-- BUSINESS MODEL'
insert_point = bizmodel.find(biz_start_marker)
assert insert_point != -1, "BUSINESS MODEL marker not found"

# Insert attention + problem BEFORE business model section
# Insert tariffs AFTER business model + BEFORE financials
fin_marker = '<!-- FINANCIALS'
fin_point  = bizmodel.find(fin_marker)
assert fin_point != -1, "FINANCIALS marker not found"

# Build new bizmodel
bizmodel_new = (
    bizmodel[:insert_point]          # nav + header
    + attention                       # Рестораны теряют деньги…
    + problem                         # Решение section
    + bizmodel[insert_point:fin_point]  # Business Model
    + tariffs                         # Тарифы
    + bizmodel[fin_point:]            # Financials → rest
)

print(f"business-model.html: {len(bizmodel):,} → {len(bizmodel_new):,} chars")

# ── 4. Write files ────────────────────────────────────────────────────────────
open(product_path,  'w').write(product_new)
open(bizmodel_path, 'w').write(bizmodel_new)
print("\nDone! Both files written.")
