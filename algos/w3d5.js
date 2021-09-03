const obj1 = { name: "Zaphod", charm: "high", morals: "dicey"};
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    myKeys = Object.keys(obj);
    myVals = Object.values(obj);
    obj = {};
    for (let index = 0; index < myKeys.length; index++) {
        obj[myVals[index]] = myKeys[index];
    }
    return obj;
}

console.log(invertObj(obj1))