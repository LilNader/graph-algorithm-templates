def binary_search(data,target):
	data = sorted(data)
	low = 0
	high = len(data)-1

	while low <=high:

		mid = (low + high) //2

		if target == data[mid]:
			print(Element exsits)
			return True

		elif target < data[mid]:
			high = mid -1

		else:
			low = mid +1
	return False


def binary_search_rec(data,target, low,high): #low = 0, high = len(data) -1
	
	data = sorted(data)

	if low < high:
		mid = (low +high)//2
		if target ==data[mid]:
			return True
		elif target < data[mid]:

			return binary_search_rec(data, target, low, mid-1)

		else:

			return binary_search_rec(data, target, mid+1 , high)


	else:
		return False



###################################

#FINDING CLOSEST NUMBER

def find_closest_num(A,target):
	min_diff = float("inf")
	low = 0
	high = len(A) - 1
	closest_num = None

	#Edge Cases for empty list
	if len(A) ==0:
		return None
	if len(A) ==1:
		return A[0]

	while low <= high:

		mid = (low+high)//2

		left_mid = mid - 1
		right_mid = mid + 1

		if right_mid < len(A):
			min_diff_right =  abs(A[right_mid] - target)

		if left_mid >0:
			min_diff_left = abs(A[left_mid] - target)

		# Check if abs  between left and right
		# elements are smaller than any prior

		if min_diff_left < min_diff:
			min_diff = min_diff_left
			closest_num = A[left_mid]

		if min_diff_right < min_diff:
			min_diff = min_diff_right
			closest_num = A[right_mid]

		if A[mid] < target:
			low = mid +1

		elif A[mid] > target:
			high = mid - 1

		else:
			return A[mid]

	return closest_num


#
