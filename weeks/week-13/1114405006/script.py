stones=[4,1,7,5,6,8]
L=10
S=2
T=2
stones_sorted=sorted(stones)
shift=0
new_positions=[]
prev=0
L2=L
print('stones_sorted:',stones_sorted)
for p in stones_sorted:
    p_shifted = p - shift
    gap = p_shifted - prev
    print(f'orig p={p}, shift={shift}, p_shifted={p_shifted}, prev={prev}, gap={gap}')
    if gap > T:
        delta = gap - T
        shift += delta
        p_shifted = p - shift
        L2 -= delta
        print('  gap>T: delta',delta,'new shift',shift,'p_shifted',p_shifted,'L2',L2)
    new_positions.append(p_shifted)
    prev = p_shifted
final_gap = L2 - prev
print('after loop new_positions',new_positions,'L2',L2,'final_gap',final_gap)
if final_gap > T:
    delta=final_gap-T
    L2-=delta
    print('shrink L2 by',delta,'->',L2)
print('final new_positions',new_positions,'L2',L2)
