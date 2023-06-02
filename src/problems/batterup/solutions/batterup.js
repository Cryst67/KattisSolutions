//read from console 
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.once('line', n => 
    rl.once('line', arr =>
        {
            const nums = arr.split(' ').map(num => parseInt(num))
            const negatives = nums.filter(num => num === -1).length
            const nonNegSum = nums.filter(num => num > 0).reduce((x, y) => x + y, 0)
            const res = nonNegSum/(n - negatives)
            console.log(res)
        }
    )
)