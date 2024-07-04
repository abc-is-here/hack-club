const scene = document.querySelector('a-scene');
const backgroundElements = document.getElementById('background-elements');
let score = 0;
let timeLeft = 30;
let timerInterval;
let isGameRunning = false;

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

    target.setAttribute('animation', 'property: scale; to: 2 2 2; dur: 1000; easing: easeInOutQuad');

    target.addEventListener('click', function() {
        score++;
        updateScore();
        this.parentNode.removeChild(this);
    });

    setTimeout(() => {
        if (target.parentNode) {
            target.parentNode.removeChild(target);
        }
    }, 900);

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
    scoreElement.setAttribute('visible', true);
}

function updateTimer() {
    const timerElement = document.getElementById('timer');
    timerElement.setAttribute('value', `Time: ${timeLeft}`);
    timerElement.setAttribute('visible', true);
    timeLeft--;

    if (timeLeft < 0) {
        endGame();
    }
}

function endGame() {
    isGameRunning = false;
    clearInterval(timerInterval);
    document.getElementById('end-screen').style.display = 'flex';
    document.getElementById('final-score').innerText = `Your score is ${score}`;
}


function restartGame() {
    score = 0;
    timeLeft = 30;
    isGameRunning = true;
    updateScore();
    updateTimer();

    document.getElementById('end-screen').style.display = 'none';

    timerInterval = setInterval(updateTimer, 1000);
    spawnTargets();
}

function startGame() {
    isGameRunning = true;
    timerInterval = setInterval(updateTimer, 1000);
    spawnTargets();
}


function createBackgroundElements() {
    const colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8'];
    for (let i = 0; i < 50; i++) {
        const cube = document.createElement('a-box');
        const positionX = Math.random() * 20 - 10;
        const positionY = Math.random() * 10 - 5;
        const positionZ = Math.random() * -20 - 10;
        const size = Math.random() * 0.5 + 0.2;

        cube.setAttribute('position', `${positionX} ${positionY} ${positionZ}`);
        cube.setAttribute('scale', `${size} ${size} ${size}`);
        cube.setAttribute('color', colors[Math.floor(Math.random() * colors.length)]);

        cube.setAttribute('animation', {
            property: 'rotation',
            to: `${Math.random() * 360} ${Math.random() * 360} ${Math.random() * 360}`,
            loop: true,
            dur: 10000
        });

        backgroundElements.appendChild(cube);
    }
}

document.getElementById('start-button').addEventListener('click', () => {
    document.getElementById('start-screen').style.display = 'none';
    startGame();
});

document.getElementById('restart-button').addEventListener('click', restartGame);

createBackgroundElements();
