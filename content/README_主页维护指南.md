# 🌐 个人主页维护与发布指南 (Obsidian Workflow)

欢迎使用 Obsidian 维护个人学术主页！你的主页源码与内容现已全面集成至 `PhD Demo` 工作区及 Obsidian Vault 中。

---

## 📁 目录结构说明

你在 Obsidian 中看到此文档时，主页的所有 MD 文章内容均实时映射在目录 `06_个人主页_Homepage` 下：

- **`06_个人主页_Homepage/about/_index.md`**：关于我 (About Me, 毕业院校、研究方向、个人简介)
- **`06_个人主页_Homepage/research/_index.md`**：研究方向 (Research Focus & Topology Engineering)
- **`06_个人主页_Homepage/publications/_index.md`**：学术论文与发表列表 (Publications)
- **`06_个人主页_Homepage/news/_index.md`**：学术动态与博客 (News & Blog)
- **`06_个人主页_Homepage/cv/_index.md`**：个人简历相关配置 (CV)

---

## ✏️ 如何在 Obsidian 中更新主页

1. **直接编辑文章**：
   - 打开 `06_个人主页_Homepage` 文件夹下的任意 `.md` 文件。
   - 直接修改文本、添加新的论文、课题或 News 动态。
   - 保留文件开头的 Frontmatter（即 `--- title: "xxx" ---` 部分）。

2. **添加简历或图片**：
   - PDF 简历文件存放于 `academic-homepage/static/files/CV.pdf`
   - 头像与 Banner 图片存放于 `academic-homepage/static/images/`

---

## 🚀 编译预览与发布到 GitHub Pages

在终端或使用 Python 脚本均可一键完成编译发布：

### 1. 本地编译测试 (Preview)
在终端运行：
```bash
python3 "/Users/gyc/PhD Demo/academic-homepage/build_and_publish.py"
```
或者直接使用 Hugo：
```bash
cd "/Users/gyc/PhD Demo/academic-homepage"
hugo server -D
```

### 2. 一键发布更新 (Publish to GitHub Pages)
当你修改完 Markdown 笔记，想要更新在线网站（`https://guo-yu-chao.github.io/`）时，只需运行：
```bash
python3 "/Users/gyc/PhD Demo/academic-homepage/build_and_publish.py" --deploy "更新了 Publications 和 News"
```

---

> ✨ **提示**：如果需要更新网站主题样式，样式文件位于 `academic-homepage/static/css/extended.css`。
