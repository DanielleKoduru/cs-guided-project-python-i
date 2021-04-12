"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def foo(str_item):
    return len(str_item)
​
def sort_by_length(lst):
    # Your code here
                                # () => {}
    # sorted_list = sorted(lst, key=lambda str_item: len(str_item))  
    # sorted_list = sorted(lst, key=foo)  
    sorted_list = sorted(lst, key=len)  
    print(sorted_list)
​
​
str_list = ["a", "ccc", "dddd", 'bbbbbb']
​
print(sort_by_length(str_list))
