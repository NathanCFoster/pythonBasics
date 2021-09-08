/* 
Given a string,
return a new string with the duplicates excluded
Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var expected = "";
    for (let index = 0; index < str.length; index++) {
        expected += str[index];
        for (let x = 0; x < str.length; x++) {
            if (str[index] == str[x] && index != x) {
                str = str.substr(index, str.length);
            }
        }
    } return expected;
}
console.log(stringDedupe(str1));
console.log(stringDedupe(str2));

/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    var expected = "";
    var arr = str.split(" ");
    for (let index = 0; index < arr.length; index++) {
        for (let x = str.length; x >= 0; x--) {
            if (arr[index][x] != undefined) {
                expected += arr[index][x];
            }
        } expected += " ";
    } return expected;
}
console.log(reverseWords(str1));
console.log(reverseWords(str2));
console.log(reverseWords(str3));