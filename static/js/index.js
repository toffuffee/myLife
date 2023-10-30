(function(){
    let text = 'Привет! Hi! Salut! 嗨。!'
    let content = document.querySelector('#content')
    
    for (let i in [...text]) {
      let letter = document.createElement('span')
      letter.textContent = [...text][i]
      if(letter.textContent.match(/\s/)) {
        letter.style.margin = 'auto 3px'
      }
      letter.style.animationDelay = i/10+'s'
      content.appendChild(letter)
    }

})();