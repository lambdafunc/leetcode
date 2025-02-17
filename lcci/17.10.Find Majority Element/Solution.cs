public class Solution {
    public int MajorityElement(int[] nums) {
        int cnt = 0, m = 0;
        foreach (int v in nums)
        {
            if (cnt == 0)
            {
                m = v;
                cnt = 1;
            }
            else
            {
                cnt += m == v ? 1 : -1;
            }
        }
        cnt = 0;
        foreach (int v in nums)
        {
            if (m == v)
            {
                ++cnt;
            }
        }
        return cnt > nums.Length / 2 ? m : -1;
    }
}
