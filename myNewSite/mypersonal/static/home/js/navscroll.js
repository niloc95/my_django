  // Get the Navbar element
  const navbar = document.querySelector('nav');

  // Function to toggle the 'sticky' class
  function toggleSticky() {
      if (window.scrollY > 1000) {
          navbar.classList.add('sticky');
      } else {
          navbar.classList.remove('sticky');
      }
  }

  // Listen for scroll events and call toggleSticky()
  window.addEventListener('scroll', toggleSticky);
