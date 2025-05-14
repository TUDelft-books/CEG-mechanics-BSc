document.querySelectorAll('.caption-number').forEach(element => {
    element.innerHTML = element.innerHTML.replace(/Example (\d+)/, 'Voorbeeld $1');
});