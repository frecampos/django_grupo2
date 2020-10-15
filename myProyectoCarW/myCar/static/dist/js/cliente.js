class cliente {
    rut;
    nombre;
    apellido;
    correo;
    edad;
    usuario;
    contrasena;

    setRut(rut) {
        this.rut = rut;
    }
    setNombre(nombre) {
        this.nombre = nombre;
    }
    setApellido(apellido) {
        this.apellido = apellido;
    }
    setCorreo(correo) {
        this.correo = correo;
    }
    setEdad(edad) {
        this.edad = edad;
    }
    setUsuario(usuario) {
        this.usuario = usuario;
    }
    setContrasena(contrasena) {
        this.contrasena = contrasena;
    }
    getRut() { return this.rut; }
    getNombre() { return this.nombre; }
    getApellido() { return this.apellido; }
    getCorreo() { return this.correo; }
    getEdad() { return this.edad; }
    getUsuario() { return this.usuario; }
    getContrasena() { return this.contrasena; }

    imprimir() {
        return "Rut:" + this.rut +
            " Nombre:" + this.nombre +
            " Apellido:" + this.apellido +
            " Correo:" + this.correo +
            " Edad:" + this.edad +
            " Usuario:" + this.usuario +
            " Contrasena:" + this.contrasena;
    }
}
