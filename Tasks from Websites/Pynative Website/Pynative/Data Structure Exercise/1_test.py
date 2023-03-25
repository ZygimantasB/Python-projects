
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

unique_dist = dict()

for i in sample_list:
    if i in unique_dist:
        unique_dist[i] += 1
    else:
        unique_dist[i] = 1
print(unique_dist)
