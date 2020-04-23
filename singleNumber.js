//  @param {number[]} nums
//  @return {number}
// 
var singleNumber = function(nums) {
    const map = {};

    for (let n of nums) {
        if (map[n]==null)
            map[n] = 0;
        map[n] += 1;
    }

    for (let n in map) {
        if (map[n] === 1)
            return n;
    }
};