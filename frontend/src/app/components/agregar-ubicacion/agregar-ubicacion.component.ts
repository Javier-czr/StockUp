import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { IUbicacion } from '../../interfaces/i-ubicacion';
import { UbicacionService } from '../../services/ubicacion.service';

@Component({
  selector: 'app-agregar-ubicacion',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './agregar-ubicacion.component.html',
  styleUrl: './agregar-ubicacion.component.css'
})
export class AgregarUbicacionComponent {

  ubicacion: IUbicacion = {
    IdUbicacion: 0,
    Nombre: '',
  };

  constructor(private ubicacionService: UbicacionService ) {}

  ingresarUbicacion() {
    this.ubicacionService.postUbicacion(this.ubicacion)
      .subscribe(() => {
        // Mostrar mensaje de éxito o error
      });
  }

  limpiarCampos() {
    this.ubicacion.Nombre = '';
  }

}

