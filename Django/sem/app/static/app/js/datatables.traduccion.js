// document.getElementById('filtroInsumos').addEventListener('input', function() {
//     filtrarInsumos();
// });

// function filtrarInsumos() {
//     var filtro = document.getElementById('filtroInsumos').value.toUpperCase();
//     var tabla = document.getElementById('tablaInsumos');
//     var filas = tabla.getElementsByTagName('tr');

//     for (var i = 0; i < filas.length; i++) {
//         var mostrarFila = false;
//         var celdas = filas[i].getElementsByTagName('td');

//         for (var j = 0; j < celdas.length; j++) {
//             var textoCelda = celdas[j].textContent || celdas[j].innerText;
//             if (textoCelda.toUpperCase().indexOf(filtro) > -1) {
//                 mostrarFila = true;
//                 break;
//             }
//         }

//         if (mostrarFila) {
//             filas[i].style.display = '';
//         } else {
//             filas[i].style.display = 'none';
//         }
//     }
// }

// $(document).ready(function() {
//     $('#dataTable').DataTable({
//       "paging": true,
//       "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
//       "pageLength": 10
//     });
//   });

// $(document).ready(function() {
//     $('#dataTable').DataTable({
//       "language": {
//         "sLengthMenu": "Mostrar _MENU_ registros por página",
//         "sSearch": "Buscar:",
//         // Otros textos en español que desees modificar
//       }
//     });
//   });

  $(document).ready(function() {
    $('#dataTable').DataTable({
      "language": {
        "sEmptyTable": "No hay datos disponibles en la tabla",
        "sInfo": "Mostrando _START_ al _END_ de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando 0 al 0 de 0 registros",
        "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
        "sInfoPostFix": "",
        "sInfoThousands": ",",
        "sLengthMenu": "Mostrar _MENU_ registros por página",
        "sLoadingRecords": "Cargando...",
        "sProcessing": "Procesando...",
        "sSearch": "Buscar:",
        "sZeroRecords": "No se encontraron registros coincidentes",
        "oPaginate": {
          "sFirst": "Primero",
          "sLast": "Último",
          "sNext": "Siguiente",
          "sPrevious": "Anterior",
          "sLengthMenu": "Mostrar _MENU_ registros por página",
          "sSearch": "Buscar:",
        },
        "oAria": {
          "sSortAscending": ": activar para ordenar la columna en orden ascendente",
          "sSortDescending": ": activar para ordenar la columna en orden descendente"
        }
      }
    });
  });