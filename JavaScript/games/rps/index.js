
const prompt = require('prompt-sync')({
    'fake_val': 'OPTIONAL CONFIG VALUES HERE'
});


const HumanResponse = prompt("What is your choice: Rock, Paper, Scissors: ")

console.log(HumanResponse)

// function for the computer 
function Computer() {
    let computer = Math.random()
    if (computer <= 0.39) {
        computer = "Rock"
        console.log(computer)
        return computer
    } else if (computer <= 0.69) {
        computer = "Paper"
        console.log(computer)
        return computer
    } else {
        computer = "Scissors"
        
        return computer
    }
}

function is_win(human, computer) {
    if (human == "Paper" && computer == "Rock") {
        return true
    } else if (human == "Scissors" && computer == "Paper" ){
        return true
    } else if (human == "Rock" && computer == "Scissors") {
        return true
    } else return false
}

var results = is_win()
console.log(results)
Computer()

let_play()
function let_play(human, computer){
    if (is_win()) {
        console.log("You Won") 
    } else if (human === computer) {N
        console.log("it's a draw") 
    } else {console.log("You Lost") } 
    
}



