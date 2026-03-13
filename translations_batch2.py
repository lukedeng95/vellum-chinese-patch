# -*- coding: utf-8 -*-
"""Batch 2: Ability/movement descriptions #201-#400"""

TRANSLATIONS_BATCH2 = {
    # #201
    'Taking damage has a $Chance|+|5$ chance to trigger your $ability-utility$ <pos>without incurring</pos> its cooldown.':
        '受伤时有$Chance|+|5$触发$ability-utility$且<pos>不产生</pos>冷却。',
    # #202
    'Gain $+|+|200|%|SPD$ while casting $ability-secondary$.':
        '施放$ability-secondary$时$+|+|200|%|SPD$。',
    # #205
    '$ability-movement$ now launches a flask of ink ($+|30|DMG$) at a nearby foe.':
        '$ability-movement$向附近敌人投掷墨瓶($+|30|DMG$)。',
    # #214
    'Gain $+|+|5|%|DMG$ every second that resets after dealing damage. (Max $+|+|100|%|DMG$)':
        '每秒$+|+|5|%|DMG$，造成伤害后重置。(上限$+|+|100|%|DMG$)',
    # #215
    'Lose <neg>all $barrier$</neg>, gain $+|2$ <pos>Signature</pos> $temp-mana-neutral$ every $+|3|s$.':
        '失去<neg>全部$barrier$</neg>，每$+|3|s$获得$+|2$<pos>终极</pos>$temp-mana-neutral$。',
    # #217
    'Using $ability-movement$ causes your $keyword-inkling$ to $keyword-inkcast$.':
        '使用$ability-movement$使$keyword-inkling$触发$keyword-inkcast$。',
    # #218
    'Gain $+|+|30|%|SPD$ while airborne.':
        '空中时$+|+|30|%|SPD$。',
    # #219
    'Gain $+|+|60|HP$ but forfeit $-|-|20|BAR$.':
        '获得$+|+|60|HP$但失去$-|-|20|BAR$。',
    # #222
    'Roll a <pos>20-Sided Die</pos> to <b>clobber</b> foes, dealing variable effects based on the result (<neg>1</neg> - <pos>20</neg>).\nRolls can <pos>increase</pos> damage, <pos>explode</pos>, <pos>generate</pos> +$mana-neutral$, or <neg>*fizzle</neg>.':
        '投<pos>20面骰</pos><b>痛击</b>敌人，效果随结果变化(<neg>1</neg>-<pos>20</neg>)。\n可<pos>增伤</pos>、<pos>爆炸</pos>、<pos>产生</pos>$mana-neutral$或<neg>*失败</neg>。',
    # #225
    'Gain $+|+|25|%|DMG$ while your $Barrier$ is empty.':
        '$Barrier$为空时$+|+|25|%|DMG$。',
    # #226
    '$scribes$ affected by $keyword-stain$ have a $Chance|-|30|%$ to <neg>pull</neg> their targets to them when dealing damage.':
        '受$keyword-stain$的$scribes$造成伤害时有$Chance|-|30|%$<neg>拉拽</neg>目标。',
    # #227
    'Summon and defeat your <b>Embossed Duelist</b>!':
        '召唤并击败你的<b>浮雕决斗者</b>！',
    # #228
    'Within range of the <b>Atlas</b> influence.':
        '在<b>Atlas</b>影响范围内。',
    # #229
    '$scribes$ and $torn$ both shrink by <neg>-70%</neg>.':
        '$scribes$和$torn$均缩小<neg>-70%</neg>。',
    # #230
    '$+|+|30|%|DMG$ while inside the area.':
        '区域内$+|+|30|%|DMG$。',
    # #231
    '1 $mana-neutral$/s and $+|+|25|%|DMG$':
        '1$mana-neutral$/s且$+|+|25|%|DMG$',
    # #232
    '$keyword-atlas$ $ability-utility$ duration is increased by $+|2|s$.':
        '$keyword-atlas$$ability-utility$持续时间增加$+|2|s$。',
    # #233
    '$keyword-atlas$ Primary attack and $ability-utility$ damage generates $mana-neutral$.':
        '$keyword-atlas$主攻击和$ability-utility$伤害产生$mana-neutral$。',
    # #234
    '$keyword-drafts$ detonate for $+|20|%$ more damage.':
        '$keyword-drafts$引爆$+|20|%$伤害。',
    # #235
    '$keyword-finalize$ deals $+|5|%|$ of its damage in an area.':
        '$keyword-finalize$造成$+|5|%|$范围伤害。',
    # #236
    '$keyword-finalizing$ $keyword-drafts$ <pos>reduce</pos> $ability-utility$ cooldown by <pos>-0.2s</pos>.':
        '$keyword-finalizing$$keyword-drafts$<pos>降低</pos>$ability-utility$冷却<pos>-0.2s</pos>。',
    # #237
    '$keyword-finalizing$ deals $+|15|%$ more damage.':
        '$keyword-finalizing$$+|15|%$伤害。',
    # #238
    'Gain $+|+|10|%|DMG$ while at <pos>full health</pos>.':
        '<pos>满血</pos>时$+|+|10|%|DMG$。',
    # #239
    '$ability-utility$ duration increases by <pos>+1s</pos>.':
        '$ability-utility$持续时间<pos>+1s</pos>。',
    # #240
    '$+|+|10|%|DMG$ when at Full $Barrier$.':
        '满$Barrier$时$+|+|10|%|DMG$。',
    # #241
    'Deal $+|+|20|%|DMG$ with $ability-secondary$ when using $mana-teal$.':
        '使用$mana-teal$时$ability-secondary$$+|+|20|%|DMG$。',
    # #242
    'Creating a $keyword-plotthread$ generates an additional $+|2|BAR$.':
        '创建$keyword-plotthread$额外获得$+|2|BAR$。',
    # #243
    'When generating $keyword-plotthreads$, gain a <pos>25%</pos> chance to create <pos>double</pos> the amount.':
        '生成$keyword-plotthreads$时有<pos>25%</pos>概率生成<pos>双倍</pos>。',
    # #244
    'Reduce $ability-movement$ cooldown by $+|5|%$ per $keyword-plotarmor$ or $keyword-resolved$.':
        '每$keyword-plotarmor$或$keyword-resolved$降低$ability-movement$冷却$+|5|%$。',
    # #245
    '$keyword-resolved$ increases damage by $+|3|%$ per stack and lasts <b>2s</b> longer.':
        '$keyword-resolved$每层$+|3|%$伤害且延长<b>2s</b>。',
    # #246
    'Gain $+|+|20|%$ $mana-neutral$ generation while at full $Barrier$.':
        '满$Barrier$时$mana-neutral$产量$+|+|20|%$。',
    # #247
    'Have your $keyword-inkling$ do <pos>20,000</pos> damage in a single hit.':
        '使$keyword-inkling$单次命中造成<pos>20,000</pos>伤害。',
    # #248
    'Have your $keyword-inkling$ $keyword-evolve$<b>d</b> for a total of <pos>10,000</pos> Seconds.':
        '使$keyword-inkling$$keyword-evolve$<b>d</b>累计<pos>10,000</pos>秒。',
    # #249
    'Keep your $keyword-inkling$ $keyword-evolve$<b>d</b> for a continuous $+|40$ seconds.':
        '保持$keyword-inkling$$keyword-evolve$<b>d</b>连续$+|40$秒。',
    # #250
    'Deal $+|+|30|%|DMG$ to foes shorter than you.':
        '对比你矮的敌人$+|+|30|%|DMG$。',
    # #251
    'Generate $+|+|20|%$ more $mana-neutral$, but take $-|-|5|$ damage/s while at full $mana-neutral$.':
        '$mana-neutral$产量$+|+|20|%$，满$mana-neutral$时每秒受$-|-|5|$伤害。',
    # #252
    '$+|+|30|%|DMG$ while standing in your $keyword-pool$.':
        '站在$keyword-pool$中$+|+|30|%|DMG$。',
    # #253
    'You may collect $keyword-drafts$, $keyword-finalizing$ them and <pos>gaining</pos> $+|50|BAR$ and $+|25|HP$.':
        '收集$keyword-drafts$，$keyword-finalizing$后<pos>获得</pos>$+|50|BAR$和$+|25|HP$。',
    # #254
    '$keyword-finalized$ $keyword-drafts$ <pos>pull in</pos> nearby foes and deal $+|150|%|DMG$.':
        '$keyword-finalized$$keyword-drafts$<pos>拉拽</pos>附近敌人并$+|150|%|DMG$。',
    # #255
    '$keyword-drafts$ detonation radius is increased by $+|+|50|%$.':
        '$keyword-drafts$引爆范围$+|+|50|%$。',
    # #256
    '$ability-utility$ recharges <pos>3s Quicker</pos>, but <neg>reduces</neg> its range to <neg>25 meters</neg>.':
        '$ability-utility$充能<pos>快3s</pos>，但范围<neg>降至</neg><neg>25米</neg>。',
    # #257
    '$keyword-finalize$ also deals $+|25|%|DMG$ of its damage to nearby foes.':
        '$keyword-finalize$对附近敌人额外造成$+|25|%|DMG$。',
    # #258
    '$keyword-finalize$ $keyword-freeze$<b>s</b> foes for <pos>3s</pos>.':
        '$keyword-finalize$$keyword-freeze$敌人<pos>3s</pos>。',
    # #259
    '$keyword-finalize$ killing blows <pos>create</pos> and <pos>store</pos> their damage in a new $keyword-drafts$.':
        '$keyword-finalize$击杀时<pos>创建</pos>新$keyword-drafts$并<pos>存储</pos>伤害。',
    # #260
    '$ability-secondary$ damage has a $+|25|%| Chance$ to deal $+|10|%$ of $keyword-outline$ as damage. (<b>3s CD</b>)':
        '$ability-secondary$有$+|25|%| Chance$造成$+|10|%$$keyword-outline$伤害。(<b>3s CD</b>)',
    # #261
    '$keyword-finalize$ deals an additional $+|50|%|DMG$ over <pos>5s</pos>.':
        '$keyword-finalize$额外在<pos>5s</pos>内造成$+|50|%|DMG$。',
    # #262
    '$keyword-finalize$ deals $+|100|%|DMG$ to the most $keyword-outlined$ foe.':
        '$keyword-finalize$对$keyword-outlined$最多的敌人$+|100|%|DMG$。',
    # #263
    '<pos>Each</pos> $keyword-finalize$ has a $+|33|%$ chance to $keyword-finalize$ again.':
        '<pos>每次</pos>$keyword-finalize$有$+|33|%$再次触发。',
    # #264
    '$keyword-outlining$ foes <pos>reduces</pos> the cooldown $ability-utility$ by $+|0.2|s$.':
        '$keyword-outlining$敌人<pos>降低</pos>$ability-utility$冷却$+|0.2|s$。',
    # #265
    '$keyword-outline$ stores $+|+|50|%$ more of your $ability-primary$ and $ability-secondary$ damage.':
        '$keyword-outline$多存储$+|+|50|%$的$ability-primary$和$ability-secondary$伤害。',
    # #266
    '$keyword-outlining$ restores a small amount of $mana-neutral$.':
        '$keyword-outlining$恢复少量$mana-neutral$。',
    # #267
    'Increased <b>Draw</b> <neg>projectile spread</neg>.':
        '增加<b>Draw</b><neg>弹道散布</neg>。',
    # #268
    '$enemy-splices$ gain <neg>speed</neg> for <b>3s</b> when they receive damage. (Max $-|+|500|%|SPD$)':
        '$enemy-splices$受伤时<neg>加速</neg><b>3s</b>。(上限$-|+|500|%|SPD$)',
    # #269
    '$ability-secondary$ has a $Chance|+|33$ on hit to hatch <pos>another</pos> $ability-secondary$.':
        '$ability-secondary$命中时$Chance|+|33$孵化<pos>另一个</pos>$ability-secondary$。',
    # #270
    '$keyword-unrivaled$ grants $+|+|0.5|%|SPD$ per stack up to <b>25%</b>.':
        '$keyword-unrivaled$每层$+|+|0.5|%|SPD$，上限<b>25%</b>。',
    # #271
    '$mana-neutral$ Generation increased by $+|+|35|%$ while targeting an $enemy-elite$.':
        '瞄准$enemy-elite$时$mana-neutral$产量$+|+|35|%$。',
    # #272
    '$+|+|10|%|SPD$ per stack.':
        '每层$+|+|10|%|SPD$。',
    # #273
    '$enemy-tangent$ attacks apply <neg>1</neg> level of <neg>$keyword-gloom$</neg>.':
        '$enemy-tangent$攻击施加<neg>1</neg>层<neg>$keyword-gloom$</neg>。',
    # #274
    '<b>Minor</b> $torn$ you defeat <pos>explode</pos> for $+|25|DMG$.':
        '击败的<b>小型</b>$torn$<pos>爆炸</pos>$+|25|DMG$。',
    # #275
    'Each cast of $ability-primary$ gives the next $+|+|2|%|DMG$ (Max $+|+|1000|%$), resetting after casting $ability-secondary$.':
        '每次$ability-primary$使下次$+|+|2|%|DMG$(上限$+|+|1000|%$)，$ability-secondary$后重置。',
    # #276
    'Spent $mana-neutral$ has a $Chance|+|20$ to be <pos>refunded</pos> as $mana-temp-neutral$':
        '消耗的$mana-neutral$有$Chance|+|20$<pos>返还</pos>为$mana-temp-neutral$',
    # #277
    '$keyword-blot$ has a $+|15|%$ chance to deal its damage <pos>twice</pos>.':
        '$keyword-blot$有$+|15|%$概率造成<pos>双倍</pos>伤害。',
    # #279
    'Using $ability-movement$ has a $Chance|+|5$ to reset $ability-core$.':
        '$ability-movement$有$Chance|+|5$重置$ability-core$。',
    # #280
    '$+|+|1|%|DMG$ per stack.':
        '每层$+|+|1|%|DMG$。',
    # #281
    'The $torn$ <neg>suppress</neg> $scribe$ healing effects by $-|90|%$.':
        '$torn$<neg>压制</neg>$scribe$治疗效果$-|90|%$。',
    # #282
    'A <pos>slowing blizzard</pos> that $keyword-freezes$ all affected foes upon expiring.':
        '<pos>减速暴风雪</pos>，结束时$keyword-freezes$所有受影响的敌人。',
    # #283
    '$+|+|60|%|SPD$ and <pos>knocking back</pos> nearby foes.':
        '$+|+|60|%|SPD$并<pos>击退</pos>附近敌人。',
    # #284
    'Summon an <pos>extra</pos> $keyword-inkling$ but $ability-utility$ transformation duration is <neg>reduced</neg>.':
        '召唤<pos>额外</pos>$keyword-inkling$但$ability-utility$变身时间<neg>缩短</neg>。',
    # #285
    'When $ability-utility$ expires, your $keyword-inkling$ explodes for $+|50|%$ of the <b>total damage</b> it dealt while transformed.':
        '$ability-utility$结束时$keyword-inkling$爆炸，造成变身期间<b>总伤害</b>的$+|50|%$。',
    # #286
    'Casting $ability-secondary$ with $mana-green$ causes affected foes to take $+|50|%|DMG$ from $Inkling$ for <b>5s</b>.':
        '用$mana-green$施放$ability-secondary$使敌人受$Inkling$$+|50|%|DMG$持续<b>5s</b>。',
    # #287
    '$keyword-inkling$ $keyword-inkcast$ damage <pos>roots</pos> foes in place.':
        '$keyword-inkling$$keyword-inkcast$伤害<pos>定身</pos>敌人。',
    # #288
    '$keyword-inkling$ $keyword-inkcast$ flings an <pos>orb</pos> towards you, granting <pos>+1</pos> $mana-green$ if caught and <pos>+2</pos> while Transformed. (2s CD)':
        '$keyword-inkling$$keyword-inkcast$抛出<pos>球</pos>，接住得<pos>+1</pos>$mana-green$，变身时<pos>+2</pos>。(2s CD)',
    # #289
    '$keyword-inkling$ $keyword-inkcast$ causes an implosion ($+|50|DMG$) that <pos>pulls in</pos> nearby foes.':
        '$keyword-inkling$$keyword-inkcast$引发内爆($+|50|DMG$)<pos>拉拽</pos>附近敌人。',
    # #290
    '$ability-secondary$ and your $keyword-inkling$\'s $keyword-inkcast$ gain $+|+|35|%|DMG$ and <pos>Size</pos>.':
        '$ability-secondary$和$keyword-inkling$的$keyword-inkcast$$+|+|35|%|DMG$及<pos>体积</pos>。',
    # #291
    '$-|+|15|%|DMG$ taken <neg>per unspent</neg> $mana-neutral$.':
        '每未耗$mana-neutral$<neg>受</neg>$-|+|15|%|DMG$。',
    # #292
    '$enemy-raving$ area effects gain $-|+|200|% Duration$.':
        '$enemy-raving$范围效果$-|+|200|% Duration$。',
    # #293
    '$keyword-leech$ for a total of <pos>125,000</pos> health.':
        '累计$keyword-leech$<pos>125,000</pos>生命。',
    # #294
    'Do <pos>5,000,000</pos> damage with $keyword-twists$.':
        '$keyword-twists$造成<pos>5,000,000</pos>伤害。',
    # #295
    '$ability-primary$ deals $+|+|1|DMG$ for each $+|5|%|HP$ missing from the target hit.':
        '$ability-primary$目标每缺$+|5|%|HP$额外$+|+|1|DMG$。',
    # #296
    'Increase movement speed for 3 seconds.':
        '增加移动速度3秒。',
    # #298
    'You are standing in <neg>lava</neg>!':
        '你站在<neg>岩浆</neg>中！',
    # #299
    'Increases $keyword-twist$ damage by $+|+|5|%$ per stack.':
        '$keyword-twist$伤害每层$+|+|5|%$。',
    # #300
    '$ability-utility$ pulses, granting $+|+|10|%|DMG$ for 8s for each enemy hit.':
        '$ability-utility$脉冲，每命中一敌$+|+|10|%|DMG$持续8s。',
    # #301
    'Your $keyword-inkling$\'s $keyword-inkcast$ grants you $+|+|10|%|DMG$ for <b>5s</b> (<i>Max 200%</i>)':
        '$keyword-inkling$的$keyword-inkcast$给予$+|+|10|%|DMG$<b>5s</b>(<i>上限200%</i>)',
    # #302
    '$keyword-poison$ lasts for an additional $-|2|s$.':
        '$keyword-poison$延长$-|2|s$。',
    # #303
    'Gain $+|+|50|%|DMG$, but take\n $-|+|50|%|DMG$.':
        '$+|+|50|%|DMG$，但受\n $-|+|50|%|DMG$。',
    # #304
    'Call forth a <b>Meadow</b> of flowers to <pos>thrash</pos> nearby enemies.':
        '召唤<b>花丛</b><pos>鞭打</pos>附近敌人。',
    # #305
    'A combination attack that deals 50, then 100 damage in an area in front of you and leeches health for each enemy hit. (Requires 2 inputs)':
        '组合攻击，对前方区域造成50再100伤害，每命中一敌吸取生命。(需2次输入)',
    # #306
    'Call forth a <pos>Meadow</pos> of flowers to <b>thrash</b> nearby enemies.':
        '召唤<pos>花丛</pos><b>鞭打</b>附近敌人。',
    # #307
    'Lunges forward in a painted slash, dealing $+|80|DMG$ damage to enemies hit.':
        '向前突进斩击，对命中敌人造成$+|80|DMG$伤害。',
    # #308
    'Gain $+|+|100|%|DMG$ against foes with $Barrier$.':
        '对有$Barrier$的敌人$+|+|100|%|DMG$。',
    # #309
    'Mend <b>Rivals</b> & Reach <sprite name="binding"> Attunement <b>5</b>.':
        '修复<b>宿敌</b>并达到<sprite name="binding">调谐<b>5</b>。',
    # #310
    '$ability-movement$ gains up to $+|+|200|%|DMG$ based on charge time. (Max at 1s.)':
        '$ability-movement$蓄力至$+|+|200|%|DMG$。(1s满)',
    # #311
    '$ability-movement$ damage generates $mana-neutral$.':
        '$ability-movement$伤害产生$mana-neutral$。',
    # #312
    '$ability-movement$ also <pos>casts</pos> your $ability-primary$ in the opposite direction.':
        '$ability-movement$同时反向<pos>施放</pos>$ability-primary$。',
    # #313
    '$ability-movement$ reduces the cooldown of $ability-utility$ by <b>1.5s.</b>':
        '$ability-movement$降低$ability-utility$冷却<b>1.5s</b>。',
    # #314
    '$ability-movement$ now <pos>doubles</pos> your jump height for <b>2s</b>.':
        '$ability-movement$<pos>翻倍</pos>跳跃高度<b>2s</b>。',
    # #315
    '$ability-movement$ now drops exploding marks ($+|15|DMG$) behind you.':
        '$ability-movement$在身后留下爆炸印记($+|15|DMG$)。',
    # #316
    '$ability-movement$ <pos>doubles</pos> its movement strength.':
        '$ability-movement$移动力<pos>翻倍</pos>。',
    # #317
    'Every <b>5s</b> your next $ability-movement$ will not incur a cooldown.':
        '每<b>5s</b>下次$ability-movement$无冷却。',
    # #318
    'Every second in between uses of $ability-movement$ <pos>increases</pos> its movement power.':
        '两次$ability-movement$间每秒<pos>增强</pos>移动力。',
    # #319
    '$ability-movement$ gains $+|+|50|%$ maximum distance.':
        '$ability-movement$最大距离$+|+|50|%$。',
    # #320
    'For <b>2s</b> after casting $ability-movement$, you can cast it a second time.':
        '$ability-movement$后<b>2s</b>内可再次施放。',
    # #321
    '$ability-movement$ <pos>swaps places</pos> with foes at your step location.':
        '$ability-movement$与落点敌人<pos>交换位置</pos>。',
    # #322
    '$ability-movement$ applies $keyword-freeze$ for <pos>2s</pos> when passing through foes.':
        '$ability-movement$穿过敌人时施加$keyword-freeze$<pos>2s</pos>。',
    # #323
    'You may <pos>fly</pos> during $ability-movement$.':
        '$ability-movement$期间可<pos>飞行</pos>。',
    # #324
    '$ability-movement$ lasts an additional <pos>0.45s</pos>.':
        '$ability-movement$延长<pos>0.45s</pos>。',
    # #325
    '$ability-movement$ grants one mid-air jump while active.':
        '$ability-movement$期间获得一次空中跳跃。',
    # #326
    'When $ability-movement$ ends, <pos>drop a chandelier</pos> ($+|50|DMG$) on all foes passed through.':
        '$ability-movement$结束时<pos>掉落吊灯</pos>($+|50|DMG$)砸向经过的敌人。',
    # #327
    'Gain <pos>2 additional charges</pos> of $ability-movement$.':
        '$ability-movement$获得<pos>2额外充能</pos>。',
    # #328
    'Gain a bonus <pos>in-air  jump</pos> after using $ability-movement$.':
        '$ability-movement$后获得<pos>空中跳跃</pos>。',
    # #329
    'Gain $+|+|100|%|DMG$ at the apex of your $ability-movement$ backflip for <b>0.5s</b>.':
        '$ability-movement$后空翻顶点$+|+|100|%|DMG$持续<b>0.5s</b>。',
    # #330
    'Gain $+|+|50|%|SPD$ for <b>3s</b> after landing when casting $ability-movement$.':
        '$ability-movement$落地后$+|+|50|%|SPD$<b>3s</b>。',
    # #331
    '$ability-movement$ gains increased <pos>Height</pos> and <pos>Air Control</pos>.':
        '$ability-movement$增加<pos>高度</pos>和<pos>空中操控</pos>。',
    # #332
    '$ability-movement$ <pos>blasts</pos> the area when landing, dealing <pos>increased damage</pos> based on <b>air-time</b>.':
        '$ability-movement$落地时<pos>爆破</pos>区域，伤害随<b>滞空</b>时间<pos>增加</pos>。',
    # #333
    '$ability-movement$ no longer has a longer cooldown while in air.':
        '$ability-movement$在空中不再有更长冷却。',
    # #334
    'Deal $+|+|50|%|DMG$ to foes under <b>50%</b> health.':
        '对<b>50%</b>血以下的敌人$+|+|50|%|DMG$。',
    # #335
    'Gain $+|+|100|%|DMG$ while within <b>5m</b> of at least one foe.':
        '在敌人<b>5m</b>内时$+|+|100|%|DMG$。',
    # #336
    'Using your $ability-secondary$ grants $+|5|BAR$ per $mana-neutral$ spent.':
        '$ability-secondary$每消耗$mana-neutral$获得$+|5|BAR$。',
    # #337
    'Your $ability-secondary$ partially <pos>generates</pos> $mana-neutral$.':
        '$ability-secondary$部分<pos>产生</pos>$mana-neutral$。',
    # #338
    '$ability-primary$ does $+|+|50|%|DMG$ to enemies afflicted by $ability-secondary$.':
        '$ability-primary$对受$ability-secondary$影响的敌人$+|+|50|%|DMG$。',
    # #339
    '$ability-movement$ $keyword-freezes$ nearby enemies that <i>are not</i> your target for <b>2s</b>.':
        '$ability-movement$$keyword-freezes$<i>非</i>目标的附近敌人<b>2s</b>。',
    # #340
    'Will deal $+|1000000|DMG$ to all enemies after remaining <pos>untouched</pos> for <b>45s</b>.':
        '<pos>未受击</pos><b>45s</b>后对所有敌人造成$+|1000000|DMG$。',
    # #341
    '<pos>Increased speed</pos> for having heeded the warning!':
        '听从警告后<pos>速度提升</pos>！',
    # #342
    '$enemy-tangents$ have a chance to fire a <neg>spear</neg> with their normal attack that deals damage and explodes on impact.':
        '$enemy-tangents$普攻有概率发射<neg>长矛</neg>，命中后爆炸。',
    # #343
    '$enemy-tangents$ fire an <neg>additional projectile</neg>.':
        '$enemy-tangents$发射<neg>额外弹射物</neg>。',
    # #344
    '$ability-secondary$ now <pos>bounces</pos> off the environment, gaining $+|30|% Size$ each bounce.':
        '$ability-secondary$可<pos>弹射</pos>，每次弹射$+|30|% Size$。',
    # #345
    'Increase <pos>damage</pos> while <b>airborne</b>, scaling <pos>exponentially</pos> with air time.':
        '<b>空中</b>时<pos>伤害</pos>增加，随滞空<pos>指数</pos>增长。',
    # #346
    '$enemy-tangents$ apply $keyword-stain$ around themselves on death.':
        '$enemy-tangents$死亡时周围施加$keyword-stain$。',
    # #347
    '$ability-primary$ now <pos>pierces</pos> enemies and the environment, and gains $+|15|%|DMG$ for each pierced object.':
        '$ability-primary$<pos>穿透</pos>敌人和环境，每穿透$+|15|%|DMG$。',
    # #348
    'You and your $keyword-inkling$ attack $+|+|25|%$ faster while within <b>15m</b> of each other.':
        '你和$keyword-inkling$在<b>15m</b>内攻速$+|+|25|%$。',
    # #349
    'Falling below $-|35|HP$ causes your $keyword-inkling$ to rush to <pos>save you</pos> while knocking away nearby foes. (30s CD)':
        '低于$-|35|HP$时$keyword-inkling$冲来<pos>救你</pos>并击退附近敌人。(30s CD)',
    # #350
    '$keyword-inkling$ attacks $+|+|25|%$ faster while you can see them.':
        '视野内$keyword-inkling$攻速$+|+|25|%$。',
    # #351
    'Your $keyword-inkling$ gains your bonuses to <b>Generator</b> and <b>Spender</b> damage.':
        '$keyword-inkling$继承你的<b>生成</b>和<b>消耗</b>伤害加成。',
    # #352
    '$keyword-inkling$ grants you <pos>+8</pos> $keyword-varnish$ per attack and $+|+|25|BAR$ per $keyword-inkcast$.':
        '$keyword-inkling$每次攻击给你<pos>+8</pos>$keyword-varnish$，$keyword-inkcast$时$+|+|25|BAR$。',
    # #353
    'When <i>either</i> you or your $keyword-inkling$ take damage, you <i>both</i> <pos>expel thorns</pos> nearby. ($+|10|DMG$)':
        '你或$keyword-inkling$<i>任一</i>受伤时<i>双方</i>释放<pos>荆棘</pos>($+|10|DMG$)。',
    # #354
    '$keyword-inkling$ $keyword-inkcast$ coalesces <pos>3</pos> homing healing orbs ($+|+|5|HP$).':
        '$keyword-inkling$$keyword-inkcast$生成<pos>3</pos>个追踪治疗球($+|+|5|HP$)。',
    # #355
    '$keyword-twists$ gain $+|+|25|%|DMG$ per stack.':
        '$keyword-twists$每层$+|+|25|%|DMG$。',
    # #356
    '$enemy-splices$ <neg>shrink</neg> and gain $-|+|25|%|SPD$.':
        '$enemy-splices$<neg>缩小</neg>并$-|+|25|%|SPD$。',
    # #357
    '$enemy-splices$ have a $Chance|-|33$ to arrive surrounded by <neg>spinning blades</neg>.':
        '$enemy-splices$有$Chance|-|33$携带<neg>旋转刀刃</neg>。',
    # #358
    '$enemy-splices$ damage has a chance to call down a sword from the heavens devastating foes caught in its attack.':
        '$enemy-splices$伤害有概率从天降剑，重创范围内敌人。',
    # #359
    'Deal $+|+|25|%|DMG$ to foes obscured by <neg>fog</neg>.':
        '对<neg>迷雾</neg>中的敌人$+|+|25|%|DMG$。',
    # #360
    'Gain $+|+|150|%|DMG$.\nLose <neg>all</neg> extra <b>Revives</b>.':
        '$+|+|150|%|DMG$。\n丢<neg>全部</neg>额外<b>复活</b>。',
    # #361
    '$+|-|75|%|CD$ for your $ability-primary$.':
        '$ability-primary$$+|-|75|%|CD$。',
    # #362
    '$enemy-splices$ leave a <neg>slowing trail</neg> on the ground.':
        '$enemy-splices$留下<neg>减速痕迹</neg>。',
    # #363
    'Your $keyword-inkling$ casts grant you both $+|+|2.5|%|SPD$ for <pos>4s</pos>. (Max $+|15|%$)':
        '$keyword-inkling$施法给双方$+|+|2.5|%|SPD$<pos>4s</pos>。(上限$+|15|%$)',
    # #364
    'Your $keyword-inkling$\'s $keyword-inkcast$ grants you $+|3|Bar$.':
        '$keyword-inkling$的$keyword-inkcast$给予$+|3|Bar$。',
    # #365
    '$keyword-atlas$\'s $keyword-fortify$ range gains $+|+|50|%|Size$.':
        '$keyword-atlas$的$keyword-fortify$范围$+|+|50|%|Size$。',
    # #366
    '$keyword-atlas$ also fires a <pos>beam</pos> at the foe with <b>highest health</b> within range, dealing <pos>increased damage</pos> over time.':
        '$keyword-atlas$向范围内<b>最高血量</b>敌人发射<pos>光束</pos>，持续<pos>增伤</pos>。',
    # #367
    '$keyword-atlas$ deals $+|75|%|DMG$ to nearby foes.':
        '$keyword-atlas$对附近敌人$+|75|%|DMG$。',
    # #368
    '$keyword-atlas$ primary attacks <pos>bounce</pos> to nearby foes, up to 3 times.':
        '$keyword-atlas$主攻击<pos>弹射</pos>附近敌人，至多3次。',
    # #369
    'Every $+|5|s$, $keyword-atlas$ will knockback ($+|50|DMG$) nearby foes.':
        '每$+|5|s$，$keyword-atlas$击退($+|50|DMG$)附近敌人。',
    # #370
    '$keyword-atlas$ kills <pos>generate</pos> a moderate amount of  $keyword-survey$ for itself. <i>(Amount increases each chapter.)</i>':
        '$keyword-atlas$击杀<pos>生成</pos>适量$keyword-survey$。<i>(每章递增)</i>',
    # #371
    '$ability-primary$ gives your next $ability-secondary$ $+|+|50|%|DMG$, and <pos>vice versa</pos>.':
        '$ability-primary$使下次$ability-secondary$$+|+|50|%|DMG$，<pos>反之亦然</pos>。',
    # #372
    '<b>Markets</b> now have additional purchase options.':
        '<b>商店</b>新增购买选项。',
    # #373
    'Gain a $Chance|+|25$ to restore $+|50|HP$ when your $barrier$ breaks.':
        '$barrier$破碎时$Chance|+|25$恢复$+|50|HP$。',
    # #374
    '$ability-primary$ has a $Chance|+|5$ to summon an <b>Entire Ship</b>.':
        '$ability-primary$有$Chance|+|5$召唤<b>整艘船</b>。',
    # #375
    'Can be <pos>deposited</pos> in <b>Lamps</b> within the <b>Metaphorest</b>.':
        '可<pos>存入</pos><b>隐喻森林</b>的<b>灯</b>中。',
    # #376
    'Bringing a bit of <pos>light</pos> with you as you move toward the next lamp.':
        '前往下个灯时携带一缕<pos>光</pos>。',
    # #377
    'While <b>returning</b>, $ability-secondary$ gains <pos>Size</pos> and deals $+|100|%|DMG$.':
        '<b>回程</b>时$ability-secondary$增加<pos>体积</pos>并$+|100|%|DMG$。',
    # #378
    '$ability-secondary$ now <pos>bounces</pos> between foes before <b>returning</b>.':
        '$ability-secondary$<b>回程</b>前在敌人间<pos>弹射</pos>。',
    # #379
    '$ability-secondary$ hurls <pos>two additional</pos> projectiles but costs $-|+|1$ mana.':
        '$ability-secondary$额外投掷<pos>两枚</pos>弹射物但消耗$-|+|1$法力。',
    # #380
    '$ability-secondary$ restores $+|10|BAR$ and grants 3 $keyword-varnish$ when it returns to you.':
        '$ability-secondary$返回时恢复$+|10|BAR$并给予3$keyword-varnish$。',
    # #381
    '$ability-secondary$ <pos>detonates</pos> after returning, dealing damage based on total flight distance.':
        '$ability-secondary$返回后<pos>引爆</pos>，伤害基于飞行距离。',
    # #382
    '$ability-secondary$ <pos>erupts</pos> ($+|75|DMG$) at its <b>Apex</b>.':
        '$ability-secondary$在<b>顶点</b><pos>爆发</pos>($+|75|DMG$)。',
    # #383
    '$ability-secondary$ maximum increases by <pos>2 Planets</pos>.':
        '$ability-secondary$上限增加<pos>2颗星球</pos>。',
    # #384
    '$ability-secondary$ summons <pos>2 additional Planets</pos> but costs <neg>+1</neg> $mana-neutral$.':
        '$ability-secondary$额外召唤<pos>2颗星球</pos>但消耗<neg>+1</neg>$mana-neutral$。',
    # #385
    '$ability-secondary$ deals $+|50|%|DMG$ per <b>Planet</b> attacking the same target.':
        '每颗<b>星球</b>攻击同目标$ability-secondary$$+|50|%|DMG$。',
    # #386
    '$ability-secondary$ <b>Planets</b> occasionally slingshot <pos>meteors</pos> ($+|75|DMG$) at targets.':
        '$ability-secondary$<b>星球</b>偶尔弹射<pos>陨石</pos>($+|75|DMG$)。',
    # #387
    'Gain $+|100|%|SPD$ while using $ability-secondary$.':
        '使用$ability-secondary$时$+|100|%|SPD$。',
    # #388
    'Every third hit of $ability-secondary$ explodes the affected area ($+|25|DMG$).':
        '$ability-secondary$每第三击爆炸($+|25|DMG$)。',
    # #389
    '$ability-secondary$ also summons <pos>rainfall</pos>, drenching ($+|20|DMG$) up to 5 nearby foes.':
        '$ability-secondary$召唤<pos>降雨</pos>，淋湿($+|20|DMG$)至多5个敌人。',
    # #390
    'Damaging a foe <b>8 times</b> with a single $ability-secondary$ cast will detonate them for $+|100|%|DMG$ taken.':
        '单次$ability-secondary$命中敌人<b>8次</b>后引爆，造成$+|100|%|DMG$。',
    # #391
    '$ability-secondary$ <pos>pierces</pos> foes and gains $+|+|35|%|DMG$.':
        '$ability-secondary$<pos>穿透</pos>敌人并$+|+|35|%|DMG$。',
    # #392
    'Repeated $ability-secondary$ <b>rings</b> gain $+|+|33|%$ <pos> size and damage</pos>. <i>(Max 100%)</i>':
        '连续$ability-secondary$<b>环</b>$+|+|33|%$<pos>体积和伤害</pos>。<i>(上限100%)</i>',
    # #393
    'Every other $ability-secondary$ <b>ring</b> will <b>ring</b> <pos>twice</pos> on impact.':
        '每隔一个$ability-secondary$<b>环</b>命中时<pos>双响</pos>。',
    # #394
    '$ability-movement$ unleashes 3 <pos>free</pos> $ability-secondary$ <b>Needles</b>.':
        '$ability-movement$释放3根<pos>免费</pos>$ability-secondary$<b>Needles</b>。',
    # #395
    '$ability-secondary$ <b>Needles</b> <pos>return</pos> to you after impacting their initial targets, <pos>also damaging</pos> any foes in their path.':
        '$ability-secondary$<b>Needles</b>命中后<pos>返回</pos>，<pos>同时伤害</pos>路径上的敌人。',
    # #396
    '$ability-secondary$ <b>Needles</b> <pos>explode</pos> ($+|25|DMG$) on impact.':
        '$ability-secondary$<b>Needles</b>命中时<pos>爆炸</pos>($+|25|DMG$)。',
    # #397
    '$ability-secondary$ now spins $mana-neutral$ into a single,  increasingly powerful <b>Needle</b> that <pos>seeks all foes</pos> when released.':
        '$ability-secondary$将$mana-neutral$纺成一根强力<b>Needle</b>，释放后<pos>追踪所有敌人</pos>。',
    # #398
    'Generating $mana-neutral$ unleashes a <pos>free</pos> $ability-secondary$ <b>Needle</b>.':
        '产生$mana-neutral$释放<pos>免费</pos>$ability-secondary$<b>Needle</b>。',
    # #399
    'Casting $ability-secondary$ with <b>5</b> or more $mana-neutral$ causes all <b>Needles</b> to <pos>root</pos> and <pos>constrict</pos> ($+|35|DMG$) foes.':
        '以<b>5</b>+$mana-neutral$施放$ability-secondary$使<b>Needles</b><pos>缠绕</pos>($+|35|DMG$)敌人。',
    # #400
    'Spending $mana-neutral$ unleashes a <pos>free</pos> $ability-secondary$ <b>Needle</b>.':
        '消耗$mana-neutral$释放<pos>免费</pos>$ability-secondary$<b>Needle</b>。',
}
