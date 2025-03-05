def find_best_fabric_pair(fabrics, budget):
    fabrics = sorted(fabrics,key=lambda x: x[1])
    #print(fabrics)
    l,r=0,len(fabrics)-1
    nearestMax=0
    p1=""
    p2=""
    while l < r:
        if fabrics[l][1] + fabrics[r][1] <= budget:
            if fabrics[l][1] + fabrics[r][1] > nearestMax:
                p1=fabrics[l][0]
                p2=fabrics[r][0]
                nearestMax=fabrics[l][1] + fabrics[r][1]
            l += 1
        else:
            r -= 1
    return (p1,p2)
#time: O(NlogN)
#space: O(N)

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))