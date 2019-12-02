class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        """A max heap can assure that the points in the max heap are at the minium distance out of all 
        points in the list. First build a heap of the first K elements
        then for the N-K elements compare it;s distance with the point with the maximum distance in the
        heap , if the point with the maximum distance in the heap has distance greater than the point with which
        it is compared then the max point will be replaced with the point that is being compared.
        The resulting heap will consist of k elememts with the minumum distance"""
        
        max_heap = [0]*K 
        # O(k)
        for i in range(len(points)):
            print(i)
            min_heap[i] = (-(points[i][0]**2+points[i][1]**2),points[i][0],points[i][1])
            if i == K - 1:
                break
                
                
        heapq.heapify(max_heap) #O(K)
        
        for i in range(K,len(points)):
            dist = - (points[i][0]**2+points[i][1]**2)
            heapq.heappushpop(min_heap, (dist,points[i][0],points[i][1]))
            
        #O(N-K)*logK
        
        return [(x,y) for (dist,x,y) in max_heap]
        #O(K) + (N-K)logK
        
            
            
            
        