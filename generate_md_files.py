import os
from datetime import datetime

def generate_md_file(index):
    current_time = datetime.now()
    content = f"""---
title: test {index}
description: 
published: true
date: {current_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]}Z
tags: 
editor: markdown
dateCreated: {current_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]}Z
---

# TEST {index}
this is test {index}
"""
    return content

def main():
    # 确保batch文件夹存在
    if not os.path.exists('batch'):
        os.makedirs('batch')
    
    # 生成1000个文件
    for i in range(1, 1001):
        filename = f'batch/test_{i}.md'
        content = generate_md_file(i)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if i % 100 == 0:
            print(f'已生成 {i} 个文件')

if __name__ == '__main__':
    main() 