document.addEventListener('DOMContentLoaded', (event) => {
    const cajas = document.querySelectorAll('.caja');
    const modal = document.getElementById('passwordModal');
    const rewardModal = document.getElementById('rewardModal');  // Nueva modal para el regalo
    const span = document.getElementsByClassName('close')[0];
    const rewardSpan = document.getElementsByClassName('reward-close')[0];  // Cerrar modal de recompensa
    const form = document.getElementById('passwordForm');
    const passwordInput = form.querySelector('input[name="contrasenya"]');

    let selectedCaja = null;  // Variable para almacenar la caja seleccionada

    // Agregar evento de clic a cada caja
    cajas.forEach(caja => {
        caja.addEventListener('click', function() {
            const cajaId = this.getAttribute('data-caja-id');
            const pista = this.getAttribute('data-pista');
            form.setAttribute('action', `/abrir_caja/${cajaId}`);
            passwordInput.setAttribute('placeholder', pista);
            modal.style.display = 'block';
            selectedCaja = this;  // Guardar la caja seleccionada
        });
    });

    // Cerrar modal de contraseña
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // Cerrar modal de recompensa
    rewardSpan.onclick = function() {
        rewardModal.style.display = 'none';

        // Deshabilitar la caja y cambiar la imagen
        if (selectedCaja) {
            selectedCaja.querySelector('img').src = "/static/img/caja_abierta.png";
            selectedCaja.style.pointerEvents = 'none';  // Deshabilitar la caja
        }
    }

    // Cerrar modal al hacer clic fuera del contenido
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        } else if (event.target == rewardModal) {
            rewardModal.style.display = 'none';

            // Deshabilitar la caja y cambiar la imagen
            if (selectedCaja) {
                selectedCaja.querySelector('img').src = "/static/img/caja_abierta.png";
                selectedCaja.style.pointerEvents = 'none';  // Deshabilitar la caja
            }
        }
    }

    // Manejar el envío del formulario de contraseña
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevenir la recarga de la página

        const formData = new FormData(form);
        const cajaId = form.getAttribute('action').split('/').pop();

        fetch(`/abrir_caja/${cajaId}`, {
            method: 'POST',
            body: formData
        }).then(response => response.json()).then(data => {
            if (data.success) {
                modal.style.display = 'none';  // Cerrar modal de contraseña
                rewardModal.style.display = 'block';  // Mostrar modal de recompensa
                document.getElementById('rewardImage').src = `/static/img/regalo${cajaId}.png`;  // Mostrar la imagen del regalo
            } else {
                alert('Contraseña incorrecta');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });
});
