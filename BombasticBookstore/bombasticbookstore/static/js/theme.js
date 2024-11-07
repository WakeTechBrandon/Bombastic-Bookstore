document.addEventListener('DOMContentLoaded', function() {
    const themeSelect = document.getElementById('theme-select');
    const currentTheme = document.body.className;

    themeSelect.value = currentTheme;

    themeSelect.addEventListener('change', function() {
        const selectedTheme = themeSelect.value;
        document.body.className = selectedTheme;
        document.getElementById('theme-link').href = `/static/css/${selectedTheme}.css`;
        document.cookie = `theme=${selectedTheme}; path=/;`;
    });
});
