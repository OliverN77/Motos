document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.sidebar-toggle button');
    const sidebar = document.querySelector('.sidebar');
    
    // Toggle sidebar al hacer clic en la flecha
    toggleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        sidebar.classList.toggle('active');
    });
    
    // Cerrar sidebar al hacer clic fuera de ella
    document.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && !toggleBtn.contains(event.target)) {
            sidebar.classList.remove('active');
        }
    });
    
    // Evitar que los clics dentro del sidebar la cierren
    sidebar.addEventListener('click', function(e) {
        e.stopPropagation();
    });
    
    // Animación suave para las filas de la tabla
    const rows = document.querySelectorAll('table tr');
    rows.forEach((row, index) => {
        setTimeout(() => {
            row.style.opacity = '1';
            row.style.transform = 'translateY(0)';
        }, index * 50);
    });
});

// Funciones para el modal de confirmación
function openModal(event, element) {
    event.preventDefault();
    const modal = document.getElementById('deleteModal');
    const confirmBtn = document.getElementById('confirmDelete');
    const deleteUrl = element.getAttribute('data-url');
    
    confirmBtn.href = deleteUrl;
    modal.classList.add('active');
}

function closeModal() {
    const modal = document.getElementById('deleteModal');
    modal.classList.remove('active');
}

// Cerrar modal al hacer clic fuera de él
document.addEventListener('click', function(event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        closeModal();
    }
});

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

// Función para limpiar input individual
function clearInput(inputId) {
    const input = document.getElementById(inputId);
    if (input) {
        input.value = '';
        input.focus();
    }
}

// Función para alternar entre filtros básicos y avanzados
function toggleAdvancedFilters() {
    const basicFilters = document.getElementById('basicFilters');
    const advancedFilters = document.getElementById('advancedFilters');
    const toggleBtn = document.getElementById('advancedToggle');
    const toggleText = document.getElementById('toggleText');
    
    if (advancedFilters.style.display === 'none' || advancedFilters.style.display === '') {
        // Mostrar filtros avanzados
        basicFilters.style.display = 'none';
        advancedFilters.style.display = 'block';
        toggleBtn.classList.add('active');
        toggleText.textContent = 'Filtros Básicos';
    } else {
        // Mostrar filtros básicos
        advancedFilters.style.display = 'none';
        basicFilters.style.display = 'block';
        toggleBtn.classList.remove('active');
        toggleText.textContent = 'Filtros Avanzados';
    }
}