import re
import os
import socket
import time
import keyboard
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.edge.service import Service


# 颜色代码常量
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BRIGHT = '\033[1m'


# 全局集合用于存储所有唯一域名
all_unique_domains = set()
# 控制是否抓取的标志
is_running = True
# 关键词列表
keywords = []


def is_ip_address(address):
    """判断给定的地址是否为 IP 地址"""
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False


def get_domain_level(domain):
    """获取域名级别（几级域名）"""
    return len(domain.split('.'))


def extract_domains_from_content(content):
    """从内容中提取域名"""
    # 改进的域名正则表达式 - 更精确匹配域名格式
    domain_pattern = r'(?:https?://)?([a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+(?:\.[a-zA-Z]{2,}))'

    # 提取所有可能的域名
    domains = re.findall(domain_pattern, content)

    # 额外处理URL格式的域名
    urls = re.findall(r'https?://[^\s<>"\']+', content)
    for url in urls:
        try:
            parsed_url = urlparse(url)
            if parsed_url.netloc and '.' in parsed_url.netloc:
                domain = parsed_url.netloc.split(':')[0]
                domains.append(domain)
        except:
            pass

    # 过滤非域名内容，保留符合条件的子域名
    valid_subdomains = []
    for domain in domains:
        # 跳过空字符串和IP地址
        if not domain or is_ip_address(domain):
            continue

        # 跳过DNS记录类型
        if domain.upper() in {'A', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'PTR', 'AAAA'}:
            continue

        # 跳过包含非法字符的"域名"
        if re.search(r'[^\w.-]', domain) or '..' in domain:
            continue

        valid_subdomains.append(domain)

    return valid_subdomains


def filter_domains_by_keywords(domains):
    """根据关键词过滤域名，保留包含任一关键词的域名"""
    if not keywords:  # 如果没有关键词，返回所有域名
        return domains

    filtered = []
    for domain in domains:
        # 检查域名是否包含任何一个关键词（不区分大小写）
        if any(keyword.lower() in domain.lower() for keyword in keywords):
            filtered.append(domain)
    return filtered


def get_domain_color(domain):
    """根据域名级别返回不同的颜色代码"""
    level = get_domain_level(domain)
    if level == 2:  # 二级域名
        return Colors.GREEN
    elif level == 3:  # 三级域名
        return Colors.CYAN
    elif level == 4:  # 四级域名
        return Colors.YELLOW
    else:  # 更高级别的域名
        return Colors.RED


def print_colored_domain(domain):
    """彩色打印域名，并高亮显示关键词"""
    color = get_domain_color(domain)
    level = get_domain_level(domain)

    # 高亮显示关键词
    highlighted_domain = domain
    if keywords:
        for keyword in keywords:
            # 不区分大小写查找关键词
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            # 用亮色和加粗突出显示关键词
            highlighted_domain = pattern.sub(
                f"{Colors.BRIGHT}{Colors.RED}\\g<0>{Colors.RESET}{color}",
                highlighted_domain
            )

    print(f"  {color}{highlighted_domain}{Colors.RESET}  [级别: {level}]")


def save_domains_to_file(domains, filename="result.txt"):
    """将域名保存到文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        for domain in sorted(domains):
            f.write(f"{domain}\n")


def print_separator():
    """打印分隔线"""
    print(f"\n{Colors.BLUE}{'-' * 80}{Colors.RESET}\n")


def on_pause_resume():
    global is_running
    is_running = not is_running
    status = "开始" if is_running else "暂停"
    print_separator()
    print(f"{Colors.PURPLE}{Colors.BOLD}已{status}抓取{Colors.RESET}，按 Ctrl+Alt+P 可切换状态")
    print_separator()


def main():
    global all_unique_domains, is_running, keywords

    # 打印欢迎信息
    print_separator()
    print(f"{Colors.BOLD}{Colors.PURPLE}子域名抓取工具 (带关键词过滤){Colors.RESET}")
    print(f" {Colors.CYAN}功能：{Colors.RESET}自动抓取包含指定关键词的子域名，支持手动翻页和快捷键控制")
    print(f" {Colors.CYAN}快捷键：{Colors.RESET}Ctrl+Alt+P (暂停/开始) | Ctrl+C (退出)")
    print_separator()

    # 注册快捷键
    keyboard.add_hotkey('ctrl+alt+p', on_pause_resume)

    # 获取用户输入的网址
    url = input(f"{Colors.BOLD}请输入要打开的网址: {Colors.RESET}").strip()
    if not url.startswith(('http://', 'https://')):
        url = f'http://{url}'

    # 获取用户输入的关键词
    keywords_input = input(
        f"{Colors.BOLD}请输入关键词（多个关键词用英文逗号分隔，为空则抓取所有）: {Colors.RESET}").strip()
    if keywords_input:
        keywords = [kw.strip() for kw in keywords_input.split(',') if kw.strip()]
        print(f"{Colors.GREEN}已设置关键词过滤: {', '.join(keywords)}{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}未设置关键词，将抓取所有发现的子域名{Colors.RESET}")

    # 初始化Edge浏览器
    try:
        # 查找同目录下的msedgedriver.exe
        driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'msedgedriver.exe')
        service = Service(driver_path)
        driver = webdriver.Edge(service=service)
        driver.get(url)
        print_separator()
        print(f"{Colors.GREEN}已成功打开网址: {url}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}浏览器初始化失败: {e}{Colors.RESET}")
        return

    # 记录当前页面的URL和内容哈希，用于检测页面变化
    current_url = driver.current_url
    current_content_hash = hash(driver.page_source)

    # 首次提取当前页面的域名并过滤
    initial_domains = extract_domains_from_content(driver.page_source)
    filtered_domains = filter_domains_by_keywords(initial_domains)
    new_domains = set(filtered_domains) - all_unique_domains
    new_domains_count = len(new_domains)
    all_unique_domains.update(filtered_domains)

    # 保存并显示首次提取的结果
    save_domains_to_file(all_unique_domains)
    print_separator()
    print(f"{Colors.BOLD}首次提取结果:{Colors.RESET}")
    print(
        f"  新发现域名: {Colors.GREEN}{new_domains_count}{Colors.RESET}  总计: {Colors.BLUE}{len(all_unique_domains)}{Colors.RESET}")
    if keywords:
        print(f"  关键词过滤: {Colors.YELLOW}{', '.join(keywords)}{Colors.RESET}")
    print(f"  {Colors.YELLOW}域名列表:{Colors.RESET}")
    for domain in sorted(new_domains):
        print_colored_domain(domain)

    print_separator()
    print(f"{Colors.CYAN}监控页面变化中...{Colors.RESET} 按 Ctrl+Alt+P 可暂停/开始抓取，按 Ctrl+C 退出程序")

    try:
        while True:
            if is_running:
                # 检查页面是否变化（URL变化或内容变化）
                new_url = driver.current_url
                new_content_hash = hash(driver.page_source)

                if new_url != current_url or new_content_hash != current_content_hash:
                    print_separator()
                    print(f"{Colors.BOLD}{Colors.CYAN}检测到页面变化，正在提取域名...{Colors.RESET}")

                    # 更新当前页面信息
                    current_url = new_url
                    current_content_hash = new_content_hash

                    # 提取、过滤并处理新页面的域名
                    page_domains = extract_domains_from_content(driver.page_source)
                    filtered_domains = filter_domains_by_keywords(page_domains)
                    new_domains = set(filtered_domains) - all_unique_domains
                    new_domains_count = len(new_domains)

                    if new_domains_count > 0:
                        all_unique_domains.update(new_domains)
                        save_domains_to_file(all_unique_domains)
                        print(
                            f"  {Colors.GREEN}提取到 {new_domains_count} 个新域名{Colors.RESET}，总计: {Colors.BLUE}{len(all_unique_domains)}{Colors.RESET}")
                        if keywords:
                            print(f"  关键词过滤: {Colors.YELLOW}{', '.join(keywords)}{Colors.RESET}")
                        print(f"  {Colors.YELLOW}新域名列表:{Colors.RESET}")
                        for domain in sorted(new_domains):
                            print_colored_domain(domain)
                    else:
                        print(f"  {Colors.YELLOW}未发现符合关键词条件的新域名{Colors.RESET}")

                    print_separator()
                    print(f"{Colors.CYAN}继续监控页面变化中...{Colors.RESET} 按 Ctrl+Alt+P 可暂停/开始抓取")
            # 短暂休眠，减少CPU占用
            time.sleep(1)

    except KeyboardInterrupt:
        print_separator()
        print(f"{Colors.PURPLE}程序已退出{Colors.RESET}")
    finally:
        driver.quit()
        print_separator()
        print(
            f"{Colors.BOLD}最终结果:{Colors.RESET} 已保存到 {Colors.UNDERLINE}result.txt{Colors.RESET}，共 {Colors.BLUE}{len(all_unique_domains)}{Colors.RESET} 个符合条件的唯一域名")
        print_separator()


if __name__ == "__main__":
    main()
