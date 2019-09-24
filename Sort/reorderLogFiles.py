class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """letters = []
        digits = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x : (x.split(" ")[1:],x.split(" ")[0]))
        return letters + digits"""
        def f (log):
            if log.split(" ", 1)[1][0].isdigit():
                return (1,)
            else:
                return (0, log.split()[1:], log.split()[0]) 
            
        logs.sort(key = f)
        return logs
    
    """ s.split() function on string returns a list of characters by splitting the string on a seaparator
    
    Syntax : s.split(seperator, maxsplit)
    so if s = " I like algorithm and data structure
    s.split(" ", 1) will give ['I', 'like algorithm and data structure']
    s.split(" ", 2) will give ['I', 'like', 'algorithm and data structure']
    s.split( " ",3) will give ['I', 'like', 'algorithm', 'and data structure']
    
    We can use a tuple as a key in the sort function where the lements of the list to be sorted will be sorted in the order in which elements are there in the tuple
    
    eg if tuple(a,b,c) is the key for the sort function then elements of the list which is to be sorted will be sorted first on the basis of a , then everything remains the same and then the lements will be sorted on the basis of b , then everything remains the same and then the elements will be sorted on the basis of c. Such kinf of sorting is called stable sort
    
    So, if the element in the list which is to be sorted is a letter log then the tuple will be (0, content, identifier) and if it is a digit log then the tuple will be (1, None, None) as we want the digits to be returned after the letters
    
    
    On the other hand if we sort such that we inititally sort the letter with the key as the content and then sort again with key as the identifier then the initial sort by content will be changed to sort by identifier irrespective of the content.
    s = ["let5 art can","let3 art can ","let2 own kit dig"] 
    eg s.sort(key = content) will result in s as ["let5 art can","let3 art can","let2 own kit dig"]
    and now if we call s.sort(key = identifier) then s will result as ["let2 own kit", "let3 art can", "let5 art can"]
    which will is an unstable sort as it did not keep intact the sorting done by s.sort(key = content)
    
    This is an important point to note as our aim here was to sort by identifier onlhy if there is a tie in sort by content. However, this is sorting by identifier irrespective of the content
    
    Hence, for a stable sort it is important to call both of these conditions by passing a tuple to the key so that the elements can be sorted stably on the basis of a then b then c
    
    
    """

#O(n) time and O(1) space