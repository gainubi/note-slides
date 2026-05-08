# 笔记型骨架

适合播客复盘、长文章、人物稿、深度报道。重点不是宣告观点，而是把读者真正会记下来的重点、句子、线索和证据排出来。

**note-slides 默认从这个文件挑骨架。** 通用骨架（`layouts-general.md`）在补节奏时回去取。

## Layout 23：界面证据

用于产品 UI、系统方案、工具链、开发者叙事。左侧讲清主张和三个证据点，右侧放真实界面截图、产品面板或低调占位。
这类页面适合深界面编辑方向。不要模仿具体品牌页面，只借用黑场、索引、证据列表和界面截图的叙事方式。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[场景标签] · [证据主题]</div>
    <div>[页码]</div>
  </div>
  <div class="interface-grid">
    <div>
      <div class="kicker anim-item">[小标签]</div>
      <h2 class="display-zh anim-item" style="font-size:clamp(3rem,6.2vw,6rem);max-width:9em;margin-bottom:clamp(2rem,5vh,4rem)">[核心主张]</h2>
      <p class="lead-zh anim-item" style="max-width:24em;color:rgba(var(--paper-rgb),.78);margin-bottom:clamp(1.4rem,3vh,2.4rem)">[两到三行解释，说明右侧界面为什么是证据]</p>
      <div class="evidence-list anim-item">
        <div class="evidence-row"><strong>[标签一]</strong><p>[证据解释]</p><span>[状态]</span></div>
        <div class="evidence-row"><strong>[标签二]</strong><p>[证据解释]</p><span>[状态]</span></div>
        <div class="evidence-row"><strong>[标签三]</strong><p>[证据解释]</p><span>[状态]</span></div>
      </div>
    </div>
    <figure class="interface-shot anim-item">
      <div class="interface-placeholder">[界面证据占位]</div>
    </figure>
  </div>
  <div class="foot">
    <div>[来源或测试语境]</div>
    <div>[页码]</div>
  </div>
</section>
```

## Layout 24：原文摘录加侧注

用于长文章、访谈整理、播客逐字稿。左边放一句原文或一小段摘录，右边放读者侧注、语境说明或一句拆解。
它比普通引用页更像读书笔记，不负责制造气势，负责保留原句和阅读痕迹。
如果摘录超过 36 个中文字符，必须使用这个降级版式或拆页，不要把长摘录放成居中大号原话。

**签章**：必须在 callout 上加 `callout-mark` 类。它会去掉原本的左侧蓝条，改成 callout 上方一个 6mm 实心小方块，是 deck 里摘录页的视觉指纹。
**chrome**：保留，写明 Excerpt · 主题用于索引。
**宽度**：保持 `grid-2-6-6` 默认 76rem，但左侧 callout 不超过 14em，右侧侧注不超过 18em，让中间的留白成为两块内容的呼吸。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[来源或篇名]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div class="anim-item">
      <div class="kicker">Excerpt</div>
      <div class="callout callout-mark" style="max-width:14em;color:var(--ink);margin-top:clamp(1rem,2vh,1.6rem)">
        [原文摘录]
        <cite>[段落或语境]</cite>
      </div>
    </div>
    <div class="anim-item" style="padding-left:clamp(1rem,3vw,3rem)">
      <div class="kicker" style="color:var(--accent);opacity:1">Side Note</div>
      <p class="lead-zh" style="max-width:18em">[这句话为什么值得记]</p>
      <p class="body-zh" style="max-width:18em;margin-top:clamp(1rem,2vh,1.6rem)">[补一条最小必要语境]</p>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 25：段落拆解

用于一段高密度文字。上面放段落重点，下面拆成三层，例如事实、重点、余味。
适合人物稿、评论文、长访谈和深度报道。

**基线**：默认垂直居中。整页内容（标题加三列拆解）作为一个整体落在画面中段，标题在内容组上方，三列拆解在标题下方。不要让标题孤立漂在顶部。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[来源或段落编号]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <h2 class="h1-zh anim-item" style="max-width:13em">[这一段最值得记的一句话]</h2>
      <div class="grid-3">
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Fact</div>
          <p class="body-zh" style="margin-top:1vh">[这一段先讲了什么事实或场景]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Point</div>
          <p class="body-zh" style="margin-top:1vh">[真正推进理解的重点]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Aftertaste</div>
          <p class="body-zh" style="margin-top:1vh">[它为什么会留在读者脑子里]</p>
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

## Layout 26：线索词追踪

用于反复出现的关键词。把一个词在不同位置的含义并排呈现出来。
适合播客复盘，也适合长文章。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[来源或主题]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <div style="text-align:center">
        <div class="kicker anim-item">Keyword Trace</div>
        <h2 class="display-zh anim-item" style="font-size:clamp(3rem,6vw,5.6rem)">[线索词]</h2>
      </div>
      <div class="grid-3">
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">第一次出现</div>
          <p class="body-zh">[它在这里是什么意思]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">中段变化</div>
          <p class="body-zh">[含义或语气怎么变了]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">最后落点</div>
          <p class="body-zh">[这个词最后落在哪个重点上]</p>
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

## Layout 27：观点加例证

用于一个重点配两个或三个具体例子。它比观点加解释更实，更适合长文章和复盘材料。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[来源或主题]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <h2 class="h1-zh anim-item section-title">[这一页的重点]</h2>
      <div class="grid-3">
        <div class="anim-item">
          <div class="kicker">例子一</div>
          <p class="body-zh">[一个具体例子或场景]</p>
        </div>
        <div class="anim-item">
          <div class="kicker">例子二</div>
          <p class="body-zh">[一个具体例子或场景]</p>
        </div>
        <div class="anim-item">
          <div class="kicker">例子三</div>
          <p class="body-zh">[一个具体例子或场景]</p>
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

## Layout 28:一句原话，多层注解

用于一句特别值得停下来的原话。上面给原话，下面拆三层注解。
适合播客、人物访谈和评论文章。
原话必须短，中文不超过 28 个字。超过 28 个字时，不要再接三层注解，改用 Layout 24 或拆成两页。

**签章**：在 callout 上使用 `callout-mark` 类（与 L24 复用同一指纹）。上方 6mm 小方块替代左侧蓝条。
**chrome**：使用 `bare` 类去掉页眉。沉浸式原话页不应顶着索引头。
**宽度**：原话 callout 用 `--w-quote`，下方三列注解用 `--w-default`，形成上窄下宽的呼应。

```html
<section class="slide dark bare" data-theme="dark" style="text-align:center">
  <div class="slide-body" style="align-items:center">
    <div class="w-quote">
      <div class="callout callout-mark anim-item" style="max-width:16em;margin:0 auto;text-align:left">
        [一句原话]
        <cite>[说话者] · [语境]</cite>
      </div>
    </div>
    <div class="w-default" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:clamp(.8rem,2vw,2rem);margin-top:clamp(2rem,4vh,3rem);text-align:left">
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">回应</div><p class="body-zh" style="margin-top:1vh">[它回应了哪个问题]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">重点</div><p class="body-zh" style="margin-top:1vh">[它真正推进了什么理解]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">余味</div><p class="body-zh" style="margin-top:1vh">[为什么这句话会留下来]</p></div>
    </div>
  </div>
  <div class="foot" style="width:100%">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 29:文章脉络

不是目录页。用于交代一篇长文章或一段长谈是如何往前推进的。
重点是帮助观众理解推进顺序，不是展示章节名。

**签章**：使用 `timeline-row thick` 包裹起点→落点四节点，节点加 `timeline-node` 类。节点之间会出现一根 1.5px 的连接线（比 L14 时间线略粗一档），强调脉络的连续推进。
**宽度**：使用 `--w-wide`，让起点和落点之间真的有展开感。
**基线**：默认垂直居中。

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[篇名或主题]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="w-wide">
      <h2 class="h1-zh anim-item" style="text-align:center;max-width:13em;margin:0 auto clamp(2rem,4vh,3.5rem)">[这篇材料是怎么往前推进的]</h2>
      <div class="timeline-row thick" style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1rem,2vw,2rem)">
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">起点</div><p class="body-zh" style="margin-top:1vh">[从哪里进入]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">展开</div><p class="body-zh" style="margin-top:1vh">[重点怎么被打开]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">转折</div><p class="body-zh" style="margin-top:1vh">[哪里发生变化]</p></div>
        <div class="timeline-node anim-item"><div class="meta" style="color:var(--accent);opacity:1">落点</div><p class="body-zh" style="margin-top:1vh">[最后停在哪里]</p></div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 30:双张力

用于两个同时成立、互相拉扯的重点。它不是 before after，而是两股力量同时在场。

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[来源或主题]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div class="anim-item">
      <div class="kicker">Tension A</div>
      <h2 class="h2-zh" style="margin-bottom:clamp(1rem,2vh,2rem)">[第一股力量]</h2>
      <p class="body-zh" style="max-width:15em">[它为什么成立]</p>
    </div>
    <div class="anim-item">
      <div class="kicker" style="color:var(--accent);opacity:1">Tension B</div>
      <h2 class="h2-zh" style="margin-bottom:clamp(1rem,2vh,2rem)">[第二股力量]</h2>
      <p class="body-zh" style="max-width:15em">[它为什么也成立]</p>
    </div>
  </div>
  <div class="foot">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 31:未解问题

用于材料最后留下的问题、悬而未决的地方、下一步值得继续看的方向。
它不是总结页，也不负责上价值。

**chrome**：使用 `bare` 类去掉页眉。这是 deck 收束前的沉浸页，不应顶着来源和编号的索引头。
**宽度**：使用 `--w-quote`，让悬而未决的问题真的有留白等待的感觉。

```html
<section class="slide light bare" data-theme="light">
  <div class="slide-body" style="align-items:center;text-align:center">
    <div class="w-quote">
      <div class="kicker anim-item">Open Questions</div>
      <h2 class="h1-zh anim-item" style="max-width:10em;margin:clamp(1rem,3vh,2rem) auto 0">[材料停下来的地方]</h2>
      <div style="margin-top:clamp(2rem,4vh,3rem);display:grid;gap:clamp(.8rem,1.5vh,1.2rem);text-align:left">
        <p class="body-zh anim-item">01 [还没被回答的问题]</p>
        <p class="body-zh anim-item">02 [后续值得追的线索]</p>
        <p class="body-zh anim-item">03 [观众会继续带着走的问题]</p>
      </div>
    </div>
  </div>
  <div class="foot" style="width:100%">
    <div>[页脚左]</div>
    <div>[页脚右]</div>
  </div>
</section>
```

## Layout 32:核心总结

用于 deck 结尾的高获得感笔记页。每页放二到四条，不写目录，不写口号，不加评论。每条都要来自材料里的具体观点、数字、例子或方法。
默认使用深色页、大号编号和长段笔记。这个版式适合承载用户要的范文式总结：每条有细节、有获得感、好理解，核心放在嘉宾观点上。不要额外加卡片、边框、引号和装饰图形。

**签章**：编号必须使用 `summary-num` 类。衬线粗体、字号 7vw、accent 色。原模板用等宽字 5vw 让编号变成列表序号，新签章把编号提到衬线粗体大字号，让它成为页面构成元素，是 deck 里核心总结页的视觉指纹。
**chrome**：简化为只写核心总结 N/M，不再写主题，让连续 3 到 5 页的总结视觉上是一组而不是各自独立的目录页。
**宽度**：使用 `--w-default`。

```html
<section class="slide dark" data-theme="dark" data-screen-label="Summary" data-source="[核心总结编号范围]">
  <div class="chrome">
    <div>核心总结</div>
    <div>[页码] / [总页数]</div>
  </div>
  <div class="slide-body">
    <div class="w-default" style="display:flex;flex-direction:column;gap:clamp(2rem,5vh,3.5rem)">
      <div class="anim-item" style="display:grid;grid-template-columns:auto 1fr;gap:clamp(1.5rem,3vw,3rem);align-items:start">
        <div class="summary-num">01</div>
        <p class="body-zh">[一条具体、有获得感、能回到材料锚点的长笔记。优先写嘉宾的判断、机制、例子和数字，不写评论]</p>
      </div>
      <div class="anim-item" style="display:grid;grid-template-columns:auto 1fr;gap:clamp(1.5rem,3vw,3rem);align-items:start">
        <div class="summary-num">02</div>
        <p class="body-zh">[一条具体、有获得感、能回到材料锚点的长笔记。优先写嘉宾的判断、机制、例子和数字，不写评论]</p>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>[来源或栏目]</div>
    <div>[页脚右]</div>
  </div>
</section>
```
