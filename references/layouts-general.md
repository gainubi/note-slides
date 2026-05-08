# 通用骨架

适合大多数 deck 的基础演讲动作：封面、解释、对比、引用、时间、收束。

## Layout 1：封面宣告

用于开场。封面结构固定，视觉变量按材料气质调整。
第一眼看标题，第二眼看来源，第三眼看材料语境。副标题只写来源语境，例如时长、文章类型、访谈对象、作者信息，不写生成者提炼出的中心论点。
冷静访谈笔记方向下，封面要更像一本严肃笔记的第一页：黑场、居中标题、沉静蓝小标签。不要额外加图片、装饰线、卡片或摘要段落。

**chrome**：必须使用 `bare` 类去掉页眉。封面要有真正的封面气质，不应顶着来源、类型和编号的索引头。
**宽度**：使用 `--w-statement`，让标题、来源标签、副语境形成一个收紧的中心组。

```html
<section class="slide dark hero active bare" data-theme="dark" data-screen-label="Cover" data-source="[标题或来源锚点]" style="text-align:center;align-items:center">
  <div class="slide-body" style="align-items:center">
    <div class="w-statement" style="display:flex;flex-direction:column;align-items:center;gap:clamp(1.4rem,3vh,2.4rem)">
      <div class="kicker anim-item" style="color:var(--accent);opacity:1">[材料类型 / 访谈 / 播客 / 长文]</div>
      <h1 class="display-zh anim-item" style="max-width:9.5em">[主标题]</h1>
      <p class="lead-zh anim-item" style="max-width:24em;opacity:.62">[一句来源语境，不写总结]</p>
    </div>
  </div>
  <div class="foot" style="width:100%">
    <div>[作者 / 嘉宾 / 来源]</div>
    <div>[日期 / 时长 / 字数]</div>
  </div>
</section>
```

## Layout 3：居中观点（四亚型）

用于提出核心判断。强主张是 deck 的节奏点。同一种强主张版式连续出现太多次，读者会把它当成背景。所以 L3 必须分亚型，避免每页都重复 `max-width:11em + h1-zh + 居中`。

一套 25 到 35 页的 deck 里，强主张通常 4 到 6 页，必须使用至少两种亚型。同一种亚型不要连续两页出现。

### Layout 3-a：社论式

用于真正需要抛出的强判断。display-zh 8vw 撑满，**bare 类去掉 chrome**，使用 `--w-statement` 窄容器。整页只有标签、巨标和（可选）一行 attribution。这是最克制也最锋利的版本。

```html
<section class="slide light bare" data-theme="light">
  <div class="slide-body" style="align-items:flex-start">
    <div class="w-statement">
      <div class="kicker anim-item" style="margin-bottom:clamp(1.6rem,4vh,3rem)">[小标签 / 章节]</div>
      <h2 class="display-zh anim-item" style="font-size:clamp(3.2rem,8vw,7.6rem);max-width:11em;letter-spacing:0">
        [一句强主张]
      </h2>
    </div>
  </div>
  <div class="foot" style="width:100%"><div>[说话者或来源]</div><div>[页码]</div></div>
</section>
```

### Layout 3-b：长句式

用于一句必须读完的长判断（中文 18 到 28 字）。容器拉宽到 `--w-default` 或 `max-width:24em`，标题字号降一档（h1-zh），让长句横排撑满，强迫一行读完。**不要再拉成两行**。

```html
<section class="slide dark" data-theme="dark" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%"><div>[语境或来源]</div><div>[页码]</div></div>
  <div class="slide-body" style="align-items:center">
    <h2 class="h1-zh anim-item" style="max-width:24em;font-size:clamp(1.8rem,3.2vw,3rem);line-height:1.35">
      [一句必须读完的长判断，控制在 18 到 28 个中文字符]
    </h2>
  </div>
  <div class="foot" style="width:100%"><div>[说话者或来源]</div><div>[页码]</div></div>
</section>
```

### Layout 3-c：上下宣告

用于带上下文的强主张。三段中线对齐：kicker → 大判断 → 一行注解。容器用 `--w-note`，标题用 `h1-zh`，注解必须真的补足理解，不写空泛的本节讨论之类的话。

```html
<section class="slide dark" data-theme="dark" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%"><div>判断 · [主题]</div><div>[页码]</div></div>
  <div class="slide-body" style="align-items:center">
    <div class="w-note" style="display:flex;flex-direction:column;align-items:center;gap:clamp(1.4rem,3.5vh,2.6rem)">
      <div class="kicker anim-item">[标签 / 转场]</div>
      <h2 class="h1-zh anim-item" style="max-width:13em">[一句短判断，不超过两行]</h2>
      <p class="body-zh anim-item" style="max-width:22em;opacity:.62">[补一行最小必要解释，不要扩成第二页内容]</p>
    </div>
  </div>
  <div class="foot" style="width:100%"><div>[说话者或来源]</div><div>[页码]</div></div>
</section>
```

### Layout 3-d：偏置式

用于打破对称的转场判断。**bare 去掉 chrome**，标题贴左下（`slide-body bottom`），右上保留巨大负空间。

整套 deck 里这种亚型**最多用 1 页**。它是默认垂直居中之外的明确例外，多用就会稀释破对称的语义，反而让整本 deck 显得不稳定。如果 deck 里没有真正的换章节或密集证据之后的视觉换气语境，可以完全不用 L3-d。

```html
<section class="slide dark bare" data-theme="dark">
  <div class="slide-body bottom" style="align-items:flex-start">
    <div class="w-statement">
      <div class="kicker anim-item" style="color:var(--accent);opacity:1;margin-bottom:clamp(1.4rem,3vh,2.4rem)">[小标签]</div>
      <h2 class="h1-zh anim-item" style="max-width:13em">[一句转场判断]</h2>
    </div>
  </div>
  <div class="foot" style="width:100%"><div>[说话者或来源]</div><div>[页码]</div></div>
</section>
```

### L3 通用规则

1. 一套 deck 出现的 L3 强主张必须使用至少两种亚型。
2. 同一种亚型不要连续两页出现。
3. L3-a 和 L3-d 必须使用 `bare` 类去掉 chrome。L3-b 和 L3-c 保留 chrome。
4. L3-a / L3-b / L3-c / L3-d 都不允许在标题之外接三列、表格或长段解释。需要解释就改用 L5、L6 或拆页。
5. 强主张不允许使用 `--w-default` 或 `--w-wide`。这是 deck 的节奏点，必须收窄到 `--w-quote`、`--w-statement` 或 `--w-note`。

## Layout 4：观点加解释

用于补足信息。上方主张，下方三条解释。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <h2 class="h1-zh anim-item section-title">[主张]</h2>
      <div class="grid-3">
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1;margin-bottom:clamp(.7rem,1vh,1rem)">01</div>
          <p class="body-zh">[解释一]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1;margin-bottom:clamp(.7rem,1vh,1rem)">02</div>
          <p class="body-zh">[解释二]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1;margin-bottom:clamp(.7rem,1vh,1rem)">03</div>
          <p class="body-zh">[解释三]</p>
        </div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 5：标题加正文

用于一个判断加一段解释。比居中观点信息量更高。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
    <h2 class="h1-zh anim-item" style="max-width:11em;margin-bottom:clamp(1.2rem,3vh,2.4rem)">[标题]</h2>
    <p class="lead-zh anim-item" style="max-width:24em">[两到四行解释，完成信息闭环]</p>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 6：上下结构

用于先给结论，再给依据。适合信息页。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <div style="text-align:center">
        <div class="kicker anim-item">[标签]</div>
        <h2 class="h1-zh anim-item" style="max-width:12em;margin:0 auto">[上方结论]</h2>
      </div>
      <div class="grid-3">
        <p class="body-zh anim-item">[依据一]</p>
        <p class="body-zh anim-item">[依据二]</p>
        <p class="body-zh anim-item">[依据三]</p>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 7：左右分屏

用于观点加证据。左侧主张，右侧解释、图像或数字。
不要让左右两侧变成同等重量的两个标题。左侧必须是主视线，右侧必须明显退后成为证据层。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div>
      <h2 class="h1-zh anim-item" style="max-width:9em;margin-bottom:clamp(1rem,3vh,2rem)">[标题]</h2>
      <p class="body-zh anim-item" style="max-width:18em">[两到三行解释]</p>
    </div>
    <div class="anim-item" style="padding-left:clamp(1rem,3vw,3rem)">
      <div class="kicker" style="color:var(--accent);opacity:1">[证据标签]</div>
      <p class="lead-zh" style="max-width:16em">[证据或原文语境]</p>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 9：三列要点

用于三原则、三阶段、三类人、三条证据。
前提是每列都有足够信息密度。如果每列只有一句短句，不要用大方块把空白撑得很重。
不要用它承载人物履历句加三个指标。人物基础信息、学历、创业时间、增长数字、产品范围混在一起时，优先拆成时间线、表格或左右分屏。
标题超过两行时，不要再接三列。先把标题压成一句主张，或把履历信息下沉到表格和时间线。
三列里的大号数字必须是同一维度的可比数字，例如收入、年份、人数、比例。不能把 100%、8 年、产品列表这类不同维度并排做成同一种视觉重量。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <h2 class="h1-zh anim-item section-title">[三列主题]</h2>
      <div class="grid-3" style="align-items:start">
        <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">01</div><p class="body-zh" style="margin-top:1vh">[解释一]</p></div>
        <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">02</div><p class="body-zh" style="margin-top:1vh">[解释二]</p></div>
        <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">03</div><p class="body-zh" style="margin-top:1vh">[解释三]</p></div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 10：作者引用

用于引用人物原话。左侧作者，右侧原话和语境。
只放一句最锋利的话。大号原话中文不超过 36 个字，超过就改用 Layout 24 段落摘录，或拆成原话页和解释页。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div class="anim-item">
      <div class="kicker">Speaker</div>
      <h2 class="h1-zh" style="max-width:7em">[作者名]</h2>
      <p class="body-zh" style="max-width:14em;margin-top:clamp(1rem,2vh,2rem);opacity:.65">[身份或语境]</p>
    </div>
    <div class="callout anim-item" style="max-width:15em">
      [一句原话或转述]
      <cite>[来源]</cite>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 11：嘉宾观点

用于访谈中的嘉宾金句。居中呈现观点，底部保留嘉宾身份和语境。
只适合短判断，不适合长段原话。中文超过 36 个字，或视觉上超过三行，就不要用居中大字。

**签章**：必须使用 `guest-mark` 类。标题前一根 4em 1px 短水平细线（accent 65% 透明），是 deck 里嘉宾观点页的视觉指纹。
**chrome**：必须用 `bare` 类去掉页眉。嘉宾观点是沉浸页，不应该顶着 Guest View 和主题的索引头。
**宽度**：使用 `--w-quote`（极窄），让短判断有戏剧性的孤立感。

```html
<section class="slide dark bare" data-theme="dark">
  <div class="slide-body" style="align-items:center;text-align:center">
    <div class="w-quote guest-mark">
      <div class="kicker anim-item" style="margin-bottom:clamp(1rem,2vh,1.6rem)">Guest View</div>
      <h2 class="h1-zh anim-item" style="max-width:12em">
        [嘉宾一句掷地有声的话]
      </h2>
      <p class="body-zh anim-item" style="max-width:22em;margin:clamp(1.6rem,3.5vh,2.6rem) auto 0;opacity:.62">
        [嘉宾名] · [这句话出现的语境]
      </p>
    </div>
  </div>
  <div class="foot" style="width:100%">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 12：大数字加解释

用于一个关键数字或一组强关联数字。
当数字本身是证据核心，默认居中放大。标题负责解释这个数字的意义，正文只补上下文。不要把关键数字放进左右分屏的一侧。
如果一页出现两个以上大数字，必须先确认它们属于同一比较维度。不同维度的数字不要并排放大，改用表格、时间线或拆成多页。
百分比、年份、时长、产品范围不是同一种证据，不能用同一字号排成三列。

```html
<section class="slide light" data-theme="light" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div class="stat-num anim-item">[数字]</div>
    <h2 class="h2-zh anim-item" style="max-width:14em;margin-top:clamp(1rem,2vh,2rem)">[这个数字意味着什么]</h2>
    <p class="body-zh anim-item" style="max-width:22em;margin-top:clamp(.8rem,1.5vh,1.5rem)">[来源或上下文]</p>
  </div>
  <div class="foot" style="width:100%">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 13：前后对比

用于转折。左右两边各不超过三条。
两列都保持左对齐，或整页使用居中标题加下方对比。不要把右列文字右对齐，也不要让右列贴近画面右边界。右侧只是第二组内容，不是页脚。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div style="opacity:.45">
      <div class="kicker anim-item">Before</div>
      <h2 class="h2-zh anim-item" style="margin-bottom:clamp(1rem,2vh,2rem)">[过去]</h2>
      <p class="body-zh anim-item">[解释]</p>
    </div>
    <div>
      <div class="kicker anim-item" style="color:var(--accent);opacity:1">After</div>
      <h2 class="h2-zh anim-item" style="margin-bottom:clamp(1rem,2vh,2rem)">[现在]</h2>
      <p class="body-zh anim-item">[解释]</p>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 14：时间线

用于访谈、历史、项目过程。最多四个节点。

**签章**：使用 `timeline-row` 包裹节点容器，节点本身加 `timeline-node` 类。节点之间会出现一根极淡 1px 水平连接线，是 deck 里时间线页的视觉指纹。这条线全 deck 只属于时间线和文章脉络（L29），其他页型不要使用。
**宽度**：使用 `--w-wide`（92rem），强调时间的展开感。
**基线**：默认垂直居中。整页内容（标题加时间轴）作为一个整体落在画面中段。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="w-wide">
      <h2 class="h1-zh anim-item" style="text-align:center;max-width:13em;margin:0 auto clamp(2rem,5vh,4rem)">[时间线标题]</h2>
      <div class="timeline-row" style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1rem,2vw,2rem)">
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 15：流程图

用于步骤、因果链、方法论。最多五步。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <h2 class="h1-zh anim-item" style="text-align:center;max-width:11em;margin:0 auto clamp(2rem,5vh,4rem)">[流程标题]</h2>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(.8rem,1.5vw,1.5rem);align-items:start">
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">01</div><p class="body-zh" style="margin-top:1vh">[步骤一]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">02</div><p class="body-zh" style="margin-top:1vh">[步骤二]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">03</div><p class="body-zh" style="margin-top:1vh">[步骤三]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">04</div><p class="body-zh" style="margin-top:1vh">[步骤四]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">05</div><p class="body-zh" style="margin-top:1vh">[步骤五]</p></div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 16：表格

用于参数、分类、优先级。表格文字要短。排期、里程碑、任务安排默认使用 Layout 22 排期表。
默认不要通栏。优先把标题和表格作为一个整体收在中间，保持左右留白平衡。
如果每列主要是短标签、短判断、短结论，默认整表内容居中；只有单元格里出现句子级说明、较长语境或需要连续阅读时，才改为左对齐。
表格不用横线网格。默认使用 `data-table`，靠淡底、行距、字号和第一列权重建立秩序。
如果内容带时间但真正要比较的是对象、参数或优先级，可以用普通表格。只要它是日程、里程碑或任务安排，就不要用普通表格临时拼。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="table-wrap">
      <h2 class="h1-zh anim-item" style="text-align:center;max-width:11em;margin:0 auto">[表格标题]</h2>
      <table class="data-table keyed anim-item">
        <thead>
          <tr><th>[列一]</th><th>[列二]</th><th>[列三]</th></tr>
        </thead>
        <tbody>
          <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
          <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
          <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 17：矩阵

用于两个维度下的分类判断。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <h2 class="h1-zh anim-item" style="text-align:center;max-width:11em;margin:0 auto clamp(1.5rem,4vh,3rem)">[矩阵标题]</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:clamp(1rem,2vw,2rem);min-height:45vh">
      <div class="anim-item" style="padding:clamp(1rem,2vw,2rem);background:rgba(255,255,255,.04)"><div class="kicker">[象限一]</div><p class="body-zh" style="margin-top:1vh">[说明]</p></div>
      <div class="anim-item" style="padding:clamp(1rem,2vw,2rem);background:rgba(255,255,255,.04)"><div class="kicker">[象限二]</div><p class="body-zh" style="margin-top:1vh">[说明]</p></div>
      <div class="anim-item" style="padding:clamp(1rem,2vw,2rem);background:rgba(255,255,255,.04)"><div class="kicker">[象限三]</div><p class="body-zh" style="margin-top:1vh">[说明]</p></div>
      <div class="anim-item" style="padding:clamp(1rem,2vw,2rem);background:rgba(var(--accent-rgb),.12)"><div class="kicker" style="color:var(--accent);opacity:1">[象限四]</div><p class="body-zh" style="margin-top:1vh">[说明]</p></div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 18：对话分裂

用于访谈材料。左右两侧分别代表两个人或两种立场。
默认让回答方拿到更大视觉权重。提问方负责把问题抛清楚，不负责和回答方抢舞台。
如果不是两个人或两种立场的张力，不要把引用和结论做成对称分屏。
回答方在右侧时仍然左对齐，不做右对齐。需要强调回答方时，用列宽、字号、颜色和留白，不用把文字推到右边。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center;grid-template-columns:4fr 8fr">
    <div class="anim-item" style="opacity:.7">
      <div class="kicker">[人物 A]</div>
      <p class="body-zh" style="max-width:10em;margin-top:clamp(1rem,2vh,2rem)">[提问或引线]</p>
    </div>
    <div class="anim-item">
      <div class="kicker" style="color:var(--accent);opacity:1">[人物 B]</div>
      <div class="callout" style="max-width:14em;margin-top:clamp(1rem,2vh,2rem)">
        [回应或判断]
        <cite>[语境补充]</cite>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 19：图片网格

用于案例、现场、作品集。每张图必须有语境。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <h2 class="h1-zh anim-item" style="text-align:center;max-width:11em;margin:0 auto clamp(1.5rem,4vh,3rem)">[图片组标题]</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(.8rem,1.5vw,1.5rem)">
      <figure class="slide-img anim-item" style="height:clamp(18vh,24vh,30vh)"><img src="[图片]" alt="[描述]"><figcaption class="img-cap">[说明]</figcaption></figure>
      <figure class="slide-img anim-item" style="height:clamp(18vh,24vh,30vh)"><img src="[图片]" alt="[描述]"><figcaption class="img-cap">[说明]</figcaption></figure>
      <figure class="slide-img anim-item" style="height:clamp(18vh,24vh,30vh)"><img src="[图片]" alt="[描述]"><figcaption class="img-cap">[说明]</figcaption></figure>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 21：结尾回扣

用于收束。居中，回扣开场，不写空泛感谢。
结尾不需要强行写成金句，更重要的是清楚、直接，并能把整套 deck 的判断落下来。
默认优先使用更克制的停留页格式：单一主标题层级即可，不额外悬挂标签或装饰层。
只有当主标题不足以闭环，且补一句确实能显著增强理解时，才允许加一行副说明。
停留页不等于竖向海报。默认保持横向阅读重心，避免为了显得有设计感把结尾标题框收得过窄，或手动插入 `<br>` 造成生硬断句。

**chrome**：使用 `bare` 类去掉页眉。
**宽度**：使用 `--w-statement`，与封面形成对称呼应。

```html
<section class="slide dark hero bare" data-theme="dark">
  <div class="slide-body" style="align-items:center;text-align:center">
    <div class="w-statement">
      <h2 class="h1-zh anim-item" style="max-width:16em;margin:0 auto">[回扣开场的结论]</h2>
    </div>
  </div>
  <div class="foot" style="width:100%">
    <div>[演讲者]</div>
    <div>[结束语]</div>
  </div>
</section>
```

## Layout 22：排期表

用于 schedule、里程碑、拍摄计划、项目安排。它本质是表格，不是时间线。只有当演讲重点是时间流动本身时，才改用时间线。
列语义必须稳定，推荐使用时间、动作、负责人或结果、备注。不要在同一张表里同时塞观点判断、任务描述和长段解释。
三到五行最稳。超过六行必须拆成多页，或者合并为阶段。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div class="table-wrap">
      <div style="text-align:center">
        <div class="kicker anim-item">[排期标签]</div>
        <h2 class="h1-zh anim-item" style="max-width:11em;margin:0 auto">[排期主张]</h2>
      </div>
      <table class="data-table compact keyed anim-item">
        <thead>
          <tr><th>时间</th><th>动作</th><th>负责人或结果</th><th>备注</th></tr>
        </thead>
        <tbody>
          <tr><td>[时间]</td><td>[动作]</td><td>[结果]</td><td>[备注]</td></tr>
          <tr><td>[时间]</td><td>[动作]</td><td>[结果]</td><td>[备注]</td></tr>
          <tr><td>[时间]</td><td>[动作]</td><td>[结果]</td><td>[备注]</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```
