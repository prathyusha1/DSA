# n, arrival = 
# 900  940 950  1100 1500 1800
# 910 1200 1120 1130 1900 2000

def findMinPlatforms(n, arrivals, departures):
    arrivals.sort()
    departures.sort()
    plat_needed = 1
    i = 1
    j = 0
    result = 1
    while i < n and j < n:
        if arrivals[i] < departures[j]:
            i = i + 1
            plat_needed = plat_needed + 1
            if plat_needed > result:
                result = plat_needed
        else:
            j = j + 1
            plat_needed = plat_needed - 1
    return result

arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
minPl = findMinPlatforms(6, arrivals, departures)
print('platforms required', minPl)