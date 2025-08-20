# 🔍 ClickerSubdomain - 高级子域名智能抓取工具

![image-20250820113306153](https://s1.vika.cn/space/2025/08/20/bd8076a6e7c849d6ac44bcc90a5dd7e4)

<div align="center"><p>🚀 精准、高效的子域名提取与关键词过滤解决方案 🚀</p><div><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python版本"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="许可证"><img src="https://img.shields.io/badge/Browser-Edge-orange.svg" alt="依赖浏览器"><img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="项目状态"></div></div>

------

## 👨‍💻 作者信息

- **作者**：一只鱼（Bifish）
- **GitHub**：https://github.com/Bifish0
- **工具名称**：ClickerSubdomain

------

## 📖 工具简介

ClickerSubdomain 是一款由一只鱼（Bifish）开发的基于 Python 和 Selenium 的子域名抓取工具，专为网络安全测试、域名资产梳理场景设计。它能实时监控网页变化，自动提取页面中的子域名并按关键词过滤，同时通过颜色编码区分域名级别，让子域名资产收集更高效、更精准。

![image-20250820113216904](https://s1.vika.cn/space/2025/08/20/f8a44a24b5c8458ea6af3a1d3afa8fd6)

无论是手动浏览目标网站，还是监控动态加载页面，工具都能自动捕捉新出现的子域名，且支持灵活的暂停 / 继续控制，兼顾易用性与功能性。

------

## ✨ 核心功能

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 2rem 0;"><div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🕷️ 自动子域名提取</h3><p>从网页内容中智能识别并提取子域名，自动过滤IP地址和无效格式，确保结果有效性</p></div>




<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🔤 关键词精准过滤</h3><p>支持多关键词（英文逗号分隔）过滤，仅保留包含目标关键词的子域名，减少无效数据</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🎨 彩色级别标识</h3><p>按域名级别（二级/三级/四级及以上）用不同颜色区分，关键词高亮显示，视觉识别更直观</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🔄 实时页面监控</h3><p>持续检测页面URL和内容变化，手动翻页或动态加载后自动抓取新出现的子域名</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>⌨️ 快捷键控制</h3><p>支持暂停/继续（Ctrl+Alt+P）、强制退出（Ctrl+C），操作灵活不中断浏览流程</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>💾 自动结果保存</h3><p>实时将唯一子域名保存到 result.txt 文件，按字母排序，防止数据丢失，便于后续分析</p></div></div>

------

## ⌨️ 快捷键说明

| 快捷键       | 功能            | 备注                           |
| ------------ | --------------- | ------------------------------ |
| `Ctrl+Alt+P` | 暂停 / 恢复抓取 | 切换抓取状态，不中断浏览器进程 |
| `Ctrl+C`     | 强制退出程序    | 关闭浏览器并保存最终结果       |

------

## 📋 环境要求

| 依赖项     | 说明                   | 备注                                         |
| ---------- | ---------------------- | -------------------------------------------- |
| Python     | 3.x 及以上版本         | 推荐 Python 3.8+                             |
| 浏览器     | Microsoft Edge         | 需与 EdgeDriver 版本匹配                     |
| EdgeDriver | 对应 Edge 浏览器版本   | 需命名为 `msedgedriver.exe` 并放在程序同目录 |
| 依赖库     | `selenium`、`keyboard` | 用于浏览器自动化和快捷键监听                 |

------

## 🛠️ 安装步骤

1. **获取工具代码**
   从 GitHub 仓库克隆或下载 ClickerSubdomain.py 到本地目录：

   ```bash
   git clone https://github.com/Bifish0/ClickerSubdomain.git
   cd ClickerSubdomain
   ```

2. **安装依赖库**
   打开终端执行以下命令，安装所需 Python 库：

   ```bash
   pip install selenium keyboard
   ```

3. **配置 EdgeDriver**

   - 查看本地 Edge 浏览器版本（打开 Edge → 设置 → 关于 Microsoft Edge）；
   - 下载对应版本的 EdgeDriver：[微软官方下载地址](https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/)；
   - 将下载的 EdgeDriver 重命名为 `msedgedriver.exe`，放在与 ClickerSubdomain.py 相同的目录下。

------

## 📝 详细使用教程

### 1. 基础运行流程

1. **启动工具**
   在终端进入程序目录，执行命令：

   ```bash
   python ClickerSubdomain.py
   ```

2. **输入目标信息**

   - 第一步：输入要抓取的网址（支持 `http://`/`https://` 前缀，若未输入将自动补充 `http://`）
     示例：输入 `example.com` → 工具自动处理为 `http://example.com`
   - 第二步：输入关键词（多个关键词用英文逗号分隔，为空则抓取所有子域名）
     示例 1：输入 `mail,admin` → 仅抓取包含 "mail" 或 "admin" 的子域名
     示例 2：直接回车 → 抓取所有识别到的子域名

3. **开始抓取**
   工具将自动启动 Edge 浏览器并打开目标网址，同时：

   - 首次加载完成后，自动提取当前页面的子域名并过滤；
   - 手动在浏览器中翻页、点击链接，工具会实时检测页面变化并抓取新子域名；
   - 所有结果实时保存到 `result.txt` 文件（程序目录下）。

### 2. 核心操作演示

```plaintext
# 终端交互示例
--------------------------------------------------------------------------------
🔍 子域名抓取工具 (带关键词过滤)
 📌 作者：一只鱼（Bifish）
 📌 功能：自动抓取包含指定关键词的子域名，支持手动翻页和快捷键控制
 📌 快捷键：Ctrl+Alt+P (暂停/开始) | Ctrl+C (退出)
--------------------------------------------------------------------------------

请输入要打开的网址: example.com
请输入关键词（多个关键词用英文逗号分隔，为空则抓取所有）: mail,admin

✅ 已设置关键词过滤: mail, admin
✅ 已成功打开网址: http://example.com

--------------------------------------------------------------------------------
🔍 首次提取结果:
  新发现域名: 🟢 2  总计: 🔵 2
  关键词过滤: 🟡 mail, admin
  📜 域名列表:
    🟢 mail.example.com  [级别: 2]  # 二级域名（绿色）
    🟢 admin.example.com  [级别: 2]  # 二级域名（绿色）
--------------------------------------------------------------------------------

🟠 监控页面变化中... 按 Ctrl+Alt+P 可暂停/开始抓取，按 Ctrl+C 退出程序
```

------

## 🎨 结果标识说明

### 1. 域名级别颜色编码

| 域名级别 | 显示颜色 | 标识 | 示例                             |
| -------- | -------- | ---- | -------------------------------- |
| 二级域名 | 绿色     | 🟢    | `blog.example.com`               |
| 三级域名 | 青色     | 🟢🔵   | `news.blog.example.com`          |
| 四级域名 | 黄色     | 🟢🔵🟡  | `test.news.blog.example.com`     |
| 更高级别 | 红色     | 🟢🔵🟡🔴 | `dev.test.news.blog.example.com` |

### 2. 关键词高亮

- 关键词将以 **亮红色加粗** 显示，例如输入关键词 `mail`，结果中会显示：`🟢 【MAIL】.example.com`

### 3. 统计信息标识

- 新发现域名：`🟢 数量`（绿色数字）
- 累计总域名：`🔵 数量`（蓝色数字）
- 关键词过滤：`🟡 关键词列表`（黄色文字）

------

## ⚠️ 注意事项

- 🚫 **版本匹配**：务必确保 Edge 浏览器与 EdgeDriver 版本一致，否则会导致浏览器无法启动（查看浏览器版本：Edge → 设置 → 关于 Microsoft Edge）。
- 🖥️ **浏览器状态**：程序运行期间请勿关闭 Edge 浏览器窗口，手动操作浏览器（如翻页、跳转）不影响抓取。
- ⏳ **加载等待**：复杂页面（含动态加载内容）需等待完全加载，工具会自动检测内容变化，无需手动触发。
- 💾 **文件清理**：多次运行工具会覆盖 `result.txt`，若需保留历史数据，建议提前备份文件。
- ⚡ **资源占用**：大量子域名抓取（如超过 1000 条）可能占用较多内存，建议定期重启工具释放资源。

------



<div align="center"><p>✨ 用 ClickerSubdomain，让子域名抓取更高效、更精准 ✨</p><p>© 2025 一只鱼（Bifish）</p></div>
