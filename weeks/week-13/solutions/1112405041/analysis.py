"""Stage 2: 分析邏輯"""

def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    if not year_data or top_n <= 0:
        return []

    candidate_depts: set[str] = set()
    for year, depts in year_data.items():
        sorted_depts = sorted(depts.items(), key=lambda x: x[1], reverse=True)
        for dept, _ in sorted_depts[:top_n]:
            candidate_depts.add(dept)

    # 依 6 年合計人數排序
    total: dict[str, int] = {}
    for depts in year_data.values():
        for dept, count in depts.items():
            total[dept] = total.get(dept, 0) + count

    result = [d for d in sorted(total, key=lambda d: total[d], reverse=True) if d in candidate_depts]
    return result[:top_n]


def get_top_counties(all_years: dict[int, dict[str, int]], top_n: int = 10) -> list[str]:
    """6 年合計，回傳人數前 top_n 的縣市清單"""
    if not all_years or top_n <= 0:
        return []

    total: dict[str, int] = {}
    for counties in all_years.values():
        for county, count in counties.items():
            total[county] = total.get(county, 0) + count

    result = sorted(total, key=lambda c: total[c], reverse=True)
    return result[:top_n]
