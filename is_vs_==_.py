# a = [1, 2, 4] 
# b = [1, 2, 4]
# a = 4
# b = 4
# a = (1,2,3)
# b = (1,2,3)
# a = None
# b = None
# print(a == b) # compare values
# print(a is b) # compare exact location of object in memory(ke dono ke memory mai ek hi location hai ya nhi)
# print(a is None)

# (==) values ko compare krta while (is) identity ko compare krta agr mutable object hai tu wo memory mai alg jga 
# allocate honge tu (is) False return krega while agr immutable hai tu wo tu change nhi hodkte tu python in ko ek 
# hi baar bnaega tu inhe memory mai ek hi jga allocate krega tu True return hoga.