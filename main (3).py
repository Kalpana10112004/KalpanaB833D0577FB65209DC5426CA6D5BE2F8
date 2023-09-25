def linearSearchProduct (productList, targetProduct):

   indices=[]

   for index, product in enumerate   (productList):

     if product==targetProduct:               indices.append(index)

   return indices

products=["shoes", "boot", " shoes", "sandal", "shoes", "sandal","shoes"]

target="shoes"

target2="apple"
target3="tree"

result=linearSearchProduct (products, target)

print (result)