# Mingxia Qin · E-Portfolio

个人作品集网站（静态站点，零外部依赖，可独立运行）。

## 页面结构

| 文件 | 说明 |
|------|------|
| `index.html` | 首页：个人介绍 + 三大模块概览（点击可跳转模块页） |
| `modules.html` | 模块列表页：Module 1–3 及其单元详情（纯 CSS 手风琴，无 JS） |
| `about.html` | 自我介绍页：个人故事 + 专业总结 + 职业时间线 |

## 目录

```
E-portfolio/
├─ index.html
├─ modules.html
├─ about.html
├─ module1/             # Module 1 各 Unit 课程作业总结（unit1.md ~ unit12.md，从 modules.html 单元卡可跳转）
├─ images/              # 所有素材图（已统一英文命名）
├─ vendor/              # 本地化依赖（必须随站一起上传）
│  ├─ bootstrap/        # Bootstrap 5.3.3 CSS + JS
│  ├─ font-awesome/     # Font Awesome 6.5.1 CSS + webfonts
│  └─ fonts/            # Google Fonts(Poppins/Quicksand) 本地 woff2
├─ .gitignore
└─ README.md
```

> ⚠️ `vendor/`、`images/` 与 `module1/` 是网站运行/浏览必需的，上传时不要漏掉。

## 本地运行（两种方式任选）

**方式 A：直接打开**
双击 `index.html` 用浏览器打开即可（所有资源都是相对路径，无需联网）。

**方式 B：本地服务器（推荐，行为最接近线上）**
在项目根目录执行：

```bash
# Python 3
python -m http.server 8000
# 然后浏览器访问 http://127.0.0.1:8000/
```

## 上传到 GitHub

仓库已在本地初始化并完成首次提交。按以下步骤推送到你的 GitHub 即可：

```bash
# 1. 在 GitHub 新建一个空仓库（不要勾选 README/.gitignore）
# 2. 把下面两行替换成你自己的仓库地址，然后执行：
git remote add origin https://github.com/你的用户名/仓库名.git
git branch -M main
git push -u origin main
```

### 开启 GitHub Pages（让网页有公开网址）

1. 仓库页面 → **Settings → Pages**
2. Source 选 **Deploy from a branch**，Branch 选 **main**，目录选 **/ (root)**
3. 保存后几秒，访问 `https://你的用户名.github.io/仓库名/` 即可看到网站

## 技术说明

- 样式与脚本全部本地化（`vendor/`），**无任何 CDN / 外链**，断网也能跑
- 动效均为纯 CSS（`@keyframes` + `animation-timeline: view()` 滚动入场），无 JavaScript 逻辑依赖
- 字体：Poppins（正文/标题）+ Quicksand（圆润辅助），已本地化
- 图标：Font Awesome 6.5.1
