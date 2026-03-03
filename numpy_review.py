import numpy as np
import time

def get_max_index(a):
    return np.argmax(a)

def manual_mean(arr):
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i,j]
    return sum / arr.size

def numpy_mean(arr):
    return arr.mean()

def how_long(func, *args):
    t0 = time.time()
    result = func(*args)
    t1 = time.time()
    return result, t1-t0

def test_run():
    #print(np.array([(2,3,4),(5,6,7)]))
    #print(np.empty(5))
    #print(np.empty((5,4,3)))
    #print(np.ones((5,4), dtype=np.int_))
    #print(np.random.rand(5,4))
    #print(np.random.normal(50, 10, size=(2,3)))
    #print(np.random.randint(10, size=(2,3)))

    # a = np.random.random((5,4))
    # print(a.shape)
    # print(a.size)
    # print(a.dtype)

    # np.random.seed(693)
    # a = np.random.randint(0,10,size=(5,4))
    # print("Array:\n", a)
    # print("Sum of all elements:", a.sum())
    # print("Sum of each column:", a.sum(axis=0))
    # print("Sum of each row:", a.sum(axis=1))
    # print("Minimum of each column:", a.min(axis=0))
    # print("Maximum of each row:", a.max(axis=1))
    # print("Mean of all elements:", a.mean())

    # a = np.array([9,6,2,3,12,14,7,10], dtype=np.int32)
    # print("Array:", a)
    # print("Maximum value", a.max())
    # print("Index of max:", get_max_index(a))

    # t1 = time.time()
    # print("ML4T")
    # t2 = time.time()
    # print("Time to print:", t2-t1, "seconds")

    # nd1 = np.random.random((1000,1000))
    # res_maunal, t_manual = how_long(manual_mean, nd1)
    # res_numpy, t_numpy = how_long(numpy_mean, nd1)
    # print ("Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(res_maunal, t_manual, res_numpy, t_numpy))
    # assert abs(res_maunal-res_numpy)<= 10e-6, "Results aren't equal!"
    # speedup = t_manual/t_numpy
    # print("Numpy mean is", speedup, "times faster.")

    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print(a)
    mean = a.mean()
    print(mean)
    a[a<mean] = mean
    print(a)

if __name__ == '__main__':
    test_run()