document.getElementById('id_region').addEventListener('change', function () {
    var regionId = this.value;
    var comunaSelect = document.getElementById('id_comuna');
  
    // Reinicia las opciones de comuna
    comunaSelect.innerHTML = '<option>Seleccionar</option>';
  
    if (regionId) {
      console.log('regionId:', regionId);
  
      // Realiza una solicitud AJAX para obtener las comunas según la región seleccionada
      fetch('/obtener_comunas_por_region/?region_id=' + regionId)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log('Comunas recibidas:', data);
  
          // Agrega las opciones de comuna al elemento select
          data.forEach(function (comuna) {
            var option = document.createElement('option');
            option.value = comuna.ID_COMUNA;
            option.textContent = comuna.COMUNA;
            comunaSelect.appendChild(option);
          });
        });
    }
  });