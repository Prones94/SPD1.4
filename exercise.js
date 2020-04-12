// Problem 2
/*
Rephrase Question: Find the halfway point of a list, or the two items in the middle if there isn't a halfway point

Pseudocode:
    - Create Node Class
    - Create a Linked List Class
    - Use the find method to find middle of the list 
    - If list contains an even number of nodes, take both the head and head.next nodes in the middle
	
*/

// Solution:
var middleNode = function(head){
    let fast = slow = head
    while (fast&& fast.next) {
        fast = fast.next.next
        slow = slow.next
    }
    return slow, slow.next
}

// Problem 4

/*
Rephrase Question: Find the halfway point of a list, or the two items in the middle if there isn't a halfway point

Pseudocode:
    - Create a Map
    - Have a start and end point
    - Return 0 if the string is empty or no letter
    - Set both pointers to be at the beginning of string
        - Have the max substring length = 1
    -While end pointer is less than N:
        - Add the next character in the map and move end pointer to the right
        - If the letter is found again, remove the leftmost character and update max length
	
*/

// Solution

var lengthOfLongestSubstringKDistinct = function(s, k) {
    if (!s || k === 0) {
        return 0;
    }
    let map = new Map(); 
    let start = 0;
    let end = 0;
    let r = 0;
    while (end <= s.length) {
        if (map.size === k && !map.has(s[end]) || end === s.length) {
            r = Math.max(r, end - start);
            while (map.size === k) {
                const count = map.get(s[start]);
                if (count - 1 === 0) {
                    map.delete(s[start]);
                } else {
                    map.set(s[start], count - 1);
                }
                start++;
            }
        } 
        if (map.has(s[end])) {
            map.set(s[end], map.get(s[end]) + 1);
        } else {
            map.set(s[end], 1);
        }
        end++;
    }
    return r;  
};