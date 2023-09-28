// Comentarios -- Abrir box de opções

let opcoes = document.querySelectorAll('.opcoes')
let boxopcoes = document.querySelectorAll('.boxopcoes')

opcoes.forEach((opcao, index) => {
    opcao.addEventListener('click', () => {
        if (boxopcoes[index].classList.contains('ativo')) {
            boxopcoes[index].classList.remove('ativo')
            boxopcoes[index].classList.add('desativado')
        } else {
            boxopcoes[index].classList.add('ativo')
            boxopcoes[index].classList.remove('desativado')
        }
})
});

// Editar um post ou comentario

let editarBtn = document.querySelectorAll('.editarBtn')
let boxeditarpost = document.querySelectorAll('.boxeditarpost')
let opcoesFechar = document.querySelectorAll('.opcoesFechar')

editarBtn.forEach((editar, index) => {
    editar.addEventListener('click', () => {
        boxeditarpost[index].classList.toggle('ativo')
})
});

opcoesFechar.forEach((fechar, index) => {
    fechar.addEventListener('click', () => {
        boxeditarpost[index].classList.toggle('ativo')
})
});