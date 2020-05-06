class Subtree {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s == null || t == null){
            return s == t;
        }
        if (s.val == t.val){
            if (isSame(s,t) == true){
                return true;
            }
            
        }
        
        return isSubtree(s.left, t) || isSubtree(s.right, t);        
        }
     public boolean isSame(TreeNode a,TreeNode b){
         if(a == null || b == null){
             return a == b;
        }
         if (a.val != b.val){
             return false;
         }
         return isSame(a.left, b.left) && isSame(a.right, b.right);
         
     }

     public static void main(String[] args){
      
        TreeNode parent = new TreeNode(5);
        TreeNode second = new TreeNode(4);
        TreeNode third = new TreeNode(8);
        parent.left = second;
        parent.right = third;
        second.left = null;
        second.right = null ;
        third.left = null;
        third.right = null;

        TreeNode child = new TreeNode(5);
        TreeNode second = new TreeNode(4);
        TreeNode third = new TreeNode(8);
        child.left = second;
        child.right = third;
        second.left = null;
        second.right = null ;
        third.left = null;
        third.right = null;

        System.out.println(Subtree.isSubtree(parent,child));
    }
    }

    // O(m+n) time and O(m+n) space
