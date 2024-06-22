import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ingresar-danados',
  standalone: true,
  imports: [CommonModule,
            FormsModule
  ],
  templateUrl: './ingresar-danados.component.html',
  styleUrl: './ingresar-danados.component.css'
})
export class IngresarDanadosComponent {
  productosDanados: any[] = [];
}
