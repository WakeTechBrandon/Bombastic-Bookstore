document.addEventListener("DOMContentLoaded", function() {
    const navBar = document.getElementById('nav-bar');
    const path = window.location.pathname;
  
    if (path.includes('index')) {
      navBar.classList.add('index');
    } else if (path.includes('add_book')) {
      navBar.classList.add('add_book');
    } else if (path.includes('search')) {
      navBar.classList.add('search');
    } else if (path.includes('view_all')) {
      navBar.classList.add('view_all');
    } else if (path.includes('generate_report')) {
      navBar.classList.add('generate_report');
    } else if (path.includes('settings')) {
      navBar.classList.add('settings');
    } else if (path.includes('logout')) {
      navBar.classList.add('logout');
    } else if (path.includes('about')) {
      navBar.classList.add('about');
    }
  });
  