import { Component } from '@angular/core';
import { IProveedor } from '../../interfaces/i-proveedor';
import { ProveedorService } from '../../services/proveedor.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ingresar-proveedor',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './ingresar-proveedor.component.html',
  styleUrl: './ingresar-proveedor.component.css'
})
export class IngresarProveedorComponent {

  proveedores: IProveedor = {
    RutProveedor: '',
    Empresa: '',
    Nombre: '',
    Apellido: '',
    Telefono: 0,
    Correo: ''
  };

  constructor(private proveedorService: ProveedorService) {}

  ingresarProveedor() {
    this.proveedorService.postProveedor(this.proveedores)
      .subscribe(() => {
        this.limpiarCampos();
      });
  }

  limpiarCampos() {
    this.proveedores.RutProveedor = '';
    this.proveedores.Empresa = '';
    this.proveedores.Nombre = '';
    this.proveedores.Apellido = '';
    this.proveedores.Telefono = 0;
    this.proveedores.Correo = '';
  }

}
