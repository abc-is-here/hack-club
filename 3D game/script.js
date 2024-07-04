const scene = document.querySelector('a-scene');
let score = 0;
let timeLeft = 30;
let gameInterval;
let timerInterval;

function createTarget() {
    const positionX = Math.random() * 10 - 5;
    const positionY = Math.random() * 4;
    const positionZ = -10;

    const target = document.createElement('a-sphere');
    target.setAttribute('class', 'target');
    target.setAttribute('position', `${positionX} ${positionY} ${positionZ}`);
    target.setAttribute('radius', '0.5');
    target.setAttribute('color', '#FFC65D');

    target.addEventListener('click', function() {
        score++;
        updateScore();
        this.parentNode.removeChild(this);
    });

    setTimeout(() => {
        if (target.parentNode) {
            target.parentNode.removeChild(target);
        }
    }, 1000);

    scene.appendChild(target);
}

function updateScore() {
    const scoreElement = document.getElementById('score');
    scoreElement.setAttribute('value', `Score: ${score}`);
}

function updateTimer() {
    const timerElement = document.getElementById('timer');
    timerElement.setAttribute('value', `Time: ${timeLeft}`);
    timeLeft--;

    if (timeLeft < 0) {
        endGame();
    }
}

function endGame() {
    clearInterval(gameInterval);
    clearInterval(timerInterval);
    alert(`Game Over! Your score is ${score}`);
}

function startGame() {
    gameInterval = setInterval(createTarget, 1000);
    timerInterval = setInterval(updateTimer, 1000);
}

startGame();
