// Validaciones Formulario Usuario
function validarRut() {
    var rut = document.getElementById("rut").value;
    if (rut.length != 10) {
        alert("Largo de rut incorrecto, debe tener 10 caracteres.");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut incorrecto.");
        return false;
    } else {
        // alert("Rut correcto.");
        return true;
    }
}

function validarFecha() {
    var fechaControl = document.getElementById("fecha_naci").value;
    var fechaSistema = new Date();
    if (fechaControl.length == 0) {
        alert("Fecha de nacimiento vacía.");
        return false;
    }
    /////////////////////////////////////
    var ano = fechaControl.slice(0, 4);
    var mes = fechaControl.slice(5, 7);
    var dia = fechaControl.slice(8, 10);
    ////////////////////////////////////
    var fechaDelControl = new Date(ano, (mes - 1), dia);
    ////////////////////////////////////
    if (fechaDelControl > fechaSistema) {
        alert("Fecha de nacimiento incorrecta.");
        return false;
    } else {
        //alert("Fecha correcta." + fechaControl);
        return true;
    }
}

function validarNombre() {
    var n = document.getElementById("nombres").value;
    if (n.trim().length > 2 && n.trim().length < 81) {
        return true;
    }
    alert("Largo de nombre incorrecto , debe estar entre 3 y 80 caracteres.");
    return false;
}

function validarApellido() {
    var a = document.getElementById("apellido").value;
    if (a.trim().length > 2 && a.trim().length < 81) {
        return true;
    }
    alert("Largo de apellido incorrecto, debe estar entre 3 y 80 caracteres.");
    return false;
}

function validarUsuario() {
    var u = document.getElementById("usuario").value;
    if (u.trim().length > 8) {
        return true;
    }
    alert("Largo de usuario incorrecto, debe ser mayor a 8 caracteres.");
    return false;
}

function validarContraseña() {
    var p = document.getElementById("passw").value;
    if (p.trim().length > 8) {
        return true;
    }
    alert("Largo de contraseña incorrecto, debe ser mayor a 8 caracteres.");
    return false;

}

function validarTodo_formularioUsuario() {
    var resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validarNombre();
    if (resp == false) {
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        return false;
    }
    resp = validarFecha();
    if (resp == false) {
        return false;
    }
    resp = validarUsuario();
    if (resp == false) {
        return false;
    }
    resp = validarContraseña();
    if (resp == false) {
        return false;
    }

}

// Validaciones Formulario Insumo
function validarNombre_Insumo() {
    var n = document.getElementById("nombreInsumo").value;
    if (n.length > 2 && n.length < 121) {
        return true;
    }
    alert("Largo de nombre incorrecto, debe estar entre 3 y 120 caracteres.");
    return false;
}

function validarPrecio_Insumo() {
    var n = document.getElementById("precio").value;
    if (n > 0) {
        return true;
    }
    alert("Precio de insumo incorrecto, debe ser mayor a 0");
    return false;
}

function validarDescripcion_Insumo() {
    var n = document.getElementById("descrip").value;
    if ((n.length > 2 && n.length < 121) || n.length == 0) {
        return true;
    }
    alert("Largo de descripción incorrecto, debe estar entre 3 y 200 caracteres.");
    return false;
}

function validarTodo_formularioInsumo() {
    var resp = validarNombre_Insumo();
    if (resp == false) {
        return false;
    }
    resp = validarPrecio_Insumo();
    if (resp == false) {
        return false;
    }
    resp = validarDescripcion_Insumo();
    if (resp == false) {
        return false;
    }
}