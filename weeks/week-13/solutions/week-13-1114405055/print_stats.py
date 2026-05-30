from task1_grouped_bar import load_year, get_top_depts, DATA_DIR
from task2_zipcode_heatmap import load_county_counts, get_top_counties

years = [112, 113, 114]
yd = {y: load_year(y, DATA_DIR) for y in years}
print("=== Task 1 Top Depts ===")
for dept in get_top_depts(yd):
    print(f"{dept}: {[yd[y].get(dept, 0) for y in years]}")

years2 = [109, 110, 111, 112, 113, 114]
yd2 = {y: load_county_counts(y, DATA_DIR) for y in years2}
print("=== Task 2 Top Counties ===")
for c in get_top_counties(yd2):
    print(f"{c}: {sum(yd2[y].get(c, 0) for y in years2)}")
