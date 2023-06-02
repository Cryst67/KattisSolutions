//read from console 
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.once('line', string => 
    {
        const str = string.split('()').map(s => s.length)
        str[0] === str[1] ? console.log('correct') : console.log('fix')
    }
)