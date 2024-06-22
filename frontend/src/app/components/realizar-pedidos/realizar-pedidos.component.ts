import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

interface Producto {
  nombre: string;
  cantidad: number;
  empaque: string;
  unidades: number;
}

@Component({
  selector: 'app-realizar-pedidos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './realizar-pedidos.component.html',
  styleUrl: './realizar-pedidos.component.css'
})
export class RealizarPedidosComponent {

  producto: string = '';
  cantidad: number = 0;
  empaque: string = '';
  unidades: number = 0;
  productos: Producto[] = [];

  agregarProducto() {
    if (this.producto && this.cantidad && this.empaque && this.unidades) {
      const nuevoProducto: Producto = {
        nombre: this.producto,
        cantidad: this.cantidad,
        empaque: this.empaque,
        unidades: this.unidades
      };
      this.productos.push(nuevoProducto);
      this.producto = '';
      this.cantidad = 0;
      this.empaque = '';
      this.unidades = 0;
    }
  }

  enviarProductos() {
    // Aquí puedes enviar los productos a tu backend u otro servicio
    console.log(this.productos);
    // Lógica para enviar los productos
  }
}
