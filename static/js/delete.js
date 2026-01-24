document.addEventListener('DOMContentLoaded', function() {
    const modal = document.querySelector('.modal');
    const overlay = document.querySelector('.overlay');
    
    // Animación inicial
    setTimeout(() => {
        modal.style.animation = 'modalSlideIn 0.4s ease';
    }, 100);

    // Redirección automática después de 3 segundos
    setTimeout(() => {
        // Animación de salida
        modal.style.animation = 'modalSlideOut 0.4s ease';
        overlay.style.animation = 'fadeOut 0.4s ease';
        
        setTimeout(() => {
            window.location.href = "/";
        }, 400);
    }, 3000);
});

// Animaciones de salida
const style = document.createElement('style');
style.textContent = `
    @keyframes modalSlideOut {
        from {
            opacity: 1;
            transform: translate(-50%, -50%);
        }
        to {
            opacity: 0;
            transform: translate(-50%, -40%);
        }
    }
    
    @keyframes fadeOut {
        from {
            opacity: 1;
        }
        to {
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);