#!/usr/bin/env python3
"""
CPE Question Content Scraper
Fetches missing content from ZeroJudge and fills QUESTION-*.md files
"""

import asyncio
import re
from pathlib import Path
from typing import Dict, Optional, Tuple
from playwright.async_api import async_playwright, Page

# UVA to ZeroJudge ID mapping
UVA_TO_ZJ = {
    272: "c007",
    490: "c045",
    10008: "c044",
    10035: "c014",
    10038: "d097",
    10041: "a737",
    10050: "e579",
    10056: "e510",
    10057: "e606",
    10170: "a041",
    10193: "a084",
    10221: "e483",
    10222: "e484",
    10409: "b025",
    10415: "c011",
    10420: "d016",
    10642: "e619",
    10783: "e837",
    10812: "a680",
    10908: "a853",
    10929: "a875",
    10931: "a877",
    11005: "a901",
    11417: "c080",
    11461: "d224",
    12019: "e652",
}

# Priority 1: Week 2-4
PRIORITY_1 = {
    "week-02": [272, 490],
    "week-03": [10008, 10035, 10038],
    "week-04": [10041, 10050, 10056, 10057],
}

# Priority 2: Week 6-7
PRIORITY_2 = {
    "week-06": [10170],
    "week-07": [10193, 10221, 10222],
}

# Priority 3: Week 9-13
PRIORITY_3 = {
    "week-09": [10409, 10415],
    "week-10": [],
    "week-11": [],
    "week-12": [10812, 10908],
    "week-13": [10929, 10931, 11005, 11417, 11461, 12019],
}

# Additional Priority 3 from other weeks
PRIORITY_3_ADDITIONAL = {
    "week-09": [10420, 10642],
    "week-10": [10783],
}

BASE_PATH = Path("/Users/fychao/Work/2026-python/weeks")


async def scrape_zerojudge(page: Page, zj_id: str) -> Optional[Dict[str, str]]:
    """Scrape problem content from ZeroJudge"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"

    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)  # Extra wait for dynamic content

        # Extract problem description
        description = await extract_section(page, "題目敘述")
        input_desc = await extract_section(page, "輸入說明")
        output_desc = await extract_section(page, "輸出說明")

        if not description or not input_desc or not output_desc:
            print(
                f"⚠️  Missing content for {zj_id}: desc={bool(description)}, input={bool(input_desc)}, output={bool(output_desc)}"
            )
            return None

        return {
            "description": description.strip(),
            "input": input_desc.strip(),
            "output": output_desc.strip(),
        }
    except Exception as e:
        print(f"❌ Error scraping {zj_id}: {e}")
        return None


async def extract_section(page: Page, section_name: str) -> Optional[str]:
    """Extract a specific section from the page"""
    try:
        # Try to find the section header and get the next content
        selector = f"text='{section_name}'"

        # Get all text content and parse manually
        content = await page.content()

        # Look for the section in HTML
        pattern = rf"{section_name}.*?<div[^>]*>(.*?)</div>"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if match:
            text = match.group(1)
            # Clean HTML tags
            text = re.sub(r"<[^>]+>", "", text)
            text = re.sub(r"\s+", " ", text).strip()
            return text if len(text) > 10 else None

        return None
    except Exception as e:
        print(f"Error extracting {section_name}: {e}")
        return None


def update_question_file(file_path: Path, content: Dict[str, str]) -> bool:
    """Update QUESTION-*.md file with scraped content"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Find section positions
        desc_idx = None
        input_idx = None
        output_idx = None

        for i, line in enumerate(lines):
            if "## 題目敘述" in line:
                desc_idx = i
            elif "## 輸入說明" in line:
                input_idx = i
            elif "## 輸出說明" in line:
                output_idx = i

        if desc_idx is None or input_idx is None or output_idx is None:
            print(f"❌ Cannot find section markers in {file_path}")
            return False

        # Replace content sections
        # Description: from desc_idx+2 to input_idx-1
        new_lines = lines[: desc_idx + 2]
        new_lines.append(content["description"] + "\n\n")
        new_lines.extend(lines[input_idx : input_idx + 2])
        new_lines.append(content["input"] + "\n\n")
        new_lines.extend(lines[output_idx : output_idx + 2])
        new_lines.append(content["output"] + "\n\n")
        new_lines.extend(lines[output_idx + 3 :])

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False


async def process_priority(priority_dict: Dict[str, list], browser) -> int:
    """Process all files in a priority level"""
    completed = 0

    for week, uva_ids in priority_dict.items():
        for uva_id in uva_ids:
            zj_id = UVA_TO_ZJ.get(uva_id)
            if not zj_id:
                print(f"⚠️  No ZJ mapping for UVA {uva_id}")
                continue

            file_path = BASE_PATH / week / f"QUESTION-{uva_id}.md"
            if not file_path.exists():
                print(f"⚠️  File not found: {file_path}")
                continue

            print(f"\n📝 Processing UVA {uva_id} (ZJ {zj_id})...")

            page = await browser.new_page()
            try:
                content = await scrape_zerojudge(page, zj_id)
                if content:
                    if update_question_file(file_path, content):
                        print(f"✅ Updated {file_path.name}")
                        completed += 1
                    else:
                        print(f"❌ Failed to update {file_path.name}")
            finally:
                await page.close()

            await asyncio.sleep(1)  # Rate limiting

    return completed


async def main():
    """Main execution"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        print("🚀 Starting CPE Question Content Scraper")
        print(f"📍 Base path: {BASE_PATH}\n")

        total_completed = 0

        # Priority 1
        print("=" * 60)
        print("PRIORITY 1: Week 2-4 (9 questions)")
        print("=" * 60)
        completed = await process_priority(PRIORITY_1, browser)
        total_completed += completed
        print(f"\n✅ Priority 1: {completed}/9 completed")

        # Priority 2
        print("\n" + "=" * 60)
        print("PRIORITY 2: Week 6-7 (4 questions)")
        print("=" * 60)
        completed = await process_priority(PRIORITY_2, browser)
        total_completed += completed
        print(f"\n✅ Priority 2: {completed}/4 completed")

        # Priority 3
        print("\n" + "=" * 60)
        print("PRIORITY 3: Week 9-13 (13 questions)")
        print("=" * 60)
        all_priority_3 = {**PRIORITY_3, **PRIORITY_3_ADDITIONAL}
        completed = await process_priority(all_priority_3, browser)
        total_completed += completed
        print(f"\n✅ Priority 3: {completed}/13 completed")

        await browser.close()

        print("\n" + "=" * 60)
        print(f"🎉 FINAL RESULT: {total_completed}/26 files completed")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
