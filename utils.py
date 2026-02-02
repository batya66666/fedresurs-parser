import re

BAD_VALUES = {"null", "-", "н/д", "n/a", "none", "undefined"}

def clean(v):
    if v is None:
        return ""
    s = str(v).strip()
    if not s or s.lower() in BAD_VALUES:
        return ""
    return s

def pick(*vals):
    for v in vals:
        s = clean(v)
        if s:
            return s
    return ""

def format_date(x):
    s = clean(x)
    if not s:
        return ""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return f"{m.group(3)}.{m.group(2)}.{m.group(1)}"
    return s
