class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
    int n=prices.size();
    stack<int> st;
    vector<int>v;
    vector<int> ans;
    for(int i=n-1;i>=0;i--){
        if(st.empty())
        v.push_back(-1);
        else if(st.size()>0 && st.top()<prices[i])
            v.push_back(st.top());
        else if(st.size()>0 && st.top()>=prices[i])
        {
            while(st.size()>0 && st.top()>prices[i]){
                st.pop();
            }
            if(st.size()==0)
            {
                v.push_back(-1);
            }
            else{
                v.push_back(st.top());
            }
        }
        st.push(prices[i]);
    }
    reverse(v.begin(),v.end());
    for(int i=0;i<n;i++){
        if((prices[i]-v[i])> prices[i])
        ans.push_back(prices[i]);
        else
        ans.push_back(prices[i]-v[i]);
    }
    return ans;
    }
};