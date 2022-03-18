document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#alert').style.visibility = 'hidden';
    const button = document.querySelector('#button-addon2');
    const url = document.querySelector('#inurl');
    button.addEventListener('click', () => gen_url(url.value));


})

function gen_url(old_url) {
    fetch(`shorten/${old_url}`)
        .then(response => response.json())
        .then(new_url => {
            console.log(new_url);
            document.querySelector('#url-message').innerHTML = new_url.shortened_url;
            document.querySelector('#alert').style.visibility = 'visible';
        })
        .catch(error => console.log(error))
}