let btnProfile = document.querySelector('.btnProfile')
let popAccount = document.querySelector('.boxLogin')
let arrow = document.querySelector('.arrow')

btnProfile.addEventListener('click', () => {
    popAccount.classList.toggle('ativo')
    arrow.classList.toggle('arrowativo')
})