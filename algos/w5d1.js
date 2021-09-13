/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) { 
    var expected = true;
    for (let index = 0; index < queue.length; index++) {
        if (queue[index] == 1) {
            for (let x = index+1; x < queue.length; x++) {
                if (queue[x] == queue[index] && x != index+5) {
                    expected = false;
                    return expected;
                } else if (x >= index+6) {
                    break;
                }
            }
        }
    } return expected;
}
console.log(socialDistancingEnforcer(queue1));
console.log(socialDistancingEnforcer(queue2));