#!/usr/bin/env python3
"""
Obsidian 网页一键发布与同步脚本 (Site Sync & Publisher)
用法:
  python build_and_publish.py          # 本地预览构建并检查状态
  python build_and_publish.py --deploy # 构建并一键 Git 提交部署到 GitHub Pages
"""

import subprocess
import sys
import os

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_cmd(cmd, cwd=SITE_DIR):
    print(f"➜ Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Command failed:\n{res.stderr}")
        return False
    print(res.stdout)
    return True

def main():
    print("=== 🚀 正在构建 Hugo 学术个人主页... ===")
    if not run_cmd("hugo -d public"):
        print("❌ Hugo 构建失败！")
        sys.exit(1)
    
    print("✅ Hugo 静态页面构建成功！")

    if "--deploy" in sys.argv:
        commit_msg = "Update content via Obsidian workflow"
        if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
            commit_msg = sys.argv[2]
        
        print("=== 📦 正在提交并发布到 GitHub Pages... ===")
        run_cmd("git add .")
        run_cmd(f'git commit -m "{commit_msg}"')
        if run_cmd("git push origin main"):
            print("🎉 部署成功！访问地址: https://guo-yu-chao.github.io/")
        else:
            print("⚠️ 推送失败，请检查网络或 GitHub 认证权限。")

if __name__ == "__main__":
    main()
