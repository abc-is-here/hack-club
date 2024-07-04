const scene = document.querySelector('a-scene');
let score = 0;

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

    scene.appendChild(target);
}

function updateScore() {
    const scoreElement = document.getElementById('score');
    scoreElement.setAttribute('value', `Score: ${score}`);
}
setInterval(createTarget, 1000);
