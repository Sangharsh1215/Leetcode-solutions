class Solution(object):
    def repairCars(self, ranks, cars):
        def totcarsrep(time):
            carsrep = 0
            for r in ranks:
                carsrep += floor(sqrt(time/r))
            return carsrep >= cars
        n = len(ranks)
        if len(ranks) == 1:
            return ranks[0]*cars*cars

        l = 0
        r = max(ranks)*cars*cars

        while l < r:
            mid = (l+r)//2
            if totcarsrep(mid):
                r = mid

            else:
                l = mid + 1

        return l