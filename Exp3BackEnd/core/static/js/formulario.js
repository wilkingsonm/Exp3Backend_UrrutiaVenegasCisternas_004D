
    $(function() 
    {
      $("#mi-formulario").validate({
           rules: {
                  email: {
                      required: true,
                      email: true
                  },
                  password: "required",
                  fono: "required",
                  nombre: "required",
                  password2: {
                      required: true,
                      equalTo: "#password"
                  }   
                  
              }, //rules
          messages: {
              email: {
                  required: 'Ingresa tu correo electrónico',
                  email: 'Formato de correo no válido'
              },
              password: {
                  required: 'Ingresa una contraseña',
                  minlength: 'Caracteres insuficientes'
              },
              fono:{
                  required: 'Ingrese un número de celular',
                  minlength: 'Cantidad de digitos insuficiente'
              },
              nombre:{
                  required: 'Ingrese Nombre',
                  minlength: 'Cantidad de digitos insuficiente'
              },
              password2: {
                  required: 'Reingresa la contraseña',
                  equalTo: 'Las contraseñas ingresadas no coinciden',
                  minlength: 'Caracteres insuficientes'


              }
          }//messages
      }); //$('#mi-formulario').validate
  }); //function 


