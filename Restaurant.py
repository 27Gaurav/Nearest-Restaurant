class Node:
       
       def __init__(self,key) :
            self.key= key
            self.left= None
            self.right=None
            
            self.isleaf =False
def tree2d(data,k=0):
    if k==0:
        data.sort()
    elif k==1:
        data.sort(key = lambda x: x[1])
    if len(data)==0:
        return None
     
    

    if len(data)==1:
        q=Node(data[0])
        q.isleaf=True
        q.left=None
        q.right=None
    else:
        mid= len(data)//2
        q=Node(data[mid])
        
        q.left= tree2d(data[0:mid],(k+1)%2)
        q.right= tree2d(data[mid:],(k+1)%2)
    return q


def searchnearby(tree,start,end,k=0):
    results=[]
    if tree==None:
        return results
        
    elif tree.isleaf==True:

        if (tree.key[0]>start[0] and tree.key[0]<end[0] and tree.key[1]>start[1] and tree.key[1]<end[1] ):
            results.append(tree.key)

    elif tree.key[k]<start[k]:
        tree=tree.right
        results+=searchnearby(tree,start,end,(k+1)%2)
    elif tree.key[k]>=end[k]:
        tree=tree.left
        
        results+=searchnearby(tree,start,end,(k+1)%2)
    elif tree.key[k]>=start[k] and tree.key[k]<end[k]:
        results+=searchnearby(tree.left,start,end,(k+1)%2)
        results+=searchnearby(tree.right,start,end,(k+1)%2)
    return results

class PointDatabase:
    def __init__(self,pointlist):
        self._pointlist = tree2d(pointlist,k=0)
    
    def searchNearby(self,q,d):
        start = (q[0]-d,q[1]-d)
        end= (q[0]+d,q[1]+d)
        output= searchnearby(self._pointlist,start,end,k=0)
        return output