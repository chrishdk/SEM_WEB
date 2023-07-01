function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  document.getElementById("export-btn").addEventListener("click", function() {
    var csrftoken = getCookie('csrftoken');
  
    var tableData = [];
    var rows = document.querySelectorAll("#dataTable tbody tr");
  
    // Recorre todas las filas de la tabla y extrae los datos de cada celda
    rows.forEach(function(row) {
      var rowData = [];
      row.querySelectorAll("td").forEach(function(cell) {
        rowData.push(cell.innerText);
      });
      tableData.push(rowData);
    });
  
    fetch("/export/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken  // Incluye el token CSRF en el encabezado de la solicitud
      },
      body: JSON.stringify({ data: tableData })
    })
    .then(function(response) {
      return response.blob();
    })
    .then(function(blob) {
      // Crea un objeto URL para el blob y crea un enlace de descarga
      var url = URL.createObjectURL(blob);
      var link = document.createElement("a");
      link.href = url;
      link.download = "tabla.xlsx";
      link.click();
    });
  });
  
  