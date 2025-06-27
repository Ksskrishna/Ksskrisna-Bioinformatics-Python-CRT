def bubble_sort(scores):
    for i in range(len(scores)):
        for j in range(len(scores)-i-1):
            if scores[j]>scores[j+1]:
                scores[j],scores[j+1] = scores[j+1],scores[j]
    print(f"sorted scores: {scores}")
scores = [55,80,40,62,57,45]
print(f"unsorted scores: {scores}")
bubble_sort(scores)