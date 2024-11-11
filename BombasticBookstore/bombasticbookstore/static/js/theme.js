document.addEventListener('DOMContentLoaded', function() {
    const themeSelect = document.getElementById('theme-select');
    if (themeSelect) {
        const currentTheme = getCookie('theme') || 'light';

        console.log('Current theme:', currentTheme); // Debugging

        document.body.className = currentTheme;
        themeSelect.value = currentTheme;

        applyTheme(currentTheme);

        themeSelect.addEventListener('change', function() {
            const selectedTheme = themeSelect.value;
            console.log('Selected theme:', selectedTheme); // Debugging
            document.body.className = selectedTheme;
            setCookie('theme', selectedTheme, 365);
            applyTheme(selectedTheme);
        });
    } else {
        console.error('Theme select element not found');
    }
});

function applyTheme(theme) {
    const elementsToTheme = document.querySelectorAll('.theme-dependent, .search-card');

    elementsToTheme.forEach(element => {
        if (theme === 'dark') {
            element.classList.add('dark');
        } else {
            element.classList.remove('dark');
        }
    });
}

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
