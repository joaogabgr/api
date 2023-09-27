// Comentarios -- Abrir box de opções

let opcoes = document.querySelectorAll('.opcoes')
let boxopcoes = document.querySelectorAll('.boxopcoes')

opcoes.forEach((opcao, index) => {
    opcao.addEventListener('click', () => {
        boxopcoes[index].classList.toggle('ativo')
})
});