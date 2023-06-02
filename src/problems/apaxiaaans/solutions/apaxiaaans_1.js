//read from console 
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.once('line', string => 
    {
        const noRepeat = [...string].filter((char, i, strArr) => {
                if(i === strArr.length - 1) return true
                if(strArr[i + 1] === char) return false
                return true
        }).join('')
        console.log(noRepeat)
    }
)