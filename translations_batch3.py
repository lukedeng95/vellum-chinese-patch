# -*- coding: utf-8 -*-
"""Batch 3: #401-#570 - Abilities, monsters, boss mechanics"""

TRANSLATIONS_BATCH3 = {
    # #401
    'Casting $ability-secondary$ with $mana-teal$ fires off a $keyword-twist$.':
        '用$mana-teal$施放$ability-secondary$发射$keyword-twist$。',
    # #402
    'You deal $+|+|650|%|DMG$ to enemies over <b>60m</b> away.':
        '对<b>60m</b>外的敌人$+|+|650|%|DMG$。',
    # #403
    'Can be deposited at your $keyword-atlas$ to empower its damage.':
        '可存入$keyword-atlas$以增强伤害。',
    # #404
    'Your $ability-movement$ has a $+|50|%| Shorter$ cooldown while on an <b>Inkway</b>.':
        '在<b>墨道</b>上$ability-movement$冷却$+|50|%| Shorter$。',
    # #405
    '$ability-secondary$ now <pos>curves</pos> toward where you aim. The explosion now <pos>follows you</pos>.':
        '$ability-secondary$<pos>弯曲</pos>飞向瞄准处。爆炸<pos>跟随你</pos>。',
    # #406
    '$ability-secondary$ launches a second, smaller glob ($+|120|DMG$) away from the caster\'s location when it lands.':
        '$ability-secondary$落地时反向发射小球($+|120|DMG$)。',
    # #407
    '<b>Shelf Sanitization</b> will last for an additional $-|15| Seconds$.':
        '<b>书架净化</b>延长$-|15| Seconds$。',
    # #408
    'Your $barrier$ starts regenerating <pos>faster</pos> after taking damage.':
        '受伤后$barrier$<pos>更快</pos>开始恢复。',
    # #409
    'Dealing $+|+|30|%|DMG$ while near Dawn or Dusk.':
        '在Dawn或Dusk附近时$+|+|30|%|DMG$。',
    # #410
    'In view of the <b>Flabberghast\'s</b> <neg>Burble Orb</neg>!':
        '在<b>惊骇者</b>的<neg>泡沫球</neg>视野中！',
    # #411
    '$ability-primary$ can now <pos>Sync</pos>.\nSyncing with $ability-primary$ deals $+|+|1000|%|DMG$.':
        '$ability-primary$可<pos>同步</pos>。\n同步$ability-primary$造成$+|+|1000|%|DMG$。',
    # #412
    '<b>Hold & Release:</b> Continually spin $mana-neutral$ into a host of <pos>Threaded Needles</pos> that <b>seek</b> foes <pos>through terrain</pos> when released.':
        '<b>蓄力释放:</b>持续将$mana-neutral$纺为<pos>穿线针</pos>，释放后<pos>穿越地形</pos><b>追踪</b>敌人。',
    # #413
    '<b>Hold & Release:</b> Continually spin $mana-neutral$ into a host of <b>Threaded Needles</b> that <pos>seek</pos> foes <pos>through terrain</pos> when released.':
        '<b>蓄力释放:</b>持续将$mana-neutral$纺为<b>穿线针</b>，释放后<pos>穿越地形</pos><pos>追踪</pos>敌人。',
    # #414
    'Plants fire <neg>more projectiles</neg> when attacking.':
        '植物攻击时发射<neg>更多弹射物</neg>。',
    # #415
    'Tougher $enemy-ravings$  are warped in to defend the Plant.':
        '更强的$enemy-ravings$被传送来守护植物。',
    # #416
    '<b>Styxen</b>\'s slashes spawn <neg>extra whirlwinds</neg> on impact.':
        '<b>Styxen</b>的斩击命中时产生<neg>额外旋风</neg>。',
    # #417
    '$ability-movement$ damage has a $+|25|%| Chance$ to set its cooldown to <b>0.5s</b>.':
        '$ability-movement$伤害有$+|25|%| Chance$将冷却设为<b>0.5s</b>。',
    # #418
    '$ability-movement$ damage always sets its cooldown to <b>0.5s</b>.':
        '$ability-movement$伤害必定将冷却设为<b>0.5s</b>。',
    # #419
    '$ability-movement$ gives your next $ability-primary$ $+|+|150|%|DMG$.':
        '$ability-movement$使下次$ability-primary$$+|+|150|%|DMG$。',
    # #420
    'Mend <b>Quarry</b> & Reach <sprite name="binding"> Attunement <b>15</b>.':
        '修复<b>采石场</b>并达到<sprite name="binding">调谐<b>15</b>。',
    # #421
    'Mend a tome at <sprite name="binding">20 with <b>Concoct</b> equipped.':
        '装备<b>调配</b>在<sprite name="binding">20修复典籍。',
    # #422
    'Mend a tome at <sprite name="binding">20 with <b>Clatter</b> equipped.':
        '装备<b>喧嚣</b>在<sprite name="binding">20修复典籍。',
    # #423
    'Mend a tome at <sprite name="binding">20 with <b>Enkindle</b> equipped.':
        '装备<b>燃墨</b>在<sprite name="binding">20修复典籍。',
    # #424
    'Mend <b>The Lost Symphony</b> at <sprite name="binding">20.':
        '在<sprite name="binding">20修复<b>失落交响曲</b>。',
    # #425
    'Mend <b>Rivals</b> at <sprite name="binding">20.':
        '<sprite name="binding">20修复<b>宿敌</b>。',
    # #426
    'Mend <b>Quarry</b> at <sprite name="binding">20.':
        '<sprite name="binding">20修<b>采石场</b>。',
    # #427
    'Mend <b>Illegible</b> at <sprite name="binding">20.':
        '在<sprite name="binding">20修复<b>难辨</b>。',
    # #428
    'Slain $torn$ have a $Chance|+|15$ to explode in a shower of $keyword-gold$':
        '击杀的$torn$有$Chance|+|15$爆出$keyword-gold$',
    # #429
    'Casting $ability-primary$ has a $Chance|+|10$ to reset the cooldown of $ability-movement$.':
        '$ability-primary$有$Chance|+|10$重置$ability-movement$冷却。',
    # #430
    'Your $keyword-inkling$ deals $+|+|50|%|DMG$ to foes between you.':
        '$keyword-inkling$对你们之间的敌人$+|+|50|%|DMG$。',
    # #431
    'Your $keyword-inkling$\'s <pos>Primary</pos> deals $+|+|200|%|DMG$.':
        '$keyword-inkling$的<pos>主攻击</pos>$+|+|200|%|DMG$。',
    # #432
    '$keyword-inkling$ $keyword-inkcast$ grants you $+|+|25|%|DMG$ for <pos>5s</pos>. (Max 100%)':
        '$keyword-inkling$$keyword-inkcast$给予$+|+|25|%|DMG$<pos>5s</pos>。(上限100%)',
    # #433
    'Each $mana-neutral$ spent reduces the cooldown of $ability-core$ by $+|1|s$.':
        '每消耗$mana-neutral$降低$ability-core$冷却$+|1|s$。',
    # #434
    'Launches a fireball, dealing 25 damage and applying a stack of %status-burning%':
        '发射火球，造成25伤害并施加一层%status-burning%',
    # #436
    'Warp in a <pos>Planet</pos> to <b>overshadow</b> your foes for <pos>10s</pos>.':
        '传送<pos>星球</pos><b>笼罩</b>敌人<pos>10s</pos>。',
    # #437
    '<b>Hold & Release:</b> Designate a firing direction for $keyword-Atlas$, unleashing a <pos>map-wide beam</pos> when released.':
        '<b>蓄力释放:</b>指定$keyword-Atlas$发射方向，释放<pos>全图光束</pos>。',
    # #438
    'You take $+|-10|%|DMG$ while <pos>near</pos> your $keyword-inkling$.':
        '<pos>靠近</pos>$keyword-inkling$时受到$+|-10|%|DMG$。',
    # #439
    'Deal more damage to $enemy-elites$ the higher Unrivaled stacks.':
        'Unrivaled层数越高对$enemy-elites$伤害越高。',
    # #441
    'Gain $+|+|20|%|DMG$ while at full $mana-neutral$.':
        '满$mana-neutral$时$+|+|20|%|DMG$。',
    # #443
    '$ability-primary$ affects the <pos>size</pos> of your next $ability-secondary$ based on the rolled number ($-|-|20|%$-$+|+|200|%$).':
        '$ability-primary$根据骰子影响下次$ability-secondary$<pos>体积</pos>($-|-|20|%$-$+|+|200|%$)。',
    # #444
    'Increased <pos>speed</pos> while traveling on the <b>inkways</b>.':
        '在<b>墨道</b>上<pos>速度</pos>提升。',
    # #445
    '$ability-primary$ deals an <pos>additional</pos> $+|100|%|DMG$ after <b>1s.</b>':
        '$ability-primary$<b>1s</b>后<pos>额外</pos>$+|100|%|DMG$。',
    # #446
    '$ability-primary$ has a $Chance|+|10$ to deal $+|+|250|%|DMG$ and then increase all your damage by $+|+|20|%$ for <b>5s</b>.':
        '$ability-primary$有$Chance|+|10$造成$+|+|250|%|DMG$并增加$+|+|20|%$全伤害<b>5s</b>。',
    # #447
    'Every third hit from $ability-primary$ deals $+|+|30$ <pos>base damage</pos>.':
        '$ability-primary$每第三击$+|+|30$<pos>基础伤害</pos>。',
    # #448
    '$ability-primary$ has a $Chance|+|33$ to burst ($+|25|DMG$) and knock back foes behind the target.':
        '$ability-primary$有$Chance|+|33$爆裂($+|25|DMG$)并击退目标身后敌人。',
    # #449
    '$ability-primary$ causes an eruption of spikes ($+|10|DMG$) in front of you.':
        '$ability-primary$在前方喷出尖刺($+|10|DMG$)。',
    # #450
    '$ability-primary$ launches $+|3|x$ projectiles with $-|-|50|%|DMG$ and <neg>Reduced Range and Accuracy</neg>.':
        '$ability-primary$发射$+|3|x$弹射物，$-|-|50|%|DMG$且<neg>射程和精度降低</neg>。',
    # #451
    '$ability-utility$ now grants $keyword-embossed$ for 5s, but <neg>drains all mana</neg>.':
        '$ability-utility$给予$keyword-embossed$5s，但<neg>消耗全部法力</neg>。',
    # #452
    '$ability-utility$ fully restores mana.':
        '$ability-utility$完全恢复法力。',
    # #453
    'Minor characters, sidekicks, wanderers, and others are often strong foils for more central protagonists.':
        '配角和游侠常为主角的有力衬托。',
    # #454
    'As numerous and obsessive <style="bolditalic>Splices</style>, the <b>Skeleton Crews</b> leap at the opportunity to strike a killing blow.':
        '作为执着的<style="bolditalic>Splices</style>，<b>骷髅团</b>总伺机致命一击。',
    # #455
    '<b>Skeleton Crews</b> slash out with their swords, damaging nearby foes.':
        '<b>骷髅团</b>挥剑斩击附近敌人。',
    # #456
    '<b>Skeleton Crews</b> lunge gret distances to close the gap with their target.':
        '<b>骷髅团</b>远距突进接近目标。',
    # #457
    'As a rank and file <style="bolditalic>Splice</style>, <b>Imps</b> excel at staying dangerous while closing in on their prey':
        '作为基础<style="bolditalic>Splice</style>，<b>小鬼</b>善于在接近猎物时保持威胁',
    # #458
    '<b>Imp</b> unleashes a short-range gout of flame.':
        '<b>小鬼</b>释放近距火焰喷射。',
    # #459
    '<b>Imp</b> spins toward its target, dealing damage along its path.':
        '<b>小鬼</b>旋转冲向目标，沿途造成伤害。',
    # #460
    '<b>Whirlwind</b> also casts <b>Flamethrower</b> while spinning.':
        '<b>旋风</b>旋转时同时释放<b>火焰喷射</b>。',
    # #461
    'Deadly and simple, <b>Burstbugs</b> embody a core tenet of <style="bolditalic>Splices</style>: danger close.':
        '致命而简单，<b>爆虫</b>体现了<style="bolditalic>Splices</style>的核心：近身危险。',
    # #462
    'Resilience, commitment, and a medium range make <b>Wranglers</b> potent <style="bolditalic>Splices</style>. Devastating in a trio.':
        '韧性和中距攻击使<b>驭手</b>成为强力<style="bolditalic>Splices</style>。三只一组毁灭性极强。',
    # #463
    '<b>Wranglers</b> launch a series of three exploding orbs at their nearby targets.':
        '<b>驭手</b>向附近目标发射三连爆炸球。',
    # #464
    '<b>Wranglers</b> swipe weakly at nearby foes.':
        '<b>驭手</b>虚弱地挥击附近敌人。',
    # #465
    '<b>Ruminators</b> slam the ground, dealing more damage based on \nstacks of <b>Munch</b>.':
        '<b>反刍者</b>重击地面，伤害随\n<b>咀嚼</b>层数增加。',
    # #466
    '<b>Ruminators</b> stop to eat handfuls of ideas to grow in size \nand speed, for a time.':
        '<b>反刍者</b>停下吞食灵感，暂时增大\n体型和速度。',
    # #467
    'As an individual, the <b>Spewer</b> may be a manageable and unimposing foe. The coalesced vitriolic writings that make up its body are frequently released in a shower of seemingly random toxicity.':
        '单独的<b>喷吐者</b>并不起眼。但其体内汇聚的刻薄文字常以看似随机的毒液喷射而出。',
    # #468
    'With numbers and a taste for casual cruelty from afar, <b>Spewers</b> make for troublesome <style="bolditalic">Tangents</style>.':
        '凭借数量和远程攻击，<b>喷吐者</b>是棘手的<style="bolditalic">Tangents</style>。',
    # #469
    '<b>Spewer</b> unleash a hail of scattered, damaging droplets.':
        '<b>喷吐者</b>释放散射伤害液滴。',
    # #470
    'Ranged, resilient, and relentless - <b>Shades</b> rank among the simplest of <style="bolditalic">Tangents</style>.':
        '远程、坚韧、无情——<b>暗影</b>是最基本的<style="bolditalic">Tangents</style>。',
    # #471
    '<b>Shades</b> fling a couplet of weighty projectiles at their targets.':
        '<b>暗影</b>向目标投掷一对沉重弹射物。',
    # #472
    'With the sharpest wit of the lesser <style="bolditalic">Tangents</style>, the <b>Glint</b> could be considered a manifestation of unrealized potential. Some small spark - a plot thread, character, or detail of great interest - left to rot in shadow. A hint of something more.':
        '<b>微光</b>是低阶<style="bolditalic">Tangents</style>中最敏锐的——未实现潜力的化身。某个遗落在暗处的情节或角色。',
    # #473
    'Agile and angry, <b>Glints</b> excel as one of the longest-ranged <style="bolditalic">Tangents</style>.':
        '敏捷而暴怒，<b>微光</b>是射程最远的<style="bolditalic">Tangents</style>之一。',
    # #474
    '<b>Glint</b> shoots a swift, sharp, long-range attack at its target.':
        '<b>微光</b>向目标射出迅疾的远程攻击。',
    # #475
    'Immeasurably focus\'d, even among <style="bolditalic">Tangents</style>, these foes spring up in all the wrong places.':
        '即使在<style="bolditalic">Tangents</style>中也极度专注，这些敌人总出现在错误之处。',
    # #476
    '<b>Apostrophes</b> draw dense energy from the ground, then hurl\'t at their foes\' position.':
        '<b>撇号</b>从地面汲取能量，朝敌人位置投掷。',
    # #477
    'Errata comes in all shapes and sizes. Even the smallest of errors can have the largest of consequences.':
        '勘误形形色色。最小的错误也能引发最大的后果。',
    # #478
    '<b>Rats</b> are the quintessential <style="bolditalic">Raving</style>: numerous, draining, overwhelming.':
        '<b>老鼠</b>是典型的<style="bolditalic">Raving</style>：众多、消耗、压倒。',
    # #479
    '<b>Rats</b> slow the movement speed of nearby foes.':
        '<b>老鼠</b>减缓附近敌人移动速度。',
    # #480
    'There are many tales of survival, hardship, and heroism in which a Boar is challenged and defeated. Tests of strength and will - forging heroes in times of dire need. It is also a tragic and necessary rarity for the beasts to win and heroes to fall.':
        '许多关于生存和英雄主义的故事中，野猪被挑战并击败。力量与意志的考验——在危难中锻造英雄。',
    # #481
    'Direct and disruptive as <style="bolditalic">Ravings</style> come, <b>Boars</b> seek to put heroes in their place.':
        '直接而具破坏性的<style="bolditalic">Ravings</style>，<b>野猪</b>要让英雄知道厉害。',
    # #482
    '<b>Boar</b> charges its target, damaging and knocking them back.':
        '<b>野猪</b>冲锋向目标，造成伤害并击退。',
    # #483
    'As <style="bolditalic">Ravings</style>, the <b>Toads</b> thrive on displacing their foes as often as possible.':
        '作为<style="bolditalic">Ravings</style>，<b>蟾蜍</b>擅长频繁位移敌人。',
    # #484
    '<b>Toads</b> leap to reposition around their foes.':
        '<b>蟾蜍</b>跳跃重新定位。',
    # #485
    '<b>Raptors</b> quickly swipe their tails, damaging and knocking back their foes.':
        '<b>迅猛龙</b>快速尾击，伤害并击退敌人。',
    # #486
    '<b>Raptors</b> hungrily jump to their prey as often as possible.':
        '<b>迅猛龙</b>频繁扑向猎物。',
    # #487
    '<b>Gruffs</b> charge to ram foes- knocking them upwards.':
        '<b>山羊</b>冲撞敌人并将其击飞。',
    # #488
    '<b>Gruffs</b> leap to reposition, knocking back any in their path.':
        '<b>山羊</b>跳跃移位，击退沿途一切。',
    # #489
    '<b>Gruffs</b> frequently dodge when in danger or under scrutiny.':
        '<b>山羊</b>在危险时频繁闪避。',
    # #490
    '<b>Stalagmights</b> form from subtle discrepancies and misuses of similar vocabulary. They amass small errata, condensing the seemingly innocuous mistakes into larger, sharper weapons.':
        '<b>石笋怪</b>由词汇误用形成，将细小勘误凝聚为更大更锋利的武器。',
    # #491
    'As a durable and slower <style="bolditalic">Splice</style>, <b>Stalagmights</b> will often try to combine their abilities in quick succession.':
        '作为较慢但耐久的<style="bolditalic">Splice</style>，<b>石笋怪</b>常连续组合技能。',
    # #492
    '<b>Stalagmights</b> force a cone rock shards up from the ground in a damaging area.':
        '<b>石笋怪</b>从地面锥形喷射碎石造成范围伤害。',
    # #493
    '<b>Rattlespikes</b>, where hollow words and hollow deeds combine. They emerge from simple dramas, once full of promise, yet never fleshed out.':
        '<b>响刺</b>——空洞的言行交汇。源于未完成的简单戏剧。',
    # #494
    '<b>Rattlespikes</b> lead the <style="bolditalic">Splices</style> closer to their foes, though able to exert strength from afar.':
        '<b>响刺</b>带领<style="bolditalic">Splices</style>接近敌人，但也能远程发力。',
    # #495
    '<b>Rattlespikes</b> swingtheir large flail, damaging nearby foes.':
        '<b>响刺</b>挥舞大型连枷伤害附近敌人。',
    # #496
    'The <b>Ogre</b> comes from monstrous origin. \nIt does not creep. It does not sleep.\nIt does not plot. It does not plan.\nIts subtlety is discarded. Its terror is plain.\nA mercy and curse that it must rest.l':
        '<b>食人魔</b>源于怪诞。\n不潜行。不休眠。\n不密谋。不计划。\n无需伪装，恐惧昭然。\n必须休息既是慈悲亦是诅咒。',
    # #497
    'As brutal and furious as <style="bolditalic">Splices</style> come, the <b>Ogre</b> is a reckoning with legs.':
        '作为最残暴的<style="bolditalic">Splices</style>，<b>食人魔</b>是行走的清算。',
    # #498
    '<b>Ogre</b> swipes with a massive, deadly arm.':
        '<b>食人魔</b>挥舞致命巨臂。',
    # #499
    '<b>Ogre</b> sprints erratically toward its target, blind with rage.':
        '<b>食人魔</b>疯狂冲向目标，盲目暴怒。',
    # #500
    '<b>Ogre</b> pauses to regenerate its health in a small area.':
        '<b>食人魔</b>停下在小范围内回复生命。',
    # #501
    'Layers and layers and layers of armor.':
        '层层叠叠的护甲。',
    # #502
    'Few <style="bolditalic">Splices</style> traverse distance better - the irony of <b>Ironclaw</b>.':
        '少有<style="bolditalic">Splices</style>更擅长位移——<b>铁爪</b>的讽刺。',
    # #503
    '<b>Ironclaw</b> swipes nearbyfoes with its deadly gauntlets.':
        '<b>铁爪</b>用致命铁手套挥击附近敌人。',
    # #504
    '<b>Ironclaw</b> hurtles into the air, then lands with deadly force.':
        '<b>铁爪</b>跃入空中后致命落地。',
    # #505
    '<b>Slimers</b>, in their ability to overwhelm the battlefield, express a core tenet of <style="bolditalic">Splices</style>: more.':
        '<b>史莱姆</b>以淹没战场的能力体现<style="bolditalic">Splices</style>的核心：更多。',
    # #506
    '<b>Slimer</b> swipes nearby foes with a goopy arm.':
        '<b>史莱姆</b>用粘液臂挥击附近敌人。',
    # #507
    '<b>Slimer</b> coalesces mass into new slimes after receiving enough damage.':
        '<b>史莱姆</b>受足够伤害后凝聚为新个体。',
    # #508
    'The <b>Dire Zombie\'s</b> origin is strange, even to its fellow <style="bolditalic">Splices</style>.':
        '<b>恐怖僵尸</b>的起源奇异，即便对<style="bolditalic">Splices</style>同伴也是。',
    # #509
    '<b>Dire Zombies</b> gnash nearby foes, dealing damage. Thankfully, this does not transform the victim.':
        '<b>恐怖僵尸</b>撕咬附近敌人造成伤害。庆幸的是不会感染。',
    # #510
    '<b>Dire Zombies</b> hurl exploding spheres of undeath at their foes.':
        '<b>恐怖僵尸</b>向敌人投掷亡灵爆炸球。',
    # #511
    'The stone fist, grasping for answers, leaves nothing but rubble in its wake.':
        '石拳求索答案，身后只留废墟。',
    # #512
    'Controlling and precise, <b>Bold-ers</b> rank among the most disruptive <style="bolditalic">Tangents</style>.':
        '精准的<b>巨石怪</b>是最具干扰性的<style="bolditalic">Tangents</style>。',
    # #513
    '<b>Bold-er</b> flings a heavy stone at its target.':
        '<b>巨石怪</b>向目标投掷巨石。',
    # #514
    '<b>Haunt</b> launches a deadly, long-range orb at its target.':
        '<b>幽灵</b>发射致命远程球体。',
    # #515
    '<b>Haunt</b> shrinks itself and nearby allies, granting a burst of speed.':
        '<b>幽灵</b>缩小自身和附近盟友，获得速度爆发。',
    # #516
    'It is a strange error for writing to be too short. <b>Bolters</b> are impatience made corporeal: backwards wanderers, skipping swiftly to the end of things.':
        '文字过短是奇异的错误。<b>奔逃者</b>是具象化的急躁：向后的游荡者。',
    # #517
    '<b>Bolters</b> are devastating within the <style="bolditalic">Tangent</style> ranks - few have more destructive and accurate power.':
        '<b>奔逃者</b>在<style="bolditalic">Tangent</style>中毁灭力和精度首屈一指。',
    # #518
    '<b>Bolters</b> jettison a fast, deadly projectile from extreme range.':
        '<b>奔逃者</b>从极远处发射致命弹射物。',
    # #519
    '<b>Bolters</b> quickly hop as far from incoming threats as possible.':
        '<b>奔逃者</b>迅速跳离威胁。',
    # #520
    'Like its <style="bolditalic">Tangent</style> comrades, the <b>Cryptex</b> reigns from afar with relentless, distance-based precision.':
        '如同<style="bolditalic">Tangent</style>同伴，<b>密码匣</b>以远距精确攻击称霸。',
    # #521
    'Continuously hurls bolts of confusion that, after a certain distance, will <neg>seek</neg> targets.':
        '持续投掷混乱箭矢，飞行一段后<neg>追踪</neg>目标。',
    # #522
    '<b>Acolyte</b> shoves slow, damaging orbs toward its targets.':
        '<b>侍僧</b>推出缓慢伤害球体。',
    # #523
    'Hearty, mobile, ferocious - <b>Lizards</b> control areas with the best of the <style="bolditalic">Raving</style>.':
        '强壮、灵活、凶猛——<b>蜥蜴</b>是最佳区域控制<style="bolditalic">Raving</style>。',
    # #524
    '<b>Lizard</b> spins, using its tail to damage and knockback nearby foes.':
        '<b>蜥蜴</b>旋转尾击伤害并击退附近敌人。',
    # #525
    '<b>Lizard</b> leaps, attempting to land behind its target.':
        '<b>蜥蜴</b>跳跃至目标身后。',
    # #526
    '<b>Bears</b> sit unmatched in ferocity and pride among <style="bolditalic">Ravings</style>.':
        '<b>熊</b>在<style="bolditalic">Ravings</style>中凶猛和骄傲无人能及。',
    # #527
    '<b>Bears</b> maul nearby foes with deadly claws, knocking them into the air.':
        '<b>熊</b>用利爪撕裂附近敌人并将其击飞。',
    # #528
    '<b>Bears</b>will rest when damaged, healing themselves and nearby allies.':
        '<b>熊</b>受伤时休息，治疗自身和附近盟友。',
    # #529
    '<b>Spiders</b> delight in the arts of <style="bolditalic">Raving</style> disruption.':
        '<b>蜘蛛</b>精于<style="bolditalic">Raving</style>干扰之术。',
    # #530
    '<b>Spiders</b> fling a web ball that splats in an area, damaging and slowing Scirbes.':
        '<b>蜘蛛</b>投掷蛛网球溅射区域，伤害并减速抄写员。',
    # #531
    '<b>Spiders</b> eject a burst of damaging web bolts.':
        '<b>蜘蛛</b>喷射伤害蛛网弹。',
    # #532
    'Many <style="bolditalic">Ravings</style> long for the <b>Scorpion\'s</b> ability to disengage - to disrupt from delicious safety.':
        '许多<style="bolditalic">Ravings</style>渴望<b>蝎子</b>的脱战能力——安全地干扰。',
    # #533
    '<b>Scorpion</b> lobs a sickly porjectile, leaving behind a damaging, slowing pool.':
        '<b>蝎子</b>抛出毒液弹，留下减速伤害池。',
    # #534
    '<b>Scorpion</b> digs itself undergorund, becoming immune \nand secreting a poison pool.':
        '<b>蝎子</b>钻入地下变为免疫\n并分泌毒池。',
    # #535
    'The vital importance of plot hooks cannot be overstated; errata can easily upend the starting chapters of even the most compelling tale.':
        '情节钩子至关重要；勘误能轻易颠覆最引人入胜故事的开篇。',
    # #536
    '<style="bolditalic">Raving</style> <b>Crabs</b>, lethal in large numbers, might dance in exultant victory.':
        '<style="bolditalic">Raving</style><b>螃蟹</b>，数量致命，或欢舞庆胜。',
    # #537
    '<b>Crabs</b> fire bursts of three bubbles at their targets.':
        '<b>螃蟹</b>向目标射出三连泡沫。',
    # #538
    'Stuffed to the brim with prickling assertions and strawman arguments, the <b>Scarecrow</b> is an aggressive collection of potent errata.':
        '充斥着尖锐断言的<b>稻草人</b>是强力勘误的凶猛集合体。',
    # #539
    'The <b>Scarecrow</b> believes its brain to be the envy of all <style="bolditalic">Splices</style>. If only.':
        '<b>稻草人</b>自认其脑是全体<style="bolditalic">Splices</style>的羡慕对象。可惜。',
    # #540
    '<b>Scarecrow</b> cross slashes nearby foes with its sickles.':
        '<b>稻草人</b>用镰刀交叉斩击附近敌人。',
    # #541
    'When the rules of worlds within worlds crumble -':
        '当世中之世的法则崩塌——',
    # #542
    'In combat, a <style="bolditalic">Splice</style> seeks to close the gap. <b>The Wringer</b> seeks to destroy it.':
        '战斗中<style="bolditalic">Splice</style>缩短距离。<b>绞拧者</b>要摧毁距离。',
    # #543
    '<b>The Wringer</b> delivers an earth-shattering punch.':
        '<b>绞拧者</b>释放天崩地裂之拳。',
    # #544
    '<b>The Wringer</b> hurls a chunk of the setting at its target.':
        '<b>绞拧者</b>将环境碎块掷向目标。',
    # #545
    '<b>The Wringer</b> unleashes an increasingly large series of destructive rings across the arena.':
        '<b>绞拧者</b>在竞技场释放越来越大的破坏环。',
    # #546
    '<b>Howl</b> sweeps its zephyrous mace at nearby foes.':
        '<b>嚎叫</b>挥舞风锤横扫附近敌人。',
    # #547
    '<b>Howl</b> launches a sweeping salvo of fast, windy projectiles \ntoward its target.':
        '<b>嚎叫</b>向目标发射快速风弹\n横扫齐射。',
    # #548
    'A secret of gibberish - one can abandon meaning and understanding to grasp the truth: it might only be gibberish. Alone, nonsense can have its proper place.':
        '胡言乱语的秘密——放弃意义才能领悟真相：可能本就是胡话。',
    # #549
    'Able to reaching its quarry at any distance, the <b>Flabberghast</b> excels as an oppressive <style="bolditalic">Tangent</style>.':
        '能在任何距离打击猎物，<b>惊骇者</b>是压迫性极强的<style="bolditalic">Tangent</style>。',
    # #550
    'Vagaries and folklore form a lasting, dynamic relationship where the organic evolution of heroes and villains may shift in the retelling of tales.':
        '传说与民间故事形成持久的动态关系，英雄与恶人在复述中演化。',
    # #551
    'The <b>Huntsman\'s</b>  accuracy is legend among <style="bolditalic">Tangents</style>.':
        '<b>猎人</b>的精准在<style="bolditalic">Tangents</style>中堪称传奇。',
    # #552
    '<b>Huntsman</b> draws, aims, then fires a swift and deadly attack.':
        '<b>猎人</b>拉弓瞄准后射出致命一击。',
    # #553
    'There is a smoldering anger at the heart of <style="bolditalic">Tangents</style>, often concealed by distance and questions. Their hunger for knowledge typically eclipses their fury at the obstacles in their path.':
        '<style="bolditalic">Tangents</style>心中燃烧着怒火，常被距离和疑问掩盖。对知识的渴望超越了对障碍的愤怒。',
    # #554
    'From afar, the <b>Blaze</b> strikes fear into its foes and fellow <style="bolditalic">Tangents</style> alike.':
        '远方的<b>烈焰</b>令敌人和<style="bolditalic">Tangents</style>同伴都心生畏惧。',
    # #555
    '<b>Blaze</b> hurls a ball of flame at its target.':
        '<b>烈焰</b>向目标投掷火球。',
    # #556
    '<b>Blaze</b> rolls a boiling wave of magma along the ground toward its target.':
        '<b>烈焰</b>沿地面向目标滚出沸腾岩浆波。',
    # #557
    'The <b>Mimic</b> is a terrifying warning; the <style="bolditalic">Raving Lord\'s</style> whimsy survives.':
        '<b>拟态怪</b>是可怕的警告；<style="bolditalic">Raving Lord\'s</style>奇想犹存。',
    # #558
    'With forced gambits and relentless attacks, the <b>Mummy</b> sits high in the <style="bolditalic">Raving</style> hierarchy.':
        '凭借强迫赌博和无情攻击，<b>木乃伊</b>位居<style="bolditalic">Raving</style>高层。',
    # #559
    '<b>Mummy</b> launches a grim projectile at its target.':
        '<b>木乃伊</b>向目标发射阴暗弹射物。',
    # #560
    '<b>Mummy</b> lunges to attack nearby foes.':
        '<b>木乃伊</b>突进攻击近敌。',
    # #561
    'The <b>Bogwalker</b> is a uniquely jealous <style="bolditalic">Raving</style>, able to fully stop the movement of its prey.':
        '<b>沼行者</b>是独特的<style="bolditalic">Raving</style>，能完全阻止猎物移动。',
    # #562
    '<b>Bogwalker</b> crushes with a brutal attack, knocking back its target.':
        '<b>沼行者</b>残暴重击并击退目标。',
    # #563
    '<b>Bogwalker</b> corrupts the ground around its target, <neg>rooting</neg> them on contact.':
        '<b>沼行者</b>腐化目标周围地面，接触时<neg>定身</neg>。',
    # #564
    'A monstrously intelligent <style="bolditalic">Raving</style>, the <b>Bully</b> is a master of the battlefield.':
        '极度聪慧的<style="bolditalic">Raving</style>，<b>恶霸</b>是战场主宰。',
    # #565
    '<b>Bully</b> stomps, charging through and damaging its targets.':
        '<b>恶霸</b>践踏冲锋，伤害目标。',
    # #566
    '<b>Quake</b> also summons a <i>second</i> ring of quakes.':
        '<b>震颤</b>额外召唤<i>第二</i>圈震波。',
    # #567
    '<b>Quake</b> also summons a <i>third</i> ring of quakes and an echoed quake.':
        '<b>震颤</b>额外召唤<i>第三</i>圈震波和回响震。',
    # #568
    '<i>"As <b>Cromash</b> and <b>Rambul</b>, your wills are sufficient.\nYour strengths are not, alone.\nShatter now these pages, <b>Crombul</b>.\nYour power carved in stone."</i><':
        '<i>"<b>Cromash</b>与<b>Rambul</b>，你们的意志足矣。\n但力量不够。\n撕碎此页，<b>Crombul</b>。\n你的力量刻于石中。"</i><',
    # #569
    'Destroying Pylons near <b>Crombul</b> will stun him':
        '摧毁<b>Crombul</b>附近的水晶柱可眩晕他',
    # #570
    'Plan your movements - <b>Crombul</b> is slow, but deadly!':
        '规划移动——<b>Crombul</b>虽慢但致命！',
}
