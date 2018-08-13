// 给定两个整数 n 和 k，返回 1 ...n 中所有可能的 k 个数的组合。
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */

// combines(n,k) = [[n]+ i for i in combines(n-1,k-1)] + [combines(n-1,k)]

const combine = (n, k) => {
    let r = []
    // if (k > n) {
    //     return r
    // }
    if (k == 1) {
        for (let index = 1; index <= n; index++) {
            r.push([index])
        }
        return r
    }
    if (k < n) {
        let first = combine(n - 1, k - 1)
        let second = combine(n - 1, k)
        for (let index = 0; index < first.length; index++) {
            const element = first[index];
            r.push(element.concat(n))
            console.log(r)
        }
        r = r.concat(second)
        return r
    }
    if (k == n) {
        let xs = combine(n - 1, k - 1)
        for (let index = 0; index < xs.length; index++) {
            const element = xs[index]
            r.push([n].concat(element))
        }
        return r
    }
}
console.log(combine(8, 1))
console.log(combine(8, 8))
console.log(combine(4, 2))