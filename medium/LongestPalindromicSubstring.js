function expand(s, left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        left--;
        right++;
    }
    return s.slice(left + 1, right);
}

var longestPalindrome = function(s) {
    let best = "";

    for (let i = 0; i < s.length; i++) {
        const odd = expand(s, i, i);       // centro en una letra: "aba"
        const even = expand(s, i, i + 1);  // centro entre dos letras: "abba"

        if (odd.length > best.length) best = odd;
        if (even.length > best.length) best = even;
    }

    return best;
};