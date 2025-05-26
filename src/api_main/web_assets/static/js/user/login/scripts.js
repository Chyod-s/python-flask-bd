document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = e.target.username.value;
    const password = e.target.password.value;

    const data = { user_name_email: username, password: password };
    const msgEl = document.getElementById('message');

    try {
        const res = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('auth_token') || ''}`
            },
            body: JSON.stringify(data),
            credentials: 'include'  
        });
    
        const responseData = await res.json();
        
        if (res.ok) {
            msgEl.style.color = 'green';
            msgEl.textContent = responseData.message;

            if (responseData?.data?.user_name) {
                sessionStorage.setItem('user_name', responseData.data.user_name);
                sessionStorage.setItem('auth_token', responseData.data.token);
                sessionStorage.setItem('csrf_token', responseData.data.csrf_token);
            }

            setTimeout(() => {
                const token = sessionStorage.getItem('auth_token');
                
                console.log('Token:', token);

                if (token) {
                window.location.href = '/example';
                }
            }, 1000);
        } else {
            msgEl.style.color = 'red';
            msgEl.textContent = responseData.message || 'Erro ao fazer login.';
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro de conexão com o servidor.';
    }
});

document.getElementById('register-link').addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = '/register';
});