function scrollToSection(id) {
  document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section');
  let currentSection = '';

  sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (pageYOffset >= sectionTop - 50) {
          currentSection = section.getAttribute('id');
      }
  });

  if (currentSection) {
      history.replaceState(null, null, `#${currentSection}`);
  }
});