# 通用骨架

适合大多数 deck 的基础演讲动作：封面、解释、对比、引用、时间、收束。

## Layout 1：封面宣告

用于开场。封面结构固定，视觉变量按材料气质调整。
第一眼看标题，第二眼看来源，第三眼看材料语境。副标题只写来源语境，例如时长、文章类型、访谈对象、作者信息，不写生成者提炼出的中心论点。
冷静访谈笔记方向下，封面要更像一本严肃笔记的第一页：黑场、居中标题、清蓝小标签、上下 chrome。不要额外加图片、装饰线、卡片或摘要段落。

```html
<section class="slide dark hero active" data-theme="dark" data-screen-label="Cover" data-source="[标题或来源锚点]" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[来源 / 栏目 / 作者]</div>
    <div>NOTE SLIDES</div>
  </div>

  <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:translateY(-2vh)">
    <div class="kicker anim-item" style="color:var(--accent);opacity:1">[材料类型 / 访谈 / 播客 / 长文]</div>
    <h1 class="display-zh anim-item" style="max-width:9.5em;margin-top:clamp(1rem,2vh,1.8rem)">
      [主标题]
    </h1>
    <p class="lead-zh anim-item" style="max-width:24em;margin-top:clamp(1.2rem,3vh,2.4rem);opacity:.68">[一句来源语境，不写总结]</p>
  </div>

  <div class="foot" style="width:100%">
    <div>[作者 / 嘉宾 / 来源]</div>
    <div>[日期 / 时长 / 字数]</div>
  </div>
</section>
```

## Layout 3：居中观点

用于提出核心判断。适合强主张。

```html
<section class="slide light" data-theme="light" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;align-items:center;justify-content:center">
    <h2 class="h1-zh anim-item" style="max-width:11em">
      [一句话观点]
    </h2>
  </div>
  <div class="foot" style="width:100%">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

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

```html
<section class="slide dark" data-theme="dark" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div class="kicker anim-item">Guest View</div>
    <h2 class="h1-zh anim-item" style="max-width:12em;margin-top:clamp(1rem,3vh,2.5rem)">
      [嘉宾一句掷地有声的话]
    </h2>
    <p class="body-zh anim-item" style="max-width:22em;margin-top:clamp(1rem,3vh,2.5rem);opacity:.65">
      [嘉宾名] · [这句话出现的语境]
    </p>
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

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[语境或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <h2 class="h1-zh anim-item" style="max-width:10em;margin-bottom:clamp(2rem,5vh,4rem)">[时间线标题]</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1rem,2vw,2rem)">
      <div class="anim-item" style="padding-top:clamp(.5rem,1vh,1rem)"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
      <div class="anim-item" style="padding-top:clamp(.5rem,1vh,1rem)"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
      <div class="anim-item" style="padding-top:clamp(.5rem,1vh,1rem)"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
      <div class="anim-item" style="padding-top:clamp(.5rem,1vh,1rem)"><div class="meta" style="color:var(--accent);opacity:1">[时间]</div><p class="body-zh" style="margin-top:1vh">[事件]</p></div>
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
结尾不需要强行写成"金句"，更重要的是清楚、直接，并能把整套 deck 的判断落下来。
默认优先使用更克制的停留页格式：单一主标题层级即可，不额外悬挂标签或装饰层。
只有当主标题不足以闭环，且补一句确实能显著增强理解时，才允许加一行副说明。
停留页不等于竖向海报。默认保持横向阅读重心，避免为了"有设计感"把结尾标题框收得过窄，或手动插入 `<br>` 造成生硬断句。

```html
<section class="slide dark hero" data-theme="dark" style="text-align:center;align-items:center">
  <div style="flex:1;display:flex;align-items:center;justify-content:center">
    <div style="max-width:16em;text-align:center">
      <h2 class="h1-zh anim-item">[回扣开场的结论]</h2>
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
