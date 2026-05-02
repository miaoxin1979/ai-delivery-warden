# AI Delivery Warden

**AI 交付监工 / 防糊弄验收工具。**

这个工具的作用很简单：当 AI 说“我做完了”，你先别急着信，把它的交付说明丢给 `warden` 检查一遍。

它会帮你看：

- 有没有读项目
- 有没有验收标准
- 有没有验证命令和验证结果
- 有没有真实 API / 数据库 / 数据流
- 有没有 mock / 假页面 / 假按钮
- 有没有擅自分期，比如“第一期”“后续再接”
- 有没有交接太粗
- 有没有备份和回滚方案
- 有没有“应该可以”“理论上没问题”这种没证据的自信

一句话：

> 没有证据，不算交付。

## 安装

```bash
git clone https://github.com/miaoxin1979/ai-delivery-warden.git
cd ai-delivery-warden
python3 -m pip install -e .
```

如果你不想安装，也可以直接在项目目录里运行：

```bash
python3 -m ai_delivery_warden.cli examples/bad_delivery_zh.md --lang zh
```

## 怎么用

检查一个 AI 交付说明：

```bash
warden examples/bad_delivery_zh.md --lang zh
```

检查英文示例：

```bash
warden examples/bad_delivery.md
```

把 AI 回复复制成一个文件，比如 `delivery.md`，然后运行：

```bash
warden delivery.md --lang zh
```

如果当前目录是 git 项目，还可以连 git diff 一起检查：

```bash
warden delivery.md --git-diff --lang zh
```

输出报告到文件：

```bash
warden delivery.md --lang zh -o warden-report.md
```

## 你实际怎么用

1. 让 AI 干活。
2. AI 说完成。
3. 把 AI 的交付说明保存成 `delivery.md`。
4. 跑：

```bash
warden delivery.md --lang zh
```

5. 如果状态是 `BLOCK`，把报告里的“可直接贴回 AI 的返工口令”复制给 AI。
6. 让 AI 返工后再跑一遍。

## 示例

坏交付：

```bash
warden examples/bad_delivery_zh.md --lang zh
```

好交付：

```bash
warden examples/good_delivery_zh.md --lang zh
```

## 状态含义

- `PASS`：当前规则没发现阻塞问题。
- `NEEDS_WORK`：有问题，需要补充。
- `BLOCK`：存在关键问题，不建议接受交付。

## 注意

这是一个 MVP，不是万能审计工具。

它最适合检查 AI 的交付说明、交接说明和 git diff 里有没有明显糊弄风险。真正的测试、运行、截图、接口调用，后续可以继续增强。

