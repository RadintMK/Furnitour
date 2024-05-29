function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie!== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function() {
    var buyBtns = document.querySelectorAll('.buy-btn-two');

    buyBtns.forEach(function(btn) {
        btn.addEventListener('click', function(event) {
            event.preventDefault();
            var tourName = this.getAttribute('data-tour-name');
            addToCart(tourName);
        });
    });

    function addToCart(tourName) {
        fetch(`/add-to-cart/${encodeURIComponent(tourName)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken 
            },
            body: JSON.stringify({tour_name: tourName})
        })
    .then(response => {
            if (!response.ok) {
                throw new Error('Сетевой ответ не был успешным');
            }
            return response.json(); 
        })
    .then(data => {
            console.log(data); 
        })
    .catch(error => {
            console.error('Произошла проблема с операцией fetch:', error);
        });
    }
});