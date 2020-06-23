#include "Sorting.h"

void insertion_sort(int *arr, int len)
{
	int key = 0;
	int ii = 0;
	//first element is already sorted
	for(int j = 1; j < len; j++)
	{
		key = arr[j];
		//insert arr[j] into sorted array
		ii = j-1;
		while((ii >= 0) && (arr[ii] > key))
		{
			arr[ii+1] = arr[ii];
			ii = ii - 1;
		}
		arr[ii+1] = key;
	}
}