func isHappy(n int) bool {
    slow := n
    fast := sumOfN(n)

    fmt.Println(slow, fast)

    for slow != fast {
        fast = sumOfN(fast)
        fast = sumOfN(fast)
        slow = sumOfN(slow)
    }

    return fast == 1
}

func sumOfN(n int) int {
    var result int = 0

    for n>0 {
        digit := n%10
        n =int(n/10)
        result += digit*digit
    }

    return result
}
