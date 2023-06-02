//read from console 
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    const res = [...line].map(char => char.toLowerCase()).filter(char => vowels.includes(char)).length
    console.log(res)
});
    