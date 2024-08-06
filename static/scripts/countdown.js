document.addEventListener('DOMContentLoaded', (event) => {
    const daysElement = document.getElementById('days');
    const hoursElement = document.getElementById('hours');
    const minutesElement = document.getElementById('minutes');
    const secondsElement = document.getElementById('seconds');
    const targetDate = new Date('September 15, 2024 00:00:00').getTime();

    function updateCountdown() {
        const now = new Date().getTime();
        const difference = targetDate - now;

        if (difference < 0) {
            daysElement.innerHTML = '0<span>Días</span>';
            hoursElement.innerHTML = '0<span>Horas</span>';
            minutesElement.innerHTML = '0<span>Minutos</span>';
            secondsElement.innerHTML = '0<span>Segundos</span>';

            // Llama a la función para mostrar confeti
            showConfetti();
            return;
        }

        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        daysElement.innerHTML = `${days}<span>Días</span>`;
        hoursElement.innerHTML = `${hours}<span>Horas</span>`;
        minutesElement.innerHTML = `${minutes}<span>Minutos</span>`;
        secondsElement.innerHTML = `${seconds}<span>Segundos</span>`;
    }

    function showConfetti() {
        const duration = 5 * 1000; // Duración del confeti en milisegundos
        const end = Date.now() + duration;

        (function frame() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            } else {
                // Espera 5 segundos después de que termine el confeti
                setTimeout(() => {
                    window.location.href = '/'; // la URL absoluta de index.html Redirige a la página de inicio
                }, 5000);
            }
        })();
    }

    setInterval(updateCountdown, 1000);
    updateCountdown();
});
