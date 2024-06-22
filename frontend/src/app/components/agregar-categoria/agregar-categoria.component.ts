import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ICategoria } from '../../interfaces/i-categoria';
import { CategoriaService } from '../../services/categoria.service';

@Component({
  selector: 'app-agregar-categoria',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './agregar-categoria.component.html',
  styleUrl: './agregar-categoria.component.css'
})
export class AgregarCategoriaComponent {

  categorias: ICategoria = {
    IdCategoria: 0,
    Nombre: ''
  };

  constructor( private categoriaService: CategoriaService ) {}

  ingresarCategoria() {
    this.categoriaService.postCategoria(this.categorias)
      .subscribe(() => {
        // Mostrar mensaje de éxito o error
      });
  }

  limpiarCampos() {
    this.categorias.Nombre = '';
  }

}
