document.addEventListener('DOMContentLoaded', () => {
    const notification = document.querySelector('#notification');
    if (notification) {
        setTimeout(() => {
            notification.style.transition = 'opacity 0.5s';
            notification.style.opacity = '0';
            setTimeout(() => {
                notification.style.display = 'none';
            }, 500); // Після завершення перехідного періоду
        }, 5000);
    }
});
