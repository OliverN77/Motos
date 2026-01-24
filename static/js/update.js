document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('input:not([type="hidden"])');
    
    // Animación de entrada para los inputs
    inputs.forEach((input, index) => {
        input.style.opacity = '0';
        input.style.transform = 'translateX(-20px)';
        setTimeout(() => {
            input.style.transition = 'all 0.3s ease';
            input.style.opacity = '1';
            input.style.transform = 'translateX(0)';
        }, index * 100);
    });

    // Validación en tiempo real
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                this.style.borderColor = '#2A4359';
            } else {
                this.style.borderColor = '#D9D7D7';
            }
        });

        // Efecto de focus
        input.addEventListener('focus', function() {
            this.parentElement.querySelector('label').style.color = '#2A4359';
        });

        input.addEventListener('blur', function() {
            this.parentElement.querySelector('label').style.color = '#283540';
        });
    });

    // Validación al enviar el formulario
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (input.value.trim() === '') {
                isValid = false;
                input.style.borderColor = '#c62828';
                input.style.animation = 'shake 0.5s';
            }
        });

        if (!isValid) {
            e.preventDefault();
        }
    });

    // Eliminar mensaje después de 5 segundos
    const mensaje = document.querySelector('.mensaje');
    if (mensaje) {
        setTimeout(() => {
            mensaje.style.transition = 'all 0.3s ease';
            mensaje.style.opacity = '0';
            mensaje.style.transform = 'translateY(-10px)';
            setTimeout(() => mensaje.remove(), 300);
        }, 5000);
    }

    // Animación del ID display
    const idDisplay = document.querySelector('.id-display');
    if (idDisplay) {
        idDisplay.style.opacity = '0';
        idDisplay.style.transform = 'scale(0.9)';
        setTimeout(() => {
            idDisplay.style.transition = 'all 0.3s ease';
            idDisplay.style.opacity = '1';
            idDisplay.style.transform = 'scale(1)';
        }, 100);
    }
});

// Animación de shake para errores
const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }
`;
document.head.appendChild(style);