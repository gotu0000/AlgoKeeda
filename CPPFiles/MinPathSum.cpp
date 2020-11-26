class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        //get rows and columns
        int numRows = grid.size();
        int numCols = grid[0].size();
        //intialize distance matrix
        vector<vector<int>> distanceMatrix(numRows, std::vector<int>(numCols, 0));
        //now compute the distances coming backwards
        //starting from bottom right
        //it can be either towards left or towards top
        for(int row = (numRows-1); row >= 0 ; --row)
        {
            for(int col = (numCols-1); col >= 0 ; --col)
            {
                //check for bottom right corner
                if((row == (numRows-1)) && (col == (numCols-1)))
                {
                    distanceMatrix[row][col] = grid[row][col];
                }
                //check for last row
                else if(row == (numRows-1))
                {
                    distanceMatrix[row][col] = grid[row][col] + distanceMatrix[row][col+1];
                }
                //check for last col
                else if(col == (numCols-1))
                {
                    distanceMatrix[row][col] = grid[row][col] + distanceMatrix[row+1][col];
                }
                //else its normal case
                else
                {
                    distanceMatrix[row][col] = grid[row][col] + min(distanceMatrix[row+1][col]
                                                                    , distanceMatrix[row][col+1]);
                }
            }
        }
        return distanceMatrix[0][0];
    }
};