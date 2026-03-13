# 开发交接文档

## 项目结构

```
Vellum汉化补丁/
├── arialuni_sdf_u2021          # TMP 中文字体 AssetBundle (22MB)
├── winhttp.dll                 # BepInEx 引导文件
├── doorstop_config.ini         # BepInEx 引导配置
├── install_chinese_patch.py    # 一键安装脚本
├── patch_assets.py             # 资源文件二进制补丁脚本 (导入所有翻译)
├── translations_extended.py    # 扩展翻译字典 (371条)
├── translations_batch1.py      # 批次1: #24-#197 能力效果 (59条)
├── translations_batch2.py      # 批次2: #201-#400 技能/移动描述 (183条)
├── translations_batch3.py      # 批次3: #401-#570 怪物/Boss基础 (167条)
├── translations_batch4.py      # 批次4: #571-#750 Boss机制/台词 (175条)
├── translations_batch5.py      # 批次5: #751-#900 诗歌/骰子/杂项 (143条)
├── translations_batch6.py      # 批次6: #901-#1130 系统/UI/教程 (217条)
├── README.md                   # 用户说明
├── DEV_NOTES.md                # 本文档
├── 使用说明.txt                # 用户使用说明
├── 安装说明.txt                # 安装指南
├── .gitignore
└── BepInEx/
    ├── config/
    │   └── AutoTranslatorConfig.ini   # XUnity 配置
    ├── core/                          # BepInEx 核心 DLL
    ├── plugins/
    │   ├── XUnity.AutoTranslator/     # 文本钩子插件
    │   └── XUnity.ResourceRedirector/ # 资源重定向插件
    └── Translation/zh-CN/Text/
        └── _VellumChinese.txt         # 运行时翻译文件 (~1784条)
```

## 翻译覆盖统计

| 来源 | 条数 |
|------|------|
| patch_assets.py 基础翻译 | 37 |
| translations_extended.py | 371 |
| translations_batch1~6.py | 944 |
| **二进制补丁总计** | **1,352** |
| _VellumChinese.txt 运行时 | 1,784 |
| **总覆盖率** | **~92.5% (2,289/2,475)** |

未翻译的 ~186 条中，23 条为开发者内部注释（如 "Base Text:"、"Controlled via code..." 等），
其余为深层嵌入或无需翻译的内容。

## 技术架构

### 两层翻译机制

1. **XUnity.AutoTranslator 文本钩子**（`_VellumChinese.txt`）
   - 拦截 Unity TextMeshPro 的 text setter
   - 实时替换 UI 文本：菜单、按钮、Boss 名称、技能名、战斗指令等
   - 不修改游戏文件，完全运行时替换

2. **二进制资源补丁**（`patch_assets.py`）
   - 直接修改 `resources.assets`（176MB）中的嵌入文本
   - Boss 描述正文、战斗提示详情等 ScriptableObject 内嵌文本
   - XUnity 无法钩取这些文本（不经过标准 TMP text setter）

### 二进制补丁原理

Unity 字符串序列化格式：
```
[4字节 小端 uint32 长度] [N字节 UTF-8 字符串数据] [对齐填充到4字节]
```

补丁方式：
- 在文件中查找英文 UTF-8 字节序列
- 替换为中文 UTF-8 字节 + `\x00` 空字节填充
- **不修改长度前缀！** 修改会导致后续字段偏移错位，游戏黑屏
- 中文字节数必须 ≤ 英文字节数，否则跳过

### 字体方案

- 游戏使用 TMP 1.4.0，字体 AssetBundle 版本 1.1.0（有不匹配警告但可用）
- `arialuni_sdf_u2021` 放在游戏根目录
- 通过 `AutoTranslatorConfig.ini` 配置：
  ```ini
  OverrideFontTextMeshPro=arialuni_sdf_u2021
  FallbackFontTextMeshPro=arialuni_sdf_u2021
  ```

## 截图分析 — 剩余未汉化内容

### 图鉴页面（截图 1）
- ✅ Boss 名称、描述正文、「战斗提示」标题、「独特机制」标题已汉化
- ❌ 战斗提示列表项 `- Don't get overwhelmed with adds!`、`- Dodge damage!`
  - 这些在 `_VellumChinese.txt` 中有翻译，但实际是嵌入在资源中的
  - 需要加入 `patch_assets.py` 的 TRANSLATIONS 字典
- ❌ 底部 `Note: Mechanics may appear differently in other Worlds.`
  - 同上，嵌入在资源中，XUnity 无法钩取

### 独特机制页面（截图 2）
- ❌ `AoE Dodge` 标题及描述段落
- 这些文本在 `vellum_text_extracted.json` 中存在，但部分带有二进制前缀
  无法用简单的 `data.find()` 匹配
- 需要更复杂的偏移定位方式（按已知 offset 直接修补）

### 战斗场景（截图 3）
- ❌ `SOAK on ★Tank to clear a space!` — 含 `<sprite name="sym_bar">` 精灵图标
  - XUnity 看到的文本包含精灵标记，与翻译文件中的纯文本不匹配
  - 解决方案：在翻译文件中添加含精灵标记的完整变体

## 待办事项

### 已完成 (v4.0)
- [x] 全部 Boss 描述与机制说明
- [x] 全部页面效果与能力描述
- [x] 全部怪物图鉴描述
- [x] 全部设置项说明、教程文本
- [x] 全部成就/挑战文本
- [x] 全部背景故事/诗歌/台词
- [x] 墨水机制、签名技能描述
- [x] 含 `<sprite>` 标记的战斗文本

### 可能的后续工作
- [ ] 游戏版本更新后新增文本
- [ ] 极少数开发者内部注释文本（非用户可见，低优先级）

## 配置注意事项

### 会导致游戏卡死的配置（不要开启！）
```ini
TextGetterCompatibilityMode=True    # 导致游戏冻结
ForceMonoModHooks=True              # 导致游戏冻结
IgnoreVirtualTextSetterCallingRules=True  # 导致游戏冻结
```

### 调试用配置（发布时关闭）
```ini
EnableTextPathLogging=False         # 开启会生成大量日志
OutputUntranslatableText=False      # 开启会输出未翻译文本
LogAllLoadedResources=False         # 开启会记录所有加载的资源
EnableDumping=False                 # 开启会导出资源（与 CacheMetadataForAllFiles 冲突）
```

## 相关文件位置（开发环境）

- 游戏目录：Steam 库中的 `Vellum Study Hall/`
- 补丁源码：本仓库
- 辅助文件（不含在发布包中）：
  - `still_missing.txt` — 翻译进度跟踪（已完成）
  - `to_translate.txt` — 待翻译文本提取
  - `untranslated_*.txt` — 未翻译文本分析
