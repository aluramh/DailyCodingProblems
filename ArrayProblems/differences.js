// // Returns elements that are not repeated
// function difference (arr1, arr2) {
//   function flatten (arr) {
//     function traverse (arr) {
//       for (let item of arr) {
//         if (typeof item === 'number') items.push(item)
//         if (typeof item === 'object') traverse(item)
//       }
//     }

//     const items = []
//     traverse(arr)
//     return items
//   }

//   const arrA = flatten(arr1)
//   const arrB = flatten(arr2)

//   let i = 0
//   let j = 0
//   const differences = []

//   while (i < arrA.length || j < arrB.length) {
//     const itemA = arrA[i]
//     const itemB = arrB[j]
//     console.log(itemA, itemB)

//     if (itemA < itemB) {
//       differences.push(itemA)

//       while (arrA[i] && arrA[i] !== arrB[j]) {
//         differences.push(itemA)
//         i++
//       }
//     } else if (itemB < itemA) {
//       differences.push(itemB)

//       while (arrB[j] && arrB[j] !== arrA[i]) {
//         differences.push(itemB)
//         j++
//       }
//     } else if (!itemA) {
//       differences.push(itemB)
//       j++
//     } else if (!itemB) {
//       differences.push(itemA)
//       i++
//     } else {
//       i++
//       j++
//     }
//   }

//   return differences
// }

function difference (arr1, arr2) {
  var a1 = flatten(arr1, true)
  var a2 = flatten(arr2, true)

  var a = [],
    diff = []
  for (var i = 0; i < a1.length; i++) a[a1[i]] = false
  for (i = 0; i < a2.length; i++)
    if (a[a2[i]] === true) {
      delete a[a2[i]]
    } else a[a2[i]] = true
  for (var k in a) diff.push(k)
  return diff
}

var flatten = function (a, shallow, r) {
  if (!r) {
    r = []
  }
  if (shallow) {
    return r.concat.apply(r, a)
  }
  for (i = 0; i < a.length; i++) {
    if (a[i].constructor == Array) {
      flatten(a[i], shallow, r)
    } else {
      r.push(a[i])
    }
  }
  return r
}
console.log(difference([1, 2, 3], [100, 2, 1, 10]))
console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]], [5, 6]]))
console.log(difference([1, 2, 3], [100, 2, 1, 10]))

// console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]], [5, 6]]))

console.log(difference([1, 2, 3], [100, 2, 1, 10]))
// ["1", "2", "3", "10", "100"]
