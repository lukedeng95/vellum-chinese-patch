# -*- coding: utf-8 -*-
import sys, struct

sys.path.insert(0, r'D:\Desktop-Projects\汉化\Vellum汉化补丁')

batch_translations = {}
# Load all translation sources
try:
    from patch_assets import TRANSLATIONS
    batch_translations.update(TRANSLATIONS)
except Exception as e:
    print(e)
    pass

try:
    from translations_extended import TRANSLATIONS_EXTENDED
    batch_translations.update(TRANSLATIONS_EXTENDED)
except Exception as e:
    pass

for i in range(1, 7):
    try:
        mod = __import__(f'translations_batch{i}')
        d = getattr(mod, f'TRANSLATIONS_BATCH{i}')
        batch_translations.update(d)
    except Exception as e:
        pass

assets_path = r'A:\SteamLibrary\steamapps\common\Vellum Study Hall\Vellum Study Hall_Data\resources.assets.bak'
with open(assets_path, 'rb') as f:
    data = f.read()

multi_match_count = 0
for eng_text in batch_translations.keys():
    eng_bytes = eng_text.encode('utf-8')
    search_start = 0
    valid_positions = []
    
    while True:
        candidate = data.find(eng_bytes, search_start)
        if candidate == -1:
            break
        if candidate >= 4:
            length_prefix = struct.unpack('<I', data[candidate-4:candidate])[0]
            if length_prefix == len(eng_bytes):
                valid_positions.append(candidate)
        search_start = candidate + 1
        
    if len(valid_positions) > 1:
        multi_match_count += 1
        print(f"Multiple valid occurrences ({len(valid_positions)}): {eng_text[:40]}...")

print(f"Total phrases with multiple valid occurrences: {multi_match_count}")
