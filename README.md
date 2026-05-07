# Note Slides

Note Slides 是一套把访谈、播客、公众号长文、课程稿和复盘材料整理成 HTML 笔记幻灯片的工作流说明与模板。

它不是摘要器，也不是演讲稿生成器。它的核心任务是把材料里的原问题、原判断、现场追问、例子、数字、概念原词和关键张力，整理成可以横向翻阅的单文件 HTML slides。

好的输出应该像一份真实笔记：读者能顺着页面看到材料如何展开，谁在什么时候说了什么，哪些判断是从哪些例子和语境里长出来的。

## 适用场景

1. 访谈记录转笔记型 slides
2. 播客逐字稿转回顾 deck
3. 公众号长文转可翻阅笔记
4. 课程稿、PRD、口述稿转演示文稿
5. 需要保留原材料推进顺序的内容复盘

## 核心口径

1. 默认先还原材料，再提炼洞察。
2. 默认按材料原始顺序线性推进。
3. 每页必须有来源锚点，比如原问题、原判断、例子、数字、事件或概念原词。
4. 用户要求做 slides 时，直接交付单文件 HTML slides。
5. 微信公众号链接必须先确认拿到正文，不能把环境验证页当原文。
6. 商业、科技和创始人访谈默认使用冷静访谈笔记视觉系统，深色观点页、浅色证据页、清蓝编号和统一页眉页脚。

## 产出形态

1. 一个可在浏览器打开的 HTML 文件。
2. 横向翻页，适合现场讲解、复盘阅读和资料分享。
3. 页面文案以笔记链为主，不用导读腔，不用站在材料外面的总结腔。
4. 视觉设计服务阅读路径，优先保证信息关系清楚。

## 仓库结构

1. `SKILL.md`：工作流主说明。
2. `template.html`：HTML slides 基础模板。
3. `references/`：内容提取、视觉、布局和检查规则。
4. `scripts/`：材料预处理、计划检查、HTML 检查和核心文件打包脚本。

本地抓取的正文、临时 HTML、导出的 slides、PPTX 和打包产物默认不进入 GitHub。

## 脚本

本仓库的脚本都只使用 Python 标准库。

```bash
python3 scripts/prepare_source.py --input article.md --output source.json
python3 scripts/check_plan.py --plan deck.plan.json --source source.json
python3 scripts/check_deck.py --input deck.html
python3 scripts/pack_core.py --output /tmp/note-slides-core --git
```

`prepare_source.py` 用于把本地材料切成带 ID 的来源块。`check_plan.py` 用于在写 HTML 前检查每页是否有来源和锚点。`check_deck.py` 用于交付前做机械 P0。`pack_core.py` 用于发布前只复制核心文件，避免本地生成物进入 GitHub。

## 使用方式

把需要整理的文章、访谈、播客逐字稿、课程稿或链接交给支持本地工作流说明的 AI 工具，并要求使用 Note Slides 生成 slides。

如果是微信公众号链接，先校验是否拿到正文。如果只返回环境验证页，需要改用正文粘贴、导出的 md/html/pdf，或其他可验证的正文来源。

## License

MIT
