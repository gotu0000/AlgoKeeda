class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        //frequency of the task
        //initialize to zeros
        array<unsigned int, 26> freq;
        int idleTime;
        int idleTimeTemp;
        int ret;
        freq.fill(0);
        
        //update occurence of each task
        for (char x : tasks)
        {
            freq[((unsigned int)(x)-65)] = freq[((unsigned int)(x)-65)] + 1;
        }
        for(unsigned int i : freq)
        {
            cout << i << " "; 
        }
        cout << endl;
        
        //sort the freq in decreasing order
        //0th element corresponds to max idle time
        sort(begin(freq), end(freq), greater<unsigned int>());
        //max idle time
        if(n > 0)
        {
            idleTime = (freq[0]-1)*n;

            //iterate through the loop
            auto it = freq.begin();
            advance(it, 1); 
            while ( it != freq.end() )
            {
                idleTimeTemp = idleTime - min((freq[0]-1), *it);
                if(idleTimeTemp < 0)
                {
                    idleTime = 0;
                    break;
                }
                else
                {
                    idleTime = idleTimeTemp;
                }
                 ++it;
            }
            ret = tasks.size() + idleTime;
        }
        else
        {
            ret = tasks.size();
        }
        return ret;
    }
};