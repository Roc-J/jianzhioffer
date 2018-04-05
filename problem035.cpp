#include<stdio.h>

class Solution {
public:
    int InversePairs(vector<int> data) {
        if(data.empty())
        {
            return 0;
        }
        vector<int> copyData(data.begin(),data.end());
        long long result = InversePairsHelp(data, copyData, 0, data.size()-1);
        return result%1000000007;
    }

    long long InversePairsHelp(vector<int> &data, vector<int> &copyData, int start, int end)
    {
        if(start == end)
        {
            copyData[start] = data[start];
            return 0;
        }
        int mid = start +(end-start)/2;
        long long left=InversePairsHelp(copyData,data,start,mid);
        long long right = InversePairsHelp(copyData,data,mid+1,end);

        int i = mid;
        int j = end;
        int indexCopy = end;
        long long count = 0;

        while(i>=start && j>=mid+1)
        {
            if(data[i]>data[j])
            {
                copyData[indexCopy--]=data[i--];
                count += j-mid;
            }
            else{
                copyData[indexCopy--]=data[j--];
            }
        }
        while(i>=start)
        {
            copyData[indexCopy--]=data[i--];
        }
        while(j>=mid+1)
        {
            copyData[indexCopy--]=data[j--];
        }
        return count+left+right;
    }
};
