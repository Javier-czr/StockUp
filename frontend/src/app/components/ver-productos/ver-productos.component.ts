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
  styleUrls: ['./ver-productos.component.css']
})
export class VerProductosComponent implements OnInit {

  productos: IProducto[] = [];
  productosFiltrados: IProducto[] = [];
  page: number = 1;
  pageSize: number = 15;
  modalSwitchProducto: boolean = false;
  productoSeleccionado: IProducto = {} as IProducto;
  buscarProducto: string = '';

  constructor(private productoService: ProductoService, private http: HttpClient) {}

  ngOnInit() {
    this.obtenerProductos();
  }

  obtenerProductos() {
    this.productoService.getProductos().subscribe(
      (resp: IProducto[]) => {
        this.productos = resp;
        this.productosFiltrados = resp;
      },
      error => {
        console.error('Error obteniendo productos:', error);
      }
    );
  }

  eliminarProducto(idProducto: number): void {
    this.productoService.eliminarProducto(idProducto).subscribe(
      () => {
        this.productos = this.productos.filter(producto => producto.IdProducto !== idProducto);
        this.filtrarProductos();
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
        this.closeModalProducto();
        this.obtenerProductos(); // Refresca la lista de productos
      },
      error => {
        console.error('Error actualizando producto:', error);
      }
    );
  }

  filtrarProductos(): void {
    if (this.buscarProducto.trim() !== '') {
      this.productosFiltrados = this.productos.filter(producto =>
        producto.Nombre.toLowerCase().includes(this.buscarProducto.toLowerCase()) ||
        producto.Marca.toLowerCase().includes(this.buscarProducto.toLowerCase()) ||
        producto.IdCategoria.toString().includes(this.buscarProducto) ||
        producto.IdProducto.toString().includes(this.buscarProducto)
      );
    } else {
      this.productosFiltrados = [...this.productos];
    }
  }
}
