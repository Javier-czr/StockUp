import { Component } from '@angular/core';
import { HistorialCambioService } from '../../services/historial-cambio.service';
import { CommonModule } from '@angular/common';
import { NgxPaginationModule } from 'ngx-pagination';

interface Cambio {
  IdCambio: number;
  fechaCambio: string;
  DescripcionCambio: string;
}

@Component({
  selector: 'app-historial-cambios',
  standalone: true,
  imports: [CommonModule, NgxPaginationModule],
  templateUrl: './historial-cambios.component.html',
  styleUrl: './historial-cambios.component.css'
})
export class HistorialCambiosComponent {
  cambios: Cambio[] = [];
  page: number = 1;
  pageSize: number = 15;

  constructor(private historialCambioService: HistorialCambioService) {}

  ngOnInit(): void {
    this.historialCambioService.obtenerCambios().subscribe(
      data => this.cambios = data,
      error => console.error(error)
    );
  }
}
