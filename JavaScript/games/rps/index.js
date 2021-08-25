const readline = require('readline')

// accepting user input 
readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

// function for the computer 
function Computer() {
    let computer = Math.random()
    if (computer <= 0.39) {
        
        computer = "Rock"
        console.log(computer)
    } else if (computer <= 0.69) {
        computer = "Paper"
        console.log(computer)
    } else {
        computer = "Scissors"
        console.log(computer)
    }
}

