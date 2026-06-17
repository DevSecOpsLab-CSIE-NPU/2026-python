#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
補充缺失的 CPE 題目內容
從 ZeroJudge 爬取題目敘述、輸入說明、輸出說明
"""

import requests
from bs4 import BeautifulSoup
import time
import re
from pathlib import Path
from typing import Optional, Tuple

# UVA 到 ZeroJudge 的映射
UVA_TO_ZJ = {
    272: "c007", 490: "c045", 10008: "c044", 10035: "c014", 10038: "d097",
    10041: "a737", 10050: "e579", 10056: "e510", 10057: "e606", 10170: "a041",
    10193: "a084", 10221: "e483", 10222: "e484", 10409: "b025", 10415: "c011",
    10420: "d016", 10642: "e619", 10783: "e837", 10812: "a680", 10908: "a853",
    10929: "a875", 10931: "a877", 11005: "a901", 11417: "c080", 11461: "d224",
    12019: "e652"
}

# 優先級分類
PRIORITY_MAP = {
    1: [(2, [272, 490]), (3, [10008, 10035, 10038]), (4, [10041, 10050, 10056, 10057])],
    2: [(6, [10170]), (7, [10193, 10221, 10222])],
    3: [(10, [10409, 10415, 10420, 10642, 10783]), 
        (11, [10812, 10908, 10929, 10931]), 
        (12, [11005]), 
        (13, [11417, 11461, 12019])]
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

def fetch_problem_content(zj_id: str) -> Optional[Tuple[str, str, str]]:
    """從 ZeroJudge 爬取題目內容"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.encoding = 'utf-8'
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # 提取題目敘述
        desc_elem = soup.find(id='problem_content')
        description = desc_elem.get_text(strip=True) if desc_elem else ""
        
        # 提取輸入說明
        input_elem = soup.find(id='problem_theinput')
        input_desc = input_elem.get_text(strip=True) if input_elem else ""
        
        # 提取輸出說明
        output_elem = soup.find(id='problem_theoutput')
        output_desc = output_elem.get_text(strip=True) if output_elem else ""
        
        if description and input_desc and output_desc:
            return description, input_desc, output_desc
        return None
    
    except Exception as e:
        print(f"  ❌ 爬取失敗 ({zj_id}): {e}")
        return None

def update_question_file(week: int, uva_id: int, description: str, input_desc: str, output_desc: str) -> bool:
    """更新 QUESTION-*.md 檔案"""
    file_path = Path(f"weeks/week-{week:02d}/QUESTION-{uva_id}.md")
    
    if not file_path.exists():
        print(f"  ⚠️ 檔案不存在: {file_path}")
        return False
    
    content = file_path.read_text(encoding='utf-8')
    
    # 替換各欄位，移除"說明請見上方連結"
    def replace_section(content, section_name, new_content):
        pattern = rf"(## {section_name}\n)(.*?)((?=##)|$)"
        replacement = rf"\1{new_content}\n\n\2"
        return re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 更新各欄位
    if "## 題目敘述" in content and (description or "【待補充】" in content):
        content = replace_section(content, "題目敘述", description)
    
    if "## 輸入說明" in content and (input_desc or "【待補充】" in content):
        content = replace_section(content, "輸入說明", input_desc)
    
    if "## 輸出說明" in content and (output_desc or "【待補充】" in content):
        content = replace_section(content, "輸出說明", output_desc)
    
    # 移除"說明請見上方連結"
    content = content.replace("說明請見上方連結", "")
    content = re.sub(r"> ⚠️ 【待補充】.*?\n", "", content)
    
    file_path.write_text(content, encoding='utf-8')
    return True

def main():
    print("=" * 80)
    print("🔧 CPE 題目內容補充工具")
    print("=" * 80)
    
    total_success = 0
    total_failed = 0
    
    for priority in [1, 2, 3]:
        print(f"\n⏳ Priority {priority}:")
        priority_items = PRIORITY_MAP[priority]
        
        for week, problems in priority_items:
            print(f"\n  Week {week}:")
            
            for uva_id in problems:
                if uva_id not in UVA_TO_ZJ:
                    print(f"    ⚠️ UVA {uva_id} 無映射")
                    continue
                
                zj_id = UVA_TO_ZJ[uva_id]
                print(f"    ⏳ UVA {uva_id} (ZJ {zj_id})...", end=" ")
                
                # 爬取內容
                result = fetch_problem_content(zj_id)
                
                if result:
                    description, input_desc, output_desc = result
                    if update_question_file(week, uva_id, description, input_desc, output_desc):
                        print(f"✅")
                        total_success += 1
                    else:
                        print(f"❌")
                        total_failed += 1
                else:
                    print(f"❌")
                    total_failed += 1
                
                time.sleep(0.5)  # 禮貌延遲
    
    print(f"\n{'=' * 80}")
    print(f"📊 補充結果: ✅ {total_success} 個 | ❌ {total_failed} 個")
    print(f"{'=' * 80}")

if __name__ == "__main__":
    main()
