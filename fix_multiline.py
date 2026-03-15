# -*- coding: utf-8 -*-
"""Fix broken multi-line entries in _VellumChinese.txt."""

filepath = r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
merge_count = 0

i = 0
while i < len(lines):
    line = lines[i].rstrip('\r\n')
    
    if not line or line.startswith('#') or line.startswith('//'):
        fixed_lines.append(line)
        i += 1
        continue
    
    if '=' in line:
        merged = line
        j = i + 1
        while j < len(lines):
            next_line = lines[j].rstrip('\r\n')
            if not next_line or next_line.startswith('#') or next_line.startswith('//') or '=' in next_line:
                break
            merged += '\\n' + next_line
            merge_count += 1
            j += 1
        fixed_lines.append(merged)
        i = j
    else:
        fixed_lines.append(line)
        i += 1

print(f"Merged {merge_count} broken lines")

with open(filepath, 'w', encoding='utf-8') as f:
    for line in fixed_lines:
        f.write(line + '\r\n')

print("File saved")

issues = 0
with open(filepath, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        line = line.rstrip('\r\n')
        if not line or line.startswith('#') or line.startswith('//'):
            continue
        if '=' not in line:
            issues += 1
            if issues <= 5:
                print(f"  Still broken L{i}: {line[:60]}")

print(f"Remaining issues: {issues}")
