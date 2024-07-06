
# -----------------------------< Mutable Datatypes >-------------------------------------
# In Python, the following datatypes are mutable:
# 1. List
# 2. Dictionary
# 3. Set ---> Sets are mutable but its elements are immutable
# 4. User-defined classes (unless specifically made immutable)
# Mutable datatypes can be modified after they are created.
# -------------------------------------------------------------------------------------
# ------------------------------< Immutable Datatypes >----------------------------------
# In Python, the following datatypes are immutable:
# 1. Integers
# 2. Floats
# 3. Complex numbers
# 4. Strings
# 5. Tuples
# 6. Boolean
# Immutable datatypes cannot be modified after they are created.
# -------------------------------------------------------------------------------------

#-----------------------------------< Sets (Immutable) >------------------------------
# A set is a collection of unique elements. Sets are unordered and unindexed.
# Sets are written with curly brackets.
# Sets are mutable, but the elements inside the set are immutable.
# List and Dictionary are not included in sets
# -------------------------------------------------------------------------------------

# Dictionary Contains Key:Value Pairs but sets don't contain the pairs
Collection = {
    1,2,3,4,5,5,5 #-----> Duplicate Values are ignored in sets
}
Empty = set() #---> For Creating the empty set 
# Empty = {} -----> This will Create the Dictionary not the set
print(Collection) # {1,2,3,4,5}
print(len(Collection))
print(type(Collection))

#--------------------------------------< Methods/Functions in Sets >---------------------------------------
# 1. add() - Adds an element to the set
# 2. clear() - Removes all the elements from the set
# 3. copy() - Returns a copy of the set
# 4. difference() - Returns a set that contains the difference between two or more sets
# 5. difference_update() - Removes the items in the set that are also included in other
# 6. discard() - Removes the specified item
# 7. intersection() - Returns a set that contains the similarity between two or more sets
# 8. intersection_update() - Removes the items in the set that are not present in other
# 9. isdisjoint() - Returns True if two sets have a null intersection
# 10. issubset() - Returns True if all elements in the set exist in the specified
# 11. issuperset() - Returns True if all elements in the specified set exist in
# 12. pop() - Removes an element from the set
# 13. remove() - Removes the specified element
# 14. symmetric_difference() - Returns a set that contains the symmetric differences
# 15. symmetric_difference_update() - Inserts the symmetric differences from this set and the
# 16. union() - Returns a set that contains the union of sets
# 17. update() - Updates the set with the union of itself and others
# -------------------------------------------------------------------------------------