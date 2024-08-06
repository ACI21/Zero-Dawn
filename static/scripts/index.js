document.addEventListener('DOMContentLoaded', (event) => {
    const cajas = document.querySelectorAll('.caja');
    const modal = document.getElementById('passwordModal');
    const span = document.getElementsByClassName('close')[0];
    const form = document.getElementById('passwordForm');
    const passwordInput = form.querySelector('input[name="password"]');

    cajas.forEach(caja => {
        caja.addEventListener('click', function() {
            const cajaId = this.getAttribute('data-caja-id');
            const pista = this.getAttribute('data-pista');
            form.setAttribute('action', `/abrir_caja/${cajaId}`);
            passwordInput.setAttribute('placeholder', pista);
            modal.style.display = 'block';
        });
    });

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
