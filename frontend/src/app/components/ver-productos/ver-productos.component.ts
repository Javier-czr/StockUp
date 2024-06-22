import { Component, OnInit } from '@angular/core';
import { IProducto } from '../../interfaces/i-producto'; 
import { ProductoService } from '../../services/producto.service';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { NgxPaginationModule } from 'ngx-pagination';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ver-productos',
  standalone: true,
  imports: [CommonModule, NgxPaginationModule, FormsModule],
  templateUrl: './ver-productos.component.html',
  styleUrl: './ver-productos.component.css'
})
export class VerProductosComponent implements OnInit {

  modalSwitchProducto: boolean;
  productoSeleccionado: IProducto;
  Producto: IProducto[] = [];
  page: number = 1;
  pageSize: number = 15;

  constructor(private productoService: ProductoService, private http: HttpClient) {}

  ngOnInit() {
    this.obtenerProductos();
  }

  obtenerProductos() {
    this.productoService.getProductos().subscribe(
      (resp: IProducto[]) => {
        console.log(resp);
        this.Producto = resp;
      },
      error => {
        console.error('Error obteniendo productos:', error);
      }
    );
  }

  eliminarProducto(idProducto: number): void {
    this.productoService.eliminarProducto(idProducto).subscribe(
      () => {
        this.Producto = this.Producto.filter(producto => producto.IdProducto !== idProducto);
      },
      error => {
        console.error('Error eliminando producto:', error);
      }
    );
  }

  openModalProducto(producto: IProducto): void {
    this.productoSeleccionado = { ...producto }; // Clonamos el objeto para evitar cambios directos en el original
    this.modalSwitchProducto = true;
  }

  closeModalProducto(): void {
    this.modalSwitchProducto = false;
  }

  actualizarProducto(): void {
    this.productoService.actualizarProducto(this.productoSeleccionado).subscribe(
      () => {
        console.log('Producto actualizado correctamente');
        this.closeModalProducto();
        // Actualizar la lista de productos después de la actualización
        this.obtenerProductos();
      },
      error => {
        console.error('Error actualizando producto:', error);
        // Aquí podrías manejar el error y mostrar un mensaje al usuario
      }
    );
  }

}
