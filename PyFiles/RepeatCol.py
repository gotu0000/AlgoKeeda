import numpy as np

def repeat_column(arr, repeatTime):
	oneN = np.ones((1,repeatTime))
	if(len(arr.shape)) < 2:
		ret = np.reshape(arr,(arr.shape[0],1))
		ret = ret @ oneN
	else:
		if(arr.shape[1] != 1):
			raise Exception("Only one dimensional vectors are allowed")
		else:
			ret = arr @ oneN
	return ret

if __name__ == '__main__':
	ret = repeat_column(np.array([1,2,3,4]),2)
	# ret = repeat_column(np.array([[1],[2],[3],[4]]),2)
	# ret = repeat_column(np.array([[1,2,3,4],[5,6,7,8]]),2)
	print(ret)