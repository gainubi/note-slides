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

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[来源或篇名]</div>
    <div>[页码]</div>
  </div>
  <div class="grid-2-6-6" style="flex:1;min-height:0;align-items:center">
    <div class="anim-item">
      <div class="kicker">Excerpt</div>
      <div class="callout" style="max-width:14em;color:var(--ink);background:rgba(var(--ink-rgb),.05)">
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

```html
<section class="slide dark" data-theme="dark">
  <div class="chrome">
    <div>[来源或段落编号]</div>
    <div>[页码]</div>
  </div>
  <div class="slide-body">
    <div class="note-stack">
      <h2 class="h1-zh anim-item section-title">[这一段最值得记的一句话]</h2>
      <div class="grid-3">
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Fact</div>
          <p class="body-zh">[这一段先讲了什么事实或场景]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Point</div>
          <p class="body-zh">[真正推进理解的重点]</p>
        </div>
        <div class="anim-item">
          <div class="meta" style="color:var(--accent);opacity:1">Aftertaste</div>
          <p class="body-zh">[它为什么会留在读者脑子里]</p>
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

```html
<section class="slide dark" data-theme="dark" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[说话者或来源]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div class="callout anim-item" style="max-width:16em">
      [一句原话]
      <cite>[说话者] · [语境]</cite>
    </div>
    <div class="grid-3" style="width:min(100%,72rem);margin-top:clamp(2rem,4vh,3rem);text-align:left">
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">回应</div><p class="body-zh">[它回应了哪个问题]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">重点</div><p class="body-zh">[它真正推进了什么理解]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">余味</div><p class="body-zh">[为什么这句话会留下来]</p></div>
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

```html
<section class="slide light" data-theme="light">
  <div class="chrome">
    <div>[篇名或主题]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <h2 class="h1-zh anim-item" style="text-align:center;max-width:11em;margin:0 auto clamp(2rem,4vh,3.5rem)">[这篇材料是怎么往前推进的]</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1rem,2vw,2rem)">
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">起点</div><p class="body-zh">[从哪里进入]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">展开</div><p class="body-zh">[重点怎么被打开]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">转折</div><p class="body-zh">[哪里发生变化]</p></div>
      <div class="anim-item"><div class="meta" style="color:var(--accent);opacity:1">落点</div><p class="body-zh">[最后停在哪里]</p></div>
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

```html
<section class="slide light" data-theme="light" style="text-align:center;align-items:center">
  <div class="chrome" style="width:100%">
    <div>[来源或主题]</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div class="kicker anim-item">Open Questions</div>
    <h2 class="h1-zh anim-item" style="max-width:10em;margin-top:clamp(1rem,3vh,2rem)">[材料停下来的地方]</h2>
    <div style="margin-top:clamp(2rem,4vh,3rem);display:grid;gap:clamp(.8rem,1.5vh,1.2rem);text-align:left;width:min(100%,32rem)">
      <p class="body-zh anim-item">01 [还没被回答的问题]</p>
      <p class="body-zh anim-item">02 [后续值得追的线索]</p>
      <p class="body-zh anim-item">03 [观众会继续带着走的问题]</p>
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

```html
<section class="slide dark" data-theme="dark" data-screen-label="Summary" data-source="[核心总结编号范围]">
  <div class="chrome">
    <div>核心总结</div>
    <div>[页码]</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div style="width:min(100%,68rem);margin:0 auto;display:flex;flex-direction:column;gap:clamp(2rem,5vh,3.5rem)">
      <div class="anim-item" style="display:grid;grid-template-columns:auto 1fr;gap:clamp(1.5rem,3vw,3rem);align-items:start">
        <div style="font-family:var(--mono);font-size:clamp(2.5rem,5vw,5rem);font-weight:600;color:var(--accent);line-height:1">01</div>
        <p class="body-zh">[一条具体、有获得感、能回到材料锚点的长笔记。优先写嘉宾的判断、机制、例子和数字，不写评论]</p>
      </div>
      <div class="anim-item" style="display:grid;grid-template-columns:auto 1fr;gap:clamp(1.5rem,3vw,3rem);align-items:start">
        <div style="font-family:var(--mono);font-size:clamp(2.5rem,5vw,5rem);font-weight:600;color:var(--accent);line-height:1">02</div>
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
