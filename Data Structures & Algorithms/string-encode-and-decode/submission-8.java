class Solution {

    public String encode(List<String> strs) {
        if (strs.size() == 0) return null;
        String str = strs.get(0);
        for (int i = 1; i < strs.size(); i++) {
            str = str + "  !" + strs.get(i);
        }
        return str;
    }

    public List<String> decode(String str) {
        if (str == null) return new ArrayList<>();
        List<String> list = new ArrayList<>();
        String[] ss = str.split("  !");
        for (String s : ss) {
            list.add(s);
        }
        return list;
    }
}
