# -*- coding: utf-8 -*-
"""Scan resources.assets for English combat prompt texts that aren't in our translation files."""
import sys, struct, re

sys.path.insert(0, r'D:\Desktop-Projects\汉化\Vellum汉化补丁')

# Load all known translations
known = set()
# From _VellumChinese.txt
with open(r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            eng = line.split('=', 1)[0]
            known.add(eng)

# From python dicts
from patch_assets import TRANSLATIONS
known.update(TRANSLATIONS.keys())
try:
    from translations_extended import TRANSLATIONS_EXTENDED
    known.update(TRANSLATIONS_EXTENDED.keys())
except: pass
for i in range(1, 7):
    try:
        mod = __import__(f'translations_batch{i}')
        d = getattr(mod, f'TRANSLATIONS_BATCH{i}')
        known.update(d.keys())
    except: pass

print(f"Loaded {len(known)} known translations")

# Read the binary
assets_path = r'A:\SteamLibrary\steamapps\common\Vellum Study Hall\Vellum Study Hall_Data\resources.assets.bak'
with open(assets_path, 'rb') as f:
    data = f.read()

# Scan for Unity strings that look like combat prompts
# Unity string format: [4-byte LE length][UTF-8 content][padding to 4-byte align]
# We look for strings 10-200 bytes long that contain common combat keywords
combat_keywords = [
    b'Kill', b'KILL', b'Soak', b'SOAK', b'Dodge', b'DODGE',
    b'Don\'t', b'DON\'T', b'before', b'Killable', b'transforms',
    b'Move', b'MOVE', b'Stand', b'STAND', b'Run', b'RUN',
    b'Get to', b'GET TO', b'Watch', b'Avoid', b'AVOID',
    b'Interrupt', b'Break', b'BREAK', b'Stack', b'STACK',
    b'Spread', b'SPREAD', b'Hide', b'HIDE',
    b'Phase', b'PHASE', b'Intermission', b'Warning',
    b'incoming', b'Incoming', b'careful', b'Careful',
    b'dangerous', b'Dangerous',
]

found_missing = []
offset = 0
while offset < len(data) - 4:
    # Read potential string length
    str_len = struct.unpack('<I', data[offset:offset+4])[0]
    
    # Reasonable string length for combat prompts: 10-300 bytes
    if 10 <= str_len <= 300:
        str_start = offset + 4
        str_end = str_start + str_len
        if str_end <= len(data):
            try:
                text = data[str_start:str_end].decode('utf-8')
                # Check: is it mostly printable ASCII / valid text?
                if text.isprintable() or '\n' in text:
                    # Check if it contains a combat keyword  
                    raw = data[str_start:str_end]
                    has_keyword = any(kw in raw for kw in combat_keywords)
                    if has_keyword and text not in known:
                        # Skip if it's clearly code/path/metadata
                        if not any(x in text for x in ['/', '\\', '.dll', '.cs', '.asset', 'Unity', 'System.', 'Debug']):
                            found_missing.append(text)
            except (UnicodeDecodeError, ValueError):
                pass
    offset += 1
    if offset % 10000000 == 0:
        print(f"  Scanned {offset/1000000:.0f}MB...")

# Deduplicate and print
seen = set()
print(f"\n=== Missing combat-related texts ({len(found_missing)} raw hits) ===\n")
for text in found_missing:
    if text not in seen:
        seen.add(text)
        short = text[:100].replace('\n', '\\n')
        print(f"  {short}")
print(f"\nTotal unique missing: {len(seen)}")
