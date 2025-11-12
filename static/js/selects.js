console.log("ASDOKJASLDJASÑLDASLD")

document.addEventListener('DOMContentLoaded', function() {
    const regionSelect = document.getElementById('region')
    const provinciaSelect = document.getElementById('provincia')
    const comunaSelect = document.getElementById('comuna')

    fetch('/api/regiones')
        .then(response => response.json())
        .then(regiones => {
            regiones.forEach(region => {
                const option = document.createElement('option')
                option.value = region.id
                option.textContent = "REGION " + region.nombre
                regionSelect.appendChild(option)
            })
        })

    regionSelect.addEventListener('change', function() {
        regionId = this.value

        // Resetear y deshabilitar selects dependientes
        provinciaSelect.innerHTML = '<option value="">Seleccione una provincia</option>';
        provinciaSelect.disabled = !regionId;
        
        comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
        comunaSelect.disabled = true;

        if(regionId){
            fetch('/api/provincias/' + regionId)
                .then(response => response.json())
                .then(provincias => {
                    provincias.forEach(provincia => {
                        const option = document.createElement('option')
                        option.value = provincia.id
                        option.textContent = provincia.nombre
                        provinciaSelect.appendChild(option)
                    })
                    provinciaSelect.disabled = false
                })
        }
    })
    // Evento cuando cambia la provincia
    provinciaSelect.addEventListener('change', function() {
        const provinciaId = this.value;
        
        // Resetear comuna
        comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
        comunaSelect.disabled = !provinciaId;

        if (provinciaId) {
            // Cargar comunas de la provincia seleccionada
            fetch(`/api/comunas/${provinciaId}`)
                .then(response => response.json())
                .then(comunas => {
                    comunas.forEach(comuna => {
                        const option = document.createElement('option');
                        const capitalizedNombre = comuna.nombre.charAt(0).toUpperCase() + comuna.nombre.slice(1).toLowerCase();
                        option.value = capitalizedNombre;
                        option.textContent = comuna.nombre;
                        comunaSelect.appendChild(option);
                    });
                    comunaSelect.disabled = false;
                });
        }
    });
})