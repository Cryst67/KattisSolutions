//read from console 
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.once('line', string => 
    {
        const str = string.split(' ').map(str => parseInt(str))
        let start;
        let end;
        if (str[0] > str[1]) {
            start = str[1]
            end = str[0]
        }
        else{
            start = str[0]
            end = str[1]
        }
        for(let i = start + 1; i < end + 2; i++) console.log(i)
    }
)