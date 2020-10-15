class insumo {
    nombre;
    precio;
    descripcion;

    setNombre(nombre) {
        this.nombre = nombre;
    }
    setPrecio(precio) {
        this.precio = precio;
    }
    setDescripcion(descripcion) {
        this.descripcion = descripcion;
    }
    getNombre() { return this.nombre; }
    getPrecio() { return this.precio; }
    getDescripcion() { return this.descripcion; }

    imprimir() {
        return "Nombre:" + this.nombre + " Precio:" + this.precio + " Descripcion:" + this.descripcion;
    }
}