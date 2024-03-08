function fetch_cities() {
const provinceSelect = document.getElementById('province');
const citySelect = document.getElementById('city');

const province = provinceSelect.value;

fetch(`/get_cities/?province=${province}`)
    .then(response => response.json())
    .then(data => {
        citySelect.innerHTML = ''; // Limpiar las opciones actuales
        data.cities.forEach(city => {
            const option = document.createElement('option');
            option.text = city;
            option.value = city;
            citySelect.appendChild(option);
        });
    });
}