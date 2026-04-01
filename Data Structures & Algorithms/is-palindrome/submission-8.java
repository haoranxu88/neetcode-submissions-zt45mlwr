class Solution {
    public boolean isPalindrome(String s) {
        if (s == null) return true;
        String str = s.toLowerCase();
        String a = "";
        for (int i = 0; i < str.length(); i++) {
            if (!Character.isLetterOrDigit(str.charAt(i))) {
                continue;
            } else {
                a += str.charAt(i);
            }
        }
        System.out.println(a);
        String[] strs = a.split(" ");
        String forward = "";
        String backward = "";
        for (String ss : strs) {
            forward += ss;
        }
        for (int i = forward.length() - 1; i >= 0; i--) {
            backward += forward.charAt(i);
        }
        System.out.println(forward);
        System.out.println(backward);
        for (int i = 0; i < forward.length(); ++i) {
            if (forward.charAt(i) != backward.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
