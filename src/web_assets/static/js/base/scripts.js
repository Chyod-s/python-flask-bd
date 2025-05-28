document.getElementById('logout')?.addEventListener('click', (e) => {
    e.preventDefault();
    sessionStorage.removeItem('auth_token'); 
    sessionStorage.removeItem('user_name');
    sessionStorage.removeItem('csrf_token');
    window.location.href = '/logout';
});
