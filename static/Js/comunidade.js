// Comunidade -- mudar css do botao "Enviar fotos"

let image = document.getElementById('image');
let label = document.querySelector('.image');
image.addEventListener('change', function() {
    if (image.value != '') {
        label.classList.add('com_foto')
        label.innerHTML = 'Foto enviada'
    } else {
        label.classList.remove('com_foto')
        label.innerHTML = 'Enviar fotos'
    }
});