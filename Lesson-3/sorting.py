# Bubble sort is in place, O(n²) (best case = O(n)) 

# Merge sort, split as much as possible then sort
# https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge_sort_algorithm_diagram.svg
# O(n*log(n)) -> Better than bubble sort but use more space because of new arrays generated

# Quick sort, pick random value (pivot) then move value that are larger to the right and smaller to the left of this pivot
# https://fr.wikipedia.org/wiki/Tri_rapide#/media/Fichier:Partition_example.svg
# Worst case (when array is near sorted)= O(n²) / best case = O(log(n))