import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AgregarCategoriaComponent } from '../agregar-categoria/agregar-categoria.component';
import { AgregarUbicacionComponent } from '../agregar-ubicacion/agregar-ubicacion.component';
import { IProducto} from '../../interfaces/i-producto';
import { ProductoService } from '../../services/producto.service';
import { CategoriaService } from '../../services/categoria.service';
import { UbicacionService } from '../../services/ubicacion.service';
import { HttpClient } from '@angular/common/http';
import { ICategoria } from '../../interfaces/i-categoria';
import { IUbicacion } from '../../interfaces/i-ubicacion';
import { IProveedor } from '../../interfaces/i-proveedor';
import { ProveedorService } from '../../services/proveedor.service';
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-ingresar-producto',
  standalone: true,
  imports: [CommonModule,
            AgregarCategoriaComponent,
            AgregarUbicacionComponent,
            FormsModule            
  ],
  templateUrl: './ingresar-producto.component.html',
  styleUrl: './ingresar-producto.component.css'
})
export class IngresarProductoComponent {

  opcionesCategorias: ICategoria[] = [];
  opcionesUbicacion: IUbicacion[] = [];
  opcionesProveedores: IProveedor[] = []; 

  Producto: IProducto = {
    IdProducto: 0,
    Nombre: '',
    Marca: '',
    IdCategoria: '',
    Cantidad: 0,
    FechaVencimiento: new Date(),
    Precio: 0,
    IdUbicacion: ''
  };

  constructor(private productoService: ProductoService,
              private categoriaService: CategoriaService,
              private ubicacionService: UbicacionService,
              private proveedorService: ProveedorService,
              private http: HttpClient) {}

  ngOnInit() {
    this.obtenerCategorias();
    this.obtenerUbicaciones();
    this.obtenerProveedor();
  }

  ingresarProducto() {
    this.productoService.postProducto(this.Producto)
      .subscribe(() => {
        console.log('Producto ingresado');
        this.limpiarCampos();
      });
  }

  limpiarCampos() {
    this.Producto.IdProducto = 0;
    this.Producto.Nombre = '';
    this.Producto.Marca = '';
    this.Producto.IdCategoria = '';
    this.Producto.Cantidad = 0;
    this.Producto.FechaVencimiento = new Date();
    this.Producto.Precio = 0;
    this.Producto.IdUbicacion = '';
  }

  obtenerCategorias() {
    return this.http.get('http://127.0.0.1:5000/categoria').subscribe(
      (resp:any) => {
        console.log(resp);
        this.opcionesCategorias = resp;
      })
  }

  obtenerUbicaciones() {
    return this.http.get('http://127.0.0.1:5000/ubicacion').subscribe(
      (resp:any) => {
        console.log(resp);
        this.opcionesUbicacion = resp;
      })
  }

  obtenerProveedor() {
    return this.http.get('http://127.0.0.1:5000/proveedor').subscribe(
      (resp:any) => {
        console.log(resp);
        this.opcionesProveedores = resp;
      })
  }
}
