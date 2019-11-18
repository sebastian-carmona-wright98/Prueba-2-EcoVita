/* Método para que el formulario sea dinámico  */
/* Acá se llaman a las clases input-100 para que los label aparezcan sobre las cajas cuando se seleccione y se complete */
/* Cuando se limpia las cajas se remueve el fijado */
var inputs = document.getElementsByClassName('input-100');
for (var i =0; i < inputs.length; i++){
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijar');
        } else{
            this.nextElementSibling.classList.remove('fijar');
        }
    });
} 
/* Acá se llaman a las clases input-48 para que los label aparezcan sobre las cajas cuando se seleccione y se complete */
/* Cuando se limpia las cajas se remueve el fijado */
var inputs = document.getElementsByClassName('input-48');
for (var i =0; i < inputs.length; i++){
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijar');
        } else{
            this.nextElementSibling.classList.remove('fijar');
        }
    });
}
/* Acá se llaman a las clases input-48-2 (correo) para que los label aparezcan sobre las cajas cuando se seleccione y se complete */
/* Cuando se limpia las cajas se remueve el fijado */
var inputs = document.getElementsByClassName('input-48-2');
for (var i =0; i < inputs.length; i++){
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijarmail');
        } else{
            this.nextElementSibling.classList.remove('fijarmail');
        }
    });
}
/* Acá se llaman a las clases input-1 (mensaje) para que los label aparezcan sobre las cajas cuando se seleccione y se complete */
/* Cuando se limpia las cajas se remueve el fijado */
var inputs = document.getElementsByClassName('input-1');
for (var i =0; i < inputs.length; i++){
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijarmessage');
        } else{
            this.nextElementSibling.classList.remove('fijarmessage');
        }
    });
}