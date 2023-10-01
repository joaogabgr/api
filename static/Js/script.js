//  Abrir boxlogin

let btnProfile = document.querySelector('.btnProfile')
let popAccount = document.querySelector('.boxLogin')
let arrow = document.querySelector('.arrow')

btnProfile.addEventListener('click', () => {
    popAccount.classList.toggle('ativo')
    arrow.classList.toggle('arrowativo')
})

// Abrir menuMobileBox

let btnMenu = document.querySelector('.menuMobile')
let menuMobileBox = document.querySelector('.menuMobileBox')

btnMenu.addEventListener('click', () => {
    if (menuMobileBox.classList.contains('ativo')) {
        menuMobileBox.classList.remove('ativo')
        menuMobileBox.classList.add('desativado')
        btnMenu.classList.remove('ativo')
        btnMenu.classList.add('desativado')
    } else {
        menuMobileBox.classList.remove('desativado')
        menuMobileBox.classList.add('ativo')
        btnMenu.classList.remove('desativado')
        btnMenu.classList.add('ativo')
    }
})