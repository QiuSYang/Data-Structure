记录数据结构的算法题
    
    1. 排序
    2. 二分法
    3. 动态规划


题目1: 36进制加法

    36进制由0-9，a-z，共36个字符表示。
    要求按照加法规则计算出任意两个36进制正整数的和，如1b + 2x = 48 （解释：47+105=152）
    要求：不允许使用先将36进制数字整体转为10进制，相加后再转回为36进制的做法
    
    codes:
    
    #include <iostream>
    #include <algorithm>
    using namespace std;
    class Solution {
    public:
        char getChar(int n) {
            if(n <= 9) return n + '0';
            else return n - 10 + 'a'; 
        }
        int getInt(char ch) {
            if('0' <= ch && ch <='9') return ch - '0';
            else return ch - 'a' + 10;
        }
        string add36Strings(string num1, string num2) {
            int carry = 0;
            int i = num1.size()-1, j = num2.size()-1;
            string res;
            while(i >= 0 || j >= 0 || carry) {
                int x = i >= 0 ? getInt(num1[i]) : 0;
                int y = j >= 0 ? getInt(num2[j]) : 0;
                int temp = x + y + carry;
                res += getChar(temp % 36);
                carry = temp / 36;
                i -- , j --;
            }
            reverse(res.begin(),res.end());
            return res;
        }
    };
    
    int main() {
        Solution s;
        string a = "1b", b = "2x", c;
        c = s.add36Strings(a,b);
        cout << c << endl;
    }
    

题目2: 十进制加法

    class Solution:
        def addStrings(self, num1: str, num2: str) -> str:
            i, j = len(num1) - 1, len(num2) - 1 
            add = 0  # 保存进位值
            answer = list()
            while i>=0 or j >=0 or add != 0:
                x = int(num1[i]) if i>=0 else 0  # 当前位没有数字，直接设置为0 
                y = int(num2[j]) if j>=0 else 0 
    
                temp = x + y + add 
    
                add = temp//10  # 进位值
                answer.append(str(temp%10))  # 当位置保留值
    
                i -= 1
                j -= 1
            
    
            return "".join(reversed(answer))
                
                
    string addStrings(string num1, string num2)
    {
        int carry = 0;
        int i = num1.size() - 1, j = num2.size() - 1;
        string res;
        while (i >= 0 || j >= 0 || carry)
        {
            int x = i >= 0 ? num1[i] - '0' : 0;
            int y = j >= 0 ? num2[j] - '0' : 0;
            int temp = x + y + carry;
            res += '0' + temp % 10;
            carry = temp / 10;
            i--, j--;
        }
        reverse(res.begin(), res.end());
        return res;
    }

