# zettelkasten-notes

[English](README.md) | 中文 · [Research Skillbox 总导航](https://github.com/windyvictor/research-skillbox)

> 将阅读、听课和研究中的材料转化为可复用卡片，并用真实连接支持写作与思考。

## 一句话定位

面向个人知识库的卡片写作、连接、审阅和体检技能。它支持闪念笔记、文献笔记、永久笔记、项目笔记及 AI 草稿协作，并以实际复用效果衡量笔记质量。

## 你会得到什么

- 忠于来源的闪念、文献、永久或项目卡片草稿
- 明确说明支持、反驳、延伸或应用关系的真实连接
- AI 候选卡从草稿到人审的清晰状态
- 从已有卡片长出的段落、提纲或文章结构
- 对断链、重复标题、长期草稿和人审状态的只读体检

工作路径是：**保留来源 → 用自己的话写出一个可复用想法 → 寻找并解释真实连接 → 不确定内容保持草稿 → 在写作中复用**。卡片盒的价值不在数量，而在未来能否重新参与思考。

## 何时使用

- 把阅读、课程、对话或 AI 问答整理为卡片
- 审查卡片是否自足、忠于来源并适合复用
- 连接卡片、处理相互冲突的旧结论
- 从已有卡片形成文章或论文段落
- 对笔记库做只读体检，检查断链、重复和草稿状态

单篇论文的深度精读不由本技能负责；用户要求把精读结果保存为卡片时，再使用本技能处理入库。

## 内容结构

- `SKILL.md`：任务路由、写入边界和完成条件
- `references/`：卡片写作、连接、输出和 AI 协作方法
- `assets/`：卡片、知识库规则和复查日志模板
- `scripts/`：单卡检查和知识库只读体检
- `evals/`：触发测试、任务案例和样例知识库
- `tests/`：检查器回归测试

## 基本原则

卡片先忠于来源，再追求表达流畅。AI 生成内容保持草稿状态，经过人审后才能升级。没有合适旧卡时可以保留无连接草稿，不为数量、标签或图谱外观制造弱连接。

## 快速检查

```bash
python3 scripts/check_card.py card.md
python3 scripts/lint_vault.py /path/to/vault
python3 -m unittest discover -s tests -v
```

检查结果只提供机械线索。作者归因、上下文指代、卡片长度和连接质量仍需结合语义判断。

## 安装

```bash
git clone https://github.com/windyvictor/zettelkasten-notes.git
ln -s "$PWD/zettelkasten-notes" ~/.agents/skills/zettelkasten-notes
```

其他宿主请把仓库放入对应的 skills 目录。写入个人知识库前，请先确认目标路径和写入范围。

## 许可

本项目采用 MIT License。参考资料中的第三方观点、引文和原始材料仍归各自作者及权利人所有。
