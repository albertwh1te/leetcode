var isPalindrome = function(string) {
    string += "";
    for (var i = 0, j = string.length - 1; i < j; i++, j--) {
        if (string[i] == string[j]) {
            return true;
        }
    }
    return false
}
console.log(isPalindrome('ab'))
console.log(isPalindrome('aa'))
