
//https:leetcode.com/problems/path-sum/

public class PathSum {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null){
            return false;
        }
        sum = sum - root.val;
        if (root.left == null && root.right == null){
            return sum == 0;
        }
        return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
    }

    public static void main(String[] args){
        PathSum pathSum = new PathSum();
        int sum = 9;
        TreeNode root = new TreeNode(5);
        TreeNode second = new TreeNode(4);
        TreeNode third = new TreeNode(8);
        root.left = second;
        root.right = third;
        second.left = null;
        second.right = null ;
        third.left = null;
        third.right = null;

        System.out.println(pathSum.hasPathSum(root,sum));

    }
}





//O(n) time and O(n) space

