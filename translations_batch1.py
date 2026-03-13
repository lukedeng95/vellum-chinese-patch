# -*- coding: utf-8 -*-
"""Batch 1: Ability effects #24-#197"""

TRANSLATIONS_BATCH1 = {
    # #24
    'Deal a <pos>Hand of Cards</pos> to <b>cut</b> foes.\nIncreases <neg>spread</neg> when cast in quick succession.':
        '打出<pos>手牌</pos><b>切割</b>敌人。\n连续施放时<neg>散布</neg>增加。',
    # #25
    '<b>Hold & Release:</b> Conjure a <pos>Lance</pos> to <b>devastate</b> foes at <pos>any range</pos>.':
        '<b>蓄力释放:</b>召唤<pos>长枪</pos>在<pos>任意距离</pos><b>毁灭</b>敌人。',
    # #57
    'After spending $mana-neutral$, <pos>recharge</pos> them and  take $-|10|DMG$ increasing with each consecutive use.':
        '消耗$mana-neutral$后<pos>回充</pos>，并受到$-|10|DMG$，每次递增。',
    # #77
    'You occasionally hear a booming shout from afar, inspiring you to $ability-primary$ $+|+|50|%$ faster for <b>5s</b>.':
        '偶尔听到远方的呐喊，使你$ability-primary$$+|+|50|%$更快持续<b>5s</b>。',
    # #80
    '$ability-secondary$ has a $+|25|%| Chance$ to cause $keyword-blot$ to immediately deal all <pos>future damage</pos> at once.\n(10s CD)':
        '$ability-secondary$有$+|25|%| Chance$使$keyword-blot$立即造成全部<pos>剩余伤害</pos>。\n(10s CD)',
    # #97
    '$torn$ that are damaged from a $keyword-inkcast$ have a $-|35|% Chance$ to launch a mortar.':
        '$torn$被$keyword-inkcast$命中时有$-|35|% Chance$发射迫击炮。',
    # #100
    'Your $ability-primary$ can deflect your $ability-secondary$ <b>shields</b>.':
        '$ability-primary$可偏转你的$ability-secondary$<b>shields</b>。',
    # #101
    'While moving, gain $keyword-hare$.\nWhile stationary, gain $keyword-tortoise$.':
        '移动时获得$keyword-hare$。\n静止时获得$keyword-tortoise$。',
    # #104
    'When consumed, this refunds the consuming ability\'s mana cost as neutral, temporary mana.':
        '消耗时返还技能法力消耗为临时法力。',
    # #106
    '$keyword-blot$ duration reduced by $-|2|s$, but gains a $Chance|+|25$ to $keyword-spread$ each tick.':
        '$keyword-blot$持续时间减少$-|2|s$，但每跳有$Chance|+|25$触发$keyword-spread$。',
    # #109
    '$ability-primary$ explosions send out spikes ($+|25|DMG$) to either side.':
        '$ability-primary$爆炸向两侧发射尖刺($+|25|DMG$)。',
    # #122
    'Your next $ability-primary$ gains $+|+|150|%|DMG$.':
        '下次$ability-primary$获得$+|+|150|%|DMG$。',
    # #124
    'Knockback effects against you are reduced by $+|-|30|%$.':
        '受到的击退效果降低$+|-|30|%$。',
    # #125
    'Gain $+|+|100|%|DMG$, but take\n $-|+|100|%|DMG$.':
        '$+|+|100|%|DMG$，但受\n $-|+|100|%|DMG$。',
    # #127
    '$ability-movement$ grants a $temp-mana-neutral$.':
        '$ability-movement$给予$temp-mana-neutral$。',
    # #129
    'Your $keyword-inkling$ damage reduces your $ability-movement$ cooldown slightly.':
        '$keyword-inkling$伤害略微降低$ability-movement$冷却。',
    # #130
    '$enemy-Ravings$ have a $-|50|%| Chance$ to spawn a <b>Rat</b> on death.':
        '$enemy-Ravings$死亡时有$-|50|%| Chance$生成<b>Rat</b>。',
    # #131
    '$enemy-Ravings$ plant <neg>mines</neg> while not within <b>15m</b> of any $scribe$.':
        '$enemy-Ravings$在$scribe$<b>15m</b>外时布置<neg>地雷</neg>。',
    # #132
    'The <b>Eye of the Storm</b> is revealed!':
        '<b>风暴之眼</b>已显现！',
    # #133
    '$enemy-ravings$ launch <neg>pools</neg> that send $keyword-varnish$ back to them if a $scribe$ enters.':
        '$enemy-ravings$发射<neg>水池</neg>，$scribe$进入时会将$keyword-varnish$回传。',
    # #134
    'During $keyword-tortoise$, gain $+|-|20|% Size$ and take $+|-|15|%|DMG$.':
        '$keyword-tortoise$期间获得$+|-|20|% Size$并受到$+|-|15|%|DMG$。',
    # #135
    "Don't soak back to back attacks.":
        '不要连续承受攻击。',
    # #136
    'Using $ability-movement$ will restore $+|25|HP$.':
        '使用$ability-movement$恢复$+|25|HP$。',
    # #139
    'Deal $+|+|150|%|DMG$ to enemies affected by $keyword-freeze$.':
        '对$keyword-freeze$的敌人造成$+|+|150|%|DMG$。',
    # #140
    '$ability-movement$ gives your next $ability-secondary$ $+|+|10|%| Size$ per enemy hit.':
        '$ability-movement$使下次$ability-secondary$每命中一敌$+|+|10|%| Size$。',
    # #141
    '$keyword-varnish$ grants $+|+|1|%|SPD$ per stack.':
        '$keyword-varnish$每层$+|+|1|%|SPD$。',
    # #142
    'Deal <pos>7,500</pos> damage in a single $keyword-blot$ tick.':
        '单次$keyword-blot$造成<pos>7,500</pos>伤害。',
    # #143
    'Deploy your $keyword-atlas$ in a group of $+|8$ or more enemies':
        '在$+|8$个以上敌人中部署$keyword-atlas$',
    # #144
    '<pos>Deposit</pos> <pos>7,926</pos> $keyword-survey$ into your $keyword-atlas$ at once':
        '一次<pos>存入</pos><pos>7,926</pos>$keyword-survey$至$keyword-atlas$',
    # #145
    'You can collect $keyword-drafts$, $keyword-finalizing$ them and empowering your next $keyword-inkcast$.':
        '收集$keyword-drafts$，$keyword-finalizing$后强化下次$keyword-inkcast$。',
    # #146
    'Gain $+|+|15|%|SPD$ while airborne.':
        '空中时获得$+|+|15|%|SPD$。',
    # #147
    'Knockback effects against you are reduced by $+|-|25|%$.':
        '受到的击退效果降低$+|-|25|%$。',
    # #148
    '$ability-primary$ generates $+|+|100|%$ $mana-neutral$ but deals $-|-|30|%|DMG$.':
        '$ability-primary$产生$+|+|100|%$$mana-neutral$但$-|-|30|%|DMG$。',
    # #149
    'Gain $+|+|25|%|DMG$ while $ability-utility$ is on cooldown.':
        '$ability-utility$冷却时获得$+|+|25|%|DMG$。',
    # #150
    'Collect the widespread Ink motes!\nCollected: $Value_1$/$Value_2$':
        '收集散落的墨水微粒！\n已收集：$Value_1$/$Value_2$',
    # #160
    'Remaining <pos>untouched</pos> for <b>45s</b> in a chapter will deal $+|1000000|DMG$ to all enemies.\n(Does not proc additional effects.)':
        '在章节中保持<pos>未受击</pos><b>45s</b>将对所有敌人造成$+|1000000|DMG$。\n(不触发额外效果。)',
    # #164
    'You must collect your $mana-neutral$ from the ground!':
        '你需要从地面拾取$mana-neutral$！',
    # #166
    '$ability-utility$ grants you $+|+|15|%|DMG$ for <pos>5s</pos>.':
        '$ability-utility$给予$+|+|15|%|DMG$持续<pos>5s</pos>。',
    # #167
    '$ability-primary$ also fires 2 arrows ($+|10|DMG$) at your target.':
        '$ability-primary$额外发射2支箭($+|10|DMG$)。',
    # #169
    'Gain $+|+|200|%$ $mana-neutral$ generation from $ability-primary$.':
        '$ability-primary$的$mana-neutral$产量$+|+|200|%$。',
    # #171
    'Have your $keyword-inkling$ $keyword-inkcast$ $+|8$ times in <b>5s</b>':
        '使$keyword-inkling$在<b>5s</b>内$keyword-inkcast$$+|8$次',
    # #172
    'Have your $keyword-inkling$ do a total of <pos>500,000</pos> damage.':
        '使$keyword-inkling$累计造成<pos>500,000</pos>伤害。',
    # #173
    '$keyword-finalize$ a total of <pos>6,500</pos> $keyword-drafts$.':
        '共$keyword-finalize$<pos>6,500</pos>个$keyword-drafts$。',
    # #174
    'Gain <pos>+3 Rewrites</pos>.':
        '获得<pos>+3改写</pos>。',
    # #175
    '$enemy-elite$s will now <neg>$keyword-tornparry$</neg> periodically.':
        '$enemy-elite$会定期<neg>$keyword-tornparry$</neg>。',
    # #177
    '$ability-secondary$ afflicts foes with <b>brambles</b>, <pos>slowing</pos> and <pos>infesting</pos> ($+|105|DMG$) over <pos>3s</pos>.':
        '$ability-secondary$对敌施加<b>荆棘</b>，<pos>减速</pos>并<pos>侵蚀</pos>($+|105|DMG$)持续<pos>3s</pos>。',
    # #178
    'All $ability-secondary$ effects gain $+|+|50|DMG$.':
        '$ability-secondary$所有效果$+|+|50|DMG$。',
    # #179
    '$ability-secondary$ summons rotating sets of vines that deal $+|20|DMG$.':
        '$ability-secondary$召唤旋转藤蔓造成$+|20|DMG$。',
    # #181
    '$ability-secondary$ now grants <pos>soothing spores</pos> ($+|5|HP$/s). Your 5th spore <b>blooms</b>, <pos>healing</pos> and <pos>lowering</pos> $ability-signature$ cooldown.':
        '$ability-secondary$释放<pos>舒缓孢子</pos>($+|5|HP$/s)。第5个孢子<b>绽放</b>，<pos>治疗</pos>并<pos>降低</pos>$ability-signature$冷却。',
    # #182
    '$ability-secondary$ also conjures a <b>tree trunk</b>, <pos>bludgeoning</pos> ($+|100|DMG$) and <pos>throwing</pos> foes.':
        '$ability-secondary$还召唤<b>树干</b>，<pos>重击</pos>($+|100|DMG$)并<pos>抛飞</pos>敌人。',
    # #183
    '$ability-secondary$ gains $+|+|50|%|SPD$ and deals $+|35|DMG$ on impact.':
        '$ability-secondary$$+|+|50|%|SPD$并命中时$+|35|DMG$。',
    # #187
    'A friendly $ability-secondary$ periodically <pos>attacks</pos> nearby foes.':
        '友方$ability-secondary$定期<pos>攻击</pos>附近敌人。',
    # #188
    '$ability-secondary$ now summons <pos>+2 additional</pos> birds. Each bird does $-|-|35|%|DMG$':
        '$ability-secondary$额外召唤<pos>+2</pos>只鸟。每只$-|-|35|%|DMG$',
    # #189
    '$ability-secondary$ now summons <pos>+2 additional</pos> birds. <i>Most fowl.</i>':
        '$ability-secondary$额外召唤<pos>+2</pos>只鸟。<i>禽兽！</i>',
    # #191
    'Every $ability-secondary$ bird summoned grants $+|+|20|%|DMG$ to subsequent $ability-secondary$s for <b>4s</b>. (Max 200%)':
        '每只$ability-secondary$鸟使后续$ability-secondary$$+|+|20|%|DMG$持续<b>4s</b>。(上限200%)',
    # #193
    '$keyword-blot$ deals $+|10|%|DMG$ per stack on the target. (Max 200%)':
        '$keyword-blot$每层$+|10|%|DMG$。(上限200%)',
    # #194
    'Foes affected by your $keyword-blot$ take $+|+|30|%|DMG$.':
        '受$keyword-blot$影响的敌人受到$+|+|30|%|DMG$。',
    # #195
    '$+|+|1|HP$ Maximum <b>per stack</b> of $keyword-waves$.':
        '$keyword-waves$<b>每层</b>$+|+|1|HP$上限。',
    # #197
    '$+|+|0.5|%|DMG$ per stack, gained from killing $torn$.':
        '击杀$torn$每层$+|+|0.5|%|DMG$。',
}
