const scrollToTopButton = document.getElementById('scrollToTopButton');

// Показываем кнопку, когда пользователь прокручивает страницу вниз на 100px
window.addEventListener('scroll', function() {
  if (window.scrollY > 100) {
    scrollToTopButton.style.display = 'block';
  } else {
    scrollToTopButton.style.display = 'none';
  }
});

// Прокручиваем страницу наверх при нажатии на кнопку
scrollToTopButton.addEventListener('click', function() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});