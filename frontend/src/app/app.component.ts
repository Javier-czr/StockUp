import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { IngresarProductoComponent } from './components/ingresar-producto/ingresar-producto.component';
import { VerProductosComponent } from './components/ver-productos/ver-productos.component';
import { IngresarProveedorComponent } from './components/ingresar-proveedor/ingresar-proveedor.component';
import { NavMenuComponent } from './components/nav-menu/nav-menu.component';
import { IngresarDanadosComponent } from './components/ingresar-danados/ingresar-danados.component';
import { VerProveedoresComponent } from './components/ver-proveedores/ver-proveedores.component';
import { RealizarPedidosComponent } from './components/realizar-pedidos/realizar-pedidos.component';
import { ListaNotificacionesComponent } from './components/lista-notificaciones/lista-notificaciones.component';
import { HistorialCambiosComponent } from './components/historial-cambios/historial-cambios.component';
import { HistorialPedidosComponent } from './components/historial-pedidos/historial-pedidos.component';
import { AgregarCategoriaComponent } from './components/agregar-categoria/agregar-categoria.component';
import { AgregarUbicacionComponent } from './components/agregar-ubicacion/agregar-ubicacion.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ProductoService } from './services/producto.service';
import { LoginComponent } from './components/login/login.component';
import { AuthService } from './services/auth.service';
import { FormsModule } from '@angular/forms';
import { RegistrarseComponent } from './components/registrarse/registrarse.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: 
          [ 
            RouterOutlet, 
            CommonModule, 
            IngresarProductoComponent,
            NavMenuComponent,   
            VerProductosComponent,
            IngresarProveedorComponent,
            IngresarDanadosComponent,
            VerProveedoresComponent,
            RealizarPedidosComponent,
            ListaNotificacionesComponent,
            HistorialCambiosComponent,
            HistorialPedidosComponent,
            AgregarCategoriaComponent,
            AgregarUbicacionComponent,
            HttpClientModule,
            LoginComponent,
            FormsModule,
            RegistrarseComponent
          ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  title = 'StockApp';  

  opcionesCategorias: string[] = ['Categoría 1', 'Categoría 2'];
  opcionesUbicacion: string[] = ['Ubicación 1', 'Ubicación 2'];

  // Variables para mostrar las opciones de los botones
  mostrarOpcionesProductos: boolean = false;
  mostrarOpcionesProveedores: boolean = false;
  mostrarOpcionesNotificacion: boolean = false;
  mostrarOpcionesHistorial: boolean = false;
  mostrarOpcionesRegistro: boolean = false;

  // Funciones para mostrar las opciones de los botones
  verListaProductos: boolean = false;
  ingresarProductos: boolean = false;
  ingresarProductosDanados: boolean = false;
  ingresarProveedores: boolean = false;
  verListaProveedores: boolean = false;
  crearPedido: boolean = false;
  verNotificaciones: boolean = false;
  verHistorialPedidos: boolean = false;
  verHistorialCambios: boolean = false;
  registrarUsuario: boolean = false;

  constructor(private http: HttpClient, public authService: AuthService) { }

  mostrarSeccion(seccion: string) {
    this.mostrarOpcionesProductos = seccion === 'productos';
    this.mostrarOpcionesProveedores = seccion === 'proveedores';
    this.mostrarOpcionesNotificacion = seccion === 'notificacion';
    this.mostrarOpcionesHistorial = seccion === 'historial';
    this.mostrarOpcionesRegistro = seccion === 'registro';
  }

  mostrarFunciones(funcion: string) {
    this.verListaProductos = funcion === 'verProductos';
    this.ingresarProductos = funcion === 'ingresarProductos';
    this.ingresarProductosDanados = funcion === 'ingresarProductosDanados';
    this.verListaProveedores = funcion === 'verProveedores';
    this.ingresarProveedores = funcion === 'ingresarProveedores';
    this.crearPedido = funcion === 'crearPedido';
    this.verNotificaciones = funcion === 'verNotificaciones';
    this.verHistorialPedidos = funcion === 'verHistorialPedidos';
    this.verHistorialCambios = funcion === 'verHistorialCambios';
    this.registrarUsuario = funcion === 'registrarUsuario';
  }

  isLoggedIn(): boolean {
    return this.authService.isLoggedIn();
  }

}
