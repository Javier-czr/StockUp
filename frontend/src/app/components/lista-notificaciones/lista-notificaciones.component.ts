import { Component, OnInit } from '@angular/core';
import { NotificacionService } from '../../services/notificacion.service';
import { Subscription, interval } from 'rxjs';
import { CommonModule } from '@angular/common';
import { NgxPaginationModule } from 'ngx-pagination';  // Importa NgxPaginationModule

interface Notificacion {
  IdNotificacion: number;
  FechaNotificacion: string;
  DescripcionNotificacion: string;
}

@Component({
  selector: 'app-lista-notificaciones',
  standalone: true,
  imports: [CommonModule, NgxPaginationModule],  // Añade NgxPaginationModule a los imports
  templateUrl: './lista-notificaciones.component.html',
  styleUrls: ['./lista-notificaciones.component.css']
})
export class ListaNotificacionesComponent implements OnInit {

  notificaciones: Notificacion[] = [];
  page: number = 1;
  pageSize: number = 15;

  constructor(private notificacionService: NotificacionService) { }

  ngOnInit(): void {
    this.listarNotificaciones();
  }

  listarNotificaciones(): void {
    this.notificacionService.getNotificaciones().subscribe(data => {
      this.notificaciones = data;
    });
  }
}
