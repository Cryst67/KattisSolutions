const readline = require('readline')

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

rl.on('line', line => {
	const nums = line.split(';')
	const noContig = nums.filter(str => !str.includes('-'))
	const contig = nums.filter(str => str.includes('-'))
	if (noContig.length === nums.length) {
		console.log(noContig.length)
		return
	}
	const problems = contig
		.map(str => str.split('-').map(x => parseInt(x)))
		.map(arr => {
			return arr[1] - arr[0] + 1
		})
		.reduce((x, y) => x + y)
	console.log(noContig.length + problems)
})
