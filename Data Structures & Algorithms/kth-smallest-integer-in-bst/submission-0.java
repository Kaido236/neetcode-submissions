/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> result = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        postorder(root);
        return result.get(k - 1);
    }

    void postorder(TreeNode node) {
        if (node == null) {
            return;
        }

        postorder(node.left);
        result.add(node.val);
        postorder(node.right);
    }
}