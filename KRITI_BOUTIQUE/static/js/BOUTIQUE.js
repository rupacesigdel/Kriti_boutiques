const themeToggle = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('theme');

if (currentTheme === 'dark') {
document.documentElement.classList.add('dark-mode');
themeToggle.textContent = '☀️ Light Mode';
}

themeToggle.addEventListener('click', () => {
document.documentElement.classList.toggle('dark-mode');

let theme = 'light';
if (document.documentElement.classList.contains('dark-mode')) {
    theme = 'dark';
    themeToggle.textContent = '☀️ Light Mode';
} else {
    themeToggle.textContent = '🌙 Dark Mode';
}

localStorage.setItem('theme', theme);
});
