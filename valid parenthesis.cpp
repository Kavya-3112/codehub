class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
    
        for(int i=0;i<s.length();i++)
        {
            if(st.size()==0 && (s[i]==')'|| s[i]=='}' || s[i]==']'))
            return false;
            else if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                st.push(s[i]);
            }
            else if((s[i]==')' && st.top()=='(') || (s[i]=='}' && st.top()=='{' )
                || s[i]==']' && st.top()=='[' )
                st.pop();
                
                else if((s[i]==')' && st.top()!='(') || (s[i]=='}' && st.top()!='{' )
                || s[i]==']' && st.top()!='[' )
                return false;
            
        }
        if(st.size()!=0)
        return false;
        else
        return true;
    }
        

};
