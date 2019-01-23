uxe = ("apple", "banana", "coco", "apple", "damson")
print(uxe)
for x in uxe:
    print(x)
print('total apple :', uxe.count("apple"))
print('coco found at position :', uxe.index("coco")+1)
del uxe
print(uxe)  # error as no tuple exists
