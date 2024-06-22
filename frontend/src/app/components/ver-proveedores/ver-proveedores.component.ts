import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { IProveedor } from '../../interfaces/i-proveedor';
import { ProveedorService } from '../../services/proveedor.service';
import { HttpClient } from '@angular/common/http';
import { NgxPaginationModule } from 'ngx-pagination';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ver-proveedores',
  standalone: true,
  imports: [CommonModule, NgxPaginationModule, FormsModule],
  templateUrl: './ver-proveedores.component.html',
  styleUrls: ['./ver-proveedores.component.css']
})
export class VerProveedoresComponent implements OnInit {
  
  proveedores: IProveedor[] = [];
  page: number = 1;
  pageSize: number = 15;
  mostrarModal: boolean = false;
  proveedorSeleccionado: IProveedor = {} as IProveedor;
  rutBuscar: string = '';
  
  constructor(private proveedorService: ProveedorService, private http: HttpClient) { }

  ngOnInit() {
    this.obtenerProveedores();
  }

  obtenerProveedores() {
    this.proveedorService.getProveedores().subscribe(
      (resp:any) => {
        console.log(resp);
        this.proveedores = resp;
      },
      (error) => {
        console.error('Error al obtener proveedores', error);
      }
    );
  }

    buscarProveedor() {
    if (this.rutBuscar.trim() !== '') {
      this.proveedorService.getProveedor(this.rutBuscar).subscribe(
        (resp:any) => {
          this.proveedores = [resp];
        },
        (error) => {
          console.error('Error al buscar proveedor', error);
          this.proveedores = []; // Limpia la lista si no se encuentra
        }
      );
    } else {
      this.obtenerProveedores(); // Si el campo de búsqueda está vacío, obtener todos los proveedores
    }
  }

  abrirModal(proveedor: IProveedor): void {
    this.proveedorSeleccionado = { ...proveedor };
    this.mostrarModal = true;
  }

  cerrarModal(): void {
    this.mostrarModal = false;
  }

  enviarActualizacion(): void {
    this.proveedorService.actualizarProveedor(this.proveedorSeleccionado)
      .subscribe(() => {
        this.cerrarModal();
        this.obtenerProveedores(); // Refresca la lista de proveedores
      }, (error) => {
        console.error('Error al actualizar el proveedor', error);
      });
  }

  eliminarProveedor(idProveedor: number): void {
    this.proveedorService.eliminarProveedor(idProveedor)
      .subscribe(() => {
        this.proveedores = this.proveedores.filter(proveedor => proveedor.RutProveedor !== idProveedor); // Eliminar el proveedor de la lista
        // Mostrar mensaje de éxito o error
      });
  }
  
}
