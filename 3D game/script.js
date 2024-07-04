const scene = document.querySelector('a-scene');
let score = 0;
let timeLeft = 30;
let timerInterval;
let isGameRunning = true;

function createTarget() {
    const positionX = Math.random() * 10 - 5;
    const positionY = Math.random() * 4;
    const positionZ = -10;

    const target = document.createElement('a-sphere');
    target.setAttribute('class', 'target');
    target.setAttribute('position', `${positionX} ${positionY} ${positionZ}`);
    target.setAttribute('radius', '0.5');
    target.setAttribute('color', '#FF0000');
    target.setAttribute('material', 'emissive: #808080; emissiveIntensity: 1');

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

function spawnTargets() {
    if (!isGameRunning) return;

    createTarget();
    const randomTime = Math.random() * 1000 + 500;

    setTimeout(spawnTargets, randomTime);
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
    isGameRunning = false;
    clearInterval(timerInterval);
    alert(`Game Over! Your score is ${score}`);
}

function startGame() {
    isGameRunning = true;
    timerInterval = setInterval(updateTimer, 1000);
    spawnTargets();
}

startGame();
