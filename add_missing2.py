# -*- coding: utf-8 -*-
"""Add missing translations found from user screenshots."""

fp = r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

new_entries = [
    # H5 三骑士 — lust phase combat prompt (with rich text tags)
    'During <neg>lust</neg> two of the three are <neg>Invulnerable</neg>!=<neg>色欲</neg>阶段三个中有两个<neg>无敌</neg>！',
    'During lust two of the three are Invulnerable!=色欲阶段三个中有两个无敌！',
    # Dodge damage with various formats
    '- <pos>Dodge</pos> damage!=- <pos>躲避</pos>伤害！',
    '<pos>Dodge</pos> damage!=<pos>躲避</pos>伤害！',
    # Bottom bar note
    'Note: Mechanics may appear differently in other Worlds=注意：不同世界中机制可能有所不同',
    '<b>Note:</b> Mechanics may appear differently in other Worlds=<b>注意：</b>不同世界中机制可能有所不同',
    'Mechanics may appear differently in other Worlds=不同世界中机制可能有所不同',
    # Wordcraft body text - try alternate forms (game may split into separate lines)
    'Study hard - learn the basics of beating these Bosses of upcoming non-Vellum Raids!=努力学习——掌握击败即将到来的非Vellum团本Boss的基础！',
    'Check out the Codex for a deeper look at mechanics.=查看图鉴深入了解机制。',
    'Good luck!=祝好运！',
    'Check out the Codex for a deeper look at mechanics. Good luck!=查看图鉴深入了解机制。祝好运！',
    'Note: Some of these encounters may appear differently in other Worlds=注意：部分遭遇战在其他世界中可能表现不同',
]

# Find a good insertion point - after the existing Wordcraft section
marker = 'Note: Some of these encounters may appear differently in other Worlds='
pos = content.find(marker)
if pos != -1:
    end = content.find('\n', pos) + 1
    insert = '\r\n'.join(new_entries) + '\r\n'
    content = content[:end] + insert + content[end:]
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Added {len(new_entries)} new translations')
else:
    # Insert at end of combat tips section
    marker2 = '# 龙'
    pos2 = content.find(marker2)
    if pos2 != -1:
        insert = '\r\n'.join(new_entries) + '\r\n'
        content = content[:pos2] + insert + '\r\n' + content[pos2:]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added {len(new_entries)} new translations (before dragons section)')
    else:
        print('Could not find insertion point!')
