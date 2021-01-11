const howSum = (targetSum, numbers) => {
  const memo = {};

  function helper(targetSum) {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let num of numbers) {
      const remainder = targetSum - num;
      const remainderResult = helper(remainder);

      if (remainderResult !== null) {
        memo[targetSum] = [...remainderResult, num];
        return memo[targetSum];
      }
    }

    memo[targetSum] = null;
    return null;
  }

  return helper(targetSum);
};

console.log(howSum(7, [2, 3]));
console.log(howSum(300, [7, 14]));
