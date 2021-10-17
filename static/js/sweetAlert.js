function agregarOtro() {
    

Swal.fire({
    title: '¿Quieres agregar otro?',
    text: 'QUieres añadir a la factura oto vehiculo',
    icon: 'question',
    allowEscapeKey: false,
    allowEnterKey: false,
    allowOutsideClick: false,
    
    showConfirmButton: true,
    confirmButtonText: 'Sí, sí quiero',
    confirmButtonArialLabel: 'Confrimar',
    
    showCancelButton: true,
    cancelButtonText: 'No, gracias',
    cancelButtonArialLabel: 'No, gracias',

    reverseButtons: true
}).then(function(result)  {
    if(result.isConfirmerd){
        location.reload();
    }else{
        window.location.href = "/factura/"
    }
})
}